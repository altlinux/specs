%define _unpackaged_files_terminate_build 1
%define oname veusz

Name: python3-module-%oname
Version: 4.2
Release: alt1

Summary: A Scientific Plotting Package
License: GPL-2.0-or-later
Group: Development/Python3
URL: https://veusz.github.io
VCS: https://github.com/veusz/veusz.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: /usr/bin/pod2man /usr/bin/man
BuildRequires: python3-devel libnumpy-py3-devel
BuildRequires: qt6-base-devel python3-module-PyQt6-devel
BuildRequires: python3-module-sip6
BuildRequires: python3(tomli)
BuildRequires: desktop-file-utils
BuildRequires: qt6-designer

%add_python3_req_skip pyemf3 pyemf3.emr
%py3_requires numpy.testing

%description
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

%package docs
Summary: Documentation for Veusz
Group: Development/Documentation
BuildArch: noarch

%description docs
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This packagec contains documentation for Veusz.

%package examples
Summary: Examples for Veusz
Group: Development/Documentation
Requires: %name = %EVR

%description examples
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains examples for Veusz.

%package -n %oname
Summary: A Scientific Plotting Package
Group: Graphics
Conflicts: %name < %version-%release
Requires: %name = %EVR
Requires: %name-examples = %EVR

%description -n %oname
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains main scripts for Veusz.

%prep
%setup
%autopatch -p1
find ./ -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%build
#add_optflags -fno-strict-aliasing
%pyproject_build
%make_build -C Documents/ man

# make translations
lrelease-qt6 translation/*.ts

%install
%pyproject_install

# Install .desktop, mime and appdata files from upstream tarball
install -Dm0644 support/veusz.appdata.xml %buildroot%_datadir/appdata/veusz.appdata.xml
install -Dm0644 support/veusz.xml %buildroot/%_datadir/mime/packages/veusz.xml
desktop-file-install -m 0644 \
	--dir=%buildroot%_desktopdir/ \
	--add-category=2DGraphics \
	support/veusz.desktop

# link main veusz icon also into hicolor-icon-theme dir (for desktop file)
for size in 16 32 48 64 128; do
	odir=%buildroot%_iconsdir/hicolor/${size}x${size}/apps
	mkdir -p $odir
	ln -s %python3_sitelibdir/veusz/icons/veusz_${size}.png ${odir}/veusz.png
done
odir=%buildroot%_iconsdir/hicolor/scalable/apps
mkdir -p $odir
ln -s %python3_sitelibdir/veusz/icons/veusz.svg $odir/veusz.svg

# install man pages
mkdir -p %buildroot%_man1dir
install -p Documents/man-page/veusz.1 -m 0644 %buildroot%_man1dir

# install translations
mkdir -p %buildroot/%_datadir/%oname/translation
cp translation/*.qm %buildroot/%_datadir/%oname/translation/
%find_lang --with-qt %oname

%files
%python3_sitelibdir/veusz-%version.dist-info
%python3_sitelibdir/veusz
%exclude %python3_sitelibdir/veusz/examples

%files examples
%python3_sitelibdir/veusz/examples

%files -n %oname -f %oname.lang
%doc AUTHORS ChangeLog COPYING README.md
%_bindir/veusz
%_datadir/applications/veusz.desktop
%_datadir/appdata/veusz.appdata.xml
%_iconsdir/hicolor/*/apps/veusz.*
%_datadir/mime/packages/veusz.xml
%_man1dir/*
%dir %_datadir/%oname
%dir %_datadir/%oname/translation

%changelog
* Sat Nov 01 2025 Anton Midyukov <antohami@altlinux.org> 4.2-alt1
- New version 4.2.

* Tue Jun 24 2025 Anton Midyukov <antohami@altlinux.org> 4.1-alt1
- new version 4.1
- disable feedback and version check by default

* Tue Jun 03 2025 Anton Midyukov <antohami@altlinux.org> 4.0-alt2
- bind desktop file to display icon in wayland

* Mon Jun 02 2025 Anton Midyukov <antohami@altlinux.org> 4.0-alt1
- new version 4.0
- build with qt6
- add .desktop, mime and appdata files

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt3
- rebuild with sip6

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt2
- drop unused BR: texlive-dist

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1, build with sip5

* Thu Mar 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1-alt2
- Build for python2 disabled.

* Thu Jan 23 2020 Grigory Ustinov <grenka@altlinux.org> 3.1-alt1
- Build new version for python3.8.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.25.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.25.1-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.21-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.21-alt2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.21-alt1
- Version 1.21

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.19.1-alt1
- Version 1.19.1

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt2
- Fixed build

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt1
- Version 1.18

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.17-alt1
- Version 1.17

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt3
- Extracted %oname package (ALT #28282)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.14-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Dec 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt2
- Extracted examples into separate package

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1
- Initial build for Sisyphus

