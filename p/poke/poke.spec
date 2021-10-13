# Spec file for poke - binary data editor

%def_without gui
%def_with    devel
%def_without static

Name: poke
Version: 1.3
Release: alt2

Summary: extensible editor for structured binary data

License: %gpl3plus
Group: Text tools
URL: http://www.jemarch.net/poke.html
#URL: https://git.savannah.gnu.org/cgit/poke.git

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Mon Jun 28 2021
# optimized out: fontconfig glib2-devel gnu-config libX11-devel libjson-c5 libncurses-devel libtinfo-devel perl pkg-config python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4 shared-mime-info tcl-devel texlive tzdata xorg-proto-devel xz
BuildRequires: appstream flex glibc-devel-static help2man libgc-devel libjson-c-devel libreadline-devel libtextstyle-devel makeinfo texi2dvi valgrind

# for poke-qui:
%{?_with_gui:#BuildRequires: libgtk+3-devel tk-devel}


%description
GNU poke is an interactive, extensible editor for binary data.
Not limited to editing basic entities such as bits and bytes,
it provides a full-fledged procedural, interactive programming
language designed to describe data structures and to operate
on them.

%if_with gui
%package gui
Summary: Poke TCL/TK GUI interface
Group: Text tools
Requires: %name = %version-%release
BuildArch: noarch

%description gui
GNU poke is an interactive, extensible editor for binary data.

This package contains Poke TCL/TK GUI interface.

%endif

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

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-3.0+ %_docdir/%name/COPYING) COPYING

%build

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%autoreconf
%configure \
    --disable-rpath \
     %{?_without_gui:--disable-gui} \
    --with-libtextstype-prefix \
    --with-libreadline-prefix \
    %nil

%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc NEWS TODO README ChangeLog
%doc --no-dereference COPYING

%_bindir/%name
%_bindir/pk-*
%_libdir/lib%name.so.*

%_infodir/%name.*
%_man1dir/%name.*

%_datadir/%name
%exclude %_datadir/emacs


%if_with gui
%files gui
%_bindir/%name-gui
%_datadir/%name/gui
%endif

%if_with devel
%files devel
%_includedir/lib%name.h
%_libdir/lib%name.so
%else
%exclude %_includedir/lib%name.h
%exclude %_libdir/lib%name.so
%endif

%if_with static
%files static
%_libdir/lib%name.a
%else
%exclude %_libdir/lib%name.a
%endif


%changelog
* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3-alt2
- Fix build with LTO flags

* Tue Jun 29 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3-alt1
- Initial build for ALT Linux Sisyphus
