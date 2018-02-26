%define filever 052

Name: gromacs-gui
Version: 0.5.2
Release: alt5
License: GPL
Group: Sciences/Chemistry
Summary: GUI for molecular dynamics package, GROMACS
Url: http://resal.atspace.com/grogui.htm
# http://www.kde-apps.org/CONTENT/content-files/47665-grogui052.tar.gz
Source: grogui%filever-%version.tar.gz
Packager: Eugeny A. Rostovtsev <real at altlinux.org>

Requires: gromacs-common gromacs-doc
BuildRequires: libqt4-devel gcc-c++ libqwt-devel

%description
Gromacs GUI is a graphics user interface for widely used molecular dynamics
package, GROMACS. This package is useful but far from perfect.

%package devel
Summary: Header files for Gromacs GUI
Group: Development/C++
Requires: %name = %version-%release

%description devel
Header files for Gromacs GUI

%prep
%setup -q -n grogui%filever-%version

%build
pushd gui_withplotting
sed -i -e 's/\(qwt\)-qt4/\1/g' grogui.pro
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags"
%make_build
popd

%install
pushd gui_withplotting
mkdir -pv %buildroot%_bindir %buildroot%_includedir %buildroot%_miconsdir
mkdir -pv %buildroot%_pixmapsdir/%name
mv grogui %buildroot%_bindir/
mv include/* %buildroot%_includedir/
rm ui/images/konqueror.png
mv ui/images/* %buildroot%_miconsdir/
mv icons/16x16/* %buildroot%_pixmapsdir/%name/
popd
rm %buildroot%_miconsdir/terminal.png

%files
%_bindir/*
%_miconsdir/*
%_pixmapsdir/*

%files devel
%_includedir/*

%changelog
* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt5
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt4
- Fixed for gcc 4.5.1

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt3
- Rebuild with gcc 4.4

* Tue Feb 10 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.5.2-alt2
- Delete terminal.png from %%_miconsdir (was conflict with xfce4-terminal)

* Sat Feb 07 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus
