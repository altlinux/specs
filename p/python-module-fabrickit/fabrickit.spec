%define _unpackaged_files_terminate_build 1
%define oname fabrickit

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.2.2
Release: alt2
Summary: Fabric API wrapper
License: Free
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/fabrickit/

Source: %oname-%version.tar.gz

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-Fabric
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-Fabric
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%py_requires fabric

%description
This is a simple fabric wrapper for emitting Exceptions and several
utils.

%package -n python3-module-%oname
Summary: Fabric API wrapper
Group: Development/Python3
%py3_provides %oname
%py3_requires fabric

%description -n python3-module-%oname
This is a simple fabric wrapper for emitting Exceptions and several
utils.

%prep
%setup -q -n %{oname}-%{version}

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.2-alt2
- Disabled python-3 build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Version 0.1.8

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1
- Initial build for Sisyphus

