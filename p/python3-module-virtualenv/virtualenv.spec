%define _unpackaged_files_terminate_build 1
%define pypi_name virtualenv
%define system_wheels_path %(%__python3 -c 'import os, sys, system_seed_wheels; sys.stdout.write(os.path.dirname(system_seed_wheels.__file__))' 2>/dev/null || echo unknown)

%def_with check

Name: python3-module-%pypi_name
Version: 20.26.6
Release: alt1
Summary: Virtual Python Environment builder
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/virtualenv/
VCS: https://github.com/pypa/virtualenv
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# system seed wheels
Requires: python3-module-system-seed-wheels-wheels
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-module-system-seed-wheels-wheels
%endif

%description
Tool to create isolated Python environments.

With virtualenv it is became possible to keep separate set of python libraries
for each of your project.

Just exec "virtualenv /your/dir" and whole python enviroment (including
setuptools and easy_install) will be installed there. You could exec scripts
in newly created environment by invoking /your/dir/bin/python

%description -l ru_RU.UTF-8
Утилита для создания изолированных окружений для Python.

С Virtualenv вы можете создать независимые наборы библиотек для каждого
вашего проекта. Опционально вы можете запретить использование системных
библиотек.

Просто выполните "virtualenv /your/dir" и полное виртуальное окружение Python
будет создано в каталоге, который вы указали (setuptools  и easy_install будут
также установлены и при вызове будут устанавливать новые библиотеки в ваше
виртуальное окружение). Чтобы выполнить ваши скрипты в вновь созданном окружение
запускайте их при помощи /your/dir/bin/python

%prep
%setup
%patch -p1

# remove all bundled seed wheels
rm src/virtualenv/seed/wheels/embed/*.whl
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%_bindir/{virtualenv,virtualenv3}

%check
export PIP_FIND_LINKS=%system_wheels_path
%pyproject_run_pytest -ra tests

%files
%doc README.md
%_bindir/virtualenv3
%python3_sitelibdir/virtualenv/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 07 2024 Stanislav Levin <slev@altlinux.org> 20.26.6-alt1
- 20.26.5 -> 20.26.6.

* Wed Sep 18 2024 Stanislav Levin <slev@altlinux.org> 20.26.5-alt1
- 20.26.4 -> 20.26.5.

* Tue Sep 10 2024 Stanislav Levin <slev@altlinux.org> 20.26.4-alt1
- 20.26.3 -> 20.26.4.

* Mon Jun 24 2024 Stanislav Levin <slev@altlinux.org> 20.26.3-alt1
- 20.26.2 -> 20.26.3.

* Tue May 14 2024 Stanislav Levin <slev@altlinux.org> 20.26.2-alt1
- 20.26.1 -> 20.26.2.

* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 20.26.1-alt1
- 20.26.0 -> 20.26.1.

* Wed Apr 24 2024 Stanislav Levin <slev@altlinux.org> 20.26.0-alt1
- 20.25.3 -> 20.26.0.

* Thu Apr 18 2024 Stanislav Levin <slev@altlinux.org> 20.25.3-alt1
- 20.25.2 -> 20.25.3.

* Wed Apr 17 2024 Stanislav Levin <slev@altlinux.org> 20.25.2-alt1
- 20.25.1 -> 20.25.2.

* Wed Mar 27 2024 Stanislav Levin <slev@altlinux.org> 20.25.1-alt1
- 20.24.6 -> 20.25.1.

* Thu Nov 09 2023 Stanislav Levin <slev@altlinux.org> 20.24.6-alt1
- 20.24.3 -> 20.24.6.

* Mon Aug 14 2023 Stanislav Levin <slev@altlinux.org> 20.24.3-alt1
- 20.24.2 -> 20.24.3.

* Wed Jul 26 2023 Stanislav Levin <slev@altlinux.org> 20.24.2-alt1
- 20.24.1 -> 20.24.2.

* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 20.24.1-alt1
- 20.23.1 -> 20.24.1.

* Tue Jun 20 2023 Stanislav Levin <slev@altlinux.org> 20.23.1-alt1
- 20.23.0 -> 20.23.1.

* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 20.23.0-alt1
- 20.20.0 -> 20.23.0.

* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 20.20.0-alt1
- 20.19.0 -> 20.20.0.

* Fri Feb 17 2023 Stanislav Levin <slev@altlinux.org> 20.19.0-alt1
- 20.17.1 -> 20.19.0.

* Tue Dec 06 2022 Stanislav Levin <slev@altlinux.org> 20.17.1-alt1
- 20.17.0 -> 20.17.1.

* Wed Nov 30 2022 Stanislav Levin <slev@altlinux.org> 20.17.0-alt1
- 20.16.7 -> 20.17.0.

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 20.16.7-alt1
- 20.16.6 -> 20.16.7.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 20.16.6-alt1
- 20.16.5 -> 20.16.6.

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 20.16.5-alt1
- 20.16.3 -> 20.16.5.

* Fri Aug 12 2022 Stanislav Levin <slev@altlinux.org> 20.16.3-alt1
- 20.14.2 -> 20.16.3.

* Fri Jun 24 2022 Fr. Br. George <george@altlinux.org> 20.14.2-alt1
- 20.14.0 -> 20.14.2.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 20.14.0-alt1
- 20.13.4 -> 20.14.0.

* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 20.13.4-alt1
- 20.13.3 -> 20.13.4.

* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 20.13.3-alt1
- 20.13.2 -> 20.13.3.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 20.13.2-alt1
- 20.13.1 -> 20.13.2.

* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 20.13.1-alt1
- 20.13.0 -> 20.13.1.

* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 20.13.0-alt1
- 20.10.0 -> 20.13.0.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 20.10.0-alt1
- 20.9.0 -> 20.10.0.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 20.9.0-alt1
- 20.8.1 -> 20.9.0.

* Mon Sep 27 2021 Stanislav Levin <slev@altlinux.org> 20.8.1-alt1
- 20.8.0 -> 20.8.1.

* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 20.8.0-alt1
- 20.7.2 -> 20.8.0.

* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 20.7.2-alt1
- 20.6.0 -> 20.7.2.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 20.6.0-alt1
- 20.4.7 -> 20.6.0.

* Mon May 24 2021 Stanislav Levin <slev@altlinux.org> 20.4.7-alt1
- 20.4.6 -> 20.4.7.

* Fri May 07 2021 Stanislav Levin <slev@altlinux.org> 20.4.6-alt1
- 20.4.4 -> 20.4.6.

* Fri Apr 23 2021 Stanislav Levin <slev@altlinux.org> 20.4.4-alt1
- 20.1.0 -> 20.4.4.
- Switched to system seed wheels.

* Mon Oct 26 2020 Stanislav Levin <slev@altlinux.org> 20.1.0-alt1
- 16.7.9 -> 20.1.0.

* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 16.7.9-alt2
- Disabled testing against Python2.

* Fri Feb 07 2020 Stanislav Levin <slev@altlinux.org> 16.7.9-alt1
- 16.7.7 -> 16.7.9.

* Fri Nov 15 2019 Stanislav Levin <slev@altlinux.org> 16.7.7-alt1
- 16.7.6 -> 16.7.7.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 16.7.6-alt1
- 16.7.2 -> 16.7.6.

* Tue Aug 13 2019 Stanislav Levin <slev@altlinux.org> 16.7.2-alt1
- 16.6.0 -> 16.7.2.

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 16.6.0-alt1
- 16.5.0 -> 16.6.0.

* Thu May 09 2019 Stanislav Levin <slev@altlinux.org> 16.5.0-alt1
- 16.4.3 -> 16.5.0.

* Sun Mar 24 2019 Stanislav Levin <slev@altlinux.org> 16.4.3-alt1
- 16.1.0 -> 16.4.3.

* Thu Nov 01 2018 Stanislav Levin <slev@altlinux.org> 16.1.0-alt1
- 16.0.0 -> 16.1.0.

* Thu May 31 2018 Stanislav Levin <slev@altlinux.org> 16.0.0-alt1
- 15.1.0 -> 16.0.0

* Thu Mar 29 2018 Stanislav Levin <slev@altlinux.org> 15.1.0-alt3
- Fix system sys.path down to virtualenv
- Cleanup patches

* Sun Mar 25 2018 Stanislav Levin <slev@altlinux.org> 15.1.0-alt2
- Fix installation within the bare virtualenv under python3
- Cleanup spec

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 15.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Fr. Br. George <george@altlinux.ru> 15.1.0-alt1
- Autobuild version bump to 15.1.0

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.0.3-alt2
- Fixed build spec with py.test3

* Thu Sep 01 2016 Fr. Br. George <george@altlinux.ru> 15.0.3-alt1
- Autobuild version bump to 15.0.3
- Fix build/tests

* Wed Aug 31 2016 Denis Medvedev <nbr@altlinux.org> 13.1.0-alt2
- fixed sitelibs for python3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 13.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 13.1.0-alt1
- Version 13.1.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.0.5-alt1
- Version 12.0.5

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.0.4-alt1
- Version 12.0.4

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.0.1-alt1
- Version 12.0.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.6-alt1
- Version 1.11.6

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt2
- Added provides '%%modulename' for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1.1
- Fixed build

* Tue Apr 02 2013 Aleksey Avdeev <solo@altlinux.ru> 1.9.1-alt1
- 1.9.1 (Closes: #28670)

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon May 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.1
- Added module for Python 3

* Wed Feb 08 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7-alt1
- New version (Closes: #26819)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt1.1.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.1
- Rebuilt with python 2.6

* Sun May 17 2009 Maxim Ivanov <redbaron at altlinux.org> 1.3.3-alt1
- Bump to 1.3.3
- added docs

* Wed Sep 17 2008 Maxim Ivanov <redbaron at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

