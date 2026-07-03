%define _unpackaged_files_terminate_build 1
%define node_module detect-libc

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-detect-libc
Version: 2.1.2
Release: alt1

Summary: Node.js module to detect the C standard library implementation
License: Apache-2.0
Group: Development/Other
Url: https://github.com/lovell/detect-libc
Vcs: https://github.com/lovell/detect-libc.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

Requires: node

Provides: npm(%node_module) = %version
Provides: nodejs-%node_module = %EVR

%description
detect-libc is a Node.js module to detect the C standard library (libc)
implementation family and version in use on a given Linux system.

It supports GNU glibc and musl, and provides asynchronous and synchronous
APIs suitable for prebuild, prebuild-ci and prebuild-install workflows.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json index.d.ts lib %buildroot%nodejs_sitelib/%node_module/
%nodejs_symlink_deps

%check
node - <<'EOF'
const libc = require('./');
for (const name of ['family', 'familySync', 'version', 'versionSync', 'isNonGlibcLinux', 'isNonGlibcLinuxSync']) {
  if (typeof libc[name] !== 'function') {
    throw new Error(`${name} is not exported`);
  }
}
if (libc.GLIBC !== 'glibc' || libc.MUSL !== 'musl') {
  throw new Error('libc constants are invalid');
}
EOF

%files
%doc README.md CHANGELOG.md
%doc LICENSE
%nodejs_sitelib/%node_module/

%changelog
* Fri Jul 03 2026 Grant Makyan <karonus@altlinux.org> 2.1.2-alt1
- Update version to 2.1.2

* Thu Sep 22 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1.1
- ! rename in favor of proper name (closes #43435)

* Fri Jan 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- NPM.js package for detect-libc built for Sisyphus
