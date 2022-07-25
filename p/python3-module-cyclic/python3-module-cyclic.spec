%define _unpackaged_files_terminate_build 1

Name: python3-module-cyclic
Version: 1.0.0
Release: alt1

Summary: Handle cyclic relation
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/neurobin/cyclic
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Handle cyclic relation compared by value.

%prep
%setup

%build
%pyproject_build

cp LICENSE README.md %_builddir/

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/*

%changelog
* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

