%define oname dobbin

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: Pure-Python object database
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/dobbin
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Dobbin is a transactional object database for Python (2.6+). It's a fast
and convenient way to persist Python objects on disk.

Key features:

* MVCC concurrency model
* Implemented all in Python
* Multi-thread, multi-process with no configuration
* Zero object access overhead in general case
* Optimal memory sharing between threads
* Efficient storing and serving of binary streams
* Architecture open to alternative storages

%package tests
Summary: Tests for Dobbin
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Dobbin is a transactional object database for Python (2.6+). It's a fast
and convenient way to persist Python objects on disk.

This package contains tests for Dobbin.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- build for python3 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt1.1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.1.1
- NMU: Use buildreq for BR.

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-3.3

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

