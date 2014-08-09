Name:             python-module-cinderclient
Version:          1.0.9
Release:          alt1
Summary:          Python API and CLI for OpenStack Cinder

Group:            Development/Python
License:          ASL 2.0
URL:              http://github.com/openstack/python-cinderclient
Source0:          %{name}-%{version}.tar

#
# patches_base=1.0.9
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch
Patch0002: 0002-Stop-pbr-from-installing-requirements-during-build.patch

BuildArch:        noarch

BuildRequires:    python-devel
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-pbr
BuildRequires:    python-module-d2to1

Requires:         python-module-babel
Requires:         python-module-prettytable
Requires:         python-module-requests
Requires:         python-module-setuptools
Requires:         python-module-simplejson
Requires:         python-module-six

%description
Client library (cinderclient python module) and command line utility
(cinder) for interacting with OpenStack Cinder (Block Storage) API.


%package doc
Summary:          Documentation for OpenStack Nova API Client
Group:            Documentation

BuildRequires:    python-module-sphinx

%description      doc
Client library (cinderclient python module) and command line utility
(cinder) for interacting with OpenStack Cinder (Block Storage) API.

This package contains auto-generated documentation.


%prep
%setup

%patch0001 -p1
%patch0002 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATCINDERCLIENTVERSION/%{version}/ cinderclient/__init__.py

# Remove bundled egg-info
rm -rf python_cinderclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%python_build

%install
%python_install

install -p -D -m 644 tools/cinder.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/cinderclient/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/cinder.1 %{buildroot}%{_mandir}/man1/cinder.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%{_bindir}/cinder
%{python_sitelibdir}/cinderclient
%{python_sitelibdir}/*.egg-info
%{_sysconfdir}/bash_completion.d/cinder.bash_completion
%{_mandir}/man1/cinder.1*

%files doc
%doc html

%changelog
* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.9-alt1
- New version (based on Fedora 1.0.9-1.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2.26-alt1
- Initial release for Sisyphus (based on Fedora)

