Name:           python-module-troveclient
Version:        1.0.5
Release:        alt1
Summary:        Client library for OpenStack DBaaS API
Group:          Development/Python

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        %{name}-%{version}.tar

#
# patches_base=1.0.5
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch

BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-sphinx
BuildRequires:  python-module-requests
BuildRequires:  python-module-pbr

Requires:       python-module-argparse
Requires:       python-module-prettytable
Requires:       python-module-requests
Requires:       python-module-setuptools
Requires:       python-module-simplejson
Requires:       python-module-six

# required for tests
# tests currently disabled due missing deps
#BuildRequires:  python-pep8
#BuildRequires:  pyflakes
# currently under review
# https://bugzilla.redhat.com/show_bug.cgi?id=839056
# BuildRequires:  python-flake8

# Currently under review
# https://bugzilla.redhat.com/show_bug.cgi?id=958007
# BuildRequires:  python-hacking
#BuildRequires: python-mock
#BuildRequires: python-testtools
#BuildRequires: python-testrepository

%description
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100 percent (or less ;) ) of the Trove API.

%prep
%setup

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr
sed -i s/REDHATTROVECLIENTVERSION/%{version}/ troveclient/__init__.py

# Remove bundled egg-info
rm -rf %{name}.egg-info

# Let RPM handle the requirements
rm -f {test-,}requirements.txt

# Generate html docs
#export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
%python_build

%install
%python_install

# currently disabling tests
# see buildrequires
#%check
#%%{__python2} setup.py test


%files
%doc html README.rst LICENSE
%{python_sitelibdir}/python_troveclient-%{version}-py?.?.egg-info
%{python_sitelibdir}/troveclient
%{_bindir}/trove

%changelog
* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.5-alt1
- First build for ALT (based on Fedora 1.0.5-1.fc21.src)

