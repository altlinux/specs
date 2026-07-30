%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without static

Name: poke
Version: 4.3
Release: alt1

%define sover 1

Summary: Extensible editor for structured binary data

License: GPLv3+
Group: Development/Other
URL: http://www.jemarch.net/poke.html
#URL: https://git.savannah.gnu.org/cgit/poke.git

Source0: https://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source2: %name.watch
Source3: upstream-signing-key.asc

Requires: lib%name%sover = %version-%release

BuildRequires(pre): rpm-macros-valgrind

# Automatically added by buildreq on Sat Jan 13 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libatomic_ops-devel libgpg-error libp11-kit perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent pkg-config python3-base sh5 shared-mime-info termutils tzdata
BuildRequires: appstream flex glibc-devel-static help2man libgc-devel libnbd-devel libreadline-devel makeinfo texi2dvi dejagnu libtextstyle-devel
BuildRequires: /proc /dev/pts

%ifarch %valgrind_arches
BuildRequires: valgrind
%endif

# for poke-qui:
%{?_with_gui:#BuildRequires: libgtk+3-devel tk-devel}


%description
GNU poke is an interactive, extensible editor for binary data.
Not limited to editing basic entities such as bits and bytes,
it provides a full-fledged procedural, interactive programming
language designed to describe data structures and to operate
on them.

%package -n lib%name%sover
Summary: The Poke library
Group: Development/Other

%description -n lib%name%sover
GNU poke is an interactive, extensible editor for binary data.

This package contains the Poke shared library.

%package -n lib%name-devel
Summary: Headers for the Poke library
Group: Development/C
Requires: lib%name%sover = %version-%release

%description -n lib%name-devel
GNU poke is an interactive, extensible editor for binary data.

This package contains headers for Poke library.

%if_with static
%package -n lib%name-devel-static
Summary: Poke static library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
GNU poke is an interactive, extensible editor for binary data.

This package contains Poke static library.
%endif

%prep
%setup
mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-3.0+ %_docdir/%name/COPYING) COPYING

%build
# TODO parallel LTO is buggy for now
#global optflags_lto %optflags_lto -flto=jobserver -ffat-lto-objects
%global optflags_lto %nil

%configure --disable-rpath

# As there we have a release tarball and it seems to be too hard
# to reconfigure it anyway, just use the system libtool in order
# to get proper linking:
rm -fv libtool
ln -s /usr/bin/libtool-default ./
ln -s libtool-default libtool

%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc NEWS TODO README ChangeLog
%doc --no-dereference COPYING
%_bindir/*
%_infodir/*.info*
%_man1dir/*.1.*
%_datadir/%name
%_datadir/emacs/site-lisp/*.el
%_datadir/vim/vimfiles/*/*

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files -n lib%name-devel
%_includedir/lib%name.h
%_libdir/lib%name.so
%_libdir/pkgconfig/*
%_datadir/aclocal/poke.m4

%if_with static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%else
%exclude %_libdir/lib%name.a
%endif

%check
make check

%changelog
* Thu Jul 30 2026 Paul Wolneykien <manowar@altlinux.org> 4.3-alt1
- New version 4.3.
- Moved to Development/Other group.
- Added shared library package.
- Links with the system libtextstyle.
- Tests enabled.
- Emacs mode files included.

* Thu Mar 28 2024 Nikolay A. Fetisov <naf@altlinux.org> 3.3-alt1
- New version

* Sat Jan 13 2024 Fr. Br. George <george@altlinux.org> 3.2-alt1
- Build new version
- Vendor libtextstyle in (it's safe for no CSS is parsed)
- Introduce checks
- Remove gui build option dropped by upstream

* Mon Nov 13 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.3-alt4
- NMU: fixed FTBFS on LoongArch.

* Tue Aug 29 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3-alt3
- Dropped BR: libtextstyle-devel which is being removed along with
  unsupported libcroco library.

* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3-alt2
- Fix build with LTO flags

* Tue Jun 29 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3-alt1
- Initial build for ALT Linux Sisyphus
