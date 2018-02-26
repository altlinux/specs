Name: liborigin2
Version: 20110829
Release: alt1
Summary: A library for reading OriginLab project files, version 2
License: BSD
Group: System/Libraries
Url: http://soft.proindependent.com/liborigin2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.zip

BuildPreReq: unzip boost-devel gcc-c++ libqt4-devel

%description
A library for reading OriginLab project files. Only files created with
Origin version 7.5 can be parsed for the moment.

%package devel
Summary: Development files of liborigin library, version 2
Group: Development/C++
Requires: %name = %version-%release

%description devel
A library for reading OriginLab project files. Only files created with
Origin version 7.5 can be parsed for the moment.

This package contains development files of liborigin library, version 2.

%package devel-doc
Summary: Documentation for liborigin library, version 2
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
A library for reading OriginLab project files. Only files created with
Origin version 7.5 can be parsed for the moment.

This package contains development documentation for liborigin library,
version 2.

%prep
%setup

%build
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags"
%make_build

%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name
install -d %buildroot%_docdir/%name

install -p -m644 *.h* %buildroot%_includedir/%name
cp -P *.so* %buildroot%_libdir
cp -fR doc/html/* %buildroot%_docdir/%name/


%files
%doc copying FORMAT readme
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-doc
%_docdir/%name

%changelog
* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110829-alt1
- Version 20110829

* Wed Jul 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100913-alt4
- Rebuilt with Boost 1.47.0

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100913-alt3
- Rebuilt for debuginfo

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100913-alt2
- Rebuilt for soname set-versions

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100913-alt1
- Version 20100913

* Thu Sep 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090406-alt1
- Fixed package versioning (inspired by mike@)

* Thu Sep 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 06042009-alt1.1
- Fixed library's installation

* Thu Sep 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 06042009-alt1
- Initial build for Sisyphus

