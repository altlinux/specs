%define _unpackaged_files_terminate_build 1
%define pypi_name typer
%define module_name %pypi_name
%define slim_pypi_name typer-slim
%define slim_module_name typer_slim
%def_with check

Name: python3-module-%pypi_name
Version: 0.26.7
Release: alt1

Summary: Typer, build great CLIs. Easy to code. Based on Python type hints
License: MIT
Group: Development/Python3
Url: https://typer.tiangolo.com/
Vcs: https://github.com/tiangolo/typer
BuildArch: noarch
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: clean_coverage.py
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
BuildRequires: python3-module-wheel
%pyproject_builddeps_build
%if_with check
BuildRequires: /proc
%pyproject_builddeps_check
%pyproject_builddeps_metadata
%endif

%description
Typer is a library for building CLI applications that users will love
using and developers will love creating. Based on Python 3.6+ type hints.

The key features are:
* Intuitive to write: Great editor support. Completion everywhere. Less
  time debugging. Designed to be easy to use and learn. Less time reading
  docs.
* Easy to use: It's easy to use for the final users. Automatic help, and
  automatic completion for all shells.
* Short: Minimize code duplication. Multiple features from each parameter
  declaration. Fewer bugs.
* Start simple: The simplest example adds only 2 lines of code to your app:
  1 import, 1 function call.
* Grow large: Grow in complexity as much as you want, create arbitrarily
  complex trees of commands and groups of subcommands, with options and
  arguments.

%package slim
Summary: A slimmed-down version of Typer
Group: Development/Python3
Requires: %name = %EVR

%description slim
There used to be a slimmed-down version of Typer called typer-slim,
which didn't include the dependencies rich and shellingham, nor the
typer command.

However, since version 0.22.0, it has been stopped supporting, and
typer-slim now simply installs (all of) Typer.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

%build
for tiangolo_build_package in %slim_pypi_name %pypi_name; do
	export TIANGOLO_BUILD_PACKAGE="$tiangolo_build_package"
	%pyproject_build
done

%install
%pyproject_install
pushd dist/
%__python3 -m wheel unpack %slim_module_name-%version-py3-none-any.whl
%__cp -a %slim_module_name-%version/%{pyproject_distinfo %slim_pypi_name} \
	%buildroot%python3_sitelibdir
popd
%__mkdir_p %buildroot%_docdir/%name-%version
%__ln_s %name-%version %buildroot%_docdir/%name-slim-%version
# Avoid conflict with Erlang.
%__mv %buildroot%_bindir/{%pypi_name,%pypi_name.py3}

%check
# Clean of the using coverage module, because we don't needs to it.
%SOURCE2 tests/
# Increase terminal line size, because some tests (test_not_exists from
# test_tutorial002.py and test_tutorial002_an.py) don't pass at narrow
# terminals.
export COLUMNS=135
# Set TERMINAL_WIDTH to a large value to prevent Rich from cropping error
# messages in panels, which causes test_path_convert_failures assertions to
# fail. Upstream CI also uses this approach.
export TERMINAL_WIDTH=3000
# Add the build directory to PYTHONPATH so that subprocess-based tests can
# import the tests package (e.g. test_binary_stderr runs __file__ via
# subprocess). See upstream PR #1827.
export PYTHONPATH="${PWD}${PYTHONPATH:+:$PYTHONPATH}"
# Set TERM to "xterm-256color" because some tests rely on decorated output from
# Python's Rich module. When "TERM=dumb", the Rich will disable any decorations
# and output plain text.
export TERM="xterm-256color"
## test_show_completion and test_install_completion
# Deselect these tests because of typer doesn't support SH, but this shell is
# run in hasher.
%pyproject_run_pytest -nauto \
    --deselect="tests/test_completion/test_completion.py::test_show_completion" \
    --deselect="tests/test_completion/test_completion.py::test_install_completion"

%files
%_bindir/%pypi_name.py3
%doc README.md LICENSE docs
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files slim
%_docdir/%name-slim-%version
%python3_sitelibdir/%{pyproject_distinfo %slim_pypi_name}

%changelog
* Mon Jun 08 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.26.7-alt1
- Updated to 0.26.7.

* Tue Apr 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.25.0-alt1
- Updated to 0.25.0.

* Tue Feb 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.24.1-alt1
- Updated to 0.24.1.

* Sat Feb 21 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.24.0-alt2
- Renamed /usr/bin/typer to typer.py3 to avoid conflict with Erlang
  (Closes: 57946).

* Tue Feb 17 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.24.0-alt1
- Updated to 0.24.0.
- Dropped the provide for typer-slim in favor of creating a subpackage
  that includes the typer-slim metadata directory (Closes: 57831).

* Wed Feb 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.22.0-alt1
- Updated to 0.22.0.
- Added provide on typer-slim for backward compatibility.

* Thu Jan 15 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.21.1-alt1
- Updated to 0.21.1.

* Mon Dec 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.21.0-alt1
- Updated to 0.21.0.

* Mon Dec 22 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.20.1-alt1
- Updated to 0.20.1.

* Wed Dec 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.20.0-alt1
- Updated to 0.20.0.

* Wed Sep 24 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.19.2-alt1
- Updated to 0.19.2.

* Tue Sep 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.19.1-alt1
- Updated to 0.19.1.

* Thu Sep 18 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.17.4-alt1
- Updated to 0.17.4.

* Wed Sep 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.17.3-alt1
- Updated to 0.17.3.

* Wed May 28 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.16.0-alt1
- Updated to 0.16.0.

* Tue May 20 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.15.4-alt1
- Updated to 0.15.4.

* Tue Apr 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.15.3-alt1
- Updated to 0.15.3.

* Fri Feb 28 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.15.2-alt1
- Updated to 0.15.2.

* Wed Jan 15 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.15.1-alt1
- Updated to 0.15.1.

* Sat Nov 23 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.13.1-alt1
- Updated to 0.13.1.

* Thu Aug 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.12.5-alt1
- Updated to 0.12.5.

* Mon Apr 15 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.12.3-alt1
- Updated to 0.12.3.

* Thu Mar 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.11.0-alt1
- Updated to 0.11.0.

* Sat Oct 21 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.0-alt2
- Fixed FTBFS: deselect some tests for bash completion.

* Thu Sep 14 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.0-alt1
- Initial build for ALT Sisyphus.
