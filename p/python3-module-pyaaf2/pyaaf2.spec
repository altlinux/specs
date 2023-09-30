%define _unpackaged_files_terminate_build 1
%define oname pyaaf2

Name: python3-module-%oname
Version: 1.7.0
Release: alt1

Summary: A python module for reading and writing Advanced Authoring Format (AAF) files.

License: MIT
Group: Development/Python3
Url: https://github.com/markreidvfx/pyaaf2

BuildArch: noarch

Source: %name-%version.tar

%py3_provides %oname

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
A python module for reading and writing Advanced Authoring Format (AAF) files.
pyaaf2 is a rewrite of pyaaf1 in pure python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst

%python3_sitelibdir_noarch/*

%changelog
* Thu Sep 14 2023 Aleksei Kalinin <kaa@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus
