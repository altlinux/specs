%global pypi_name fixtures
%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.3.14
Release:        alt1
Summary:        Fixtures, reusable state for writing clean tests and more

Group:		Development/Python
License:        ASL 2.0 or BSD
URL:            https://launchpad.net/python-fixtures
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

BuildRequires:  python-devel

Requires:       python-module-testtools

%description
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Fixtures, reusable state for writing clean tests and more
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
Requires:       python3-module-testtools

%description -n python3-module-%{pypi_name}
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%endif

%prep
%setup

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.14-alt1
- First build for ALT (based on Fedora 0.3.14-3.fc21.src)
