%define _unpackaged_files_terminate_build 1
%define pypi_name BTrees
%define oname %pypi_name

%define dynamic_mods %(echo `cat %SOURCE2 2>/dev/null || echo unknown`)

%def_with check

Name: python3-module-%oname
Version: 6.0
Release: alt1

Summary: Scalable persistent object containers
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/BTrees/
Vcs: https://github.com/zopefoundation/BTrees.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: dynamic_mods.list
%pyproject_runtimedeps_metadata
# dynamic names
%add_python3_req_skip %dynamic_mods
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
%py3_provides %dynamic_mods
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-persistent-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside ZODB's
"optimistic concurrency" paradigm, and include explicit resolution of
conflicts detected by that mechanism.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

# make sure we provide actual names
# these names are generated at runtime, see src/BTrees/__init__.py for details
%pyproject_run -- python - <<-'ENDRUN'
from pathlib import Path
import BTrees

Path("mods.actual.list").write_text(
    "\n".join(sorted([f'BTrees.{n}BTree' for n in BTrees._FAMILIES])) + "\n",
    encoding="utf-8",
)
ENDRUN

sort %SOURCE2 > mods.expected.list
diff -y mods.expected.list mods.actual.list || {
    echo 'Update expected list of mods: %SOURCE2' ;
    exit 1 ;
}

%install
%pyproject_install

# don't ship sources for C extensions
rm %buildroot%python3_sitelibdir/%pypi_name/*.{h,c}

%check
%pyproject_run -- zope-testrunner --test-path=src -vv

%files
%doc LICENSE.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/BTrees-%version.dist-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Fri May 31 2024 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.2 -> 6.0.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 5.2-alt1
- 5.0 -> 5.2.

* Mon Jul 31 2023 Stanislav Levin <slev@altlinux.org> 5.0-alt2
- Mapped PyPI name to distro's one.

* Wed Jun 07 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Fri Dec 24 2021 Grigory Ustinov <grenka@altlinux.org> 4.9.2-alt2
- Build without check for python3.10.

* Fri Jun 18 2021 Nikolai Kostrigin <nickel@altlinux.org> 4.9.2-alt1
- 4.7.2 -> 4.9.2

* Tue Aug 11 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.7.2-alt1
- 4.6.1 -> 4.7.2

* Mon Jan 13 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.6.1-alt1
- NMU: 4.4.1 -> 4.6.1
- Remove python2 module build
- Rearrange unittest execution
- Fix license

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.1-alt3
- Bootstrap for python3.7.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt2.S1
- (NMU) Rebuilt without bootstrap.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 09 2018 Stanislav Levin <slev@altlinux.org> 4.4.1-alt1.S1
- v4.4.0 -> v4.4.1

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.5-alt2.dev0.git20150602.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 4.1.5-alt2.dev0.git20150602.1
- NMU: Use buildreq for BR.

* Tue Jan 19 2016 Sergey Alembekov <rt@altlinux.ru> 4.1.5-alt2.dev0.git20150602
- remove ZODB cyrcular dependency

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.5-alt1.dev0.git20150602
- Version 4.1.5.dev0

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev0.git201411227
- Version 4.1.2.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.9-alt1.dev.git20141008
- Version 4.0.9dev

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Initial build for Sisyphus
