%define _unpackaged_files_terminate_build 1
%define node_module native-keymap
%define pname native-keymap

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-native-keymap
Version: 3.3.9
Release: alt1

Summary: Native Node.js module for OS keyboard mapping
License: MIT
Group: Development/Other
Url: https://github.com/microsoft/node-native-keymap
Vcs: https://github.com/microsoft/node-native-keymap.git

Source: %name-%version.tar

ExclusiveArch: %nodejs_arches

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node
BuildRequires: node-devel
BuildRequires: node-gyp
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkg-config
BuildRequires: libX11-devel
BuildRequires: libxkbfile-devel

Requires: node

Provides: npm(%node_module) = %version
Provides: nodejs-%node_module = %EVR

%description
native-keymap is a native Node.js module that returns the characters produced
by pressing keys with different modifiers on the current operating system
keyboard layout. On Linux it uses the X11 keyboard APIs.

%prep
%setup
touch .npmignore .gitignore

%build
node-gyp configure
node-gyp build --release

%install
%npm_install

rm -rf %buildroot%nodejs_sitelib/%node_module/{src,deps,test,binding.gyp,pipeline.yml}
rm -f %buildroot%nodejs_sitelib/%node_module/{package-lock.json,PoliCheckExclusions.xml,SECURITY.md,ThirdPartyNotices.txt}

%check
node - <<'EOF'
const keymap = require('./');
for (const name of ['getCurrentKeyboardLayout', 'getKeyMap', 'onDidChangeKeyboardLayout', 'isISOKeyboard']) {
  if (typeof keymap[name] !== 'function') {
    throw new Error(`${name} is not exported`);
  }
}
EOF

%files
%doc License.txt README.md ThirdPartyNotices.txt
%nodejs_sitelib/%node_module

%changelog
* Tue Jul 07 2026 Grant Makyan <karonus@altlinux.org> 3.3.9-alt1
- Initial build for ALT.
