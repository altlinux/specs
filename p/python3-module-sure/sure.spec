%define _unpackaged_files_terminate_build 1
%define modname sure

%def_with check

Name: python3-module-%modname
Version: 2.0.1
Release: alt1
Summary: Utility belt for automated testing in python for python
License: GPLv3+
Group: Development/Python3
Url: https://pypi.org/project/sure/
Vcs: https://github.com/gabrielfalcao/sure
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# nose is deprecated and was removed from sisyphus
%add_pyproject_deps_check_filter rednose
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
An idiomatic testing library for python with powerful and flexible assertions.
Sure's developer experience is inspired and modeled after RSpec Expectations and
should.js.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile development.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -o=addopts=''

%files
%_bindir/%modname
%doc README.rst
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version.dist-info/

%changelog
* Fri May 17 2024 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 2.0.0 -> 2.0.1.

* Sat Jan 27 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1.1
- NMU: moved on modern pyproject macros.

* Sat Mar 05 2022 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.4.11 -> 2.0.0.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.4.11-alt1
- 1.2.12 -> 1.4.11.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.12-alt2.git20150625.2
- Rebuild with python-module-six

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.12-alt2.git20150625.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.12-alt2.git20150625.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt2.git20150625
- Fixed for new mock

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt1.git20150625
- Version 1.2.12

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8-alt1.git20141223
- Version 1.2.8
- Added module for Python 3

* Sat Feb 09 2013 Ivan A. Melnikov <iv@altlinux.org> 1.1.7-alt1
- New version.

* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus.

