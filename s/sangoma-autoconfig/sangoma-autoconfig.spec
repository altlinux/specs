Name: sangoma-autoconfig
Version: 0.1
Release: alt2
BuildArch: noarch
Summary: Create config files for Sangoma cards
Group: System/Kernel and hardware
License: GPL

Url: http://sisyphus.ru/ru/srpm/Sisyphus/sangoma-autoconfig

Requires: wanpipe

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Fri Sep 18 2009 (-bb)
BuildRequires: perl-devel

%description
%summary

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install
install -D -m644 config-default %buildroot%_sysconfdir/wanpipe/config.txt

%files
%_bindir/*
%perl_vendor_privlib/Mithraen
#perl_vendor_archlib/*
#perl_vendor_autolib/*
#perl_vendor_man3dir/*
%_sysconfdir/wanpipe/config.txt

%changelog
* Sat Oct 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- add Url tag

* Wed Oct 21 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

