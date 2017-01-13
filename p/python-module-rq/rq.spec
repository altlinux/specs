%define _unpackaged_files_terminate_build 1
%define oname rq

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1
Summary: Simple job queues for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rq/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nvie/rq.git
Source0: https://pypi.python.org/packages/4a/ee/30024f604d33b18e9e15e5780f20e1dc51a96f1a1162889694939a390593/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-redis-py redis
#BuildPreReq: python-module-click
#BuildPreReq: python-module-argparse
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-redis-py
#BuildPreReq: python3-module-click
#BuildPreReq: python3-module-argparse
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3

%description
RQ is a simple, lightweight, library for creating background jobs, and
processing them.

%package -n python3-module-%oname
Summary: Simple job queues for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
RQ is a simple, lightweight, library for creating background jobs, and
processing them.

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
%doc *.md examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6-alt1.git20140917.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1.git20140917.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20140917
- Initial build for Sisyphus

