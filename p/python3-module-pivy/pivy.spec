%define oname pivy
Name: python3-module-%oname
Version: 0.6.9
Release: alt1
Epoch: 2
Summary: Pivy is a Coin binding for Python
License: ISC
Group: Development/Python3
Url: https://github.com/coin3d/pivy
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: pivy-0.6.6-0001-fix-CMakeLists.txt-for-distutils_cmake.patch
Patch2: pivy-0.6.6-0002-Gentoo-specific-clear-swig-deprecation-warning.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): qt6-base-devel
BuildRequires: gcc-c++
BuildRequires: libcoin3d-devel
BuildRequires: libsoqt-devel
BuildRequires: swig

%add_python3_req_skip pivy.qt pivy.qt.QtCore pivy.qt.QtGui pivy.qt.QtWidgets

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
#add_optflags -I%_includedir/qt4/Qt -fno-strict-aliasing
%ifarch %e2k
# error: "Qt requires a C++17 compiler"
%add_optflags -std=c++17
%endif
export PATH=%_qt6_bindir:$PATH
%python3_build_debug

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/%oname \
	%buildroot%python3_sitelibdir_noarch/*.egg-info \
	%buildroot%python3_sitelibdir/
%endif

%files
%doc AUTHORS HACKING NEWS THANKS docs/*
%python3_sitelibdir/*

%changelog
* Fri Sep 27 2024 Andrey Cherepanov <cas@altlinux.org> 2:0.6.9-alt1
- New version.

* Tue Apr 09 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:0.6.8-alt3.gitd77e175
- Fixed build for Elbrus.

* Thu Apr 04 2024 Andrey Cherepanov <cas@altlinux.org> 2:0.6.8-alt2.gitd77e175
- New snapshot supporting Qt6 and Python 3.12.

* Thu Aug 25 2022 Andrey Cherepanov <cas@altlinux.org> 2:0.6.8-alt1
- New version.

* Fri Apr 29 2022 Andrey Cherepanov <cas@altlinux.org> 2:0.6.7-alt1
- New version.

* Thu Mar 03 2022 Andrey Cherepanov <cas@altlinux.org> 2:0.6.6-alt1
- New version.

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 2:0.6.5-alt2
- Drop python2 support.

* Fri Sep 18 2020 Andrey Cherepanov <cas@altlinux.org> 2:0.6.5-alt1
- New version.
- Fix License tag, project URL and maintainer.
- Build from upstream tag.

* Thu Jun 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:0.5.0-alt2.hg20100619.3.3
- Fixed build on architectures with "%_lib" != lib.

* Mon Jun 11 2018 Anton Midyukov <antohami@altlinux.org> 2:0.5.0-alt2.hg20100619.3.2
- Rebuilt for aarch64

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2:0.5.0-alt2.hg20100619.3.1
- Rebuild with Python-2.7

* Sun May 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619.3
- Fixed build

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619.2
- Rebuilt for debuginfo

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619.1
- Fixed build

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619
- New snapshot

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt1.svn20091216
- Rebuilt with new SoQt

* Fri Jan 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.svn20091716
- Initial build for Sisyphus

