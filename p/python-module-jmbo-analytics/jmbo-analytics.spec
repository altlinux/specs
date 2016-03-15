%define oname jmbo-analytics

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20120507.1
Summary: Jmbo analytics app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-analytics/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-analytics.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
panomena-analytics
http://unomena.com

%package -n python3-module-%oname
Summary: Jmbo analytics app
Group: Development/Python3

%description -n python3-module-%oname
panomena-analytics
http://unomena.com

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20120507.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20120507
- Initial build for Sisyphus

