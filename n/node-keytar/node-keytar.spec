%define _unpackaged_files_terminate_build 1
%define node_module keytar
%define pname keytar

%filter_from_requires /^nodejs.engine./d
%filter_from_requires /^npm(node-addon-api)/d
%filter_from_requires /^npm(prebuild-install)/d
%{?nodejs_find_provides_and_requires}

Name: node-keytar
Version: 7.9.0
Release: alt1

Summary: Native Node.js bindings for system keychains
License: MIT
Group: Development/Other
Url: https://github.com/atom/node-keytar
Vcs: https://github.com/atom/node-keytar.git

Source: %name-%version.tar

ExclusiveArch: %nodejs_arches

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node
BuildRequires: node-devel
BuildRequires: node-addon-api
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkg-config
BuildRequires: libsecret-devel

Requires: node

Provides: npm(%node_module) = %version
Provides: nodejs-%node_module = %EVR

%description
keytar is a native Node.js module for storing, retrieving, and deleting
passwords in the operating system credential store. On Linux it uses the
Secret Service API through libsecret.

%prep
%setup

%build
%npm_build

%install
%npm_install

rm -rf %buildroot%nodejs_sitelib/%pname/{docker,script,spec,src,binding.gyp}
rm -f %buildroot%nodejs_sitelib/%pname/{package-lock.json,.babelrc}

%check
node - <<'EOF'
const keytar = require('./');
for (const name of ['getPassword', 'setPassword', 'deletePassword', 'findPassword', 'findCredentials']) {
  if (typeof keytar[name] !== 'function') {
    throw new Error(`${name} is not exported`);
  }
}
EOF

%files
%doc LICENSE.md README.md
%nodejs_sitelib/%pname

%changelog
* Tue Jul 07 2026 Grant Makyan <karonus@altlinux.org> 7.9.0-alt1
- Initial build for ALT.
