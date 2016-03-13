%define oname SVGMath

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt3.2.1

Summary: MathML to SVG Converter in Python

Group: Development/Python
License: MIT
Url: http://grigoriev.ru/svgmath/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://dl.sf.net/svgmath/%oname-%version.tar.bz2

%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
SVGMath formats MathML 2.0 expressions as SVG 1.1 images.

%package -n python3-module-%oname
Summary: MathML to SVG Converter in Python
Group: Development/Python3

%description -n python3-module-%oname
SVGMath formats MathML 2.0 expressions as SVG 1.1 images.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.txt LICENSE.txt doc/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.txt LICENSE.txt doc/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt3.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt3.2
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt3.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt3
- Rebuilt with python 2.6

* Mon Feb 23 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt2
- cleanup spec, build as noarch (thanks to Dmitry Levin)

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt1
- new version 0.3.3 (with rpmrb script)

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux Sisyphus
