%define _unpackaged_files_terminate_build 1
%define sname XML-SemanticDiff

Name: perl-XML-SemanticDiff
Version: 1.0007
Release: alt1
Summary: Perl extension for comparing XML documents
License: GPL+ or Artistic
Group: Development/Perl
Url: https://metacpan.org/release/XML-SemanticDiff
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl(XML/Parser.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/TrailingSpace.pm)

%description
XML::SemanticDiff provides a way to compare the contents and structure of two
XML documents. By default, it returns a list of hashrefs where each hashref
describes a single difference between the two docs.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/XML*
%doc Changes LICENSE META.json META.yml  README eg

%changelog
* Mon Apr 08 2019 Alexandr Antonov <aas@altlinux.org> 1.0007-alt1
- initial build for ALT
