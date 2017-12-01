%define _unpackaged_files_terminate_build 1
%def_with python3

%define oname mccabe

Name:               python-module-%oname
Version:            0.6.1
Release:            alt1
Summary:            McCabe complexity checker

Group:              Development/Python
License:            Expat
BuildArch:          noarch
URL:                http://pypi.python.org/pypi/mccabe

# https://github.com/pycqa/mccabe.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-pytest-runner
%if_with python3
BuildRequires: python3-module-setuptools rpm-build-python3
BuildRequires: python3-module-pytest-runner
%endif

%description
Ned's script to check McCabe complexity.

This module provides a plugin for ``flake8``, the Python code
checker.

%if_with python3
%package -n python3-module-%oname
Summary: McCabe checker, plugin for flake8
Group: Development/Python3

%description -n python3-module-%oname
Ned's script to check McCabe complexity.

This module provides a plugin for ``flake8``, the Python code
checker.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc README.rst LICENSE
%python_sitelibdir/%{oname}.py*
%python_sitelibdir/%{oname}-%{version}*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/%{oname}.py*
%python3_sitelibdir/%{oname}-%{version}-*
%python3_sitelibdir/__pycache__/%{oname}.*
%endif

%changelog
* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Updated to upstream version 0.6.1.

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Version 0.3.1

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.1-alt1
- First build for ALT (based on Fedora 0.2.1-6.fc21.src)

