%define _unpackaged_files_terminate_build 1

Name: xsct
Version: 2.3
Release: alt1

Summary: sct - set color temperature of screen
License: unlicense
Group: System/X11
Url: https://github.com/faf0/sct

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: pkgconfig(xrandr)

%description
Xsct (X11 set color temperature) is a UNIX tool which allows you to set
the color temperature of your screen. It is simpler than Redshift and
f.lux.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%buildroot%prefix

%files
%_bindir/xsct
%_man1dir/%name.1*
%doc LICENSE CHANGELOG README.md

%changelog
* Fri May 09 2025 Nikolay Strelkov <snk@altlinux.org> 2.3-alt1
- NMU: New version 2.3.

* Thu Sep 17 2020 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt1
- first build for Sisyphus
