%define _unpackaged_files_terminate_build 1
%define pypi_name invoke

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.3
Release: alt1
Summary: Pythonic task execution
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/invoke/
Vcs: https://github.com/pyinvoke/invoke
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
%pyproject_runtimedeps -- vendored
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
%add_pyproject_deps_check_filter alabaster types-
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%pyproject_builddeps -- vendored
%endif

%description
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

%prep
%setup
%autopatch -p1

# gen vendored list for upstream
set -o pipefail
%__python3 - <<-'EOF' | sort -u > _vendor.txt
import pkgutil
for mod in pkgutil.iter_modules(["invoke/vendor"]):
    if not mod.name.startswith("_") and mod.name != "fluidity":
        print(mod.name)
EOF

%pyproject_deps_resync vendored pip_reqfile _vendor.txt
# drop everything except fluidity (not packaged (unmaintained))
find invoke/vendor/ \
    -mindepth 1 -maxdepth 1 \
    \( ! \( -name '__init__.py' -type f \) -a ! \( -name 'fluidity' -type d \) \) \
    -exec rm -rfv '{}' +

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- inv test

%files
%doc README.*
%_bindir/inv
%_bindir/invoke
%python3_sitelibdir/invoke/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jun 15 2023 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- 2.1.2 -> 2.1.3.

* Tue May 16 2023 Stanislav Levin <slev@altlinux.org> 2.1.2-alt1
- 2.1.1 -> 2.1.2.

* Fri May 05 2023 Stanislav Levin <slev@altlinux.org> 2.1.1-alt2
- Enabled testing.

* Wed May 03 2023 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 1.7.3 -> 2.1.1.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 1.7.3-alt1
- 1.6.0 -> 1.7.3.

* Mon Jul 19 2021 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- Restored back runtime dep on lexicon.

* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 0.21.0 -> 1.4.1.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.21.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.0-alt1
- Updated to upstream version 0.21.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt2.git20150730.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.10.1-alt2.git20150730
- cleanup buildreq

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20150730
- Version 0.10.1

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20141113
- Initial build for Sisyphus

