Name: mermaid-cli
Version: 12.2.0
Release: alt1

Summary: Generate SVG, PNG and PDF images from Mermaid diagrams

License: MIT
Group: Graphics
Url: https://github.com/mermaid-js/mermaid-cli

# Source-url: https://github.com/mermaid-js/mermaid-cli/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source1: %name-production-%version.tar
Source2: README.ALT
Patch: system-chromium.patch

# Pure JS, but it runs the system Chromium, which is built only for these
# architectures: a noarch package would get an unmet /usr/bin/chromium on i586
# (girar checks noarch packages on every architecture, ExcludeArch aside)
ExclusiveArch: x86_64 aarch64
BuildRequires: node >= 22.13.0

# All JavaScript dependencies are private, pure JS modules (Node.js Policy).
# Language heuristics misidentify vendored JS as Lua and font build scripts
# as runtime Python/Perl dependencies. Only the public wrapper needs scanning.
%add_findreq_skiplist %_datadir/%name/*
AutoProv: no
Requires: node >= 22.13.0
Requires: /usr/bin/chromium

%description
The Mermaid command line interface (mmdc) converts text diagram definitions
to SVG, PNG and PDF. It also converts Mermaid code blocks in Markdown files.
It uses the system Chromium browser through puppeteer-core.

%prep
%setup -a1
%patch -p1
cp %SOURCE2 .

%build
# Upstream JS needs no transpilation. Vite's only HTML input has no imports;
# install that source directly instead of vendoring native build tools.
node --check src/index.js
node --check src/cli.js

%install
mkdir -p %buildroot%_datadir/%name/dist %buildroot%_bindir
cp -a src node_modules package.json %buildroot%_datadir/%name/
install -m644 index.html %buildroot%_datadir/%name/dist/index.html
cat > %buildroot%_bindir/mmdc <<'EOF'
#!/bin/sh
exec /usr/bin/node /usr/share/mermaid-cli/src/cli.js "$@"
EOF
chmod 755 %buildroot%_bindir/mmdc
# Private dependencies may contain CLI entrypoints, but expose only mmdc.
rm -rf %buildroot%_datadir/%name/node_modules/.bin
find %buildroot%_datadir/%name -type d -exec chmod 755 '{}' +

%check
node src/cli.js --version

%files
%doc LICENSE README.md README.ALT
%_bindir/mmdc
%_datadir/%name/

%changelog
* Wed Nov 11 2026 Vitaly Lipatov <lav@altlinux.ru> 12.2.0-alt1
- initial build for ALT Linux with system Chromium.

