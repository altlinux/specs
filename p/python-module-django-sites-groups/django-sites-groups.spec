%define _unpackaged_files_terminate_build 1
%define oname django-sites-groups

%def_with python3

Name: python-module-%oname
Version: 1.9.2
Release: alt1
Summary: Organize sites from the Django sites framework into groups
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-sites-groups/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-sites-groups.git
Source0: https://pypi.python.org/packages/96/a6/83111bfd4f057ff5ae1ee1c02383ca4ce50c50d5a6c3a58378b1db6ac978/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Organize sites from the Django sites framework into groups.

%package -n python3-module-%oname
Summary: Organize sites from the Django sites framework into groups
Group: Development/Python3

%description -n python3-module-%oname
Organize sites from the Django sites framework into groups.

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20120513.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20120513
- Initial build for Sisyphus

