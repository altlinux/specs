Name: wxsvg
Version: 1.1.8
Release: alt1
Epoch: 1

Summary: wxSVG is viewer SVG files
License: GPL
Group: Graphics
Url: http://wxsvg.sourceforge.net
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Source: %name-%version.tar.bz2

BuildRequires: gcc-c++ libart_lgpl-devel libpango-devel libwxGTK-devel libavformat-devel libswscale-devel libexpat-devel libagg-devel

%description
wxSVG is viewer SVG files

%package -n lib%name
License: GPL
Group: System/Libraries
Summary: lib%name is C++ library to create, manipulate and render SVG files

%description -n lib%name
lib%name is C++ library to create, manipulate and render SVG files

%package -n lib%name-devel-static
License: GPL
Group: System/Libraries
Summary: lib%name is static C++ library to create, manipulate and render SVG files
Obsoletes: lib%name-static

%description -n lib%name-devel-static
lib%name is static C++ library to create, manipulate and render SVG files

%package -n lib%name-devel
License: GPL
Group: Development/C++
Summary: Development shared library for wxSVG
Requires: lib%name = 1:%version-%release

%description -n lib%name-devel
Development shared library for wxSVG

%prep
%setup -q

touch INSTALL
touch NEWS
touch README

sed -i '/AC_CONFIG_MACRO_DIR/d' configure.in

%build
%add_optflags -D__STDC_CONSTANT_MACROS
%autoreconf
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
make install DESTDIR=%buildroot

%files
%doc ChangeLog AUTHORS TODO COPYING
%_bindir/*

%files -n lib%name
%_libdir/lib*so.*
%exclude %_libdir/lib*.a

%files -n lib%name-devel-static
%_libdir/lib*.a

%files -n lib%name-devel
%_includedir/wx*
%_libdir/lib*so
%_libdir/pkgconfig/*

%changelog
* Wed May 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.1.8-alt1
- New version
- Drop patches

* Sun Feb 26 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.1.6-alt1
- New version
- Update patch from ubuntu

* Fri Feb 10 2012 Sergey Bolshakov <sbolshakov at altlinux.ru> 1:1.0.10-alt1.4
- rebuilt with restored optflags

* Mon Feb 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.10-alt1.3
- Fixed build with libav 0.8

* Mon Jan 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.10-alt1.2
- Fixed build

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.10-alt1.1
- Fixed build

* Sat Aug 13 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.10-alt1
- New version
- Add fix-ftbs-libav-0.7.patch

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.8_1-alt2.1
- Rebuilt with updated wxGTK2.9

* Fri Mar 25 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.8_1-alt2
- Rebuild with libwxGTK2.9-devel

* Sun Mar 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.8_1-alt1
- New version

* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.7_1-alt1
- New version

* Sun Sep 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.6-alt1
- New version

* Mon Jun 21 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.3-alt1
- New version

* Mon Feb 08 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.1-alt1
- New version

* Wed Sep 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0r-alt2
- Rebuild with new libavcodec, libavformat
- Fix altlinux-policy-shared-lib-contains-devel-so repocop test

* Sun Nov 30 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0r-alt1
- New version
- Remmove depricated ldconfig call in post

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0b11-alt1
- New version

* Sat Mar 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0b8-alt2
- Rename lib%name-static -> lib%name-devel-static

* Tue Jan 22 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0b8-alt1
- built for ALT Linux
