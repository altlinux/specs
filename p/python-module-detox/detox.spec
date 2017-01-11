%define _unpackaged_files_terminate_build 1
%define oname detox

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.10.0
Release: alt1
Summary: Distributing activities of the tox tool
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/detox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/43/09/104095be078149e441ef926112521ec4bb5796a7828850167f7d0d95ab50/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tox python-module-eventlet
#BuildPreReq: python-module-greenlet 
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tox python3-module-eventlet
#BuildPreReq: python3-module-greenlet python3-module-virtualenv
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
detox is the distributed version of "tox". It makes efficient use of
multiple CPUs by running all possible activities in parallel. It has the
same options and configuration that tox has.

%package -n python3-module-%oname
Summary: Distributing activities of the tox tool
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
detox is the distributed version of "tox". It makes efficient use of
multiple CPUs by running all possible activities in parallel. It has the
same options and configuration that tox has.

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
export PYTHONPATH=%buildroot%python_sitelibdir
export PATH=$PATH:%buildroot%_bindir
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
sed -i 's|"detox"|"detox.py3"|' tests/conftest.py
py.test-%_python3_version
popd
%endif

%files
%doc CHANGELOG
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt2.1
- NMU: Use buildreq for BR.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.9.4-alt2
- Rebuild with "def_disable check"
- Turn off some build dependencies

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt2
- Enabled testing for Python 3 module

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus

