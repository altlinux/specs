%define dist Data-Structure-Util
Name: perl-%dist
Version: 0.15
Release: alt2.2

Summary: Change nature of data within a structure
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-File-Find-Rule perl-Test-Pod

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
