%define oname bcdoc

%def_with python3

Name: python-module-%oname
Version: 0.16.0
Release: alt3.git20150617
Summary: ReST document generation tools for botocore
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/bcdoc/

# https://github.com/boto/bcdoc.git
# branch: develop
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-six python-module-docutils
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-six python3-module-docutils
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Tools to help document botocore-based projects.

%package -n python3-module-%oname
Summary: ReST document generation tools for botocore
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Tools to help document botocore-based projects.

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
py.test

%if_with python3
pushd ../python3
python3 setup.py test
py.test3
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
* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.0-alt3.git20150617
- Updated build dependencies.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.16.0-alt2.git20150617.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.0-alt2.git20150617
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.16.0-alt1.git20150617.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.0-alt1.git20150617
- Version 0.16.0

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.git20150223
- Version 0.13.0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.git20140304
- Initial build for Sisyphus

