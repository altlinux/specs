%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): perl(ExtUtils/MakeMaker.pm) perl(LWP/UserAgent.pm) perl(XML/DOM.pm) perl(XML/Parser.pm) perl(XML/Parser/PerlSAX.pm) perl(XML/RegExp.pm)
# END SourceDeps(oneline)
%define module_version 0.13
%define module_name XML-Checker
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.13
Release: alt1.1
Summary: A perl module for validating XML
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TJ/TJMATHER/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
XML::Checker can be used in different ways to validate XML. See the manual
pages of the XML::Checker::Parser manpage and the XML::DOM::ValParser manpage
for more information. 

This document only describes common topics like error handling
and the XML::Checker class itself.

WARNING: Not all errors are currently checked. Almost everything is subject to
change. Some reported errors may not be real errors.  For production code,
it is recommended that you use the XML::LibXML manpage or the XML::GDOME manpage instead of
the XML::Checker manpage.  Both modules share the same DTD validation code with libxml2
and the XML::LibXML manpage is easier to install.

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/X*

%changelog
* Fri Dec 09 2022 Igor Vlasenko <viy@altlinux.org> 0.13-alt1.1
- to Sisyphus (closes: #44588)

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- initial import by package builder

