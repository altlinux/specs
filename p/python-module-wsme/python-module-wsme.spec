# Created by pyp2rpm-1.0.1
%global pypi_name WSME
%global lpypi_name wsme

Name:           python-module-%{lpypi_name}
Version:        0.6.4
Release:        alt1
Summary:        Web Services Made Easy
Group:          Development/Python

License:        MIT
URL:            https://pypi.python.org/pypi/WSME
Source0:        %{name}-%{version}.tar
Patch:          %{name}-namespace-disable.patch
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-pbr

Requires:       python-module-simplegeneric
Requires:       python-module-six
Requires:       python-module-webob
Requires:       python-module-ipaddr
Requires:       python-module-ordereddict

%description
Web Services Made Easy, simplifies the implementation of
multiple protocol REST web services by providing simple yet
powerful typing which removes the need to directly
manipulate the request and the response objects.

%prep
%setup
%patch

%build
%python_build

%install
%python_install

%files
%doc README.rst LICENSE examples/
%{python_sitelibdir}/wsme*
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Version 0.6.4

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.6-alt1
- First build for ALT (based on Fedora 0.6-3.fc21.src)

