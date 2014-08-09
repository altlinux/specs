Name:             python-module-novaclient
Version:          2.17.0
Release:          alt1
Summary:          Python API and CLI for OpenStack Nova

Group:            Development/Python
License:          ASL 2.0
URL:              http://pypi.python.org/pypi/python-novaclient
Source0:          %{name}-%{version}.tar


#
# patches_base=2.17.0
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch
Patch0002: 0002-Fix-session-handling-in-novaclient.patch
Patch0003: 0003-Fix-authentication-bug-when-booting-an-server-in-V3.patch
Patch0004: 0004-Nova-CLI-for-server-groups.patch
Patch0005: 0005-Avoid-AttributeError-in-servers.Server.__repr__.patch
Patch0006: 0006-Enable-delete-multiple-server-groups-in-one-request.patch

BuildArch:        noarch
BuildRequires:    python-module-setuptools
BuildRequires:    python-devel
BuildRequires:    python-module-d2to1
BuildRequires:    python-module-pbr

Requires:         python-module-argparse
Requires:         python-module-iso8601
Requires:         python-module-prettytable
Requires:         python-module-requests
Requires:         python-module-simplejson
Requires:         python-module-six
Requires:         python-module-babel
Requires:         python-module-keyring
Requires:         python-module-setuptools

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

%package doc
Summary:          Documentation for OpenStack Nova API Client
Group:            Documentation

BuildRequires:    python-module-sphinx

%description      doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%setup -q

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATNOVACLIENTVERSION/%{version}/ novaclient/__init__.py

# Remove bundled egg-info
rm -rf python_novaclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/nova.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/nova

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/novaclient/tests
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/nova.1 %{buildroot}%{_mandir}/man1/nova.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%{_bindir}/nova
%{python_sitelibdir}/novaclient
%{python_sitelibdir}/*.egg-info
%{_sysconfdir}/bash_completion.d
%{_mandir}/man1/nova.1.gz

%files doc
%doc html

%changelog
* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 2.17.0-alt1
- New version (based on Fedora 2.17.0-2.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.0.26-alt1
- Initial release for Sisyphus (based on Fedora)

