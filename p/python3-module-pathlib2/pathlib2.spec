%define _unpackaged_files_terminate_build 1
%define pypi_name pathlib2
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.7.post1
Release: alt1.1
Summary: Fork of pathlib aiming to support the full stdlib Python API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pathlib2
Vcs: https://github.com/jazzband/pathlib2
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-six
BuildRequires: python3-module-pytest
BuildRequires: python3-test
%endif

%description
The old pathlib module on bitbucket is in bugfix-only mode. The goal of
pathlib2 is to provide a backport of standard pathlib module which tracks
the standard library module, so all the newest features of the standard
pathlib can be used also on older Python versions.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.3.7.post1-alt1.1
- Demodernized packaging.

* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 2.3.7.post1-alt1
- 2.3.7 -> 2.3.7.post1.

* Wed Feb 05 2025 Grigory Ustinov <grenka@altlinux.org> 2.3.7-alt1
- Automatically updated to 2.3.7.

* Tue Jan 30 2024 Grigory Ustinov <grenka@altlinux.org> 2.3.6-alt1.1
- NMU: moved on modern pyproject macros.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 2.3.6-alt1
- 2.3.3 -> 2.3.6.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 2.3.3-alt2
- Built Python3 package from its ows src.

* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 2.3.3-alt1
- 2.3.2 -> 2.3.3.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 2.3.2-alt1
- 2.1.0 -> 2.3.2.

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt3
- Fixed build dependencies.

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt2
- Updated build spec.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-2
- Add %%check.
- Change URL from pathlib to pathlib2 page.

* Mon Nov 14 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-1
- Initial package.
