%define oname validate_email

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1.git20141013
Summary: Validate_email verify if an email address is valid and really exists
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/validate_email/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/syrusakbary/validate_email.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pydns
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-py3dns
%endif

%py_provides %oname
%py_requires DNS

%description
Validate_email is a package for Python that check if an email is valid,
properly formatted and really exists.

%package -n python3-module-%oname
Summary: Validate_email verify if an email address is valid and really exists
Group: Development/Python3
%py3_provides %oname
%py3_requires DNS

%description -n python3-module-%oname
Validate_email is a package for Python that check if an email is valid,
properly formatted and really exists.

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
%doc AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20141013
- Initial build for Sisyphus

