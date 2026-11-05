%define _unpackaged_files_terminate_build 1
%define pypi_name pygit2
%define mod_name pygit2

%def_with check

Name: python3-module-%pypi_name
Version: 1.21.0
Release: alt1

Summary: Python bindings for libgit2
License: GPL-2.0 with linking exception
Group: Development/Python3
Url: https://pypi.org/project/pygit2/
Vcs: https://github.com/libgit2/pygit2

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0
BuildRequires: libgit2-devel

%description
Bindings to the libgit2 shared library, implements Git plumbing.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
rm -r pygit2
%pyproject_run_pytest -vra test

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 05 2026 Anton Zhukharev <ancieg@altlinux.org> 1.21.0-alt1
- Updated to 1.21.0.

* Wed Sep 23 2026 Anton Zhukharev <ancieg@altlinux.org> 1.20.1-alt1
- Updated to 1.20.1.

* Mon Aug 10 2026 Anton Zhukharev <ancieg@altlinux.org> 1.20.0-alt1
- Updated to 1.20.0.

* Mon Jun 15 2026 Anton Zhukharev <ancieg@altlinux.org> 1.19.3-alt1
- Updated to 1.19.3.

* Mon Mar 30 2026 Anton Zhukharev <ancieg@altlinux.org> 1.19.2-alt1
- Updated to 1.19.2.

* Mon Dec 29 2025 Anton Zhukharev <ancieg@altlinux.org> 1.19.1-alt1
- Updated to 1.19.1.

* Tue Dec 16 2025 Anton Zhukharev <ancieg@altlinux.org> 1.19.0-alt1
- Updated to 1.19.0.

* Fri May 23 2025 Anton Zhukharev <ancieg@altlinux.org> 1.18.0-alt1
- Updated to 1.18.0 (closes #54422).

* Sun Feb 11 2024 Anton Zhukharev <ancieg@altlinux.org> 1.14.1-alt1
- Updated to 1.14.1.

* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 1.14.0-alt1
- Updated to 1.14.0.

* Fri Dec 15 2023 Anton Zhukharev <ancieg@altlinux.org> 1.13.3-alt1
- Built for ALT Sisyphus.
