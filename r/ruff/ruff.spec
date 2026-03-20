%define _unpackaged_files_terminate_build 1
%ifnarch i586
%define _stripped_files_terminate_build 1
%endif

%define ruff_pypi_name ruff
%define ruff_import_name ruff
%define ruff_version 0.15.7

%define ty_pypi_name ty
%define ty_import_name ty
%define ty_version 0.0.24

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: %ruff_pypi_name
Version: %ruff_version
Release: alt1

Summary: An extremely fast Python linter, written in Rust
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ruff/
Vcs: https://github.com/astral-sh/ruff

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
Source3: %pyproject_deps_config_name
Source4: ty.toml

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libjemalloc-devel
BuildRequires: libzstd-devel

%description
%summary.

%package -n python3-module-%ruff_pypi_name
Summary: An extremely fast Python linter, written in Rust (Python package)
Group: Development/Python3
BuildArch: noarch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
Requires: %ruff_pypi_name = %EVR

%description -n python3-module-%ruff_pypi_name
%summary.

%package -n %ty_pypi_name
Version: %ty_version
Summary: An extremely fast Python type checker and language server, written in Rust
Group: Development/Python3
Url: https://pypi.org/project/ty/
Vcs: https://github.com/astral-sh/ty

%description -n %ty_pypi_name
%summary.

%package -n python3-module-%ty_pypi_name
Version: %ty_version
Summary: An extremely fast Python type checker and language server, written in Rust (Python package)
Group: Development/Python3
Url: https://pypi.org/project/ty/
Vcs: https://github.com/astral-sh/ty
BuildArch: noarch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
Requires: %ty_pypi_name = %EVR

%description -n python3-module-%ty_pypi_name
%summary.

%prep
%setup -a1
install -v %SOURCE2 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

touch python/%ruff_import_name/py.typed

# do not ship dependencies lists
rm -rv docs/requirements*.txt docs/.gitignore docs/.overrides

%build
export CARGO_BUILD_JOBS=%__nprocs
%ifarch aarch64
# aarch64 needs this flag to avoid the following building errors:
#    - undefined reference to `__aarch64_swp1_acq'
#    - undefined reference to `__aarch64_cas1_acq_rel'
export CFLAGS="$CFLAGS -mno-outline-atomics"
%endif
%ifarch i586
# i586 needs this flag to avoid the following building error:
#    - undefined reference to '__stack_chk_fail_local'
export CFLAGS="$CFLAGS -fno-stack-protector"
# decrease parallel jobs to lower required memory allocation
# (this need to fit in 4GB limit for 32-bit machines)
export CARGO_BUILD_JOBS=1
%endif
%pyproject_build -o dist-%ruff_pypi_name

# build ty
install -v %SOURCE4 pyproject.toml
mv python/%ruff_import_name python/%ty_import_name
sed -i 's/ruff/ty/g' python/%ty_import_name/__main__.py
export TY_VERSION="%version"
%pyproject_build -o dist-%ty_pypi_name

%install
%pyproject_install dist-%ruff_pypi_name/$(cat dist-%ruff_pypi_name/.wheeltracker)
%pyproject_install dist-%ty_pypi_name/$(cat dist-%ty_pypi_name/.wheeltracker)

chmod 755 %buildroot%_bindir/ruff
chmod 755 %buildroot%_bindir/ty

mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir

%buildroot%_bindir/ruff generate-shell-completion bash \
    > %buildroot%bash_completionsdir/%ruff_pypi_name
%buildroot%_bindir/ruff generate-shell-completion fish \
    > %buildroot%fish_completionsdir/%ruff_pypi_name.fish
%buildroot%_bindir/ruff generate-shell-completion zsh \
    > %buildroot%zsh_completionsdir/_%ruff_pypi_name

%buildroot%_bindir/ty generate-shell-completion bash \
    > %buildroot%bash_completionsdir/%ty_pypi_name
%buildroot%_bindir/ty generate-shell-completion fish \
    > %buildroot%fish_completionsdir/%ty_pypi_name.fish
%buildroot%_bindir/ty generate-shell-completion zsh \
    > %buildroot%zsh_completionsdir/_%ty_pypi_name

# move python-module to noarch-directory
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir_noarch
mv %buildroot%python3_sitelibdir/* %buildroot%python3_sitelibdir_noarch/
%endif

%files
%_bindir/ruff
%bash_completionsdir/%ruff_pypi_name
%fish_completionsdir/%ruff_pypi_name.fish
%zsh_completionsdir/_%ruff_pypi_name

%files -n python3-module-%ruff_pypi_name
%python3_sitelibdir_noarch/%ruff_import_name/
%python3_sitelibdir_noarch/%{pep427_name %ruff_pypi_name}-%ruff_version.dist-info/

%files -n %ty_pypi_name
%_bindir/ty
%bash_completionsdir/%ty_pypi_name
%fish_completionsdir/%ty_pypi_name.fish
%zsh_completionsdir/_%ty_pypi_name

%files -n python3-module-%ty_pypi_name
%python3_sitelibdir_noarch/%ty_import_name/
%python3_sitelibdir_noarch/%{pep427_name %ty_pypi_name}-%ty_version.dist-info/

%changelog
* Fri Mar 20 2026 Anton Zhukharev <ancieg@altlinux.org> 0.15.7-alt1
- Updated ruff to 0.15.7.
- Updated ty to 0.0.24.

* Fri Mar 13 2026 Anton Zhukharev <ancieg@altlinux.org> 0.15.6-alt1
- Updated ruff to 0.15.6.
- Updated ty to 0.0.22.

* Fri Mar 06 2026 Anton Zhukharev <ancieg@altlinux.org> 0.15.5-alt1
- Updated ruff to 0.15.5.
- Updated ty to 0.0.20.

* Fri Feb 27 2026 Anton Zhukharev <ancieg@altlinux.org> 0.15.4-alt1
- Updated ruff to 0.15.4.
- Updated ty to 0.0.19.

* Wed Feb 04 2026 Anton Zhukharev <ancieg@altlinux.org> 0.15.0-alt1
- Updated ruff to 0.15.0.
- Updated ty to 0.0.14.

* Tue Jan 20 2026 Anton Zhukharev <ancieg@altlinux.org> 0.14.13-alt1
- Updated ruff to 0.14.13.
- Updated ty to 0.0.12.

* Mon Dec 29 2025 Anton Zhukharev <ancieg@altlinux.org> 0.14.10-alt1
- Updated ruff to 0.14.10.
- Updated ty to 0.0.4.
- Shipped shell completions for ty.

* Fri Oct 03 2025 Anton Zhukharev <ancieg@altlinux.org> 0.13.3-alt1
- Updated ruff to 0.13.3.

* Fri Sep 26 2025 Anton Zhukharev <ancieg@altlinux.org> 0.13.2-alt1
- Updated ruff to 0.13.2.

* Fri Sep 19 2025 Anton Zhukharev <ancieg@altlinux.org> 0.13.1-alt1
- Updated ruff to 0.13.1.
- Updated ty to 0.0.1a21.

* Tue Aug 26 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.10-alt2
- Packaged ty (ruff and ty are in the same repo).

* Fri Aug 22 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.10-alt1
- Updated to 0.12.10.

* Fri Aug 15 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.9-alt1
- Updated to 0.12.9.

* Fri Jul 25 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.5-alt1
- Updated to 0.12.5.

* Fri Jul 18 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.4-alt1
- Updated to 0.12.4.

* Tue Jul 15 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.3-alt1
- Updated to 0.12.3.

* Fri Jul 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.2-alt1
- Updated to 0.12.2.

* Fri Jun 27 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.1-alt1
- Updated to 0.12.1.

* Wed Jun 18 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.0-alt1
- Updated to 0.12.0.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.12-alt1
- Updated to 0.11.12.

* Fri May 23 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.11-alt1
- Updated to 0.11.11.

* Mon May 05 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.8-alt1
- Updated to 0.11.8.

* Fri Apr 25 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.7-alt1
- Updated to 0.11.7.

* Fri Apr 18 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.6-alt1
- Updated to 0.11.6.

* Fri Apr 11 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.5-alt1
- Updated to 0.11.5.

* Mon Apr 07 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.4-alt1
- Updated to 0.11.4.

* Thu Apr 03 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.3-alt1
- Updated to 0.11.3.

* Fri Mar 21 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.2-alt1
- Updated to 0.11.2.

* Fri Mar 21 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.1-alt1
- Updated to 0.11.1.

* Mon Mar 17 2025 Anton Zhukharev <ancieg@altlinux.org> 0.11.0-alt1
- Updated to 0.11.0.

* Fri Mar 14 2025 Anton Zhukharev <ancieg@altlinux.org> 0.10.0-alt1
- Updated to 0.10.0.

* Sun Mar 09 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.10-alt1
- Updated to 0.9.10.

* Fri Feb 28 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.9-alt1
- Updated to 0.9.9.

* Thu Feb 27 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.8-alt1
- Updated to 0.9.8.

* Fri Feb 21 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.7-alt1
- Updated to 0.9.7.

* Tue Feb 11 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.6-alt1
- Updated to 0.9.6.

* Fri Feb 07 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt1
- Updated to 0.9.5.

* Mon Feb 03 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.4-alt1
- Updated to 0.9.4.

* Fri Jan 10 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Thu Jan 09 2025 Anton Zhukharev <ancieg@altlinux.org> 0.8.6-alt1
- Updated to 0.8.6.

* Fri Dec 06 2024 Anton Zhukharev <ancieg@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Fri Nov 29 2024 Anton Zhukharev <ancieg@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Fri Nov 22 2024 Anton Zhukharev <ancieg@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Mon Nov 18 2024 Anton Zhukharev <ancieg@altlinux.org> 0.7.4-alt1
- Updated to 0.7.4.

* Fri Oct 18 2024 Anton Zhukharev <ancieg@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Thu Oct 10 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.9-alt1
- Updated to 0.6.9.

* Fri Sep 27 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.8-alt1
- Updated to 0.6.8.

* Mon Sep 23 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.7-alt1
- Updated to 0.6.7.

* Fri Sep 20 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.6-alt1
- Updated to 0.6.6.

* Mon Sep 16 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.5-alt1
- Updated to 0.6.5.

* Mon Sep 09 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.4-alt1
- Updated to 0.6.4.

* Mon Aug 26 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.2-alt1
- Updated to 0.6.2.

* Fri Aug 09 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.7-alt1
- Updated to 0.5.7.

* Mon Aug 05 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.6-alt1
- Updated to 0.5.6.

* Fri Jul 26 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.5-alt1
- Updated to 0.5.5.

* Thu Jul 25 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.4-alt1
- Updated to 0.5.4.

* Fri Jul 19 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Wed Jul 17 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Fri Jul 05 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Mon Jul 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Thu Jun 06 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.8-alt1
- Updated to 0.4.8.

* Sat Jun 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.7-alt1
- Updated to 0.4.7.

* Thu May 30 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.6-alt1
- Updated to 0.4.6.

* Thu May 23 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.5-alt1
- Updated to 0.4.5.

* Mon May 13 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.4-alt1
- Updated to 0.4.4.

* Fri Apr 26 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.2-alt1
- Updated to 0.4.2.

* Mon Apr 22 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Fri Apr 12 2024 Anton Zhukharev <ancieg@altlinux.org> 0.3.7-alt1
- Updated to 0.3.7.

* Tue Apr 02 2024 Anton Zhukharev <ancieg@altlinux.org> 0.3.5-alt1
- Updated to 0.3.5.

* Mon Mar 25 2024 Anton Zhukharev <ancieg@altlinux.org> 0.3.4-alt1
- Updated to 0.3.4.

* Fri Mar 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Sun Feb 18 2024 Anton Zhukharev <ancieg@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Tue Feb 06 2024 Anton Zhukharev <ancieg@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Tue Jan 09 2024 Anton Zhukharev <ancieg@altlinux.org> 0.1.11-alt1
- Updated to 0.1.11.

* Fri Dec 22 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.9-alt1
- Updated to 0.1.9.

* Mon Dec 18 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.8-alt1
- Updated to 0.1.8.

* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.7-alt1
- Updated to 0.1.7.

* Mon Nov 20 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.6-alt1
- Updated to 0.1.6.

* Thu Nov 09 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.5-alt1
- Updated to 0.1.5.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Wed Nov 01 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Fri Oct 20 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Tue Oct 17 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.0-alt1
- Updated to 0.1.0.

* Tue Oct 03 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.292-alt1
- Updated to 0.0.292.

* Mon Sep 25 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.291-alt1
- Updated to 0.0.291.

* Sat Sep 16 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.290-alt1
- Updated to 0.0.290.

* Wed Sep 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.289-alt1
- Updated to 0.0.289.

* Tue Sep 12 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.288-alt1
- Updated to 0.0.288.

* Sat Sep 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.287-alt1
- Updated to 0.0.287.

* Sat Aug 26 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.286-alt1
- Updated to 0.0.286.

* Sat Aug 26 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.285-alt3
- Renamed to "ruff".
- Fixed documetation packaing.

* Wed Aug 23 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.285-alt2
- Packaged documentation.
- Packaged shell completions for bash, fish and zsh.

* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.285-alt1
- Built for ALT Sisyphus.
