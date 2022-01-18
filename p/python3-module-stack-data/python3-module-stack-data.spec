%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname stack_data

Name: python3-module-stack-data
Version: 0.1.4
Release: alt1
Summary: Library that extracts data from stack frames and tracebacks
License: MIT
Group: Development/Python3
Url: https://github.com/alexmojaki/stack_data

BuildArch: noarch

# https://github.com/alexmojaki/stack_data.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3(executing) python3(asttokens) python3(pure_eval)
# test dependencies
BuildRequires: python3(pytest) python3(typeguard) python3(pygments) python3(littleutils)

%description
This is a library that extracts data from stack frames and tracebacks,
particularly to display more useful tracebacks than the default.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

python3 setup.py test

%files
%doc LICENSE.txt
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.4-alt1
- Initial build for ALT.
