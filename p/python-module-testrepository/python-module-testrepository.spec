# Created by pyp2rpm-1.0.1
%global pypi_name testrepository
%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.0.18
Release:        alt3
Summary:        A repository of test results
Group:          Development/Python

License:        ASL 2.0
URL:            https://launchpad.net/testrepository
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-fixtures
buildRequires:  python-module-python-subunit
BuildRequires:  python-module-testtools
BuildRequires:  python-module-extras

Requires:       python-module-fixtures
Requires:       python-module-python-subunit
Requires:       python-module-testtools
Requires:       python-module-extras

%description
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        A repository of test results
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-fixtures
buildRequires:  python3-module-python-subunit
BuildRequires:  python3-module-testtools
BuildRequires:  python3-module-extras

Requires:       python3-module-fixtures
Requires:       python3-module-python-subunit
Requires:       python3-module-testtools
Requires:       python3-module-extras

%description -n python3-module-%{pypi_name}
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%endif

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

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
mv %{buildroot}%{_bindir}/testr %{buildroot}%{_bindir}/python3-testr
popd
%endif

%python_install

%files
%doc README.txt Apache-2.0
%{_bindir}/testr
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README.txt Apache-2.0
%{_bindir}/python3-testr
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt3
- Enable python3

* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt2
- BuildReq: python-module-subunit -> python-module-python-subunit

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt1
- First build for ALT (based on Fedora 0.0.18-1.fc21.src)

