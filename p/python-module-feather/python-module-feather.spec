%define  modulename feather

Name:    python-module-%modulename
Version: 0.9.1
Release: alt2

Summary: a framework for writing small plugin-based applications
License: BSD-3-Clause
Group:   Development/Python
URL:     https://github.com/jdodds/feather

Packager: Evgenii Terechkov <evg@altlinux.ru>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar
Patch: %name-%version-%release.patch

%description
%summary

%prep
%setup -n %modulename-%version
%patch -p1

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Sun Jul 02 2017 Evgenii Terechkov <evg@altlinux.ru> 0.9.1-alt2
- Initial build for Sisyphus
