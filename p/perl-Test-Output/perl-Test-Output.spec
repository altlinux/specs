%define module Test-Output

Name: perl-%module
Version: 1.01
Release: alt1

Summary: Utilities to test STDOUT and STDERR messages
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Test/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Sub-Exporter perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Tester

%description
Test::Output provides a simple interface for testing output sent to STDOUT or
STDERR. A number of different utilities are included to try and be as flexible
as possible to the tester.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/

%changelog
* Wed Apr 27 2011 Victor Forsiuk <force@altlinux.org> 1.01-alt1
- 1.01

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- Initial build.
