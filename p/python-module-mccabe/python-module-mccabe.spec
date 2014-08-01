%def_with python3

%global modname mccabe

Name:               python-module-mccabe
Version:            0.2.1
Release:            alt1
Summary:            McCabe complexity checker

Group:              Development/Python
License:            MIT
URL:                http://pypi.python.org/pypi/mccabe
Source0:            %{name}-%{version}.tar

BuildArch:          noarch
BuildRequires:      python-devel, python-module-setuptools

%if_with python3
BuildRequires:      rpm-build-python3, python3-module-setuptools
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
%doc README.rst
%{python_sitelibdir}/%{modname}.py*
%{python_sitelibdir}/%{modname}-%{version}*

%if_with python3
%files -n python3-module-mccabe
%doc README.rst
%{python3_sitelibdir}/%{modname}.py*
%{python3_sitelibdir}/%{modname}-%{version}-*
%{python3_sitelibdir}/__pycache__/%{modname}.*

%endif

%changelog
* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.1-alt1
- First build for ALT (based on Fedora 0.2.1-6.fc21.src)

