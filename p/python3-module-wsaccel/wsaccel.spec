%define oname wsaccel

Name: python3-module-%oname
Version: 0.6.2
Release: alt2

Summary: Accelerator for ws4py and AutobahnPython
License: Apache
Group: Development/Python3
Url: https://pypi.python.org/pypi/wsaccel/

# https://github.com/methane/wsaccel.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython python3-module-pytest

%py3_provides %oname


%description
WSAccell is WebSocket accelerator for AutobahnPython, ws4py and Tornado.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc ChangeLog *.rst examples
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt1.git20131112.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.2-alt1.git20131112.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.2-alt1.git20131112.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20131112
- Initial build for Sisyphus

