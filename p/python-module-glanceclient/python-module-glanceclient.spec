Name:             python-module-glanceclient
Version:          0.12.0
Release:          alt1
Summary:          Python API and CLI for OpenStack Glance

Group:            Development/Python
License:          ASL 2.0
URL:              http://github.com/openstack/python-glanceclient
Source0:          %{name}-%{version}.tar

#
# patches_base=0.12.0
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch

BuildArch:        noarch
BuildRequires:    python-devel
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-d2to1
BuildRequires:    python-module-pbr
BuildRequires:    python-module-sphinx

Requires:         python-module-httplib2
Requires:         python-module-keystoneclient
Requires:         python-module-prettytable
Requires:         python-module-setuptools
Requires:         python-module-warlock
Requires:         python-module-pyOpenSSL

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.


%package doc
Summary:          Documentation for OpenStack Nova API Client
Group:            Documentation

BuildRequires:    python-module-sphinx

%description      doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

This package contains auto-generated documentation.


%prep
%setup

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATGLANCECLIENTVERSION/%{version}/ glanceclient/__init__.py

# Remove bundled egg-info
rm -rf python_glanceclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

%build
%python_build

%install
%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# generate man page
sphinx-build -b man doc/source man
install -p -D -m 644 man/glance.1 %{buildroot}%{_mandir}/man1/glance.1


%files
%doc README.rst
%doc LICENSE
%{_bindir}/glance
%{python_sitelibdir}/glanceclient
%{python_sitelibdir}/*.egg-info
%{_mandir}/man1/glance.1.gz

%files doc
%doc html


%changelog
* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 0.12.0-alt1
- First build for ALT (based on Fedora 0.12.0-1.fc20.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.1-alt1
- Initial release for Sisyphus (based on Fedora)

