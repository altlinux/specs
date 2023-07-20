%define _unpackaged_files_terminate_build 1
%define pypi_name conan
%define pypi_name_server conan-server
%define mod_name %pypi_name
%define mod_name1 conans

%def_with check

Name: %pypi_name
Version: 2.0.8
Release: alt1
Summary: Conan - The open-source C/C++ package manager (client)
License: MIT
Group: System/Libraries
Url: https://conan.io
Vcs: https://github.com/conan-io/conan
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps -- metadata_client
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps -- metadata_server
%pyproject_builddeps_check
BuildRequires: python3-modules-sqlite3
%endif

%description
Decentralized, open-source (MIT), C/C++ package manager (client).

%package -n python3-module-%pypi_name_server
Summary: Conan - The open-source C/C++ package manager (server)
Group: System/Libraries
Requires: python3-module-%pypi_name
%pyproject_runtimedeps -- metadata_server

%description -n python3-module-%pypi_name_server
Decentralized, open-source (MIT), C/C++ package manager (server).

%prep
%setup
%autopatch -p1
mkdir -p ../%pypi_name_server
cp -a -t ../%pypi_name_server/ .
mv ../%pypi_name_server/setup{_server,}.py
%pyproject_deps_resync_build
%pyproject_deps_resync metadata_client metadata
pushd ../%pypi_name_server
%pyproject_deps_resync metadata_server metadata
popd
%if_with check
%pyproject_deps_resync_check_pipreqfile %mod_name1/requirements_dev.txt
%endif

%build
%pyproject_build
cd ../%pypi_name_server
%pyproject_build

%install
%pyproject_install
cd ../%pypi_name_server
# overwrite everything installed by client package
# today's actual difference is conans/server only
%pyproject_install
rm -r %buildroot%python3_sitelibdir/%mod_name1/test/

%check
%pyproject_run_pytest -ra -Wignore %mod_name1/test/unittests/

%files
%doc README.md
%_bindir/conan
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name1/
%exclude %python3_sitelibdir/%mod_name1/server/
%exclude %python3_sitelibdir/%mod_name1/conan_server.py
%exclude %python3_sitelibdir/%mod_name1/__pycache__/conan_server.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n python3-module-%pypi_name_server
%_bindir/conan_server
%python3_sitelibdir/%mod_name1/server/
%python3_sitelibdir/%mod_name1/conan_server.py
%python3_sitelibdir/%mod_name1/__pycache__/conan_server.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name_server}/

%changelog
* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 2.0.8-alt1
- 2.0.4 -> 2.0.8.

* Thu May 11 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)
- update requires

* Tue Feb 14 2023 Alexander Stepchenko <geochip@altlinux.org> 1.58.0-alt1
- Update to 1.58.0

* Fri Jan 06 2023 Pavel Vainerman <pv@altlinux.ru> 1.56.0-alt1
- new version (1.56.0) with rpmgs script

* Sun Mar 13 2022 Vitaly Lipatov <lav@altlinux.ru> 1.46.0-alt1
- new version 1.46.0 (with rpmrb script)
- update buildreqs

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.43.1-alt2
- drop artificial upper bound for yaml req

* Mon Dec 20 2021 Vitaly Lipatov <lav@altlinux.ru> 1.43.1-alt1
- new version 1.43.1 (with rpmrb script)
- update buildreqs

* Fri Oct 08 2021 Vitaly Lipatov <lav@altlinux.ru> 1.41.0-alt1
- new version 1.41.0 (with rpmrb script)

* Tue Oct 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.40.1-alt2
- drop artificial upper bound for jwt req

* Thu Sep 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.40.1-alt1
- new version 1.40.1 (with rpmrb script)

* Mon Sep 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.40.0-alt1
- new version 1.40.0 (with rpmrb script)
- update (build)requires

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.39.0-alt1
- new version 1.39.0 (with rpmrb script)

* Tue Jun 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.37.1-alt2
- drop artificial upper bound for jinja2 req

* Fri Jun 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.37.1-alt1
- new version 1.37.1 (with rpmrb script) (ALT bug 40208)
- update requires, drop urllib3 < 1.26

* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 1.35.0-alt1
- new version 1.35.0 (with rpmrb script)

* Tue Feb 02 2021 Vitaly Lipatov <lav@altlinux.ru> 1.33.1-alt1
- new version 1.33.1 (with rpmrb script)

* Sat Jan 23 2021 Pavel Vainerman <pv@altlinux.ru> 1.33.0-alt1
- new version (1.33.0) with rpmgs script

* Wed Dec 16 2020 Vitaly Lipatov <lav@altlinux.ru> 1.32.1-alt1
- new version 1.32.1 (with rpmrb script)
- use node_semver instead of semver (see bug 39442)

* Fri Dec 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.32.0-alt1
- new version 1.32.0 (with rpmrb script)
- update requirements, fix test removing

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt1
- new version 1.31.0 (with rpmrb script)

* Thu Oct 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.30.2-alt1
- new version 1.30.2 (with rpmrb script)

* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.22.0-alt1
- new version 1.22.0 (with rpmrb script)
- cleanup spec, switch to python3

* Fri Dec 01 2017 Pavel Vainerman <pv@altlinux.ru> 0.29.1-alt1
- new build (returned the tests to the package)

* Fri Dec 01 2017 Pavel Vainerman <pv@altlinux.ru> 0.29.1-alt0.1
- initial build version (0.29.1) with rpmgs script

