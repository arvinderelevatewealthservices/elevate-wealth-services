/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: '/elevate-wealth-services',
  assetPrefix: '/elevate-wealth-services/',
  trailingSlash: true,
}

module.exports = nextConfig
