Name: liboggz
Version: 0.9.7
Release: alt2.2

Summary: Simple programming interface for Ogg files and streams
Group: System/Libraries
License: BSD
URL: http://www.annodex.net/
Source0: http://www.annodex.net/software/liboggz/download/%name-%version.tar.gz

Packager: Repocop Q. A. Robot <repocop@altlinux.org>

BuildPreReq: libogg-devel >= 1.0

# Automatically added by buildreq on Fri Jun 13 2008
BuildRequires: docbook-utils doxygen gcc-c++ libogg-devel

%description
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

%package devel
Summary: Files needed for development using liboggz
Group: Development/C
Requires: liboggz = %version-%release
Requires: libogg-devel >= 1.0

%description devel
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

This package contains the header files and documentation needed for
development using liboggz.

%prep
%setup -q

%build
%configure \
	--disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall docdir=`pwd`/doxygen

%files
%doc AUTHORS ChangeLog COPYING README
%_libdir/liboggz.so.*
%_man1dir/*
%_bindir/oggz*

%files devel
%doc doxygen/html
%_libdir/liboggz.so
%_pkgconfigdir/oggz.pc
%_includedir/oggz

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt2.2
- Removed bad RPATH

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt2.1
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt2
- Rebuilt for soname set-versions

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for liboggz
  * postun_ldconfig for liboggz

* Fri Jun 13 2008 Igor Zubkov <icesik@altlinux.org> 0.9.7-alt1
- 0.9.5 -> 0.9.7

* Sat Apr 15 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.5-alt1
- Initial build for Sisyphus

* Thu Jun 16 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.1-3: update for Ville's comments

* Mon Jun 13 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.1-2: rpmlint cleanup

* Fri Jun 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.1-1: initial package
