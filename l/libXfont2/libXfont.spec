Name: libXfont2
Version: 2.0.3
Release: alt1%ubt
Summary: X.Org libXfont runtime library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: bzlib-devel libfontenc-devel libfreetype-devel xorg-fontsproto-devel
BuildRequires: xorg-xproto-devel xorg-xtrans-devel xorg-util-macros zlib-devel
#BuildRequires: fop xorg-sgml-doctools xmlto

%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font file
formats, and rasterizing them.   It is used by the X servers, the
X Font Server (xfs), and some font utilities (bdftopcf for instance),
but should not be used by normal X11 clients.  X11 clients access fonts
via either the new API's in libXft, or the legacy API's in libX11.

%package devel
Summary: X.Org libXfont development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the libXfont development library and header files

%def_enable ipv6

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-bzip2 \
	%{subst_enable ipv6} \
	--disable-devel-docs \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/X11/fonts
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Dec 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.3-alt1%ubt
- fixes:
 + CVE-2017-16611 Open files with O_NOFOLLOW

* Fri Oct 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Fri Jan 13 2017 Michael Shigorin <mike@altlinux.org> 2.0.1-alt1.1
- BOOTSTRAP: dropped docs-related BRs (unused)

* Wed Nov 30 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.1-alt1
- 2.0.1

