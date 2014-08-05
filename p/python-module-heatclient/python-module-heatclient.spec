Name:    python-module-heatclient
Version: 0.2.9
Release: alt1
Summary: Python API and CLI for OpenStack Heat

Group:   Development/Python
License: ASL 2.0
URL:     http://pypi.python.org/pypi/python-heatclient
Source0: %{name}-%{version}.tar

#
# patches_base=0.2.9
#
Patch0001: 0001-Nuke-pbr-requirements-handling.patch
Patch0002: 0002-Remove-runtime-dependency-on-python-pbr.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-d2to1
BuildRequires: python-module-pbr

Requires: python-module-argparse
Requires: python-module-httplib2
Requires: python-module-iso8601
Requires: python-module-keystoneclient
Requires: python-module-prettytable
Requires: python-module-six
Requires: python-module-yaml

%description
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

%package doc
Summary: Documentation for OpenStack Heat API Client
Group:   Documentation

BuildRequires: python-module-sphinx

%description doc
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

This package contains auto-generated documentation.

%prep
%setup

%patch0001 -p1
%patch0002 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATHEATCLIENTVERSION/%{version}/ heatclient/__init__.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config.
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%python_build

%install
%python_install
echo "%{version}" > %{buildroot}%{python_sitelibdir}/heatclient/versioninfo

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/heatclient/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%{_bindir}/heat
%{python_sitelibdir}/heatclient
%{python_sitelibdir}/*.egg-info

%files doc
%doc html

%changelog
* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.9-alt1
- First build for ALT (based on Fedora 0.2.9-1.fc21.src)

