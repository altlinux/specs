%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname Quamash

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.5
Release: alt2.1
Summary: Implementation of the PEP 3156 event-loop (tulip) api using the Qt Event-Loop
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/Quamash/

# https://github.com/harvimt/quamash.git
Source: %{oname}-%{version}.zip

BuildRequires: xvfb-run
%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(asyncio) python-module-pathlib
BuildRequires: python-module-pytest
BuildRequires: python-module-PyQt4
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio) python3-module-pathlib
BuildRequires: python3-module-pytest
BuildRequires: python3-module-PyQt4
%endif

%py_provides quamash
%py_requires asyncio

%description
Implementation of the PEP 3156 Event-Loop with Qt.

Quamash requires Python 3.4 and either PyQt4, PyQt5 or PySide.

%package -n python3-module-%oname
Summary: Implementation of the PEP 3156 event-loop (tulip) api using the Qt Event-Loop
Group: Development/Python3
%py3_provides quamash
%py3_requires asyncio

%description -n python3-module-%oname
Implementation of the PEP 3156 Event-Loop with Qt.

Quamash requires Python 3.4 and either PyQt4, PyQt5 or PySide.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
xvfb-run py.test -vv
python setup.py test
%endif

%if_with python3
pushd ../python3
python3 setup.py test
xvfb-run py.test3 -vv
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
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

