%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define teaname img
%define major 1.4

Name: tcl-img
Version: 1.4.14
Release: alt1

Summary: Tcl Image Formats (Img)
License: TCL
Group: Development/Tcl
Url: https://sourceforge.net/projects/tkimg/

Provides: %teaname = %version-%release
Obsoletes: %teaname
Conflicts: tcl < 8.6.7-alt2

# repacked https://sourceforge.net/projects/tkimg/files/tkimg/1.4/ "tkimg %version" Img-%version-Sources.tar.gz
Source0: tkimg-%version.tar
Source1: tcl-img.watch
Patch1: 0001-ALT-TEA.patch
Patch2: 0002-DEBIAN-libz.patch
Patch3: 0003-DEBIAN-libjpeg.patch
Patch4: 0004-DEBIAN-libpng.patch
Patch5: 0005-DEBIAN-libtiff.patch
Patch6: 0006-DEBIAN-pixmap.patch
Patch7: 0007-DEBIAN-window.patch
Patch8: 0008-ALT-tests-TCLLIBPATH.patch

BuildRequires: rpm-build-tcl >= 0.5-alt1
BuildRequires: libjpeg-devel libpng-devel tk-devel zlib-devel
BuildRequires: libtiff-devel
BuildRequires: tcllib
# tests
BuildRequires: xvfb-run

%description
%name is a Tk enhancement, adding support for many other Image formats:
BMP, XBM, XPM, GIF, PNG, JPEG, postscript and others.

%prep
%setup -q -n tkimg-%version
%autopatch -p2
find . -name config.cache -delete

%build
export TCL_SRC_DIR=%_includedir/tcl
export TK_SRC_DIR=%_includedir/tk
%autoreconf
%configure \
	   --with-tcl=%_libdir \
	   --with-tk=%_libdir \
	   --enable-threads \
	   #
%make_build

xz ChangeLog

%install
%make_install DESTDIR=%buildroot install

%check
log="$(mktemp)"
cleanup_check()
{
	for p in $(jobs -p); do
		kill "$p"
	done

	rm "$log"
	exit "$@"
}

trap 'cleanup_check $?' EXIT

Xvfb :0 &
export DISPLAY=:0

# broken
rm tests/jpeg.test

# tcltest always retuns 0
set -eo pipefail
make test 2>&1 |tee "$log"
! grep -q FAILED "$log" ||exit 1

%files
%doc ANNOUNCE ChangeLog* README doc/*.css doc/*.htm license.terms
%dir %_tcllibdir/Img%version
%_tcllibdir/Img%version/*.so
%_tcllibdir/Img%version/pkgIndex.tcl
%_mandir/mann/*

%changelog
* Sun Mar 19 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.14-alt1
- Updated to 1.4.14.
- Built against system libtiff again.
- Packed extension dir itself as well.

* Tue Aug 31 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.13-alt2
- Fixed FTBFS: built fat LTO objects.

* Mon Feb 15 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.13-alt1
- Updated to 1.4.13.

* Tue Jan 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.11-alt2
- Built against internal libtiff (ALT#39407).
- Enabled tests.

* Sun May 17 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.11-alt1
- Updated to 1.4.11.
- Built against system libtiff.
- Updated patches.
- Imported watch file from Debian.

* Mon Sep 16 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.9-alt1
- 1.4.9.
- Explicitly enabled threads in configure.
- Packaged license.terms file.
- Refreshed Url.
- Fixed license field.

* Thu Feb 28 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.2-alt2
- rebuilt against libpng16

* Tue Sep 12 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.2-alt1
- 1.4.2 released

* Sun Apr 07 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt2
- use png12 from now

* Tue Jun 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt1
- 1.3.2 release

* Sun Nov 26 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt5
- pngtcl: removed png_{read,write}_destroy from stub table

* Fri Jul 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt4
- fixed build on x86_64

* Sun Apr 16 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt3
- CVS snapshot @ 20060125
- tiff support dropped

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt2
- rebuilt against new shiny tcl reqprov finder

* Sun Sep 26 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- new major release
- built with system libjpeg, libpng, libtiff

* Tue Oct  1 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.2.4-alt1
- name changed
- rebuilt with tcl 8.4
