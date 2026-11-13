%define _unpackaged_files_terminate_build 1
%define pypi_name flit-core
%define mod_name flit_core
# tomli is required for Python < 3.11, it's debundled and the metadata can't be
# patched
%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 4.2.0
Release: alt1
Summary: Distribution-building parts of Flit
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/flit-core
Vcs: https://github.com/pypa/flit
BuildArch: noarch
Source: %name-%version.tar
Source2: tox.ini
Patch0: %name-%version-alt.patch
# legacy name
%py3_provides flit-core
# required for older branches having Python < 3.11
%if %tomli
Requires: python3-module-tomli
%endif
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
%summary.

%prep
%setup
%autopatch -p1
# debundle tomli, required on Python < 3.11
rm -r %mod_name/vendor/
# copy top-level tox.ini to flit_core subdir
cp %SOURCE2 ./
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Nov 13 2026 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1
- 4.1.0 -> 4.2.0

* Wed Sep 30 2026 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1
- 4.0.2 -> 4.1.0

* Mon Aug 24 2026 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1
- 3.12.0 -> 4.0.2

* Thu Aug 20 2026 Stanislav Levin <slev@altlinux.org> 3.12.0-alt3
- Added missing runtime dep on tomli for Python < 3.11.

* Mon Mar 30 2026 Stanislav Levin <slev@altlinux.org> 3.12.0-alt2
- Undone Python vandalism.

* Tue Mar 25 2025 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1
- 3.11.0 -> 3.12.0.

* Wed Feb 19 2025 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.1 -> 3.11.0.

* Tue Nov 05 2024 Stanislav Levin <slev@altlinux.org> 3.10.1-alt1
- 3.9.0 -> 3.10.1.

* Mon May 15 2023 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.8.0 -> 3.9.0.

* Tue Nov 15 2022 Stanislav Levin <slev@altlinux.org> 3.8.0-alt1
- 3.7.1 -> 3.8.0.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1
- 3.6.0 -> 3.7.1.
- Subpackaged PEP517 build backend (flit_core).

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.0-alt1
- Updated to upstream version 3.6.0.

* Tue Aug 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.

* Tue Jun 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt1
- Updated to upstream version 3.2.0.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1
- Updated to upstream version 3.0.0.

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt2
- Disabled bootstrapping.

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michal Cyprian <mcyprian@redhat.com> - 0.9-5
- Use python install wheel macro

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-4
- Rebuild for Python 3.6

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9-3
- Updated spec file with license comments and provides

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9-2
- spec file cleanup

* Sat Jul 2 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.9-1
- Initial RPM release
