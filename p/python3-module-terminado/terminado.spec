%define _unpackaged_files_terminate_build 1
%define pypi_name terminado
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.18.1
Release: alt1
Summary: Tornado websocket backend for the Xterm.js Javascript terminal emulator
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/terminado/
Vcs: https://github.com/jupyter/terminado
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
%pyproject_builddeps_metadata_extra test
%endif

%description
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

Modules:

* terminado.management: controls launching virtual terminals, connecting
  them to Tornado's event loop, and closing them down.
* terminado.websocket: Provides a websocket handler for communicating
  with a terminal.
* terminado.uimodule: Provides a Terminal Tornado UI Module.

JS:

* terminado/_static/terminado.js: A lightweight wrapper to set up a
  term.js terminal with a websocket.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
* Fri Oct 04 2024 Stanislav Levin <slev@altlinux.org> 0.18.1-alt1
- 0.11.1 -> 0.18.1.

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt1
- new version 0.11.1 (with rpmrb script)

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- new version 0.9.5 (with rpmrb script)

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- use python3-module-sphinx

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- separated build python3 module, cleanup spec
- new version 0.9.1 (with rpmrb script)
- temp. disable check due its network nature
- switch to build from tarball

* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.5-alt2.git20150717
- Fixed build (closes: #35984).

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.git20150717.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools
- Fix tests

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1.git20150717.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150717.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150717
- Version 0.5

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150203
- Version 0.4

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141117
- Initial build for Sisyphus

