%define _unpackaged_files_terminate_build 1

%define oname qscintilla2

%def_without docs

Name: qscintilla2-qt6
Version: 2.14.1
Release: alt1

Summary: QScintilla is a port to Qt6 of Neil Hodgson's Scintilla C++ editor class

License: GPLv3
Group: Development/KDE and QT
Url: https://riverbankcomputing.com/software/qscintilla

# Source-url: https://www.riverbankcomputing.com/static/Downloads/QScintilla/%version/QScintilla_src-%version.zip
Source: %name-%version.tar

%define libname lib%{oname}

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel

BuildRequires: python3-module-sip6 python3-module-PyQt-builder

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: python3-module-PyQt6-devel

%description
Qscintilla is a free source code editing component. It comes with complete
source code and a license that permits use in any free project or commercial
product. As well as features found in standard text editing components,
Scintilla includes features especially useful when editing and debugging
source code. These include support for syntax styling, error indicators, code
completion and call tips. The selection margin can contain markers like those
used in debuggers to indicate breakpoints and the current line. Styling
choices are more open than with many editors, allowing the use of proportional
fonts, bold and italics, multiple foreground and background colours and
multiple fonts.

%package -n %libname-qt6
Summary: QScintilla is a port to Qt6 of Neil Hodgson's Scintilla C++ editor class.
Group: Development/KDE and QT

%description -n %libname-qt6
Qscintilla is a free source code editing component. It comes with complete
source code and a license that permits use in any free project or commercial
product. As well as features found in standard text editing components,
Scintilla includes features especially useful when editing and debugging
source code. These include support for syntax styling, error indicators, code
completion and call tips. The selection margin can contain markers like those
used in debuggers to indicate breakpoints and the current line. Styling
choices are more open than with many editors, allowing the use of proportional
fonts, bold and italics, multiple foreground and background colours and
multiple fonts.

%package -n lib%oname-qt6-devel
Requires: %libname-qt6 = %EVR
Requires: qt6-base-devel
Summary: Header files for %oname-qt6
Group: Development/KDE and QT

%description -n lib%oname-qt6-devel
Header files for %oname-qt6

%package -n lib%oname-qt6-designer
Requires: %libname-qt6 = %EVR
Summary: QScintilla designer plugin
Group: Development/KDE and QT

%description -n lib%oname-qt6-designer
QScintillla designer plugin.


%package -n python3-module-%oname-qt6
Requires: %libname-qt6 = %EVR
Summary: Python 3 bindings for %oname (Qt6)
Group: Development/KDE and QT
%py3_provides PyQt6.Qsci

%description -n python3-module-%oname-qt6
Python bindings for %oname

%package -n python3-module-%oname-qt6-devel
Requires: python3-module-%oname-qt6 = %EVR
Summary: Python 3 bindings for %oname (Qt6)
Group: Development/KDE and QT

%description -n python3-module-%oname-qt6-devel
Devel files for Python bindings for %oname


%package -n %libname-doc
Summary: Documentation for %oname
Group: Development/KDE and QT
BuildArch: noarch

%description -n %libname-doc
Documentation for %oname


%prep
%setup

%build

%ifarch %e2k
# bits/c++0x_warning.h
%add_optflags -std=gnu++11
%endif

pushd src
qmake-qt6 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qscintilla.pro
%make_build
popd

pushd designer
qmake-qt6 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags -I../src" designer.pro
%make_build
popd

%ifarch %e2k
# Qsci: error while loading shared libraries: libqscintilla2_qt5.so.15
export LD_LIBRARY_PATH=$(pwd)/src
%endif

pushd Python
cp -v pyproject-qt6.toml pyproject.toml
sip-build \
    --no-make \
    --qmake=%_qt6_bindir/qmake \
    --qsci-features-dir ../src/features \
    --qsci-include-dir ../src \
    --qsci-library-dir ../src \
    --api-dir %_datadir/qt6/qsci3/api/python \

%make_build -C build
popd

%install

# Python bindings for PyQt6
pushd Python/build
mkdir -p %buildroot%python3_sitelibdir/PyQt6/
%makeinstall_std INSTALL_ROOT=%buildroot
popd

mkdir -p %buildroot%_includedir/qt6/Qsci
mkdir -p %buildroot%_qt6_libdatadir
mkdir -p %buildroot%_qt6_translationdir
mkdir -p %buildroot%_qt6_plugindir/designer
mkdir -p %buildroot%_datadir/sip/qsci
mkdir -p %buildroot%_datadir/qt6/qsci/api/python

# Qt6 library
install src/lib%{oname}_qt6.so.*.*.* %buildroot%_libdir
install src/*.qm %buildroot%_qt6_translationdir
pushd %buildroot%_libdir
ln -s lib%{oname}_qt6.so.*.*.* `ls lib%{oname}_qt6.so.*.*.* | sed s/\.[0-9]*$//`
ln -s lib%{oname}_qt6.so.*.*.* `ls lib%{oname}_qt6.so.*.*.* | sed s/\.[0-9]*\.[0-9]*$//`
ln -s lib%{oname}_qt6.so.*.*.* `ls lib%{oname}_qt6.so.*.*.* | sed s/\.[0-9]*\.[0-9]*\.[0-9]*$//`
popd

pushd %buildroot%_qt6_libdatadir
for libname in ../../../%_lib/lib%{oname}_qt6.*; do
ln -s $libname ./
done
popd

# qt6 designer
install -D designer/libqscintillaplugin.so %buildroot%_qt6_plugindir/designer

# qt6 headers
install -m644 src/*.h %buildroot%_qt6_headerdir/
install -m644 src/Qsci/*.h %buildroot%_qt6_headerdir/Qsci/

# docs
%if_with docs
mkdir -p %buildroot%_docdir/%libname-%version
cp -a doc/Scintilla %buildroot%_docdir/%libname-%version
cp -a doc/html %buildroot%_docdir/%libname-%version
cp ChangeLog NEWS LICENSE %buildroot%_docdir/%libname-%version
%endif


%files -n %libname-qt6
%_qt6_libdatadir/*.so.*
%_libdir/*_qt6.so.*
%_qt6_translationdir/*

%files -n lib%oname-qt6-devel
%_includedir/qt6/*.h
%_includedir/qt6/Qsci/
%_qt6_libdatadir/*.so
%_libdir/*_qt6.so

%files -n lib%oname-qt6-designer
%_qt6_plugindir/designer/*.so

%files -n python3-module-%oname-qt6
%python3_sitelibdir/PyQt6/Qsci.*so
%python3_sitelibdir/PyQt6_QScintilla-%version.dist-info/
#python3_sitelibdir/PyQt6/Qsci.pyi
%_datadir/qt6/qsci3/api/python/*.api

%files -n python3-module-%oname-qt6-devel
%dir %python3_sitelibdir/PyQt6/bindings/
%dir %python3_sitelibdir/PyQt6/bindings/Qsci/
%python3_sitelibdir/PyQt6/bindings/Qsci/*

%if_with docs
%files -n %libname-doc
%_docdir/%libname-%version
%endif

%changelog
* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 2.14.1-alt1
- initial build for ALT Sisyphus
