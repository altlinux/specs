%define _unpackaged_files_terminate_build 1
%define oname Quamash

%def_with check

Name: python3-module-%oname
Version: 0.6.1
Release: alt3

Summary: Implementation of the PEP 3156 event-loop (tulip) api using the Qt Event-Loop
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Quamash/

# https://github.com/harvimt/quamash.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: xvfb-run
BuildRequires: python3-module-pytest
BuildRequires: python3-module-PyQt5
%endif

BuildArch: noarch

%description
Implementation of the PEP 3156 Event-Loop with Qt.

Quamash requires Python 3.4 and either PyQt4, PyQt5 or PySide.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export QUAMASH_QTIMPL=PyQt5
xvfb-run py.test3 -v

%files
%doc README.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/quamash/

%changelog
* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 0.6.1-alt3
- Fixed FTBFS (Python3.10).

* Mon Aug 03 2020 Stanislav Levin <slev@altlinux.org> 0.6.1-alt2
- Fixed FTBFS.

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1
- 0.5.5 -> 0.6.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.5-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20150118.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1.git20150118.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20150118
- Version 0.5.1

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

