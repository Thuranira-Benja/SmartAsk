import React, { useState } from 'react'

export default function MessageInput({ onSend }) {
  const [text, setText] = useState('')
  const submit = (e) => {
    e.preventDefault()
    if (!text.trim()) return
    onSend(text.trim())
    setText('')
  }
  return (
    <form onSubmit={submit} className="flex">
      <input value={text} onChange={(e) => setText(e.target.value)} className="flex-1 border rounded px-3 py-2 mr-2" placeholder="Ask SmartAsk..." />
      <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded">Send</button>
    </form>
  )
}
