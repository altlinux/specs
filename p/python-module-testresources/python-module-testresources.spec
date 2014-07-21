%global pypi_name testresources
%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.2.7
Release:        alt1
Summary:        Testresources, a pyunit extension for managing expensive test resources

Group:		Development/Python
License:        ASL 2.0 and BSD and GPLv2+
# file testresources/tests/TestUtil.py is GPLv2+
URL:            https://launchpad.net/testresources
Source0:        %{name}-%{version}.tar
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-testtools
BuildRequires:  python-module-fixtures

%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Testresources, a pyunit extension for managing expensive test resources
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-testtools
BuildRequires:  python3-module-fixtures

%description -n python3-module-%{pypi_name}
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%endif

%prep
%setup
# Remove bundled egg-info
rm -rf lib/%{pypi_name}.egg-info

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

# %check
# %{__python} setup.py test


%files
%doc README NEWS doc
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README NEWS doc
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.7-alt1
- First build for ALT (based on Fedora 0.2.7-6.fc21.src)

