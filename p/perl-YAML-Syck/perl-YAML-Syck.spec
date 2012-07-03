%define module YAML-Syck

Name: perl-%module
Version: 1.17
Release: alt2

Summary: Fast, lightweight YAML loader and dumper
License: MIT
Group: Development/Perl

URL: %CPAN %module
Source: %module-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Devel-Leak perl-JSON perl-Pod-Escapes perl-devel

%description
This module provides a Perl interface to the libsyck data serialization
library. It exports the Dump and Load functions for converting Perl data
structures to YAML strings, and the other way around.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/JSON
%perl_vendor_archlib/YAML
%perl_vendor_autolib/YAML

%changelog
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
