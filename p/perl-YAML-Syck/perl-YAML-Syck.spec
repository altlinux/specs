%define _unpackaged_files_terminate_build 1
%define module YAML-Syck

Name: perl-%module
Version: 1.30
Release: alt1.1

Summary: Fast, lightweight YAML loader and dumper
License: MIT
Group: Development/Perl

URL: %CPAN %module
Source0: http://www.cpan.org/authors/id/T/TO/TODDR/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Devel-Leak perl-JSON perl-Pod-Escapes perl-devel

%description
This module provides a Perl interface to the libsyck data serialization
library. It exports the Dump and Load functions for converting Perl data
structures to YAML strings, and the other way around.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/JSON
%perl_vendor_archlib/YAML
%perl_vendor_autolib/YAML

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1.1
- rebuild with new perl 5.22.0

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.27-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.27-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt1
- 1.17 -> 1.20
- built for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.17-alt2
- rebuilt for perl-5.14
- packaged JSON::Syck

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.15-alt1.1
- rebuilt with perl 5.12

* Tue Oct 12 2010 Victor Forsiuk <force@altlinux.org> 1.15-alt1
- 1.15
- License is MIT.

* Tue Sep 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.85-alt2
- fixed perl dir ownership

* Thu May 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1
- first build for ALT Linux Sisyphus
