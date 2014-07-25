##%%global sname oslo.sphinx

Name:       python-module-oslo-sphinx
Version:    1.1
Release:    alt1
Summary:    OpenStack Sphinx Extensions

Group:      Development/Python
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    %{name}-%{version}.tar

BuildArch:  noarch
Requires:   python-module-setuptools

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.

%prep
%setup
# Remove bundled egg-info
rm -rf oslo_sphinx.egg-info

%build
%python_build

%install
%python_install

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%{python_sitelibdir}/oslo
%{python_sitelibdir}/*.egg-info
%{python_sitelibdir}/*-nspkg.pth

%changelog
* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.1-alt1
- First build for ALT (based on Fedora 1.1-2.fc21.src)

