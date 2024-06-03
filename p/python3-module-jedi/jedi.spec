%define _unpackaged_files_terminate_build 1

%define pypi_name jedi
%define mod_name %pypi_name

%def_enable check

Name: python3-module-%pypi_name
Version: 0.19.1
Release: alt2
Summary: An autocompletion tool for Python that can be used for text editors
License: MIT
Group: Development/Python
Url: https://pypi.org/project/jedi/
Vcs: https://github.com/davidhalter/jedi
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: modules.tar
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_enabled check
%pyproject_builddeps_metadata_extra testing
# sqlite3 is subpackaged but required by test_sqlite3_conversion
BuildRequires: python3-modules-sqlite3
%endif

%description
Jedi is a static analysis tool for Python that is typically used in IDEs/editors
plugins. Jedi has a focus on autocompletion and goto functionality. Other
features include refactoring, code search and finding references.

Jedi has a simple API to work with. There is a reference implementation as a
VIM-Plugin. Autocompletion in your REPL is also possible, IPython uses it
natively and for the CPython REPL you can install it. Jedi is well tested and
bugs should be rare.

%prep
%setup -a2
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 28 2024 Stanislav Levin <slev@altlinux.org> 0.19.1-alt2
- Fixed FTBFS (Pytest 8.2.0).

* Thu Feb 08 2024 Anton Zhukharev <ancieg@altlinux.org> 0.19.1-alt1
- Updated to 0.19.1.

* Wed Jun 21 2023 Fr. Br. George <george@altlinux.org> 0.18.2-alt2
- Enable tests

* Fri Mar 24 2023 Fr. Br. George <george@altlinux.org> 0.18.2-alt1
- Autobuild version bump to 0.18.2

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.18.1-alt1
- Autobuild version bump to 0.18.1

* Mon Feb 01 2021 Fr. Br. George <george@altlinux.ru> 0.18.0-alt1
- Autobuild version bump to 0.18.0

* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.1-alt1.1
- Set versioned Python2 interpreter in shebang.

* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 0.12.1-alt1
- Autobuild version bump to 0.12.1

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1.git20150623.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150623.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150623.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150623
- Version 0.9.0

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.final0.git20150102
- Initial build for Sisyphus

