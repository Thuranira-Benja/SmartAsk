import React from 'react'

export default function ChatWindow({ messages }) {
  return (
    <div className="h-80 overflow-y-auto border p-3 mb-3">
      {messages.map((m, i) => (
        <div key={i} className={`mb-2 ${m.sender === 'user' ? 'text-right' : 'text-left'}`}>
          <div className={`inline-block px-3 py-2 rounded ${m.sender === 'user' ? 'bg-blue-100' : 'bg-gray-100'}`}>
            {m.text}
          </div>
        </div>
      ))}
    </div>
  )
}
