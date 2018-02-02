%define oname pebble

%def_with python3

Name: python-module-%oname
Version: 4.3.6
Release: alt2.git20171213.1
Summary: Threading and multiprocessing eye-candy
License: LGPLv3
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/Pebble/

# https://github.com/noxdafox/pebble.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-futures
BuildRequires: python-module-pytest
BuildRequires: /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires multiprocessing concurrent.futures

%description
Pebble provides a neat API to manage threads and processes within an
application.

%if_with python3
%package -n python3-module-%oname
Summary: Threading and multiprocessing eye-candy
Group: Development/Python3
%py3_provides %oname
%py3_requires multiprocessing

%description -n python3-module-%oname
Pebble provides a neat API to manage threads and processes within an
application.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3

pushd ../python3
#fix python version for python3 tests
grep -q 'python -m pytest' ./test/run-tests.sh && \
sed -i 's/python -m pytest/python3 -m pytest/' ./test/run-tests.sh
popd
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
./test/run-tests.sh

%if_with python3
pushd ../python3
./test/run-tests.sh
popd
%endif

%files
%doc *.rst doc/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.3.6-alt2.git20171213.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.6-alt2.git20171213
- Updated runtime dependencies.

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.6-alt1.git20171213
- Updated to upstream version 4.3.6.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.8-alt1.git20140910.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.8-alt1.git20140910.1
- NMU: Use buildreq for BR.

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.8-alt1.git20140910
- Initial build for Sisyphus

