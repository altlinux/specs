## SPEC file for Perl module Unicode::Stringprep

%define real_name Unicode-Stringprep

Name: perl-Unicode-Stringprep
Version: 1.103
Release: alt1.1

Summary: Perl module for preparation of Internationalized Strings

License: %perl_license
Group: Development/Perl
BuildArch: noarch

URL: http://search.cpan.org/~cfaerber/Unicode-Stringprep/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Mar 23 2010
BuildRequires: perl-Module-Build perl-Test-NoWarnings perl-Test-Pod perl-Test-Pod-Coverage perl-Unicode-Normalize

%description
Perl module Unicode::Stringprep implements the stringprep
framework for preparing Unicode text strings in order to
increase the likelihood that string input and string
comparison work in ways that make sense for typical users
throughout the world.  The stringprep protocol is useful
for protocol identifier values, company and personal
names, internationalized domain names, and other text strings.

The stringprep framework does not specify how protocols should
prepare text strings. Protocols must create profiles of
stringprep in order to fully specify the processing options.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Unicode/Stringprep*


%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.103-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Mar 23 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.103-alt1
- Initial build for ALT Linux Sisyphus
