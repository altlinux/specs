%define _unpackaged_files_terminate_build 1
%define oname pygal

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.3.1
Release: alt1.1
Summary: A python svg graph plotting library
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pygal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kozea/pygal.git
Source0: https://pypi.python.org/packages/02/bb/d1c9bd4d21b62cffda6ddeb768b8ce02d1741b2bb1f9ddcc9ece2958586f/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python-module-cairosvg python-module-html5lib python-module-pyquery python-module-setuptools
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-lxml python-module-cairosvg
#BuildPreReq: python-module-pyquery python-module-flask
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-lxml python3-module-cairosvg
#BuildPreReq: python3-module-pyquery python3-module-flask
BuildRequires: python3-module-cairosvg python3-module-html5lib python3-module-pyquery python3-module-setuptools
%endif

%py_provides %oname
#%py_requires lxml cairosvg pyquery flask

%description
pygal is a dynamic SVG charting library written in python. All the
documentation is on http://pygal.org

%package -n python3-module-%oname
Summary: A python svg graph plotting library
Group: Development/Python3
%py3_provides %oname
#%py3_requires lxml cairosvg pyquery flask

%description -n python3-module-%oname
pygal is a dynamic SVG charting library written in python. All the
documentation is on http://pygal.org

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires pytest

%description tests
pygal is a dynamic SVG charting library written in python. All the
documentation is on http://pygal.org

This package contains tests for %oname.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
#%py3_requires pytest

%description -n python3-module-%oname-tests
pygal is a dynamic SVG charting library written in python. All the
documentation is on http://pygal.org

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
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
	mv $i ${i}3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
rm -fR build
python setup.py test
%if_with python3
pushd ../python3
rm -fR build
python3 setup.py test
popd
%endif

%files
%doc README* PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc README* PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.1-alt2.git20141121.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.6.1-alt2.git20141121
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141121
- Initial build for Sisyphus

