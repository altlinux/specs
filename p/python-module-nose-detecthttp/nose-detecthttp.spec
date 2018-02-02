%define _unpackaged_files_terminate_build 1
%define oname nose-detecthttp

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.1
Summary: A nose plugin to detect tests making http calls
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/nose-detecthttp

# https://github.com/venmo/nose-detecthttp.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-vcrpy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-vcrpy
%endif

%py_provides detecthttp

%description
A nose plugin that can detect tests making external http calls.

%package -n python3-module-%oname
Summary: A nose plugin to detect tests making http calls
Group: Development/Python3
%py3_provides detecthttp

%description -n python3-module-%oname
A nose plugin that can detect tests making external http calls.

%prep
%setup

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

%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1
- Updated to upstream version 0.2.0.
- Disabled check phase due to no tests being present.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.dev.git20141124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.dev.git20141124
- Initial build for Sisyphus

