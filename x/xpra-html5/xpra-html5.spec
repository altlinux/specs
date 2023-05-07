%define minifier uglifyjs

Name: xpra-html5
Version: 5.1
Release: alt1

Summary: HTML5 client for Xpra
License: GPL-2.0+ and BSD-3-Clause and LGPL-3.0+ and MIT
Group: Networking/Remote access

Url: http://xpra.org/
Source: https://xpra.org/src/xpra-html5-%version.tar

BuildArch: noarch

Packager: Elena Mishina <lepata@altlinux.org>

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
Conflicts: xpra < 4.4.4

BuildRequires: /usr/bin/uglifyjs
BuildRequires: brotli

%description
This is the HTML5 client for Xpra,
which can be made available for browsers by the xpra server

%prep
%setup

%build
#%%python3_build

%install
%__python3 setup.py install %buildroot %_datadir/xpra/www/ %_sysconfdir/xpra/html5-client %minifier
# Ensure there are no executable files:
# find %buildroot%_datadir/xpra/www/ -type f -exec chmod 0644 {} \;

%files
%config(noreplace) %_sysconfdir/xpra/html5-client/*
%_datadir/xpra/www

%changelog
* Fri May 05 2023 Elena Mishina <lepata@altlinux.org> 5.1-alt1
- Initial build for ALT
