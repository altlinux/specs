Name: perl-PPIx-EditorTools
Version: 0.15
Release: alt1
Summary: PPIx::EditorTools - Utility methods and base class for manipulating Perl

Group: Development/Perl
License: Perl
Url: %CPAN PPIx-EditorTools

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Test-Differences perl-Class-XSAccessor perl-PPI perl-Test-Most perl-Test-Warn perl-Test-Exception perl-Test-Deep

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/PPIx/EditorTools*
%doc Changes

%changelog
* Wed Oct 26 2011 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11
- Few perl-Test-* required for tests

* Fri Oct 01 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- New version 0.10

* Mon Jan 25 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build
