%define _unpackaged_files_terminate_build 1
%define oname veusz

%def_with python3

Name: python-module-%oname
Version: 1.25.1
Release: alt1
Summary: A Scientific Plotting Package
License: GPLv2+
Group: Development/Python
Url: http://home.gna.org/veusz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/e3/20/3ddde71c3585f011fcb7ba4ce95294cf0f9c1536ccbae153247b5f805ca6/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel libnumpy-devel python-module-PyQt4-devel
BuildPreReq: libqt4-devel python-module-sip-devel python-module-pyemf
BuildPreReq: gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-PyQt4-devel
BuildPreReq: python3-module-sip-devel
%endif

%description
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

%package -n python3-module-%oname
Summary: A Scientific Plotting Package
Group: Development/Python3
%add_python3_req_skip pyemf

%description -n python3-module-%oname
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

%package -n python3-module-%oname-examples
Summary: Examples for Veusz
Group: Development/Documentation
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-examples
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains examples for Veusz.

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

%package -n %oname
Summary: A Scientific Plotting Package
Group: Graphics
Conflicts: %name < %version-%release
Requires: %name = %version-%release

%description -n %oname
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains main scripts for Veusz.

%package -n %oname-py3
Summary: A Scientific Plotting Package
Group: Graphics
Requires: python3-module-%oname = %version-%release

%description -n %oname-py3
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains main scripts for Veusz.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
#!/usr/bin/env python
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

install -d %buildroot%_man1dir
install -m644 Documents/*.1 %buildroot%_man1dir

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples

%files docs
%doc Documents/*.txt Documents/*.html Documents/*.pdf

%files examples
%python_sitelibdir/*/examples

%files -n %oname
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%_man1dir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples

%files -n %oname-py3
%doc AUTHORS ChangeLog COPYING README
%_bindir/*.py3
%endif

%changelog
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

