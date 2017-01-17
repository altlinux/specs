%define _unpackaged_files_terminate_build 1
%define oname spec

%def_with python3

Name: python-module-%oname
Version: 1.3.1
Release: alt1
Summary: Specification-style output for nose
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/spec/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bitprophet/spec.git
Source0: https://pypi.python.org/packages/32/ce/c213f54e9d395f75afa339aacb4ef5e35165c1bd96a88b63221b1701c14b/%{oname}-%{version}.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-module-psycopg2 python-module-pytest python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-psycopg2 python3-module-pytest python3-module-setuptools python3-module-yaml
BuildRequires: python-module-django python-module-nose python-module-setuptools-tests python3-module-django python3-module-nose python3-module-setuptools-tests rpm-build-python3

#BuildRequires: python-module-django python-module-nose python-module-pytest
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six
#BuildPreReq: python-module-invoke python-module-invocations
#BuildPreReq: python-module-semantic_version
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildRequires: python3-module-django python3-module-nose python3-module-pytest
#BuildPreReq: python3-module-six
#BuildPreReq: python3-module-invoke python3-module-invocations
#BuildPreReq: python3-module-semantic_version
%endif

%py_provides %oname

%description
spec is a Python (2.6+ and 3.3+) testing tool.

%package -n python3-module-%oname
Summary: Specification-style output for nose
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
spec is a Python (2.6+ and 3.3+) testing tool.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt2.git20150423.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt2.git20150423.1
- NMU: Use buildreq for BR.

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 1.2.2-alt2.git20150423
- Rebuild with fixed build requires

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20150423
- Version 1.2.2

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.git20141210
- Version 0.11.2

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.git20131231
- Initial build for Sisyphus

