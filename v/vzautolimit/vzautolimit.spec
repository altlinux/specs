#define module asterisk-perl
#define m_distro asterisk-perl
#define m_name asterisk-perl
#define m_author_id unknown
#define _enable_test 1

Name: vzautolimit
Version: 0.01
Release: alt3

Summary: Simple utility for autoconfig OpenVZ limits

License: %gpl2plus
Group: Development/Perl

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildPreReq: rpm-build-licenses

BuildArch: noarch
Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Nov 07 2007 (-bi)
BuildRequires: perl-DBD-SQLite perl-devel

BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n %name-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
mkdir -p %buildroot/var/spool/%name
touch %buildroot/var/spool/%name/cache.db

%files
%_bindir/vzautolimit
%perl_vendor_privlib/Mithraen*
#perl_vendor_man3dir/*
%dir /var/spool/%name
%ghost /var/spool/%name/cache.db

%changelog
* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.01-alt3
- rebuild

* Mon Oct 20 2008 Denis Smirnov <mithraen@altlinux.ru> 0.01-alt2
- fix building

* Wed Nov 07 2007 Denis Smirnov <mithraen@altlinux.ru> 0.01-alt1
- first build for Sisyphus

