%define oname veusz
Name: python-module-%oname
Version: 1.14
Release: alt2.1
Summary: A Scientific Plotting Package
License: GPLv2+
Group: Development/Python
Url: http://home.gna.org/veusz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar

BuildPreReq: python-devel libnumpy-devel python-module-PyQt4-devel
BuildPreReq: libqt4-devel python-module-sip-devel python-module-pyemf
BuildPreReq: python-module-stsci gcc-c++

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
Requires: %name = %version-%release

%description examples
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains examples for Veusz.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

install -d %buildroot%_man1dir
install -m644 Documents/*.1 %buildroot%_man1dir

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%_man1dir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples

%files docs
%doc Documents/*.txt Documents/*.html Documents/*.pdf

%files examples
%python_sitelibdir/*/examples

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.14-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Dec 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt2
- Extracted examples into separate package

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1
- Initial build for Sisyphus

