%define dist XML-SimpleObject
Name: perl-%dist
Version: 0.53
Release: alt2

Summary: A simple object representation of a parsed XML::Parser tree
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-XML-Parser perl-devel

%description
This is a small and simple package that takes the output of an XML parser
and gives simple methods for accessing the structure of an XML document.
It is very lightweight, but provides the simplest access to an XML document
possible. It does not subclass XML::Parser or XML::LibXML; rather, it is
meant to serve purely as an object struct for an outgoing tree.

%prep
%setup -q -n %dist%version
rm -r LibXML/

%build 
%perl_vendor_build

%install 
%perl_vendor_install
rm %buildroot%perl_vendor_privlib/XML/ex.pl

%files
%doc Changes README ex.pl
%perl_vendor_privlib/XML

%changelog
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.53-alt2
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.53-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Jun 26 2003 Grigory Milev <week@altlinux.ru> 0.53-alt1
- new version released
- spec fixed due new macros

* Wed Apr 10 2002 Grigory Milev <week@altlinux.ru> 0.51-alt1
- new version released

* Thu Dec 13 2001 Grigory Milev <week@altlinux.ru> XML-SimpleObject
- Initial build for ALT Linux distribution.
