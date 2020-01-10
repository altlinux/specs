%define oname oslo-sphinx

Name:       python3-module-%oname
Version:    1.1
Release:    alt2

Summary:    OpenStack Sphinx Extensions
License:    ASL 2.0
Group:      Development/Python3
URL:        https://launchpad.net/oslo
BuildArch:  noarch

Source0:    %{name}-%{version}.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-pbr
BuildRequires: python3-module-d2to1


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
%python3_build

%install
%python3_install

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%python3_sitelibdir/oslo
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth


%changelog
* Fri Jan 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt2
- porting on python3

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.1-alt1
- First build for ALT (based on Fedora 1.1-2.fc21.src)

