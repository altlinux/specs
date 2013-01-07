%define dist Business-ISBN
Name: perl-%dist
Version: 2.05_03
Release: alt1

Summary: work with International Standard Book Numbers

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

Packager: Vladimir A. Svyatoshenko <svyt@altlinux.ru>

BuildArch: noarch
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Jun 11 2007
BuildRequires: perl-Business-ISBN-Data perl-devel perl-libwww

%description
None.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Business*

%changelog
* Mon Jan 07 2013 Vladimir Lettiev <crux@altlinux.ru> 2.05_03-alt1
- 2.05 -> 2.05_03

* Wed Sep 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 2.03-alt1
- new version
- fixed build

* Mon Jun 11 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.84-alt1
- first build for ALT Linux Sisyphus

