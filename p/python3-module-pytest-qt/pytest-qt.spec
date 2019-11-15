%define oname pytest-qt

%def_disable check

Name: python3-module-%oname
Version: 1.2.2
Release: alt2

Summary: pytest plugin for Qt (PyQt and PySide) application testing
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-qt/
# https://github.com/nicoddemus/pytest-qt.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides pytestqt
%py3_requires PyQt4 PySide


%description
pytest-qt is a pytest plugin that allows programmers to write tests for
PySide and PyQt applications.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.git20141105.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.git20141105.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20141105
- Initial build for Sisyphus

