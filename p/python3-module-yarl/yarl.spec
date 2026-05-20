Name: python3-module-yarl
Version: 1.24.2
Release: alt1

Summary: Yet another URL library
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/yarl
VCS: https://github.com/aio-libs/yarl

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
The module provides handy URL class for url parsing and changing.
See http://yarl.readthedocs.io for more

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
sed -rn '/^[^-#]/p' requirements/test*.txt > requirements/extra.txt
%pyproject_deps_resync_check_pipreqfile requirements/extra.txt

%build
%pyproject_build

%install
%pyproject_install

%check
export YARL_NO_EXTENSIONS=1
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/yarl
%python3_sitelibdir/yarl-%version.dist-info

%changelog
* Wed May 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.24.2-alt1
- 1.24.2 released

* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.23.0-alt1
- 1.23.0 released

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.22.0-alt1
- 1.22.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.18.3-alt1
- 1.18.3 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.17.1-alt1
- 1.17.1 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.11-alt1
- 1.9.11 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.4-alt1
- 1.9.4 released

* Mon Aug 07 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.9.2-alt2
- resolved FTBFS due to wrong square brackets handling (upstream commit
  0a94c6e4948e00fff072c0cf367afbf4ac36f906)

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.2-alt1
- 1.9.2 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.1-alt1
- 1.8.1 released

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.2-alt1
- 1.7.2 released

* Sat May 22 2021 Anton Midyukov <antohami@altlinux.org> 1.6.3-alt2
- build python3-module-yarl srpm

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- 1.4.2 released

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0
- switch to git

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar at altlinux.org> 0.11.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev at altlinux.org> 0.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Nov 18 2017 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt1
- New version 0.11.0

* Mon May 8 2017 Anton Midyukov <antohami@altlinux.org> 0.9.8-alt1
- New version 0.9.8

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus.
