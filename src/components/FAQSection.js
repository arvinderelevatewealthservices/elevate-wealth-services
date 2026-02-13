'use client'

import { useState } from 'react'
import { ChevronDown, HelpCircle } from 'lucide-react'

export default function FAQSection() {
  const [openIndex, setOpenIndex] = useState(0)

  const faqs = [
    {
      question: 'How do I start investing in mutual funds with ElevateWealthServices?',
      answer: 'Starting is simple! Book a free consultation through our website, call us, or visit our Ludhiana office. We\'ll conduct a detailed discussion to understand your financial goals, risk appetite, investment horizon, and current financial situation. Based on this, we\'ll recommend a personalized portfolio. KYC completion takes just 15 minutes online, and you can start investing the same day. We support both SIP (Systematic Investment Plans) and lumpsum investments.',
    },
    {
      question: 'What is the minimum investment amount required?',
      answer: 'You can start with as low as ₹500 per month through SIPs. For lumpsum investments, most mutual funds have a minimum of ₹5,000. We believe in making wealth creation accessible to everyone, so we encourage starting small and gradually increasing your investment as you get comfortable and your income grows. Regular investing, even with small amounts, can create significant wealth over time through the power of compounding.',
    },
    {
      question: 'Do you charge any fees or commissions?',
      answer: 'As AMFI-registered distributors, we earn commissions from fund houses on Regular Plan investments - there are no direct charges to you. We also offer Direct Plans where you pay lower expense ratios, and we charge a transparent advisory fee. During our consultation, we\'ll explain both models in detail and help you choose what works best for your situation. Complete transparency is our policy.',
    },
    {
      question: 'What types of insurance do you offer?',
      answer: 'We offer comprehensive insurance solutions including Life Insurance (term plans, endowment policies, ULIPs), Health Insurance (individual, family floater, critical illness coverage), and General Insurance (motor, home, travel insurance). We analyze your current coverage, identify gaps, and recommend policies that provide adequate protection at competitive premiums. We work with leading insurance providers to give you the best options.',
    },
    {
      question: 'How is my insurance claim processed and what support do you provide?',
      answer: 'We provide end-to-end claims assistance. Simply notify us when you need to file a claim, and our team will guide you through documentation requirements, help you fill forms correctly, coordinate with the insurance company, and follow up regularly until settlement. We act as your advocate throughout the process. Our goal is to make claim settlement as smooth and stress-free as possible during what can be a difficult time.',
    },
    {
      question: 'Can I transfer my existing investments to ElevateWealthServices?',
      answer: 'Absolutely! Transferring your existing mutual fund investments to us is hassle-free and doesn\'t trigger any exit loads or tax implications. We\'ll help you complete the necessary paperwork. Your portfolio continuity is maintained, and you immediately start benefiting from our advisory services, regular reviews, and personalized recommendations. Many clients come to us for better service and professional guidance.',
    },
    {
      question: 'How often will I receive updates about my investments?',
      answer: 'You\'ll receive monthly performance reports via email and WhatsApp showing your portfolio value, returns, and allocation breakdown. We conduct quarterly portfolio reviews to assess performance against goals and recommend rebalancing when needed. You also get 24/7 access to your portfolio through our partner platforms. Additionally, you can contact us anytime for specific queries or updates - we\'re always accessible.',
    },
    {
      question: 'What makes ElevateWealthServices different from other distributors?',
      answer: 'We combine digital convenience with offline accessibility. While many distributors are purely online or offline, we offer both - visit our office for personal consultations or manage everything digitally. We focus on goal-based planning rather than product pushing, maintain complete transparency in our recommendations, provide regular communication and support, and are AMFI-registered ensuring full regulatory compliance. Our client-first approach means we succeed only when you achieve your financial goals.',
    },
  ]

  const toggleFAQ = (index) => {
    setOpenIndex(openIndex === index ? -1 : index)
  }

  return (
    <section className="py-20 bg-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <HelpCircle className="w-16 h-16 mx-auto text-primary-600 mb-4" />
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Frequently Asked Questions
          </h2>
          <p className="text-xl text-gray-600">
            Everything you need to know about our services
          </p>
        </div>

        <div className="space-y-4">
          {faqs.map((faq, index) => (
            <div
              key={index}
              className="bg-gradient-to-br from-gray-50 to-white rounded-2xl border border-gray-200 overflow-hidden hover:shadow-lg transition-all"
            >
              <button
                onClick={() => toggleFAQ(index)}
                className="w-full px-6 py-5 flex items-center justify-between text-left hover:bg-primary-50 transition-all"
              >
                <span className="text-lg font-semibold text-gray-900 pr-8">
                  {faq.question}
                </span>
                <ChevronDown
                  className={`w-6 h-6 text-primary-600 flex-shrink-0 transition-transform duration-300 ${
                    openIndex === index ? 'rotate-180' : ''
                  }`}
                />
              </button>
              
              <div
                className={`overflow-hidden transition-all duration-300 ${
                  openIndex === index ? 'max-h-[500px]' : 'max-h-0'
                }`}
              >
                <div className="px-6 pb-5 text-gray-600 leading-relaxed">
                  {faq.answer}
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-12 text-center">
          <p className="text-gray-600 mb-4">Still have questions?</p>
          <a
            href="/contact"
            className="inline-flex items-center space-x-2 bg-gradient-to-r from-primary-600 to-primary-700 text-white px-6 py-3 rounded-lg font-semibold hover:shadow-lg transition-all hover:scale-105"
          >
            <span>Talk to an Expert</span>
          </a>
        </div>
      </div>
    </section>
  )
}
