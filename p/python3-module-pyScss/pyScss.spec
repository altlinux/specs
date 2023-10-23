%define _unpackaged_files_terminate_build 1

%define pypi_name pyScss
%define norm_name pyscss
%define mod_name %norm_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt4
Summary: pyScss is a compiler for the Sass language
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pyScss
Vcs: https://github.com/Kronuz/pyScss
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: %name-%version-alt.patch
Patch2: drop-distutils.patch
%pyproject_runtimedeps_metadata
Requires: python3-module-pillow
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libpcre-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pillow
BuildRequires: python3-module-pytest
%endif

%description
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

%prep
%setup
%patch1 -p1
%patch2 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

# fix shebangs
grep -sm1 -rl \
    -e '^#!/usr/bin/env python.*$' | \
xargs sed -s -e '1 s/^#!\/usr\/bin\/env python.*$/#!\/usr\/bin\/python3/'

%build
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install
install -p -m644 scss/grammar/*.g \
	%buildroot%python3_sitelibdir/scss/grammar/

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%_bindir/less2scss.py3
%_bindir/pyscss.py3
%dir %python3_sitelibdir/scss
%python3_sitelibdir/scss/*.py
%python3_sitelibdir/scss/__pycache__/
%dir %python3_sitelibdir/scss/grammar
%python3_sitelibdir/scss/grammar/*.py
%python3_sitelibdir/scss/grammar/*.g
%python3_sitelibdir/scss/grammar/_scanner.*.so
%python3_sitelibdir/scss/grammar/__pycache__/
%python3_sitelibdir/scss/extension/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Mon Oct 23 2023 Anton Vyatkin <toni@altlinux.org> 1.4.0-alt4
- NMU: Dropped dependency on distutils.

* Tue Jul 18 2023 Stanislav Levin <slev@altlinux.org> 1.4.0-alt3
- Modernized packaging.
- Fixed FTBFS (pytest 7.4.0).

* Sat Feb 04 2023 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt2
- Fixed build with python3.11.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Fri Dec 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.7-alt3
- Fixed build with python3.10.

* Wed Aug 05 2020 Stanislav Levin <slev@altlinux.org> 1.3.7-alt2
- Fixed FTBFS(new pytest 6.0.1).

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1.3.7-alt1
- 1.3.5 -> 1.3.7.
- Dropped Python2 build.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt3.qa1
- NMU: applied repocop patch

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 1.3.5-alt3
- Fix build

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt2
- Updated build and runtime dependencies.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1
- Updated to upstream release version 1.3.5.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.4-alt1.git20150122.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.4-alt1.git20150122.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150122
- Initial build for Sisyphus

