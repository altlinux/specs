## SPEC file for Perl module Sub::Attribute

%define real_name Sub-Attribute

Name: perl-Sub-Attribute
Version: 0.07
Release: alt2

Summary: Reliable subroutine attribute handlers

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Sub-Attribute

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 04 2019
# optimized out: gem-power-assert glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel perl perl-CPAN-Meta-Requirements perl-Devel-Symdump perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Class-Trigger perl-MRO-Compat perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Sub::Attribute is a role to define attribute handlers
for specific subroutine attributes.

The feature of this module is similar to that of Attribute::Handlers,
but has less functionality and more reliability. That is, while
Attribute::Handlers provides many options for ATTR(CODE),
Sub::Attribute provides no options for ATTR_SUB. However, the attribute
handlers defined by Sub::Attribute are always called with informative
arguments. Attribute::Handlers's ATTR(CODE) is not called in run-time
eval(), so ATTR(CODE) is not reliable.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGELOG
%perl_vendor_archlib/Sub/Attribute*
%perl_vendor_autolib/Sub/Attribute*

%changelog
* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.07-alt2
- Bump release to override autoimport package

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.07-alt1
- Initial build for ALT Linux Sisyphus
