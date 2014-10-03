%define oname cmsplugin_facebook

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20120907
Summary: Django CMS Facebook Plugins
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/cmsplugin_facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrisglass/cmsplugin_facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This is an attempt at centralizing all the Facebook widgets ("like",
"share" and similar) in one reusable django-cms plugin.

%package -n python3-module-%oname
Summary: Django CMS Facebook Plugins
Group: Development/Python3

%description -n python3-module-%oname
This is an attempt at centralizing all the Facebook widgets ("like",
"share" and similar) in one reusable django-cms plugin.

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
%doc AUTHORS *.rst cms_facebook
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst cms_facebook
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20120907
- Initial build for Sisyphus

