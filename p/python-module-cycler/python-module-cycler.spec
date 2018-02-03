%define oname cycler

%def_with python3

Name: python-module-%oname
Version: 0.10.0
Release: alt1.1
Summary: Composable style cycles
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Cycler
Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/matplotlib/cycler.git
Source: https://pypi.python.org/packages/c2/4b/137dea450d6e1e3d474e1d873cd1d4f7d3beed7e0dc973b06e8e10d32488/%oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-coverage python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-coverage python3-module-pytest-cov
%endif

%py_provides %oname
%py_requires six

%description
The public API of cycler consists of a class Cycler and a factory
function cycler(). The function provides a simple interface for creating
'base' Cycler objects while the class takes care of the composition and
iteration logic.

%if_with python3
%package -n python3-module-%oname
Summary: Composable style cycles
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
The public API of cycler consists of a class Cycler and a factory
function cycler(). The function provides a simple interface for creating
'base' Cycler objects while the class takes care of the composition and
iteration logic.
%endif

%prep
%setup -n %oname-%version

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
#python run_tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
#python3 run_tests.py -v
popd
%endif

%files
%doc *.rst doc/source/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/source/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Apr 10 2017 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- New version 0.10.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.post1.git20150822.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.post1.git20150822
- Initial build for Sisyphus
