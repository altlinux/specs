%define _unpackaged_files_terminate_build 1

%define pypi_name newspaper3k

Name: python3-module-%pypi_name
Version: 0.2.8
Release: alt1

Summary: Simplified python article discovery & extraction
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/newspaper3k

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

# imported from https://files.pythonhosted.org/packages/source/n/newspaper3k/newspaper3k-0.2.8.tar.gz
# as this version is not available from upstream git-repo at
# https://github.com/codelucas/newspaper/
Source: %pypi_name-%version.tar

%description
newspaper3k is a news, full-text, and article metadata extraction in
Python 3.

%prep
%setup -n %pypi_name-%version/newspaper3k/%pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/newspaper/
%python3_sitelibdir/%{pyproject_distinfo newspaper3k}

%changelog
* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus
