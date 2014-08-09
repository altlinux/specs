Name:       python-module-keystoneclient
# Since folsom-2 OpenStack clients follow their own release plan
# and restarted version numbering from 0.1.1
# https://lists.launchpad.net/openstack/msg14248.html
Version:    0.9.0
Release:    alt1
Summary:    Client library for OpenStack Identity API
License:    ASL 2.0
URL:        http://pypi.python.org/pypi/%{name}
Source0:    %{name}-%{version}.tar
Group:      Development/Python

#
# patches_base=0.9.0
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1

# from requirements.txt
Requires: python-module-argparse
Requires: python-module-iso8601 >= 0.1.4
Requires: python-module-prettytable
Requires: python-module-requests >= 0.8.8
Requires: python-module-oslo-config >= 1.1.0
Requires: python-module-six >= 1.5.2
Requires: python-module-netaddr
Requires: python-module-babel
# other requirements
Requires: python-module-setuptools
Requires: python-module-keyring


%description
Client library and command line utility for interacting with Openstack
Identity API.

%package doc
Summary:    Documentation for OpenStack Identity API Client
Group:      Documentation

BuildRequires: python-module-sphinx

%description doc
Documentation for the client library for interacting with Openstack
Identity API.

%prep
%setup -q

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATKEYSTONECLIENTVERSION/%{version}/ keystoneclient/__init__.py

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_keystoneclient.egg-info

%build
%python_build

%install
%python_install
install -p -D -m 644 tools/keystone.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/keystone.bash_completion

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man
install -p -D -m 644 man/keystone.1 %{buildroot}%{_mandir}/man1/keystone.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%{_bindir}/keystone
%{_sysconfdir}/bash_completion.d/keystone.bash_completion
%{python_sitelibdir}/keystoneclient
%{python_sitelibdir}/*.egg-info
%{_mandir}/man1/keystone.1*

%files doc
%doc LICENSE html

%changelog
* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9.0-alt1
- New build for ALT (based on Fedora 0.9.0-2.fc21.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.2-alt1
- Initial release for Sisyphus (based on Fedora)

