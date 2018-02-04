%define _unpackaged_files_terminate_build 1
%define oname rsttst

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.1
Summary: rsttst makes your reStructuredText testable
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rsttst/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/willemt/rsttst.git
Source0: https://pypi.python.org/packages/b5/d9/fed43b27554822d8dd227f290707ae06eabf223a79522a27a1e1469994f3/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Pygments python-module-docutils
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Pygments python3-module-docutils
%endif

%py_provides %oname
%py_requires pygments docutils

%description
rsttst makes your reStructuredText documentation testable.

%package -n python3-module-%oname
Summary: rsttst makes your reStructuredText testable
Group: Development/Python3
%py3_provides %oname
%py3_requires pygments docutils

%description -n python3-module-%oname
rsttst makes your reStructuredText documentation testable.

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
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20150215.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20150215
- Initial build for Sisyphus

