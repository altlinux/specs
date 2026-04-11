%define _unpackaged_files_terminate_build 1

Name: python3-module-pyexcel-cli
Version: 0.0.3
Release: alt1

Summary: Lets consume/produce information in excel files in cli
Group: Development/Python3
License: BSD-3-Clause
URL: https://github.com/pyexcel/pyexcel-cli
VCS: https://github.com/pyexcel/pyexcel-cli.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-click
BuildRequires: python3-module-pyexcel

%description
pyexcel-cli brings pyexcel to make it easy to consume/produce information
stored in excel files on command line interface.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir_noarch/pyexcel_cli
%python3_sitelibdir_noarch/%{pyproject_distinfo pyexcel_cli}
%_bindir/pyexcel

%changelog
* Tue Apr 07 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.0.3-alt1
- Initial build (Closes: #58495).
