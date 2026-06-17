%define _unpackaged_files_terminate_build 1
%define pypi_name aiohttp
%define mod_name %pypi_name
%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 3.14.1
Release: alt1

Summary: http client/server for asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohttp/
Vcs: https://github.com/aio-libs/aiohttp

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# merged test utils into main
Provides: python3-module-aiohttp-tests = %EVR
Obsoletes: python3-module-aiohttp-tests < %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3-module-cython
BuildRequires: libllhttp-devel
%if_with check
# not packaged yet
%add_pyproject_deps_check_filter python-on-whales
%add_pyproject_deps_check_filter setuptools-git
%add_pyproject_deps_check_filter wait-for-it
%pyproject_builddeps_metadata_extra speedups
%pyproject_builddeps_check
%endif

%add_python_extra speedups

%description
http client/server for asyncio (PEP-3156).

%prep
%setup
%autopatch -p1
%python3_fix_shebang .
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
cat requirements/base.in \
    requirements/test-common-base.in \
    requirements/test-common.in \
    >> requirements/test.in
%pyproject_deps_resync_check_pipreqfile requirements/test.in
%endif

%build
# link with system libllhttp
export AIOHTTP_USE_SYSTEM_DEPS=1
rm -r vendor/llhttp/
make cythonize-nodeps
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- pytest -m 'not dev_mode and not internal' \
	-vra -o=addopts='' \
	-n auto \
	--ignore=tests/autobahn \
	--ignore=tests/test_proxy_functional.py \
	--ignore-glob='tests/test_benchmarks_*' \
	--deselect='tests/test_web_functional.py::test_keepalive_expires_on_time' \
	tests \
%ifarch ppc64le
	||:
%endif

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 08 2026 Stanislav Levin <slev@altlinux.org> 3.14.1-alt1
- 3.13.5 -> 3.14.1 (fixes: CVE-2026-34993, CVE-2026-47265).

* Wed Apr 01 2026 Stanislav Levin <slev@altlinux.org> 3.13.5-alt1
- 3.13.3 -> 3.13.5.

* Mon Jan 12 2026 Stanislav Levin <slev@altlinux.org> 3.13.3-alt1
- 3.13.2 -> 3.13.3
  + (fixes: CVE-2025-69223, CVE-2025-69224, CVE-2025-69225, CVE-2025-69226)
  + (fixes: CVE-2025-69227, CVE-2025-69228, CVE-2025-69229, CVE-2025-69230)

* Wed Oct 29 2025 Stanislav Levin <slev@altlinux.org> 3.13.2-alt1
- 3.12.15 -> 3.13.2.

* Tue Jul 29 2025 Stanislav Levin <slev@altlinux.org> 3.12.15-alt1
- 3.12.14 -> 3.12.15.

* Fri Jul 11 2025 Stanislav Levin <slev@altlinux.org> 3.12.14-alt1
- 3.12.13 -> 3.12.14.

* Mon Jun 16 2025 Stanislav Levin <slev@altlinux.org> 3.12.13-alt1
- 3.12.12 -> 3.12.13.

* Tue Jun 10 2025 Stanislav Levin <slev@altlinux.org> 3.12.12-alt1
- 3.12.11 -> 3.12.12.

* Mon Jun 09 2025 Stanislav Levin <slev@altlinux.org> 3.12.11-alt1
- 3.12.9 -> 3.12.11.

* Thu Jun 05 2025 Stanislav Levin <slev@altlinux.org> 3.12.9-alt1
- 3.12.7 -> 3.12.9.

* Tue Jun 03 2025 Stanislav Levin <slev@altlinux.org> 3.12.7-alt1
- 3.12.6 -> 3.12.7.

* Mon Jun 02 2025 Stanislav Levin <slev@altlinux.org> 3.12.6-alt1
- 3.12.4 -> 3.12.6.

* Thu May 29 2025 Stanislav Levin <slev@altlinux.org> 3.12.4-alt1
- 3.11.18 -> 3.12.4.

* Mon May 12 2025 Stanislav Levin <slev@altlinux.org> 3.11.18-alt1
- 3.11.13 -> 3.11.18.

* Thu Mar 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.13-alt1
- 3.11.13 released

* Tue Feb 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.12-alt1
- 3.11.12 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.11-alt1
- 3.11.11 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.10-alt1
- 3.10.10 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.5-alt1
- 3.10.5 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.9.5-alt1
- 3.9.5 released

* Mon Mar 25 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 3.9.3-alt2
- Added async_timeout req & BR for Python < 3.11

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.3-alt1
- 3.9.3 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.1-alt1
- 3.9.1 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.5-alt1
- 3.8.5 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.4-alt1
- 3.8.4 released

* Mon Jan 02 2023 Anton Midyukov <antohami@altlinux.org> 3.8.3-alt1
- new version 3.8.3

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 3.8.1-alt2
- Added missing mandatory runtime dependency on charset_normalizer.

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.1-alt1
- 3.8.1 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.4-alt1
- 3.7.4 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.3-alt1
- 3.7.3 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.1-alt1
- 3.7.1 released

* Sun May 10 2020 Anton Midyukov <antohami@altlinux.org> 3.6.2-alt1
- 3.6.2 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.6.1-alt1
- 3.6.1 released

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 3.5.4-alt1
- New version 3.5.4
- Disable check
- Cleanup spec

* Thu Mar 14 2019 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt2
- Added py3_requires chardet (Closes: 36270)
- Cleanup spec

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.5-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt1
- New version 2.2.5

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt2
- Updated build dependencies.

* Thu May 04 2017 Anton Midyukov <antohami@altlinux.org> 1.3.5-alt1
- New version 1.3.5

* Fri Jan 13 2017 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- Disabled build documentation

* Sun Aug 07 2016 Anton Midyukov <antohami@altlinux.org> 0.21.5-alt1
- New version 0.21.5 (Closes: 32363)
- Disable tests (girar not support IPv6)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 0.15.3-alt7.git20150425.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Mar  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.3-alt7.git20150425
- (.spec) cleanup unneeded BuildRequires(pre): rpm-macros-sphinx
  (and other BuildReq cleanups)

* Fri Mar 04 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt6.git20150425
- Removed dependence to python-module-gunicorn, which created selfdeps.

* Thu Mar  3 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.3-alt5.git20150425
- (.spec) Safer build: cleanup ../python3/ before use.
  (Nevertheless, beware: using ../python3/ for the build is very dirty
  because it is not cleaned up automatically afterwards and can cause
  side-effects in other unsafe specs, similar to this one. This dirty
  use of ../python3/ is very wide-spread in Sisyphus packages.)
- (.spec) Fail if the maintainer's intentions are not fulfilled
  (because the sources or the build environment have changed since the
  spec was written): rm/cp without -f

* Thu Mar 03 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt4.git20150425.2
- Remove self dependence.

* Wed Mar 02 2016 Denis Medvedev <nbr@altlinux.org>  0.15.3-alt3.git20150425.2
- File "inv"  for sphynx is in python-sphinx-objects.inv.

* Mon Feb 08 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt2.git20150425.2
- NMU: manual build

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.15.3-alt2.git20150425.1
- NMU: Use buildreq for BR.

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 0.15.3-alt2.git20150425
- rebuild with cleaned build requires

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.3-alt1.git20150425
- Version 0.15.3

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20150217
- Version 0.14.4

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1.git20150123
- Version 0.14.2

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt2.git20141231
- Version 0.13.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1.a0.git20141229
- Version 0.13.1a0

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20141129
- Version 0.11.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.a.git20141125
- Initial build for Sisyphus

