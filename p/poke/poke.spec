# Spec file for poke - binary data editor

%def_with    devel
%def_without static
%def_with    textstyle

Name: poke
Version: 3.2
Release: alt1

Summary: Extensible editor for structured binary data

License: GPLv3+
Group: Text tools
URL: http://www.jemarch.net/poke.html
#URL: https://git.savannah.gnu.org/cgit/poke.git

Source0: %name-%version.tar.gz
%if_with textstyle
%define libtextstyle_ver 0.20.5
Source1: libtextstyle-%libtextstyle_ver.tar.gz
%endif

BuildRequires(pre): rpm-macros-valgrind

# Automatically added by buildreq on Sat Jan 13 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libatomic_ops-devel libgpg-error libp11-kit perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent pkg-config python3-base sh5 shared-mime-info termutils tzdata
BuildRequires: appstream flex glibc-devel-static help2man libgc-devel libnbd-devel libreadline-devel makeinfo texi2dvi dejagnu chrpath

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

%if_with devel
%package devel
Summary: headers for Poke library
Group: Development/C
Requires: %name = %version-%release

%description devel
GNU poke is an interactive, extensible editor for binary data.

This package contains headers for Poke library.
%endif

%if_with static
%package static
Summary: Poke static library
Group: Development/C
Requires: %name-devel = %version-%release

%description static
GNU poke is an interactive, extensible editor for binary data.

This package contains Poke static library.

%endif


%prep
%setup
%if_with textstyle
%setup -D -a1
%endif

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-3.0+ %_docdir/%name/COPYING) COPYING

%build
# TODO parallel LTO is buggy for now
#global optflags_lto %optflags_lto -flto=jobserver -ffat-lto-objects
%global optflags_lto %nil
%if_with textstyle
cd libtextstyle-%libtextstyle_ver
%configure --disable-shared
%make_build
make install DESTDIR=`realpath ..`/libtextstyle prefix=''
cd ..
LIBTEXTSTYLE=`realpath libtextstyle`
%define libtextstyle_conf LDFLAGS=-L$LIBTEXTSTYLE/%_lib --with-libtextstyle-prefix=$LIBTEXTSTYLE --enable-hserver
%else
%define libtextstyle_conf
%endif

#autoreconf
%configure \
    --disable-rpath \
    --with-libreadline-prefix \
    %libtextstyle_conf

%make_build

%install
%make_install DESTDIR=%buildroot install
# Die ugly RPATH die die die
chrpath -d %buildroot/%_bindir/poke
chrpath -d %buildroot/%_bindir/poked
%find_lang %name

%files -f %name.lang
%if_with textstyle
%doc libtextstyle-%libtextstyle_ver/doc
%doc libtextstyle-%libtextstyle_ver/examples
%endif
%doc NEWS TODO README ChangeLog
%doc --no-dereference COPYING

%_bindir/%name
%_bindir/%{name}d
%_bindir/pk-*
%_libdir/lib%name.so.*

%_infodir/%name.*
%_man1dir/*

%_datadir/%name
%exclude %_datadir/emacs
%_datadir/vim/vimfiles/*/*

%if_with devel
%files devel
%_includedir/lib%name.h
%_libdir/lib%name.so
%_libdir/pkgconfig/*
%_datadir/aclocal/poke.m4
%else
%exclude %_includedir/lib%name.h
%exclude %_libdir/lib%name.so
%exclude %_libdir/pkgconfig/*
%exclude %_datadir/aclocal/poke.m4
%endif

%if_with static
%files static
%_libdir/lib%name.a
%else
%exclude %_libdir/lib%name.a
%endif

%check
make check

%changelog
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
