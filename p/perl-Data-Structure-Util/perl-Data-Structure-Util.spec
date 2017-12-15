%define _unpackaged_files_terminate_build 1
%define dist Data-Structure-Util
Name: perl-%dist
Version: 0.16
Release: alt1.1.1.1

Summary: Change nature of data within a structure
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AN/ANDYA/Data-Structure-Util-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-File-Find-Rule perl-Test-Pod perl-CPAN-Meta

%description
Data::Structure::Util is a toolbox to manipulate the data inside a
data structure. It can process an entire tree and perform the operation
requested on each appropriate element.

For example: It can transform all strings within a data structure to
utf8 or transform any utf8 string back to the default encoding. It can
remove the blessing on any reference. It can collect all the objects or
detect if there is a circular reference.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.22.0

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt6.1
- rebuild with new perl 5.20.1

* Fri Dec 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt6
- Remove test cases which failed for Perl 5.19.4 and higher (RT#88257)

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt5
- built for perl 5.18

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt4
- fixed build

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt3
- rebuilt for perl-5.16
- perl-CPAN-Meta required for build

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt2.2
- rebuilt for perl-5.14

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt2.1
- rebuilt with perl 5.12

* Sun Jul 12 2009 Michael Bochkaryov <misha@altlinux.ru> 0.15-alt2
- fix Url tag
- docs added

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- NMU fixing directory ownership violation

* Sat Mar 15 2008 Michael Bochkaryov <misha@altlinux.ru> 0.15-alt1
- 0.15 version;
- remove Clone dependency;
- use Storable::freeze for signature generation

* Wed Jan 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.12-alt1
- initial build for ALT Linux

* Mon Jul 02 2007 Valentyn Solomko <pere@pere.org.ua> 0.12-alt0
- build for Net Style internal repository
