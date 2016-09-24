%define _unpackaged_files_terminate_build 1
%define dist CPAN-Meta
Name: perl-%dist
Version: 2.150010
Release: alt2

Summary: The distribution metadata for a CPAN dist
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-CPAN-Meta-Requirements perl-Parse-CPAN-Meta perl-Test-Script

%description
Software distributions released to the CPAN include a META.json or,
for older distributions, META.yml, which describes the distribution,
its contents, and the requirements for building and installing the
distribution.  The data structure stored in the META.json file is
described in CPAN::Meta::Spec.

CPAN::Meta provides a simple class to represent this distribution
metadata (or distmeta), along with some helpful methods for
interrogating that data.

%package -n perl-Parse-CPAN-Meta
Summary: Parse::CPAN::Meta - Parse META.yml and META.json CPAN metadata files
Group: Development/Perl
# loaded with _can_load
Requires: perl-JSON-PP

%description -n perl-Parse-CPAN-Meta
Parse::CPAN::Meta is a parser for META.json and META.yml files, 
using JSON::PP and/or CPAN::Meta::YAML.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CPAN

%files -n perl-Parse-CPAN-Meta
%perl_vendor_privlib/Parse

%changelog
* Sat Sep 24 2016 Igor Vlasenko <viy@altlinux.ru> 2.150010-alt2
- added perl-Parse-CPAN-Meta subpackage (closes: #32523)

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.150010-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.150005-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 2.150001-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.143240-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.142690-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 2.142060-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 2.141520-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 2.141170-alt1
- automated CPAN update

* Fri Oct 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.132830-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.132661-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 2.132620-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.132510-alt1
- automated CPAN update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.132140-alt1
- automated CPAN update

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.131560-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.120921-alt1
- 2.120351 -> 2.120921

* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.120351-alt1
- New version

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 2.112621-alt1
- initial revision
