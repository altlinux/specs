%define nameD pyseq

Name: python3-module-%nameD
Version: 0.9.1
Release: alt1

Summary: Compressed sequence string module for Python
License: BSD-3-Clause
Group: Development/Python3

Url: https://pypi.org/project/pyseq
Vcs: https://github.com/rsgalloway/pyseq

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
PySeq is a python module that finds groups of items that follow a naming convention
containing a numerical sequence index (e.g. fileA.001.png, fileA.002.png, fileA.003.png...)
and serializes them into a compressed sequence string representing the entire sequence
(e.g. fileA.1-3.png). It should work regardless of where the numerical sequence index is
embedded in the name.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%exclude %_bindir/*
%python3_sitelibdir/%nameD/
%python3_sitelibdir/%{pyproject_distinfo %nameD}/

%changelog
* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.1-alt1
- 0.9.0 -> 0.9.1

* Tue Jul 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux.
