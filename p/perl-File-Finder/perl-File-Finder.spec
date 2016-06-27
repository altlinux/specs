## SPEC file for Perl module File::Finder

%define real_name File-Finder

Name: perl-File-Finder
Version: 0.53
Release: alt2

Summary: wrapper for File::Find module

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/File-Finder/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: perl perl-Devel-Symdump perl-Encode perl-Number-Compare perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Text-Glob perl-devel python-base python-modules python3
BuildRequires: libnss-mymachines perl-File-Find-Rule perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module File::Finder nice wrapper for File::Find ala
find(1).

File::Find is great, but constructing the wanted routine can
sometimes be a pain.  This module provides a wanted-writer,
using syntax that is directly mappable to the find command's
syntax.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/File/Finder*

%changelog
* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.53-alt2
- Initial build for ALT Linux Sisyphus
