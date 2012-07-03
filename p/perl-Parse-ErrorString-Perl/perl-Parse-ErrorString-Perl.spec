%define m_distro Parse-ErrorString-Perl
Name: perl-Parse-ErrorString-Perl
Version: 0.15
Release: alt1
Summary: parse error messages from the perl interpreter

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~szabgab/Parse-ErrorString-Perl/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Class-XSAccessor perl-Test-Differences perl-Module-Build perl-Pod-POM perl-podlators

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/check_perldiag
%perl_vendor_privlib/Parse/ErrorString/Perl*
%_man1dir/check_perldiag.*
%doc Changes README 

%changelog
* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt2
- fixed generation of man1 pages

* Mon Jan 25 2010 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- initial build
