%define oname hitchserve

%def_with python3

Name: python-module-%oname
Version: 0.3.8
Release: alt1.git20150705
Summary: Service orchestration library for the Hitch testing framework
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitchserve/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitchserve.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hitch python-module-humanize
BuildPreReq: python-module-colorama python-module-psutil
BuildPreReq: python-module-pyuv python-module-tblib
BuildPreReq: python-module-faketime
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hitch python3-module-humanize
BuildPreReq: python3-module-colorama python3-module-psutil
BuildPreReq: python3-module-pyuv python3-module-tblib
BuildPreReq: python3-module-faketime
%endif

%py_provides %oname
%py_requires hitch humanize colorama psutil pyuv tblib faketime

%description
HitchServe is a UNIX service orchestration library for the Hitch testing
framework.

%if_with python3
%package -n python3-module-%oname
Summary: Service orchestration library for the Hitch testing framework
Group: Development/Python3
%py3_provides %oname
%py3_requires hitch humanize colorama psutil pyuv tblib faketime

%description -n python3-module-%oname
HitchServe is a UNIX service orchestration library for the Hitch testing
framework.
%endif

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
* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt1.git20150705
- Initial build for Sisyphus

