%define _unpackaged_files_terminate_build 1
%define oname django-sortedm2m

%def_with python3

Name: python-module-%oname
Version: 1.3.3
Release: alt1
Summary: Drop-in replacement for django's many to many field with sorted relations
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-sortedm2m/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gregmuellegger/django-sortedm2m.git
Source0: https://pypi.python.org/packages/7c/b5/f09fb9e492f0a6193b17ece580663563d153949b3f323a49a0efd2bcf459/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
sortedm2m is a drop-in replacement for django's own ManyToManyField. The
provided SortedManyToManyField behaves like the original one but
remembers the order of added relations.

%package -n python3-module-%oname
Summary: Drop-in replacement for django's many to many field with sorted relations
Group: Development/Python3

%description -n python3-module-%oname
sortedm2m is a drop-in replacement for django's own ManyToManyField. The
provided SortedManyToManyField behaves like the original one but
remembers the order of added relations.

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.git20140923.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140923
- Initial build for Sisyphus

