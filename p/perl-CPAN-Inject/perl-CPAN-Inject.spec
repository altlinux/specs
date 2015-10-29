%define dist CPAN-Inject
Name: perl-CPAN-Inject
Version: 1.14
Release: alt2

Summary: CPAN::Inject - Base class for injecting distributions into CPAN sources
Group: Development/Perl
License: Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz
# https://rt.cpan.org/Ticket/Attachment/1409633/748202/CPAN-Inject-1.14-Expect-unknown-exception-while-loading-CPAN-configur.patch
Patch: CPAN-Inject-1.14-Expect-unknown-exception-while-loading-CPAN-configur.patch

BuildArch: noarch
BuildRequires: perl-Test-Script perl-devel perl-CPAN-Checksums perl-CPAN perl-File-Remove perl-Params-Util perl-File-chmod perl-podlators

%description
%summary

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/cpaninject
%perl_vendor_privlib/CPAN/Inject*
%_man1dir/cpaninject.*
%doc Changes

%changelog
* Thu Oct 29 2015 Vladimir Lettiev <crux@altlinux.ru> 1.14-alt2
- Fixed FTBFS (applied patch from RT#98774)

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.14-alt1
- 1.13 -> 1.14

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 1.13-alt1
- New version 1.13

* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt2
- Fixed generation of man1 pages

* Thu Jan 28 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
