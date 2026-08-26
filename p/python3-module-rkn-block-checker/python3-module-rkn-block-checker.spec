%define pypi_name rkn-block-checker

Name:    python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: RKN Block Checker
License: MIT
Group:   Development/Python3
URL:     https://github.com/MayersScott/rkn-block-checker
Vcs:     https://github.com/MayersScott/rkn-block-checker.git

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(requests)

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A small CLI that figures out whether the connection you're sitting on is
in an RKN/TSPU-blocked zone - and, more usefully, what kind of block it is
(DNS poisoning, TCP reset, TLS DPI on SNI, or an ISP stub page).

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/rkn-check
%python3_sitelibdir_noarch/rkn_checker/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 26 2026 Andrew A. Vasilyev <andy@altlinux.org> 0.5.1-alt1
- Initial build for ALT.

