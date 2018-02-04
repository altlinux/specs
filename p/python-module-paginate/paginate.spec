%define _unpackaged_files_terminate_build 1
%define oname paginate

%def_with python3

Name: python-module-%oname
Version: 0.5.6
Release: alt2.1
Summary: Divides large result sets into pages for easier browsing
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/paginate/

# https://github.com/Pylons/paginate.git
Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose
%endif

%py_provides %oname

%description
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.

%if_with python3
%package -n python3-module-%oname
Summary: Divides large result sets into pages for easier browsing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.
%endif

%prep
%setup -n %oname-%version

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
%doc README.md CHANGELOG.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md CHANGELOG.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.6-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.6-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140824.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140824
- Initial build for Sisyphus

