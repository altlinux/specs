Name: specgen
Version: 0.0.3
Release: alt1
BuildArch: noarch
Summary: Create spec file from multiple specs
Group: Development/Other
License: GPL

Url: http://sisyphus.ru/ru/srpm/Sisyphus/specgen

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

%files
%_bindir/*
%perl_vendor_privlib/Specgen
#perl_vendor_archlib/*
#perl_vendor_autolib/*
#perl_vendor_man3dir/*

%changelog
* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- some more fixes 

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- more correct support for ifarch/if_with

* Wed Dec 02 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

