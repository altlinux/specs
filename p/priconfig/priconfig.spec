Name: priconfig
Summary: PRI configure script
Version: 0.1
Release: alt2
License: GPL3+
Group: System/Servers
BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%install
mkdir -p %buildroot/usr/sbin
install priconfig %buildroot%_sbindir/priconfig

%files
%_sbindir/priconfig

%changelog
* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- auto rebuild

* Sun Sep 16 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus
