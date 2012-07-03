%define m_distro CPAN-Inject
Name: perl-CPAN-Inject
Version: 1.13
Release: alt1
Summary: CPAN::Inject - Base class for injecting distributions into CPAN sources

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/CPAN-Inject/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Test-Script perl-devel perl-CPAN-Checksums perl-CPAN perl-File-Remove perl-Params-Util perl-File-chmod perl-podlators

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
# disabled tests: http://bugs.debian.org/560647
%def_without test
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/cpaninject
%perl_vendor_privlib/CPAN/Inject*
%_man1dir/cpaninject.*
%doc Changes README 

%changelog
* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 1.13-alt1
- New version 1.13

* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt2
- Fixed generation of man1 pages

* Thu Jan 28 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
