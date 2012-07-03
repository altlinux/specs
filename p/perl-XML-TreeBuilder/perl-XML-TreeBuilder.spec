%define dist XML-TreeBuilder
Name: perl-%dist
Version: 3.09
Release: alt3.1

Summary: XML::TreeBuilder - Parser that builds a tree of XML::Element objects
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
Source: %dist-%version.tar
# Patch from Fedora package: perl-XML-TreeBuilder-3.09-11.fc9.src.rpm
Patch: XML-TreeBuilder-NoExpand.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Oct 07 2008
BuildRequires: perl-HTML-Tree perl-XML-Parser perl-devel

%description
This module uses XML::Parser to make XML document trees constructed of
XML::Element objects (and XML::Element is a subclass of HTML::Element
adapted for XML).  XML::TreeBuilder is meant particularly for people
who are used to the HTML::TreeBuilder / HTML::Element interface to
document trees, and who don't want to learn some other document
interface like XML::Twig or XML::DOM.

%prep
%setup -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
%dir	%perl_vendor_privlib/XML
	%perl_vendor_privlib/XML/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.09-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Oct 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 3.09-alt3
- enhanced Fedora patch (perl-XML-TreeBuilder-3.09-11.fc9.src.rpm):
  + Add ErrorContext pass through
  + Fix crash on Entity declaration. (RH #461557)

* Wed Oct 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 3.09-alt2
- applied Fedora patch to allow entities to pass thru un-expanded

* Tue Oct 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 3.09-alt1
- initial build for Sisyphus

