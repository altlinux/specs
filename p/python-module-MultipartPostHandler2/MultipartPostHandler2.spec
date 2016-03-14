%define oname MultipartPostHandler2

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20140925.1
Summary: A handler for urllib2 to enable multipart form uploading
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/MultipartPostHandler2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sergiomb2/MultipartPostHandler2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
A handler for urllib2 to enable multipart form uploading.

Enables the use of multipart/form-data for posting forms
add a fix for utf-8 systems.

%package -n python3-module-%oname
Summary: A handler for urllib2 to enable multipart form uploading
Group: Development/Python3

%description -n python3-module-%oname
A handler for urllib2 to enable multipart form uploading.

Enables the use of multipart/form-data for posting forms
add a fix for utf-8 systems.

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
%doc *.txt examples/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt examples/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20140925.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140925
- Initial build for Sisyphus

