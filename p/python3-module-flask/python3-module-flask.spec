%define _unpackaged_files_terminate_build 1
%define pypi_name Flask
%define mod_name flask

%def_with check

Name: python3-module-%mod_name
Version: 3.0.0
Release: alt1

Summary: Flask is a lightweight WSGI web application framework
License: BSD-3-Clause
Group: Development/Python3
Url: https://palletsprojects.com/p/flask/
Vcs: https://github.com/pallets/flask

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
Provides: python3-module-%pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Flask is a lightweight WSGI web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around Werkzeug and
Jinja and has become one of the most popular Python web application
frameworks.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE.rst CHANGES.rst README.rst
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0 (fixed CVE-2023-30861).

* Tue Sep 20 2022 Danil Shein <dshein@altlinux.org> 2.2.2-alt1
- new version 2.2.2
  + migrate to pyproject macroses

* Mon Mar 14 2022 Danil Shein <dshein@altlinux.org> 2.0.3-alt2
- spec clean up

* Thu Mar 03 2022 Danil Shein <dshein@altlinux.org> 2.0.3-alt1
- new version 1.1.2 -> 2.0.3
  + enable tests

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt2
- set Conflicts to python2 module instead of Provides

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- build python3 package separately

* Fri Aug 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt1
- Version updated to 1.1.1

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.12.2-alt4
- Updated runtime dependencies.

* Wed Mar 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt3
- Fixed spec.

* Wed Mar 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt2
- Fixed spec.

* Wed Mar 07 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt1
- Version 0.12.2

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Version 0.10.1
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2.1
- Fixed build

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt2
- Don't package testsuite.

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt1
- Initial build for Sisyphus.

