## SPEC file for Perl module File::ShareDir::Install

%define real_name File-ShareDir-Install

Name: perl-File-ShareDir-Install
Version: 0.14
Release: alt1

Summary: Perl extension for installing shared files

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/File-ShareDir-Install/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Aug 14 2016
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-JSON-PP perl-Module-Load perl-Module-Metadata perl-Parse-CPAN-Meta perl-Term-ANSIColor perl-devel python-base python-modules python3
BuildRequires: perl-Module-Build-Tiny perl-Pod-Coverage perl-YAML perl-autodie

%description
Perl module File::ShareDir::Install allows you to install
read-only data files from a distribution. It is a companion
module to File::ShareDir, which allows you to locate these
files after installation.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/File/ShareDir/Install*

%changelog
* Sun Dec 04 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.14-alt1
- New version

* Thu May 03 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.13-alt1
- New version

* Sat Apr 21 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.12-alt1
- New version

* Sun Aug 14 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt1
- New version

* Fri Jan 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.04-alt1
- Initial build for ALT Linux Sisyphus
