# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_without python3

Name: qhexedit2
Version: 0.8.9
Release: alt1

Summary: Binary Editor for Qt
License: LGPLv2
Group: Editors

Url: https://github.com/Simsys/qhexedit2
Source0: %name-%version.tar
Source1: qhexedit.desktop

# Fedora patches
Patch10: qhexedit2_build.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sip5 python3-module-sip-devel
BuildRequires: python3-module-PyQt5-devel
%endif

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

%if_with python3
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
%endif

%prep
%setup
%autopatch -p1

# Prevent rpmlint W: doc-file-dependency %%_docdir/qhexedit2-doc/html/installdox %%_bindir/perl
rm -f doc/html/installdox

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif

# Build library, qt5
mkdir build-lib-qt5
pushd build-lib-qt5
LDFLAGS="%optflags -Wl,--as-needed" %qmake_qt5 ../src/qhexedit.pro
%make_build
popd

%if_with python3
# Build sip bindings, qt5, python3
USE_QT5=1 CFLAGS="%optflags" %__python3 setup.py build --build-base=build-python3-qt5
%endif
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
%if_with python3
USE_QT5=1 CFLAGS="%optflags" %__python3 setup.py build --build-base=build-python3-qt5 install --skip-build --root %buildroot
#install -Dpm 0644 src/qhexedit.sip %buildroot%_datadir/sip3/qhexedit/qhexedit.sip
%endif

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

%if_with python3
%files -n python3-module-%name-qt5
%python3_sitelibdir/qhexedit-qt5.*.so
%python3_sitelibdir/QHexEdit_qt5-%version-*.egg-info

%files -n python3-module-%name-qt5-devel
%_datadir/sip3/qhexedit/
%endif

%changelog
* Tue Mar 08 2022 Anton Midyukov <antohami@altlinux.org> 0.8.9-alt1
- new version 0.8.9
- cleanup spec

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt4
- temp. disable python3 module (sip5 issue)

* Sun Feb 09 2020 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt3
- Disable build python2 bindings

* Fri Jun 21 2019 Michael Shigorin <mike@altlinux.org> 0.8.3-alt2
- E2K: explicit -std=c++11
- minor spec cleanup

* Mon Sep 17 2018 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
