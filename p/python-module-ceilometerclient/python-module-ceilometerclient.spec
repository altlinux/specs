Name:             python-module-ceilometerclient
Version:          1.0.10
Release:          alt1
Summary:          Python API and CLI for OpenStack Ceilometer

Group:            Development/Python
License:          ASL 2.0
URL:              https://github.com/openstack/%{name}
Source0:          %{name}-%{version}.tar

BuildArch:        noarch
BuildRequires:    python-module-setuptools
BuildRequires:    python-devel
BuildRequires:    python-module-pbr
BuildRequires:    python-module-d2to1

Requires:         python-module-setuptools
Requires:         python-module-argparse
Requires:         python-module-prettytable
Requires:         python-module-iso8601
Requires:         python-module-keystoneclient
Requires:         python-module-six >= 1.4.1

#
# patches_base=1.0.10
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch

%description
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).


%package doc
Summary:          Documentation for OpenStack Ceilometer API Client
Group:            Documentation

BuildRequires:    python-module-sphinx

%description      doc
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).

This package contains auto-generated documentation.


%prep
%setup

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATCEILOMETERCLIENTVERSION/%{version}/ ceilometerclient/__init__.py

# Remove bundled egg-info
rm -rf python_ceilometerclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%python_build

%install
%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%{_bindir}/ceilometer
%{python_sitelibdir}/ceilometerclient
%{python_sitelibdir}/*.egg-info

%files doc
%doc html

%changelog
* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.10-alt1
- First build for ALT (based on Fedora 1.0.10-2.fc21.src)

