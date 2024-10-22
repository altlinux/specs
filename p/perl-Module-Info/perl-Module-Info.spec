## SPEC file for Perl module Module::Info

%define real_name Module-Info

Name: perl-Module-Info
Version: 0.39
Release: alt1

Summary: Information about Perl modules

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Module-Info/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sat Nov 07 2015
# optimized out: perl-B-Utils perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-devel perl-podlators perl-threads
BuildRequires: perl-Module-Info perl-Test-Pod perl-Text-Soundex perl-podlators

%description
Perl module Module::Info gives an information about Perl modules
without actually loading the module. It actually isn't specific
to modules and should work on any perl code.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Module/Info*
%perl_vendor_privlib/B*
%_bindir/pfunc
%_bindir/module_info
%_man1dir/*

%changelog
* Tue Oct 22 2024 Nikolay A. Fetisov <naf@altlinux.org> 0.39-alt1
- New version

* Sat Nov 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.37-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.36-alt1
- New version

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.35-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.33-alt1
- New version

* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.32-alt1
- Initial build for ALT Linux Sisyphus
