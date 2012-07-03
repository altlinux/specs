Name: libiptcdata
Version: 1.0.4
Release: alt3.1

Packager: Victor Forsyuk <force@altlinux.org>

%def_disable static

Summary: IPTC tag library
License: LGPLv2+
Group: System/Libraries

URL: http://libiptcdata.sourceforge.net/
Source: http://downloads.sourceforge.net/libiptcdata/libiptcdata-%version.tar.gz

# Automatically added by buildreq on Thu Jun 18 2009
BuildRequires: python-devel

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%package -n python-module-%name
Summary: Python bindings for libiptcdata
Group: Development/C
Requires: %name = %version-%release

%if_enabled static
%package devel-static
Summary: Static library build of %name
Group: Development/C
Requires: %name-devel = %version-%release
%endif

%description
libiptcdata is a library for parsing, editing, and saving IPTC data stored
inside images. IPTC is a standard for encoding metadata such as captions,
titles, locations, etc. in the headers of an image file. libiptcdata also
includes a command-line utility for modifying the metadata.

%description devel
The libiptcdata-devel package contains the libraries and include files
that you can use to develop libiptcdata applications.

%if_enabled static
%description devel-static
The static build of libiptcdata.
%endif

%description -n python-module-%name
The libiptcdata-python package contains a Python module that allows Python
applications to use the libiptcdata API for reading and writing IPTC
metadata in images.

%prep
%setup

%build
%configure --enable-python %{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name
%find_lang --append --output=%name.lang iptc

%files -f %name.lang
%_bindir/*
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*
%_datadir/gtk-doc/html/libiptcdata

%files -n python-module-%name
%doc python/README python/examples
%python_sitelibdir/*.so
%exclude %python_sitelibdir/*.la

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.4-alt3.1
- Rebuild with Python-2.7

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt3
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt2
- Rebuilt for soname set-versions

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.1
- Rebuilt with python 2.6

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 1.0.4-alt1
- 1.0.4

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Mon Mar 16 2009 Victor Forsyuk <force@altlinux.org> 1.0.2-alt3
- Comply with python modules package naming policy.

* Fri Jan 09 2009 Victor Forsyuk <force@altlinux.org> 1.0.2-alt2
- Remove obsolete ldconfig calls.

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.0.2-alt1.1
- Rebuilt with python-2.5.

* Wed May 16 2007 Victor Forsyuk <force@altlinux.org> 1.0.2-alt1
- Initial build.
