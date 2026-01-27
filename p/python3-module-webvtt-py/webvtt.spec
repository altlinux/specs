%define _unpackaged_files_terminate_build 1
%define pypi_name webvtt-py
%define module_name webvtt

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: A Python library for reading, writing and converting WebVTT caption files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/webvtt-py
Vcs: https://github.com/glut23/webvtt-py

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
A very simple tool to debug HTTP(S) client and server request.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -s tests -p "*.py"

%files
%doc LICENSE README.rst  
%_bindir/webvtt
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 27 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.5.1-alt1
- Initial build for ALT Sisyphus.
