## SPEC file for Perl module Test::MockObject

Name: perl-Test-MockObject
Version: 1.20110612
Release: alt1

Summary: Perl extension for emulating troublesome interfaces

License: %perl_license
Group: Development/Perl

%define real_name Test-MockObject
URL: http://search.cpan.org/dist/Test-MockObject/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Jun 21 2011
# optimized out: perl-Sub-Uplevel perl-Tree-DAG_Node perl-devel
BuildRequires: perl-CGI perl-Test-Exception perl-Test-Warn perl-UNIVERSAL-can perl-UNIVERSAL-isa

%description
Perl module Test::MockObject allows to create objects that conform to particular
interfaces with very little code.  With it there are  no need to reimplement the 
behavior,  just the input and the output.  This module can be used for different
test purposes.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test/MockObject*


%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.20110612-alt1
- New version 1.20110612

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.09-alt1
- New version 1.09

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.08-alt1
- New version 1.08
  - removed noisy diag() calls from successful tests (RT #19444, Adam Kennedy)
  - removed some magic from the @ISA assignment to work with 5.9.5 (Andreas Koenig)

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.07-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.07-alt0
- Initial build
