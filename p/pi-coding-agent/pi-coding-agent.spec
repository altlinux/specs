Name: pi-coding-agent
Version: 0.73.0
Release: alt1

Summary: Coding agent CLI with read, bash, edit, write tools and session management

License: MIT
Group: Development/Tools
Url: https://github.com/badlogic/pi-mono

# Source-url: https://registry.npmjs.org/@mariozechner/pi-coding-agent/-/pi-coding-agent-%version.tgz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from
# etersoft-build-utils
Source1: %name-development-%version.tar

BuildArch: noarch

AutoReq:yes,nonodejs_native,nomono,nolua
AutoReq:nopython,nopython3,nomingw32,nomingw64,noshebang

Requires: /usr/bin/node

%description
pi (pi-coding-agent) is a terminal-based AI coding agent built on top of
the pi.dev unified LLM API. It provides read, bash, edit and write tools,
session management, an interactive TUI mode and an export-to-HTML feature.

The package ships the prebuilt JavaScript bundle from upstream npm release
together with the production node_modules tree, requiring only a Node.js
runtime to operate.

%prep
%setup -a1

%install
install -d %buildroot%_datadir/%name
cp -a dist package.json README.md CHANGELOG.md \
    %buildroot%_datadir/%name/

# move predownloaded node_modules to package dir
[ -d node_modules ] && cp -a node_modules %buildroot%_datadir/%name/

# create wrapper
install -d %buildroot%_bindir
cat > %buildroot%_bindir/pi <<'EOF'
#!/bin/sh
exec /usr/bin/node %_datadir/%name/dist/cli.js "$@"
EOF
chmod 0755 %buildroot%_bindir/pi

%files
%doc README.md CHANGELOG.md
%_bindir/pi
%_datadir/%name/

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.73.0-alt1
- initial build for ALT Sisyphus

