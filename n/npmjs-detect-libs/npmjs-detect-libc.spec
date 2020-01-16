%define        pname detect-libs

Name:          npmjs-%pname
Version:       1.0.3
Release:       alt1
Summary:       Node.js module to detect the C standard library (libc) for use with prebuild
License:       Apache-2.0
Group:         Development/Other
Url:           https://github.com/lovell/detect-libc
Vcs:           https://github.com/lovell/detect-libc.git
Packager:      Node Team <node@packages.altlinux.ru>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-nodejs

AutoProv:      yes
AutoReq:       yes

%description
Node.js module to detect the C standard library (libc) implementation family
and version in use on a given Linux system.

Provides a value suitable for use with the LIBC option of prebuild, prebuild-ci
and prebuild-install, therefore allowing build and provision of pre-compiled
binaries for musl-based Linux e.g. Alpine as well as glibc-based.

Currently supports libc detection of glibc and musl.


%prep
%setup

%build
%npm_build

%install
%npm_install

%files
%doc README.md
%nodejs_sitelib/%pname


%changelog
* Fri Jan 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- NPM.js package for %pname built for Sisyphus
