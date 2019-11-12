%define oname nose-watch

Name: python3-module-%oname
Version: 0.9.2
Release: alt2

Summary: A nose plugin that re-runs test suite on filesystem event
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/nose-watch/
# https://github.com/lukaszb/nose-watch.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-watchdog
BuildRequires: python3-module-mock
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-pytest

%py3_provides nosewatch
%py3_requires nose watchdog


%description
A Nose plugin that allows to run tests continuously (uses watchdog for
listening to filesystem events).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
rm -fR build
py.test3 -vv

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.2-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1
- Updated to upstream version 0.9.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.dev.git20130219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1.dev.git20130219.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.dev.git20130219
- Initial build for Sisyphus

