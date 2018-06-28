%define _unpackaged_files_terminate_build 1
%define sname text-brew

Name: perl-Text-Brew
Version: 0.02
Release: alt1
Summary: Implementation of the Brew edit distance
# License specified in README
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Text-Brew/
Source0: %sname-%version.tar
BuildArch: noarch

BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(warnings.pm)

Requires: perl(Carp.pm)

%description
This module implements the Brew edit distance that is very close to the
dynamic programming technique used for the Wagner-Fischer (and so for the
Levenshtein) edit distance.

%prep
%setup -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendorlib/Text*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.02-alt1
- initial build for ALT
