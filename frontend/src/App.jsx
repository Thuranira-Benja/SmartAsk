import React, { useState } from 'react'
import ChatWindow from './components/ChatWindow'
import MessageInput from './components/MessageInput'
import axios from 'axios'

export default function App() {
  const [messages, setMessages] = useState([])
  const sendMessage = async (text) => {
    const userMsg = { sender: 'user', text }
    setMessages((m) => [...m, userMsg])
    try {
      const res = await axios.post('http://localhost:8000/api/chat', { question: text })
      const bot = { sender: 'bot', text: res.data.answer }
      setMessages((m) => [...m, bot])
    } catch (err) {
      const bot = { sender: 'bot', text: 'Sorry, something went wrong.' }
      setMessages((m) => [...m, bot])
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
      <div className="w-full max-w-2xl bg-white rounded shadow p-4">
        <h2 className="text-xl font-semibold mb-4">SmartAsk — Document Chat</h2>
        <ChatWindow messages={messages} />
        <MessageInput onSend={sendMessage} />
      </div>
    </div>
  )
}
