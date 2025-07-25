%define _unpackaged_files_terminate_build 1
%define pypi_name crosshair-tool
%define import_name crosshair

%def_with check
%def_with relaxed_check

Name: python3-module-%pypi_name
Version: 0.0.94
Release: alt3

Summary: An analysis tool for Python that blurs the line between testing and type systems
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/crosshair-tool/
Vcs: https://github.com/pschanely/CrossHair

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter autodocsumm
%add_pyproject_deps_check_filter rst2pdf
%pyproject_builddeps_metadata_extra dev
BuildRequires: python3-module-mypy
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONHASHSEED=0
# Disable the test below is required to avoid dead lock.
%pyproject_run_pytest -vra -n %_smp_build_ncpus \
    --deselect 'crosshair/libimpl/datetimelib_ch_test.py::test_builtin[check_timedelta_new]' \
%if_with relaxed_check
    ||:
%endif
    %nil

%files
%doc README.md
%_bindir/crosshair
%_bindir/mypycrosshair
%python3_sitelibdir/%import_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/_crosshair_tracers.*.so

%changelog
* Thu Jul 24 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.94-alt3
- Relaxed tests because they are very flaky.

* Thu Jul 17 2025 Ilya Sorochan <k0tran@altlinux.org> 0.0.94-alt2
- Make %check tests parallel.

* Wed Jul 16 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.94-alt1
- Updated to 0.0.94.

* Wed Jul 02 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.93-alt1
- Packaged for ALT Sisyphus.
