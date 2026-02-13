'use client'

export default function AnimatedBrandBanner() {
  // Brand partner logos - Replace with your actual partner brands
  const brands = [
    { name: 'HDFC Mutual Fund', logo: 'HDFC MF' },
    { name: 'ICICI Prudential', logo: 'ICICI' },
    { name: 'SBI Mutual Fund', logo: 'SBI MF' },
    { name: 'Axis Mutual Fund', logo: 'Axis MF' },
    { name: 'Kotak Mahindra', logo: 'Kotak' },
    { name: 'Aditya Birla', logo: 'ABSL' },
    { name: 'UTI Mutual Fund', logo: 'UTI' },
    { name: 'DSP Mutual Fund', logo: 'DSP' },
  ]

  // Duplicate for seamless loop
  const duplicatedBrands = [...brands, ...brands]

  return (
    <section className="py-16 bg-white border-y border-gray-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-center text-gray-500 text-sm font-semibold uppercase tracking-wider mb-8">
          Trusted Partners
        </h2>

        {/* Infinite Scroll Container */}
        <div className="relative overflow-hidden">
          {/* Gradient Overlays */}
          <div className="absolute left-0 top-0 bottom-0 w-32 bg-gradient-to-r from-white to-transparent z-10"></div>
          <div className="absolute right-0 top-0 bottom-0 w-32 bg-gradient-to-l from-white to-transparent z-10"></div>

          {/* Scrolling Content */}
          <div className="flex animate-scroll-left">
            {duplicatedBrands.map((brand, index) => (
              <div
                key={index}
                className="flex-shrink-0 mx-8 w-32 h-24 flex items-center justify-center"
              >
                <div className="bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl p-6 shadow-md hover:shadow-xl transition-all hover:scale-110 group">
                  <p className="text-2xl font-bold text-gray-400 group-hover:text-primary-600 transition-colors text-center">
                    {brand.logo}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>

        <p className="text-center text-sm text-gray-500 mt-8">
          Partnered with India's leading financial institutions
        </p>
      </div>

      <style jsx>{`
        @keyframes scroll-left {
          0% {
            transform: translateX(0);
          }
          100% {
            transform: translateX(-50%);
          }
        }
        .animate-scroll-left {
          animation: scroll-left 30s linear infinite;
        }
        .animate-scroll-left:hover {
          animation-play-state: paused;
        }
      `}</style>
    </section>
  )
}
