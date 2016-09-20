%define _unpackaged_files_terminate_build 1
%define dist Business-ISBN
Name: perl-%dist
Version: 3.003
Release: alt1

Summary: work with International Standard Book Numbers

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

Packager: Vladimir A. Svyatoshenko <svyt@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BD/BDFOY/Business-ISBN-%{version}.tar.gz

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
* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.07-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

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

