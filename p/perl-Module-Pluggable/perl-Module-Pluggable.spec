%define dist Module-Pluggable
Name: perl-%dist
Version: 3.9
Release: alt2

Summary: Automatically give your module the ability to have plugins
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-devel

%description
Provides a simple but, hopefully, extensible way of having 'plugins'
for your module.

%prep
%setup -n %dist-%version

# disable archlib hack
sed -i- '/INST_LIB/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Module
%perl_vendor_privlib/Devel

%changelog
* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 3.9-alt2
- noarch

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.9-alt1.1
- rebuilt with perl 5.12

* Sun Jul 25 2010 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt1
- new version 3.9 (with rpmrb script)
- build as noarch, fix spec

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.97-alt1
- fix directory ownership violation

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.97-alt0.1
- new version 2.97 (with rpmrb script)

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 2.95-alt1
- new version

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt1
- first build for ALT Linux Sisyphus
