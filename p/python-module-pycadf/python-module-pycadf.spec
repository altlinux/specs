# Created by pyp2rpm-1.0.1
%global pypi_name pycadf

Name:           python-module-%{pypi_name}
Version:        0.5.1
Release:        alt1
Summary:        DMTF Cloud Audit (CADF) data model

Group:          Development/Python
License:        ASL 2.0
URL:            https://launchpad.net/pycadf
Source0:       %{name}-%{version}.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-pbr

Requires:       python-module-babel
Requires:       python-module-iso8601
Requires:       python-module-netaddr
Requires:       python-module-oslo-config >= 1.2.0
Requires:       python-module-oslo-messaging
Requires:       python-module-pytz
Requires:       python-module-six >= 1.6.0
Requires:       python-module-webob >= 1.2.3

%description
DMTF Cloud Audit (CADF) data model


%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%python_build


%install
%python_install
mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}/usr/etc/%{pypi_name} %{buildroot}/%{_sysconfdir}/
rm -rf %{buildroot}/%{python_sitelibdir}/%{pypi_name}/tests


%files
%doc README.rst LICENSE
%dir %{_sysconfdir}/%{pypi_name}
%config(noreplace) %{_sysconfdir}/%{pypi_name}/*.conf
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-1.fc21.src)

