%define _unpackaged_files_terminate_build 1
%define oname pytest-datafiles

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.1
Summary: py.test plugin to create a 'tmpdir' containing predefined files/directories
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-datafiles/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/omarkohl/pytest-datafiles.git
Source0: https://pypi.python.org/packages/22/9b/bc99e1f5abc17d746e41b1fbfb2643268a75189fd7102eff2cd6f2ecc087/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides pytest_datafiles
%py_requires pytest

%description
py.test plugin to create a tmpdir containing a preconfigured set of
files and/or directories.

%if_with python3
%package -n python3-module-%oname
Summary: py.test plugin to create a 'tmpdir' containing predefined files/directories
Group: Development/Python3
%py3_provides pytest_datafiles
%py3_requires pytest

%description -n python3-module-%oname
py.test plugin to create a tmpdir containing a preconfigured set of
files and/or directories.
%endif

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev0.git20150728.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev0.git20150728
- Initial build for Sisyphus

