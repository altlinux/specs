%define _unpackaged_files_terminate_build 1

Name: git-archive-all
Version: 1.23.1
Release: alt1
Summary: Archive git repositories along with all sumbodules
License: MIT

Group: Development/Tools

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
Requires: git-core

%description
Archives git repository similarly to git-archive(1).
Unlike git-archive this tool archives all submodules.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%_bindir/git-archive-all
%python3_sitelibdir/%{pep427_name %name}.py
%python3_sitelibdir/__pycache__/%{pep427_name %name}*.pyc
%python3_sitelibdir/%{pyproject_distinfo %name}/*

%changelog
* Thu Feb 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.23.1-alt1
- Initial build for ALT.
