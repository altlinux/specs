Name: perl-Sys-Utmp
Version: 1.8
Release: alt1

Summary: Perl interface to UTMP entries
License: Artistic-1.0 OR GPL-2.0-or-later
Group: Development/Perl

URL: https://github.com/jonathanstowe/Sys-Utmp

Source: %name-%version.tar

Patch0001: 0001-Fix-the-test-suite-to-not-die-if-the-utmp-file-is-em.patch

%define _unpackaged_files_terminate_build 1

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Encode
BuildRequires: perl-Test-Pod
BuildRequires: perl-Test-Pod-Coverage
BuildRequires: perl-devel

%description
This module provides a Perl interface to UTMP entries.

%prep
%setup -q
%autopatch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Sys/Utmp.pm
%perl_vendor_archlib//Sys/Utmp/Utent.pm
%perl_vendor_autolib/Sys/Utmp/Utmp.so

%changelog
* Sun Aug 13 2023 Alexey Gladkov <legion@altlinux.ru> 1.8-alt1
- First Altlinux release.

