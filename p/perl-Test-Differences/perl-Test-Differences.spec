%define module Test-Differences

Name: perl-%module
Version: 0.61
Release: alt1
Serial: 1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Test strings and data structures and show differences if not ok
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/O/OV/OVID/Test-Differences-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Diff

%description
Test strings and data structures and show differences if not ok.

%prep
%setup -n %module-%version

# hack; remove if perl version > 5.12.3
sed -i "s,2\.126,2.125," Makefile.PL Build.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test

%changelog
* Wed Sep 21 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.61-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.500-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.500-alt1
- 0.500

* Fri Jul 27 2007 Victor Forsyuk <force@altlinux.org> 0.47-alt2
- Spec cleanups.

* Thu Aug 25 2005 Alexey Morozov <morozov@altlinux.org> 0.47-alt1
- Initial build for ALT Linux
