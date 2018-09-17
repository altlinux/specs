# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qhexedit2
Version: 0.8.3
Release: alt1

Summary: Binary Editor for Qt
License: LGPLv2
Group: Editors
Url: https://github.com/Simsys/qhexedit2

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: qhexedit.desktop

# Fix build issues
Patch: qhexedit2_build.patch

BuildRequires: rpm-build-python rpm-build-python3
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: python-module-sip-devel
BuildRequires: python3-module-sip-devel
BuildRequires: python-module-PyQt5-devel
BuildRequires: python3-module-PyQt5-devel
BuildRequires: python-module-enum34

Requires: %name-qt5-libs = %EVR

%description
QHexEdit is a hex editor widget written in C++ for the Qt framework.
It is a simple editor for binary data, just like QPlainTextEdit is for text
data.

%package qt5-libs
Summary: %name Qt5 library
Group: Development/C++

%description qt5-libs
%name Qt5 library.

%package qt5-devel
Summary: Development files for %name Qt5
Group: Development/C++
Requires: %name-qt5-libs = %EVR

%description qt5-devel
The %name-qt5-devel package contains libraries and header files for
developing applications that use %name Qt5.

%package doc
Summary: Documentation and examples for %name
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains the documentation and examples for %name.

%package -n python-module-%name-qt5
Summary: %name Qt5 Python bindings
Group: Development/Python
Requires: %name-qt5-libs = %EVR

%description -n python-module-%name-qt5
%name Qt5 Python bindings.

%package -n python-module-%name-qt5-devel
Summary: Development files for the %name Qt5 Python bindings
Group: Development/Python
Requires: python-module-%name-qt5 = %EVR
Requires: sip-devel

%description -n python-module-%name-qt5-devel
Development files for the %name Qt5 Python bindings.

%package -n python3-module-%name-qt5
Summary: %name Qt5 Python3 bindings
Group: Development/Python3
Requires: %name-qt5-libs = %EVR

%description -n python3-module-%name-qt5
%name Qt5 Python3 bindings.

%package -n python3-module-%name-qt5-devel
Summary: Development files for the %name Qt5 Python3 bindings
Group: Development/Python3
Requires: python3-module-%name-qt5 = %EVR
Requires: python3-module-sip-devel

%description -n python3-module-%name-qt5-devel
Development files for the %name Qt5 Python3 bindings

%prep
%setup
%patch -p1

# Prevent rpmlint W: doc-file-dependency %_docdir/qhexedit2-doc/html/installdox %_bindir/perl
rm -f doc/html/installdox

%build
# Build library, qt5
# Build library, qt5
mkdir build-lib-qt5
pushd build-lib-qt5
LDFLAGS="%optflags -Wl,--as-needed" %qmake_qt5 ../src/qhexedit.pro
%make_build
popd

# Build sip bindings, qt5, python2
USE_QT5=1 CFLAGS="%optflags" %__python setup.py build --build-base=build-python-qt5
# Build sip bindings, qt5, python3
USE_QT5=1 CFLAGS="%optflags" %__python3 setup.py build --build-base=build-python3-qt5
# Build application
mkdir build-example
pushd build-example
%qmake_qt5 ../example/qhexedit.pro
%make_build

%install
# Library and headers
install -d %buildroot%_includedir/%name
cp -a src/*.h %buildroot%_includedir/%name
install -d %buildroot%_libdir
chmod 0755 build-lib-qt5/*.so.*.*
cp -a build-lib-qt5/*.so* %buildroot%_libdir

# pkg-config files
install -d %buildroot%_pkgconfigdir/

cat > %buildroot%_pkgconfigdir/%name-qt5.pc <<EOF
libdir=%_libdir
includedir=%_includedir/%name

Name: %name-qt5
Description: %summary
Version: %version
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqhexedit-qt5
EOF

# Python bindings
# Distutils does not support --build-base with install, you need to build also...
USE_QT5=1 CFLAGS="%optflags" %__python setup.py build --build-base=build-python2-qt5 install --skip-build --root %buildroot
USE_QT5=1 CFLAGS="%optflags" %__python3 setup.py build --build-base=build-python3-qt5 install --skip-build --root %buildroot
install -Dpm 0644 src/qhexedit.sip %buildroot%_datadir/sip/qhexedit/qhexedit.sip
install -Dpm 0644 src/qhexedit.sip %buildroot%_datadir/sip3/qhexedit/qhexedit.sip

# Application
install -Dpm 0755 build-example/qhexedit %buildroot%_bindir/qhexedit
desktop-file-install --dir=%buildroot%_desktopdir/ %SOURCE1

%files
%_bindir/qhexedit
%_desktopdir/qhexedit.desktop

%files qt5-libs
%doc doc/release.txt
%doc src/license.txt
%_libdir/libqhexedit-qt5.so.4*

%files qt5-devel
%_includedir/%name/
%_libdir/libqhexedit-qt5.so
%_pkgconfigdir/%name-qt5.pc

%files doc
%doc src/license.txt
%doc doc/html

%files -n python-module-%name-qt5
%python_sitelibdir/qhexedit-qt5.so
%python_sitelibdir/QHexEdit_qt5-%version-*.egg-info

%files -n python-module-%name-qt5-devel
%_datadir/sip/qhexedit/

%files -n python3-module-%name-qt5
%python3_sitelibdir/qhexedit-qt5.*.so
%python3_sitelibdir/QHexEdit_qt5-%version-*.egg-info

%files -n python3-module-%name-qt5-devel
%_datadir/sip3/qhexedit/

%changelog
* Mon Sep 17 2018 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
