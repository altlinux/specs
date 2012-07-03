%add_findprov_lib_path %_tcllibdir

Name: tcl-togl
Version: 1.7
Release: alt3
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Tk OpenGL widget
License: BSD
Group: Development/Tcl
Url: http://togl.sourceforge.net/

Source: http://mesh.dl.sourceforge.net/sourceforge/togl/Togl-%version.tar.gz
Patch: tcl-togl-1.7-alt-install.patch

Requires: tcl tk

# Automatically added by buildreq on Tue Oct 21 2008
BuildRequires: imake libGL-devel libXmu-devel tk-devel

%description
Togl is a Tk widget for OpenGL rendering. Togl was originally based
on OGLTK, written by Benjamin Bederson at the University of New Mexico.

%package devel
Summary: Header files for Togl
Group: Development/C
Requires: %name = %version-%release

%description devel
Togl is a Tk widget for OpenGL rendering. Togl was originally based
on OGLTK, written by Benjamin Bederson at the University of New Mexico.

This package includes header files for Togl.

%prep
%setup -q -n Togl-%version
%patch -p0

%build
%configure --enable-64bit --enable-shared
%make_build

%install
%makeinstall

%files
%doc LICENSE README.stubs Togl.html TODO
%_tcllibdir/libTogl%version.so
%_tcldatadir/Togl%version

%files devel
%_includedir/*
#%_tcllibdir/libToglestub%version.a

%changelog
* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt3
- Rebuilt for debuginfo

* Tue Oct 21 2008 Grigory Batalov <bga@altlinux.ru> 1.7-alt2
- Update build requirements.

* Mon Jan 08 2007 Grigory Batalov <bga@altlinux.ru> 1.7-alt1
- Rebuilt for ALT Linux.
- Specfile cleanup.

* Wed Oct 15 2003 Fuhito Suguri <bitwalk@jcom.home.ne.jp> 1bw
- build new spec.
- togl-20030711 (nightly-cvs).
