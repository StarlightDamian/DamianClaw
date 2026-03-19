#!/usr/bin/env node
// cdp-wrapper - Wrapper for chrome-cdp skill
// This is a thin wrapper that forwards all commands to the chrome-cdp cdp.mjs script
// Reuses the implementation from chrome-cdp to avoid code duplication

import { spawn } from 'child_process';
import path from 'path';
import url from 'url';

// Get the path to the original cdp.mjs from chrome-cdp
// chrome-cdp is in the same skills directory as browser-automation
const __filename = url.fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const chromeCdpPath = path.join(
  path.dirname(path.dirname(__dirname)),
  'chrome-cdp',
  'scripts',
  'cdp.mjs'
);

// Forward all arguments
const child = spawn(process.execPath, [chromeCdpPath, ...process.argv.slice(2)], {
  stdio: 'inherit',
});

child.on('error', (err) => {
  console.error(`Failed to execute chrome-cdp: ${err.message}`);
  console.error(`Looking for: ${chromeCdpPath}`);
  process.exit(1);
});

child.on('close', (code) => {
  process.exit(code);
});
