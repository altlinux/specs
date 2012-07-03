Name: perl-Capture-Tiny
Version: 0.18
Release: alt1
Summary: Capture::Tiny - Capture STDOUT and STDERR from Perl, XS or external programs

Group: Development/Perl
License: Apache 2.0
Url: %CPAN Capture-Tiny

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Module-Build perl-Test-Differences

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Capture/Tiny*
%doc Changes Todo LICENSE README 

%changelog
* Thu May 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt1
- New version 0.18

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- New version 0.17

* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- New version 0.13

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- New version 0.10

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- New version 0.09

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- New version 0.08

* Sun Jan 31 2010 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- initial build
