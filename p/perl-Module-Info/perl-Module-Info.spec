## SPEC file for Perl module Module::Info

%define real_name Module-Info

Name: perl-Module-Info
Version: 0.32
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

# Automatically added by buildreq on Sun Nov 04 2012
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Devel-Symdump perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-podlators perl-threads
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Soundex

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

%changelog
* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.32-alt1
- Initial build for ALT Linux Sisyphus
