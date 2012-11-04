## SPEC file for Perl module Test::File::ShareDir

Name: perl-Test-File-ShareDir
Version: 0.3.1
Release: alt1

Summary: Create a Fake ShareDir for your modules for testing

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Test-File-ShareDir/
#URL: https://github.com/kentfredric/Test-File-ShareDir

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Test-File-ShareDir
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Nov 04 2012
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Class-Inspector perl-Encode perl-IPC-Run3 perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Probe-Perl perl-Try-Tiny perl-devel perl-podlators
BuildRequires: perl-File-Copy-Recursive perl-File-ShareDir perl-HTML-Parser perl-Module-Build perl-Path-Class perl-Test-Fatal perl-Test-Script

%description
Test::File::ShareDir is a Perl module to create a Fake ShareDir
for your modules for testing.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test/File/ShareDir*


%changelog
* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux Sisyphus

