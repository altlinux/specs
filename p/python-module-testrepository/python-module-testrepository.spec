# Created by pyp2rpm-1.0.1
%global pypi_name testrepository

Name:           python-module-%{pypi_name}
Version:        0.0.18
Release:        alt2
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


%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%python_build

%install
%python_install

%files
%doc README.txt Apache-2.0
%{_bindir}/testr
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt2
- BuildReq: python-module-subunit -> python-module-python-subunit

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt1
- First build for ALT (based on Fedora 0.0.18-1.fc21.src)

