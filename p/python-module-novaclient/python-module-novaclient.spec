Name:		python-module-novaclient
Version:	2.8.0.26
Release:	alt1
Summary:	Python API and CLI for OpenStack Nova

Group:		Development/Python
License:	ASL 2.0
URL:		http://pypi.python.org/pypi/python-novaclient
Source0:	%{name}-%{version}.tar.gz

Patch0001:	%{name}-do-not-include-versioninfo.patch

BuildArch:	noarch
BuildRequires:	python-module-distribute

Requires:	python-module-argparse
Requires:	python-module-simplejson
Requires:	python-module-httplib2
Requires:	python-module-prettytable
Requires:	python-module-distribute

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements
100 of the OpenStack Nova API.

%package doc
Summary:	Documentation for OpenStack Nova API Client
Group:		Documentation

BuildRequires:	python-module-sphinx
BuildRequires:	python-module-objects.inv

%description doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements
100 of the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%setup -q
%patch0001 -p2

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%{_bindir}/nova
%{python_sitelibdir}/novaclient
%{python_sitelibdir}/*.egg-info

%files doc
%doc html

%changelog
* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.0.26-alt1
- Initial release for Sisyphus (based on Fedora)
