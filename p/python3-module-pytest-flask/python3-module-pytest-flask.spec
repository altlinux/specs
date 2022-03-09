%define _unpackaged_files_terminate_build 1
%define oname pytest-flask

%def_enable check

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: A set of pytest fixtures to test Flask applications
License: MIT
Group: Development/Python3
Url: https://github.com/pytest-dev/pytest-flask
VCS: https://github.com/pytest-dev/pytest-flask

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pip
BuildRequires: python3-module-flask
BuildRequires: python3-module-setuptools_scm
%if_enabled check
BuildRequires: pytest3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
BuildRequires: python3-module-tox-no-deps
BuildRequires: python3-module-tox-console-scripts
BuildRequires: python3-module-coverage
%endif

%py3_provides pytest_flask

%description
An extension of pytest test runner which provides a set of useful 
tools to simplify testing and development of the Flask extensions 
and applications.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PYTHONPATH=%buildroot%python3_sitelibdir/
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc LICENSE *.rst
%python3_sitelibdir/*


%changelog
* Fri Mar 04 2022 Danil Shein <dshein@altlinux.org> 1.2.0-alt1
- new version 0.10.0 -> 1.2.0

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20141124.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.git20141124.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141124
- Version 0.6.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141103
- Version 0.5.0

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141028
- Initial build for Sisyphus

