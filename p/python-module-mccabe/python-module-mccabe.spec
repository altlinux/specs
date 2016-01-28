%def_with python3

%global modname mccabe

Name:               python-module-mccabe
Version:            0.3.1
Release:            alt1.1
Summary:            McCabe complexity checker

Group:              Development/Python
License:            Expat
URL:                http://pypi.python.org/pypi/mccabe
Source0:            %{name}-%{version}.tar

BuildArch:          noarch
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires:      python-devel, python-module-setuptools

%if_with python3
#BuildRequires:      rpm-build-python3, python3-module-setuptools
%endif

%description
Ned's script to check McCabe complexity.

This module provides a plugin for ``flake8``, the Python code
checker.

%if_with python3
%package -n python3-module-mccabe
Summary:            McCabe checker, plugin for flake8
Group:              Development/Python

%description -n python3-module-mccabe
Ned's script to check McCabe complexity.

This module provides a plugin for ``flake8``, the Python code
checker.
%endif

%prep
%setup

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%if_with python3
rm -rf ../python3
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

# %check
# %{__python} setup.py test
# %if_with python3
# pushd ../python3
# %{__python3} setup.py test
# popd
# %endif

%files
%doc README.rst LICENSE
%{python_sitelibdir}/%{modname}.py*
%{python_sitelibdir}/%{modname}-%{version}*

%if_with python3 LICENSE
%files -n python3-module-mccabe
%doc README.rst
%{python3_sitelibdir}/%{modname}.py*
%{python3_sitelibdir}/%{modname}-%{version}-*
%{python3_sitelibdir}/__pycache__/%{modname}.*

%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Version 0.3.1

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.1-alt1
- First build for ALT (based on Fedora 0.2.1-6.fc21.src)

