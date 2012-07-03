## SPEC file for Perl module Devel::CheckLib

%define real_name Devel-CheckLib

Name: perl-Devel-CheckLib
Version: 0.91
Release: alt1

Summary: check that a library is available

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/~tonyc/Devel-CheckLib/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses

%description
Perl module Devel::CheckLib provides a way of checking whether
a particular library and its headers are available, by
attempting to compile a simple program and link against it.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%exclude /.perl.req
%_bindir/use-devel-checklib
%perl_vendor_privlib/Devel/CheckLib*

%changelog
* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.91-alt1
- Initial build for ALT Linux Sisyphus
