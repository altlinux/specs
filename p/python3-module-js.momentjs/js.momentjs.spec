%define oname js.momentjs

Name: python3-module-%oname
Version: 2.13.1
Release: alt2

Summary: Fanstatic packaging of Moment.js
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.momentjs/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-fanstatic
BuildRequires: python3-module-pytest

%py3_requires js

%description
This library packages Moment.js for fanstatic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export PYTHONPATH=$PWD
%__python3 setup.py test
py.test3

%files
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.13.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.13.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.1-alt1
- Updated to upstream version 2.13.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.3.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.3.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.3.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3.1-alt1
- Version 2.8.3-1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt1
- Initial build for Sisyphus

