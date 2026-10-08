%define _unpackaged_files_terminate_build 1
%define node_module node-pty

%filter_from_requires /^nodejs.engine./d
%filter_from_requires /^npm(node-addon-api)/d

Name: node-pty
Version: 1.1.0
Release: alt1

Summary: Pseudoterminal bindings for Node.js
License: MIT
Group: Development/Other
Url: https://github.com/microsoft/node-pty
Vcs: https://github.com/microsoft/node-pty.git

Source: %name-%version.tar
Source1: check-runtime.mjs
Source2: %name-%version-vendor.tar
Source3: tsconfig.build.json
Patch0: system-node-addon-api.patch

ExclusiveArch: %nodejs_arches

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs node node-devel >= 18
BuildRequires: node-gyp node-addon-api >= 8 gcc-c++ make
BuildRequires: node-typescript >= 6.0
BuildRequires: /proc /dev/pts

Requires: node >= 18
Provides: npm(%node_module) = %version
Provides: nodejs-%node_module = %EVR

# This addon uses stable Node-API 8, not the version-specific V8 ABI.
AutoReq: yes,nonodejs_native

%description
node-pty provides pseudoterminal bindings for Node.js. It supports spawning
processes with a terminal, reading and writing terminal data, and resizing
the terminal. The native addon is built against the stable Node-API.

%prep
%setup -a2
%patch0 -p1
cp %SOURCE3 tsconfig.build.json
ln -s vendor/node_modules node_modules

%build
export NODE_PATH=%nodejs_sitelib
export CXXFLAGS="%optflags"
tsc -p tsconfig.build.json
node-gyp rebuild --nodedir=%_prefix

%install
install -d %buildroot%nodejs_sitelib/%node_module/build/Release
cp -a lib typings package.json %buildroot%nodejs_sitelib/%node_module/
find %buildroot%nodejs_sitelib/%node_module/lib -type f \
    \( -name '*.test.js' -o -name '*.map' \) -delete
install -m644 build/Release/pty.node \
    %buildroot%nodejs_sitelib/%node_module/build/Release/pty.node

%check
node %SOURCE1 %buildroot%nodejs_sitelib/%node_module

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module

%changelog
* Thu Oct 08 2026 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
- Initial build for ALT.
