%define oname watchdog

%def_enable check

Name: python3-module-%oname
Version: 0.8.3
Release: alt4.git20150727.1

Summary: Filesystem events monitoring
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/watchdog/

BuildArch: noarch

# https://github.com/gorakhargosh/watchdog.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pathtools
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-sphinx

%add_python3_req_skip AppKit FSEvents _watchdog_fsevents

Conflicts: python-module-%oname

%description
Python API and shell utilities to monitor file system events.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Python API and shell utilities to monitor file system events.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python API and shell utilities to monitor file system events.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|&-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
rm -f tests/test_delayed_queue.py
%__python3 setup.py test -v

%files
%doc AUTHORS *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%changelog
* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.3-alt4.git20150727.1
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.3-alt3.git20150727.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt3.git20150727
- Rebuilt to update provides.
- Cleaned up spec.
- Enabled tests.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt2.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt2.git20150727.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.8.3-alt2.git20150727
- Rebuild with "def_disable check"
- Cleanup buildreq

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150727
- New snapshot

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150222
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150211
- Version 0.8.3

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141031
- Version 0.8.2

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140916
- Initial build for Sisyphus

