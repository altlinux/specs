%global sname oslo.messaging
%global milestone gf61a889

Name:       python-module-oslo-messaging
Version:    1.3.0.2
Release:    alt1
Summary:    OpenStack common messaging library

Group:      Development/Python
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    %{name}-%{version}.tar
Patch0:     ensure-routing-key-specified-for-qpid.patch

BuildArch:  noarch
Requires:   python-module-setuptools
Requires:   python-module-iso8601
Requires:   python-module-oslo-config
Requires:   python-module-six >= 1.6
Requires:   python-module-stevedore
Requires:   python-module-yaml
Requires:   python-module-kombu
Requires:   python-module-qpid

# FIXME: this dependency will go away soon
Requires:   python-module-eventlet >= 0.13.0

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package doc
Summary:    Documentation for OpenStack common messaging library
Group:      Documentation

BuildRequires: python-module-sphinx
BuildRequires: python-module-oslo-sphinx

# Needed for autoindex which imports the code
BuildRequires: python-module-iso8601
BuildRequires: python-module-oslo-config
BuildRequires: python-module-stevedore

%description doc
Documentation for the oslo.messaging library.

%prep
%setup

%patch0 -p1

sed -i 's/\.\?%{milestone}//' PKG-INFO

# Remove bundled egg-info
rm -rf %{sname}.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py

%build
%python_build

%install
%python_install

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%check

%files
%doc README.rst LICENSE
%{python_sitelibdir}/oslo
%{python_sitelibdir}/*.egg-info
%{python_sitelibdir}/*-nspkg.pth
%{_bindir}/oslo-messaging-zmq-receiver

%files doc
%doc doc/build/html LICENSE

%changelog
* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.3.0.2-alt1
- First build for ALT (based on Fedora 1.3.0.2-4.fc21.src)
