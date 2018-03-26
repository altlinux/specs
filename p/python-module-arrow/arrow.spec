%define oname arrow

%def_with python3

Name: python-module-%oname
Version: 0.10.0
Release: alt1
Summary: Better dates & times for Python
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/arrow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/crsmithdev/arrow.git
Source: %oname-%version.tar
Patch0: remove_json_test.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-dateutil python-module-nose
BuildPreReq: python-module-nose-cov python-module-chai
BuildPreReq: python-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-dateutil python3-module-nose
BuildPreReq: python3-module-nose-cov python3-module-chai
BuildPreReq: python3-module-sphinx
BuildPreReq: python3-module-simplejson
%endif

%py_provides %oname

%description
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps. It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%package -n python3-module-%oname
Summary: Better dates & times for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps. It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%prep
%setup -n arrow-%version
pushd tests/
%patch0 -p0
popd

%if_with python3
rm -rf ../python3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html
mkdir man
cp -fR docs/_build/html/* man/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md *.rst LICENSE man/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst LICENSE man/
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.4-alt1.git20140812.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt1.git20140812.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20140812
- Initial build for Sisyphus

