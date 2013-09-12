%define _unpackaged_files_terminate_build 1
%define dist Error

Name: perl-%dist
Version: 0.17021
Release: alt1

Summary: Error - Error/exception handling in an OO-ish way

License: Artistic
Group: Development/Perl
Url: %CPAN Error

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/S/SH/SHLOMIF/Error-%{version}.tar.gz

# Automatically added by buildreq on Thu Sep 01 2005
BuildRequires: perl-devel perl-Module-Build

%description
The "Error" package provides two interfaces. Firstly "Error" provides
a procedural interface to exception handling. Secondly "Error" is a
base class for errors/exceptions that can either be thrown, for
subsequent catch, or can simply be recorded.

Errors in the class "Error" should not be thrown directly, but the
user should throw errors from a sub-class of "Error".

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README examples
%perl_vendor_privlib/Error*

%changelog
* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.17021-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.17020-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17018-alt1
- 0.17016 -> 0.17018
- fixed build with perl-5.16
- packaged Error::Simple module

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.17016-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.17016-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt2
- fix directory ownership violation

* Thu Sep 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- first build for ALT Linux Sisyphus
