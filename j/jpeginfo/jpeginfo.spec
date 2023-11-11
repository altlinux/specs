%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: jpeginfo
Version: 1.7.1
Release: alt1
Summary: Prints information and tests integrity of JPEG/JFIF files
License: GPL-3.0-or-later
Group: Graphics
Url: https://www.kokkonen.net/tjko/projects.html
Vcs: https://github.com/tjko/jpeginfo

Source: %name-%version.tar

# REQUIREMENTS
#   Independent JPEG Group's jpeg library (libjpeg) version 6b or later.
#  (Alternatively should also work with libjpeg-turbo or mozjpeg)

BuildRequires: libjpeg-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: python3
}}

%description
Utility to generate informative listings from jpeg files, and to check jpeg
files for errors. Program also supports automagic deletion of broken jpegs.

%prep
%setup

%build
%ifarch x86_64
%add_optflags -fanalyzer
%endif
%add_optflags %(getconf LFS_CFLAGS)
%configure
%make_build

%install
%makeinstall_std install

%check
%make_build test

%files
%define _customdocdir %_docdir/%name
%doc COPYRIGHT LICENSE README
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Nov 11 2023 Vitaly Chikunov <vt@altlinux.org> 1.7.1-alt1
- Update to v1.7.1 (2023-10-29).

* Sat Mar 17 2012 Victor Forsiuk <force@altlinux.org> 1.6.1-alt1
- Initial build.
