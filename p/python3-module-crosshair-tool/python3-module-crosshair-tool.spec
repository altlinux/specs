%define _unpackaged_files_terminate_build 1
%define pypi_name crosshair-tool
%define mod_name crosshair

# test only on x86_64 because tests are very flaky and unstable
%ifarch x86_64
%def_with check
%else
%def_without check
%endif

Name: python3-module-%pypi_name
Version: 0.0.113
Release: alt1

Summary: An analysis tool for Python that blurs the line between testing and type systems
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/crosshair-tool/
Vcs: https://github.com/pschanely/CrossHair

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_with_check_filter autodocsumm
%pyproject_configure_with_check_filter rst2pdf
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0
%if_with check
BuildRequires: python3-module-mypy
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install
# Do not install weird 'doc' module
rm -rv %buildroot%python3_sitelibdir/doc

%check
export PYTHONHASHSEED=0
# Disable first 2 tests below is required to avoid dead lock.
# Flaky symbolic Counter view realization in 0.0.113 (2 last tests).
%pyproject_run_pytest -vra -n %_smp_build_ncpus \
    --deselect 'crosshair/libimpl/datetimelib_ch_test.py::test_builtin[check_timedelta_new]' \
    --deselect 'crosshair/libimpl/datetimelib_test.py::test_leap_year' \
    --deselect 'crosshair/fuzz_core_test.py::test_op[collections.Counter_items_method]' \
    --deselect 'crosshair/fuzz_core_test.py::test_op[collections.Counter_keys_method]'

%files
%_bindir/crosshair
%_bindir/mypycrosshair
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/_crosshair_tracers.*.so

%changelog
* Sat Nov 14 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.113-alt1
- Updated to 0.0.113.

* Wed Aug 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.110-alt1
- Updated to 0.0.110.

* Tue Jun 16 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.107-alt1
- Updated to 0.0.107.

* Tue Feb 24 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.102-alt1
- Updated to 0.0.102.

* Thu Jul 24 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.94-alt3
- Relaxed tests because they are very flaky.

* Thu Jul 17 2025 Ilya Sorochan <k0tran@altlinux.org> 0.0.94-alt2
- Make %check tests parallel.

* Wed Jul 16 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.94-alt1
- Updated to 0.0.94.

* Wed Jul 02 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.93-alt1
- Packaged for ALT Sisyphus.
