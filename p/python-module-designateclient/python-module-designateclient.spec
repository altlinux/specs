%define component designateclient
Name:           python-module-%{component}
Version:        1.0.2
Release:        alt2
Summary:        Openstack DNS (Designate) API Client
License:        Apache-2.0
Group:          Development/Python
Url:            http://launchpad.net/python-designateclient
Source:         %{name}-%{version}.tar
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-module-pbr >= 0.5.21
# Documentation requirements:
BuildRequires:  python-module-sphinx >= 1.1.2
# Test requirements:
BuildRequires:  python-module-discover

BuildRequires:  python-module-mox >= 0.5.3
BuildRequires:  python-module-python-subunit
BuildRequires:  python-module-testrepository >= 0.0.17
Requires:       python-module-cliff >= 1.4.3
Requires:       python-module-jsonschema
Requires:       python-module-keystoneclient >= 0.6.0
Requires:       python-module-pbr
Requires:       python-module-requests >= 1.1
Requires:       python-module-stevedore >= 0.14

BuildArch:      noarch

%description
This is a client for the OpenStack Designate API. There's a Python API
(the designateclient module), and a command-line tool (designate).

%package doc
Summary:        Openstack DNS (Designate) API Client - Documentation
Group:          Documentation
Requires:       %{name} = %{version}

%description doc
This package contains documentation files for %{name}.

%prep
%setup

%build
%python_build
python setup.py build_sphinx && rm doc/build/html/.buildinfo

%install
%python_install
fdupes doc

%check
testr init && testr run --parallel

%files
%doc README.rst
%{_bindir}/designate
%{python_sitelibdir}/%{component}/
%{python_sitelibdir}/python_%{component}-*.egg-info

%files doc
%doc doc/build/html

%changelog
* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.2-alt2
- BuildReq: python-module-subunit -> python-module-python-subunit

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.2-alt1
- First build for ALT (based on OpenSuSe 1.0.2-1.1.src)

