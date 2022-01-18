%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname littleutils

Name: python3-module-littleutils
Version: 0.2.2
Release: alt1.git.6a3d7b7
Summary: Small personal collection of python utility functions, partly just for fun
License: MIT
Group: Development/Python3
Url: https://github.com/alexmojaki/littleutils

BuildArch: noarch

# https://github.com/alexmojaki/littleutils.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Small personal collection of python utility functions, partly just for fun.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.2-alt1.git.6a3d7b7
- Initial build for ALT.
