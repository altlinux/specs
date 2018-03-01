%define  modulename logan

Name:    python-module-%modulename
Version: 0.7.2
Release: alt1

Summary: Logan is a toolkit for building standalone Django applications
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/dcramer/logan

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Logan is a toolkit for running standalone Django applications. It
provides you with tools to create a CLI runner, manage settings, and the
ability to bootstrap the process.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install
rm -rf %buildroot%python_sitelibdir/tests/%modulename/

%files
%doc README.rst
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus
