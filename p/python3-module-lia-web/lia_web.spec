%define _unpackaged_files_terminate_build 1
%define oname lia-web

Name: python3-module-%oname
Version: 0.3.1
Release: alt1

Summary: A universal web framework adapter for Python that lets you write code once and use it across multiple web frameworks
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lia-web/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/lia/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Fri Jul 24 2026 Alexander Burmatov <thatman@altlinux.org> 0.3.1-alt1
- New 0.3.1 version.

* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.2.3-alt2
- Fix tests.

* Wed Aug 13 2025 Alexander Burmatov <thatman@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus.
