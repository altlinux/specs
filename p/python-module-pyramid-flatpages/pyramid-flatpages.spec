%define oname pyramid-flatpages

%def_with python3

Name: python-module-%oname
Version: 0.0.1.mdfix
Release: alt2
Summary: Manage your site's pages using configurable data sources for storage
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid-flatpages/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires pyramid repoze.tm2 weberror markdown

%description
Manage your site's pages using configurable data sources for storage.

%package -n python3-module-%oname
Summary: Manage your site's pages using configurable data sources for storage
Group: Development/Python3
%py3_requires pyramid repoze.tm2 weberror markdown

%description -n python3-module-%oname
Manage your site's pages using configurable data sources for storage.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1.mdfix-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1.mdfix-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1.mdfix-alt1
- Initial build for Sisyphus

