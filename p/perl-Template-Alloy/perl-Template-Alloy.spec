## SPEC file for Perl module Template::Alloy

%define real_name Template-Alloy

Name: perl-Template-Alloy
Version: 1.016
Release: alt1

Summary: TT2/3, HT, HTE, Tmpl, and Velocity Engine

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Template-Alloy/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: perl-Encode perl-devel
BuildRequires: perl-Template

%description
Perl module Template::Alloy represents the mixing of features
and capabilities from all of the major mini-language based
template systems. With Template::Alloy you can use your
favorite template interface and syntax and get features from
each of the other major template systems. And Template::Alloy
is fast - whether your using mod_perl, cgi, or running from
the commandline.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Template/Alloy*

%changelog
* Tue Oct 11 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.016-alt1
- Initial build for ALT Linux Sisyphus
