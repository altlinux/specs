%define _unpackaged_files_terminate_build 1
%define oname spec

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt1.1
Summary: Specification-style output for nose
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/spec/

# https://github.com/bitprophet/spec.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-django python-module-nose python-module-setuptools python-module-six python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django python3-module-nose python3-module-setuptools python3-module-six python3-module-nose
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
python setup.py test ||:
%if_with python3
pushd ../python3
python3 setup.py test ||:
popd
%endif

%files
%doc *.mkd
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.mkd
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Updated to upstream version 1.4.0.

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

