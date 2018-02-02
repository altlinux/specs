%define _unpackaged_files_terminate_build 1
%define oname pkgconfig

%def_with python3

Name: python-module-%oname
Version: 1.2.2
Release: alt1.1
Summary: Interface Python with pkg-config
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pkgconfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/matze/pkgconfig.git
Source0: https://pypi.python.org/packages/9d/ba/80910bbed2b4e646a6adab4474d2e506744c260c7002a0e6b41ef8750d8d/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
pkgconfig is a Python module to interface with the pkg-config command
line tool and supports Python 2.6+.

%package -n python3-module-%oname
Summary: Interface Python with pkg-config
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pkgconfig is a Python module to interface with the pkg-config command
line tool and supports Python 2.6+.

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
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20141212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141212
- Initial build for Sisyphus

