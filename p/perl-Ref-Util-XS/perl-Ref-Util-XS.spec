## SPEC file for Perl module Ref::Util::XS

%define real_name Ref-Util-XS

Name: perl-Ref-Util-XS
Version: 0.116
Release: alt1.1

Summary: XS implementation for Ref::Util Perl module

License: %mit
Group: Development/Perl

URL: http://search.cpan.org/dist/Ref-Util-XS/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Jun 10 2017
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-Parse-CPAN-Meta python-base python-modules python3 python3-base
BuildRequires: perl-CPAN-Meta perl-Readonly perl-devel

%description
Perl module Ref::Util::XS is the XS implementation of Ref::Util,
which provides several functions to help identify references in
a more convenient way than the usual approach of examining
the return value of ref.

You should use Ref::Util::XS by installing Ref::Util itself,
Ref::Util::XS provides a significant speed boost to everything
that uses Ref::Util.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Ref/Util/XS*
%perl_vendor_autolib/Ref/Util/XS*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.116-alt1.1
- rebuild with new perl 5.26.1

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.116-alt1
- Initial build for ALT Linux Sisyphus
