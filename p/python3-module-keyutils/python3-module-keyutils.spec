%define _unpackaged_files_terminate_build 1
%define pypi_name keyutils

Name:    python3-module-%pypi_name
Version: 0.6
Release: alt1

Summary: python-keyutils is a set of python bindings for keyutils (available from http://people.redhat.com/~dhowells/keyutils), a key management suite that leverages the infrastructure provided by the Linux kernel for safely storing and retrieving sensitive infromation in your programs.
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/sassoftware/python-keyutils

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: libkeyutils-devel
BuildRequires: gcc-c++
BuildRequires: python3-module-cython

Source: %pypi_name-%version.tar

%description
python-keyutils is a set of python bindings for keyutils (available from
http://people.redhat.com/~dhowells/keyutils), a key management suite that
leverages the infrastructure provided by the Linux kernel for safely storing
and retrieving sensitive infromation in your programs.

%prep
%setup -n %pypi_name-%version

%build
%add_optflags -w -Wno-int-conversion -Wno-implicit-function-declaration
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS ChangeLog LICENSE README.rst TODO
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 28 2025 Artem Semenov <savoptik@altlinux.org> 0.6-alt1
- Initial build for Sisyphus
