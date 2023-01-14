## SPEC file for Perl module Throwable

Name: perl-Throwable
Version: 1.001
Release: alt1

Summary: Perl role for classes that are meant to be thrown as exceptions

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Throwable/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Throwable
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Tue Mar 09 2021
# optimized out: perl perl-CPAN-Meta-Requirements perl-Class-Method-Modifiers perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Role-Tiny perl-Sub-Quote perl-parent python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Devel-StackTrace perl-Module-Runtime perl-Moo perl-devel

%description
Perl module Throwable is a role for classes that are meant to be
thrown as exceptions to standard program flow. It is very simple
and does only two things: saves any previous value for $@ and
calls die $self.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Throwable*
%perl_vendor_privlib/StackTrace*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.001-alt1
- New version

* Sun Jun 27 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.000-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.200013-alt2
- Update BuildRequires

* Tue Aug 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.200013-alt1
- New version

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.200012-alt1
- New version

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.200011-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.200009-alt1
- New version

* Sat Aug 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.200008-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.102080-alt1
- Initial build for ALT Linux Sisyphus

