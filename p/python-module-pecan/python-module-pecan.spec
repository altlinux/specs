# Created by pyp2rpm-1.0.1
%global pypi_name pecan

Name:           python-module-%{pypi_name}
Version:        0.4.5
Release:        alt1
Summary:        A lean WSGI object-dispatching web framework
Group:          Development/Python

License:        BSD
URL:            http://github.com/dreamhost/pecan
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools

Requires:       python-module-webob >= 1.2
Requires:       python-module-simplegeneric >= 0.8
Requires:       python-module-mako >= 0.4.0
Requires:       python-module-singledispatch
Requires:       python-module-webtest >= 1.3.1
Requires:       python-module-setuptools
Requires:       python-module-argparse
Requires:       python-module-logutils

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc LICENSE README.rst
%{_bindir}/pecan
%{_bindir}/gunicorn_pecan
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.5-alt1
- First build for ALT (based on Fedora 0.4.5-4.fc21)

