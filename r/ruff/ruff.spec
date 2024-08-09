%define _unpackaged_files_terminate_build 1
%define pypi_name ruff

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: %pypi_name
Version: 0.5.7
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

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libjemalloc-devel

%description
%summary.

%package -n python3-module-%pypi_name
Summary: An extremely fast Python linter, written in Rust (Python package)
Group: Development/Python3
BuildArch: noarch
Requires: %pypi_name = %EVR

%description -n python3-module-%pypi_name
%summary.

%prep
%setup -a1
%__cat %SOURCE2 >> .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

# do not ship dependencies lists
%__rm -rv docs/requirements*.txt docs/.gitignore docs/.overrides

%build
%ifarch aarch64
# aarch64 needs this flag to avoid the following building errors:
#    - undefined reference to `__aarch64_swp1_acq'
#    - undefined reference to `__aarch64_cas1_acq_rel'
export CFLAGS="$CFLAGS -mno-outline-atomics"
%endif
%pyproject_build

%install
%pyproject_install

%__chmod 755 %buildroot%_bindir/%pypi_name

%__mkdir_p %buildroot%bash_completionsdir
%__mkdir_p %buildroot%fish_completionsdir
%__mkdir_p %buildroot%zsh_completionsdir

%buildroot%_bindir/%pypi_name generate-shell-completion bash \
    > %buildroot%bash_completionsdir/%pypi_name
%buildroot%_bindir/%pypi_name generate-shell-completion fish \
    > %buildroot%fish_completionsdir/%pypi_name.fish
%buildroot%_bindir/%pypi_name generate-shell-completion zsh \
    > %buildroot%zsh_completionsdir/_%pypi_name

# move python-module to noarch-directory
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
%__mkdir_p %buildroot%python3_sitelibdir_noarch
%__mv %buildroot%python3_sitelibdir/* %buildroot%python3_sitelibdir_noarch/
%endif

%files
%doc LICENSE README.md BREAKING_CHANGES.md docs
%_bindir/%pypi_name
%bash_completionsdir/%pypi_name
%fish_completionsdir/%pypi_name.fish
%zsh_completionsdir/_%pypi_name

%files -n python3-module-%pypi_name
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
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

