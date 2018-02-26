%define dist XML-TokeParser
Name: perl-%dist
Version: 0.05
Release: alt1.1

Summary: Simplified interface to XML::Parser
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/P/PO/PODMASTER/XML-TokeParser-0.05.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: perl-XML-Parser perl-devel

%description
XML::TokeParser provides a procedural ("pull mode") interface to
XML::Parser in much the same way that Gisle Aas' HTML::TokeParser
provides a procedural interface to HTML::Parser. XML::TokeParser splits
its XML input up into "tokens," each corresponding to an XML::Parser
event.

A token is a bless'd reference to an array whose first element is an
event-type string and whose last element is the literal text of the XML
input that generated the event, with intermediate elements varying
according to the event type.

Each token is an *object* of type XML::TokeParser::Token. Read
"XML::TokeParser::Token" to learn what methods are available for
inspecting the token, and retrieving data from it.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README TODO
%perl_vendor_privlib/XML/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.05-alt1
- initial build for Sisyphus

