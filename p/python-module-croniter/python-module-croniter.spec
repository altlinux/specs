%global pypi_name croniter

%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.3.4
Release:        alt1.1
Summary:        Iteration for datetime object with cron like format
Group:          Development/Python

License:        MIT
URL:            http://github.com/kiorky/croniter
Source0:        %{name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  python-devel unzip
BuildRequires:  python-module-setuptools

# For tests
BuildRequires:  python-module-dateutil
BuildRequires:  python-module-pytz

Requires:       python-module-dateutil

%description
Croniter provides iteration for datetime object with cron like format.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Iteration for datetime object with cron like format
Group:          Development/Python
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-dateutil
BuildRequires:  python3-module-pytz

Requires:       python3-module-dateutil

%description -n python3-module-%{pypi_name}
Croniter provides iteration for datetime object with cron like format.
%endif

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove reundant script header to avoid rpmlint warnings
find -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

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

%check
PYTHONPATH=%{buildroot}%{python_sitelibdir}/ %{__python} -m unittest %{pypi_name}.tests.test_croniter
rm -fr %{buildroot}%{python_sitelibdir}/%{pypi_name}/tests/

%if_with python3
PYTHONPATH=%{buildroot}%{python3_sitelibdir}/ %{__python3} -m unittest discover -s %{buildroot}%{python3_sitelibdir}/%{pypi_name}/tests -p 'test_*.py'
rm -fr %{buildroot}%{python3_sitelibdir}/%{pypi_name}/tests/
%endif

%files
%doc README.rst docs/LICENSE
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README.rst docs/LICENSE
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.4-alt1
- First build for ALT (based on Fedora 0.3.4-4.fc21.src)

