%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define pypi_name ty
%define mod_name ty

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: %pypi_name
Version: 0.0.95
Release: alt1

Summary: An extremely fast Python type checker and language server, written in Rust
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ty/
Vcs: https://github.com/astral-sh/ty

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-%version-ruff.tar
Source3: cargo-config.toml
Source4: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: libjemalloc-devel
BuildRequires: libzstd-devel

%description
%summary.

%package -n python3-module-%pypi_name
Summary: An extremely fast Python type checker and language server, written in Rust (Python package)
Group: Development/Python3
BuildArch: noarch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
Requires: %pypi_name = %EVR

%description -n python3-module-%pypi_name
%summary.

%prep
%setup -a1 -a2
%autopatch -p1
[ -d .cargo ] || mkdir .cargo
cat %SOURCE3 >> .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%ifarch %ix86
export CARGO_PROFILE_RELEASE_LTO=false
export CARGO_PROFILE_RELEASE_OPT_LEVEL=0
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
# i586 needs this flag to avoid the following building error:
#    - undefined reference to '__stack_chk_fail_local'
export CFLAGS="$CFLAGS -fno-stack-protector"
%else
export CARGO_PROFILE_RELEASE_LTO=thin
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
%endif
%ifarch aarch64
# aarch64 needs this flag to avoid the following building errors:
#    - undefined reference to `__aarch64_swp1_acq'
#    - undefined reference to `__aarch64_cas1_acq_rel'
export CFLAGS="$CFLAGS -mno-outline-atomics"
%endif
export CARGO_PROFILE_RELEASE_DEBUG=true
export CARGO_PROFILE_RELEASE_STRIP=none
export RUSTFLAGS="-Clink-args=-ljemalloc -Clink-args=-lzstd"
export MATURIN_STRIP=false
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir

%buildroot%_bindir/ty generate-shell-completion bash > %buildroot%bash_completionsdir/ty
%buildroot%_bindir/ty generate-shell-completion fish > %buildroot%fish_completionsdir/ty.fish
%buildroot%_bindir/ty generate-shell-completion zsh > %buildroot%zsh_completionsdir/_ty

# move python-module to noarch-directory
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir_noarch
mv %buildroot%python3_sitelibdir/* %buildroot%python3_sitelibdir_noarch/
%endif

%files
%_bindir/ty
%bash_completionsdir/ty
%fish_completionsdir/ty.fish
%zsh_completionsdir/_ty

%files -n python3-module-%pypi_name
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.95-alt1
- Updated to 0.0.95.
- Separated from ruff source package.
