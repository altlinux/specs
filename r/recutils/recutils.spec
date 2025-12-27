# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 1

Name: recutils
Version: 1.9
Release: alt1
Summary: Text-based databases called recfiles
License: GPL-3.0-or-later
Group: Databases
Url: https://https.git.savannah.gnu.org/git/recutils.git
Requires: librec%sover = %EVR

Source: %name-%version.tar
BuildRequires: flex
BuildRequires: gnulib
BuildRequires: help2man
BuildRequires: libgcrypt-devel
BuildRequires: libmdbtools-devel
BuildRequires: libuuid-devel
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: texinfo

%description
GNU Recutils is a set of tools and libraries to access human-editable
text-based databases called recfiles.

%package -n librec%sover
Summary: Shared library for %name
Group: System/Libraries

%description -n librec%sover
%summary.

%package -n librec-devel
Summary: Development files for librec
Group: Development/C
Requires: librec%sover = %EVR

%description -n librec-devel
%summary.

%prep
%setup

%build
./bootstrap \
	--gnulib-srcdir=/usr/share/gnulib \
	--no-bootstrap-sync \
	--no-git \
	--skip-po
%configure \
	--disable-rpath \
	--disable-static \
	%nil
%make_build

%install
%makeinstall_std

%check
./utils/recinf --version | grep -Fx 'recinf (GNU %name) %version'
%make_build check

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*rec*
%_man1dir/*rec*.1*
%_infodir/%name.info.*
%_datadir/%name

%files -n librec%sover
%doc COPYING
%_libdir/librec.so.%sover
%_libdir/librec.so.%sover.*

%files -n librec-devel
%_includedir/rec.h
%_libdir/librec.so

%changelog
* Sat Dec 27 2025 Vitaly Chikunov <vt@altlinux.org> 1.9-alt1
- First import v1.9-11-g0e4c96c (2025-10-30).
