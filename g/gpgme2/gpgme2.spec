%define _unpackaged_files_terminate_build 1
%define gpgme_sover 45
%define libgpgme libgpgme%gpgme_sover
%define min_gnupg_version 2.2.41
%define gpg_bin_path %_bindir/gpg2
%define gpgsm_bin_path %_bindir/gpgsm
%def_disable beta
%def_disable static

Name: gpgme2
Version: 2.1.2
Release: alt1

Group: System/Libraries
Summary: GnuPG Made Easy core C library and tools
License: LGPL-2.1-or-later AND MIT
Url: https://www.gnupg.org/software/gpgme/index.html
Vcs: git://git.gnupg.org/gpgme.git

Requires: %gpg_bin_path
Conflicts: libgpgme-devel < 1.7

Source: gpgme-%version.tar
Patch1: alt-revision.patch

%{?_enable_static:BuildPreReq: glibc-devel-static}
BuildRequires: /proc gnupg2 libgpg-error-devel libassuan-devel glib2-devel texinfo

%package -n gpgme
Summary: GnuPG Made Easy tools
Group: System/Libraries
Requires: %gpg_bin_path
Requires: %name-common >= %EVR

%description -n gpgme
GPGME tools and runtime helpers for applications using GnuPG.

%package common
Summary: GPGME common files
Group: System/Configuration/Other
Conflicts: libgpgme < 1.7

%description common
Common documentation and shared files for GPGME packages.

%package -n %libgpgme
Group: System/Libraries
Summary: GPGME C library
Requires: %name-common >= %EVR
Requires: %gpg_bin_path

%description -n %libgpgme
GPGME C library.

%package devel
Summary: Include files for development with GPGME
Group: Development/C
Requires: libgpg-error-devel
#
Conflicts: gpgme1-devel

%description devel
This package contains include files required for development of
GPGME-based applications using the C API.

%package devel-static
Summary: Static libraries for development with GPGME
Group: Development/C
Requires: gpgme2-devel

%description devel-static
Static libraries required for development with GPGME.

%description
GPGME is a C language library that allows applications to use GnuPG.
This source package builds the GPGME 2.x core C library and tools.

%prep
%setup -n gpgme-%version
%patch1 -p1

%if_disabled beta
sed -i -e 's/@BETA@/no/' configure.ac
%else
sed -i -e 's/@BETA@/yes/' configure.ac
%endif
sed -i -e 's/@REVISION@/1/' -e 's/@REVISION_DESC@/ALT/' configure.ac
sed -i -e 's/@COMMITID@/1/' -e 's/@COMMITID@/ALT/' configure.ac
%autoreconf

%build
mkdir -p tmp_bin
ln -sf %_bindir/gpg2 tmp_bin/gpg
export PATH=$PWD/tmp_bin:$PATH
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure \
	--disable-silent-rules \
	%{subst_enable static} \
	--disable-fd-passing \
	--with-gpg=%gpg_bin_path \
	--with-gpgsm=%gpgsm_bin_path
%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std

%check
export PATH=$PWD/tmp_bin:$PATH
%make_build -k check

%files -n gpgme
%_bindir/gpgme-tool
%_bindir/gpgme-json
%_bindir/gnupg-key-manage
%_man1dir/gpgme-json.1.*

%files common
%doc AUTHORS NEWS README THANKS

%files devel
%_bindir/gpgme-config
%_includedir/gpgme.h
%_libdir/libgpgme.so
%_datadir/aclocal/gpgme.m4
%_infodir/*.info*
%_datadir/common-lisp/source/gpgme/
%_pkgconfigdir/gpgme*.pc

%if_enabled static
%files devel-static
%_libdir/libgpgme.a
%endif

%files -n %libgpgme
%_libdir/libgpgme.so.%gpgme_sover
%_libdir/libgpgme.so.*

%changelog
* Thu Jul 09 2026 Sergey V Turchin <zerg@altlinux.org> 2.1.2-alt1
- initial build
