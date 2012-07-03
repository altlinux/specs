%define dist Config-General
Name: perl-%dist
Version: 2.50
Release: alt1

Summary: Generic Config Module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TL/TLINDEN/Config-General-2.50.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 27 2010
BuildRequires: perl-devel

%description
This module opens a config file and parses it's contents
for you. After parsing the module returns a hash structure
which contains the representation of the config file.

The format of config files supported by Config::General is
inspired by the well known apache config format, in fact,
this module is 100%% read-compatible to apache configs, but
you can also just use simple name/value pairs in your config
files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changelog README
%perl_vendor_privlib/Config*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.50-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.49-alt1
- automated CPAN update

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 2.48-alt1
- 2.42 -> 2.48

* Sun Jul 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.42-alt1
- NMU: new version 2.42 (with rpmrb script)

* Sat Mar 25 2006 Andrey Brindeew <abr@altlinux.org> 2.31-alt1
- 2.31

* Sat Aug 27 2005 Andrey Brindeew <abr@altlinux.org> 2.29-alt1
- 2.29

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 2.27-alt1
- 2.24 -> 2.27

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 2.24-alt1
- 2.24 release

* Mon Oct 06 2003 Andrey Brindeew <abr@altlinux.ru> 2.23-alt1
- 2.23 release
- Packager tag updated
- Url tag added

* Tue Jul 01 2003 Dmitry V. Levin <ldv@altlinux.org> 2.18-alt2
- Rebuilt to fix dependencies broken by rpm-build-4.0.4-alt16.

* Wed Apr 23 2003 Sir Raorn <raorn@altlinux.ru> 2.18-alt1
- Built for Sisyphus
