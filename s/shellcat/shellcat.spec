%define _unpackaged_files_terminate_build 1

Name: shellcat
Version: 1.2.1
Release: alt2
Summary: Templating system with shell syntax
License:  MIT
Group: Terminals
Url: https://github.com/jwilk/shellcat

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: /usr/bin/pod2man

%description
%summary

%prep
%setup
%autopatch -p1
sed -i 's|/usr/local|%prefix|g' Makefile

%build
%make_build CFLAGS="%optflags"
%make_build -C doc

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Sat Jul 26 2025 Pavel Shilov <zerospirit@altlinux.org> 1.2.1-alt2
- Update based on upstream.

* Tue Apr 16 2024 Pavel Shilov <zerospirit@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus
