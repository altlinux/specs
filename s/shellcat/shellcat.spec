%define _unpackaged_files_terminate_build 1

Name: shellcat
Version: 1.2.1
Release: alt1
Summary: Templating system with shell syntax
License:  MIT
Group: Terminals
Url: https://github.com/jwilk/shellcat

Source: %name-%version.tar

%description
%summary

%prep
%setup
sed -i 's|/usr/local|%prefix|g' Makefile

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std

%files
%_bindir/*

%changelog
* Tue Apr 16 2024 Pavel Shilov <zerospirit@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus
