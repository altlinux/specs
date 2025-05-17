%define _unpackaged_files_terminate_build 1
%define pypi_name wheel

%def_with check

Name: python3-module-%pypi_name
Version: 0.45.1
Release: alt4
Summary: A built-package format for Python3
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/wheel/
VCS: https://github.com/pypa/wheel.git

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: debundler.py.in
Patch0: %name-%version-alt.patch
# manage deps with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
%pyproject_runtimedeps -- vendored
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps -- vendored
%endif

%description
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%prep
%setup
%autopatch -p1
VENDORED_PATH='src/wheel/vendored'
%pyproject_deps_resync vendored pip_reqfile "$VENDORED_PATH/vendor.txt"
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE2" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"wheel.vendored"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
# https://github.com/pypa/wheel/issues/658
%pyproject_run_pytest -ra \
    --deselect='tests/test_bdist_wheel.py::test_licenses_default' \
    --deselect='tests/test_bdist_wheel.py::test_licenses_deprecated' \
    --deselect='tests/test_bdist_wheel.py::test_licenses_override' \


%files
%doc *.txt
%_bindir/wheel
%python3_sitelibdir/wheel/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 15 2025 Stanislav Levin <slev@altlinux.org> 0.45.1-alt4
- debundled vendored dependencies
- stopped shipping built wheel as a whl

* Wed May 14 2025 Stanislav Levin <slev@altlinux.org> 0.45.1-alt3
- fixed FTBFS (setuptools 77.0.0).

* Mon May 05 2025 Stanislav Levin <slev@altlinux.org> 0.45.1-alt2
- fixed FTBFS (setuptools 75.8.1).

* Mon Nov 25 2024 Stanislav Levin <slev@altlinux.org> 0.45.1-alt1
- 0.45.0 -> 0.45.1.

* Mon Nov 11 2024 Stanislav Levin <slev@altlinux.org> 0.45.0-alt1
- 0.44.0 -> 0.45.0.

* Mon Aug 19 2024 Stanislav Levin <slev@altlinux.org> 0.44.0-alt1
- 0.43.0 -> 0.44.0.

* Tue Mar 12 2024 Stanislav Levin <slev@altlinux.org> 0.43.0-alt1
- 0.42.0 -> 0.43.0.

* Thu Dec 07 2023 Stanislav Levin <slev@altlinux.org> 0.42.0-alt1
- 0.41.3 -> 0.42.0.

* Thu Nov 02 2023 Stanislav Levin <slev@altlinux.org> 0.41.3-alt1
- 0.41.2 -> 0.41.3.

* Tue Sep 26 2023 Stanislav Levin <slev@altlinux.org> 0.41.2-alt1
- 0.41.1 -> 0.41.2.

* Mon Aug 07 2023 Stanislav Levin <slev@altlinux.org> 0.41.1-alt1
- 0.41.0 -> 0.41.1.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 0.41.0-alt1
- 0.40.0 -> 0.41.0.

* Thu Apr 20 2023 Stanislav Levin <slev@altlinux.org> 0.40.0-alt1
- 0.38.4 -> 0.40.0.

* Fri Nov 11 2022 Stanislav Levin <slev@altlinux.org> 0.38.4-alt1
- 0.37.1 -> 0.38.4.

* Fri Aug 12 2022 Stanislav Levin <slev@altlinux.org> 0.37.1-alt2
- Modernized packaging.

* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 0.37.1-alt1
- 0.37.0 -> 0.37.1.

* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 0.37.0-alt1
- 0.36.2 -> 0.37.0.

* Fri Apr 23 2021 Stanislav Levin <slev@altlinux.org> 0.36.2-alt1
- 0.34.2 -> 0.36.2.
- Enabled testing.
- Built wheel package(for virtualenv).

* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 0.34.2-alt1
- 0.34.2

