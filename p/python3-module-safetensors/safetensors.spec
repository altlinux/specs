%define _unpackaged_files_terminate_build 1
%define pypi_name safetensors
%define module_name safetensors
%define py_dir bindings/python

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: Simple, safe way to store and distribute tensors
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/safetensors/
Vcs: https://github.com/huggingface/safetensors

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: crates.tar
Source3: Cargo.lock

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: python3-dev
BuildRequires: python3-module-abi3audit
%pyproject_builddeps_build

%if_with check
# s3fs and setuptools-rust (only used by the "testing" extra) aren't
# packaged in Sisyphus. The torch/tensorflow/flax/paddle/mlx
# comparison tests are all skipped in %%check below (none of those
# frameworks are packaged in Sisyphus either), so torch is not pulled
# in here -- only numpy, needed by the tests that do run.
%add_pyproject_deps_check_filter '^(s3fs|setuptools-rust)$'
%pyproject_builddeps_metadata_extra testing
%pyproject_builddeps_metadata_extra numpy
%endif

# safetensors/{torch,tensorflow,flax,paddle,mlx}.py are optional
# per-backend integration modules: each unconditionally imports its
# framework, so the automatic Requires generator turns that into a
# hard python3(torch)/python3(tensorflow)/python3(jax)/python3(paddle)/
# python3(mlx.core) dependency -- none of which are packaged in
# Sisyphus under those names. Users who need a given backend install
# it themselves; the base package must not require it.
# Note: the generator appends a "< 0" path constraint to every line
# (see /usr/lib/rpm/python3.req.constraint.py), so the patterns below
# must not anchor on end-of-line.
%filter_from_requires /^python3(torch)/d
%filter_from_requires /^python3(tensorflow)/d
%filter_from_requires /^python3(jax)/d
%filter_from_requires /^python3(jax\.numpy)/d
%filter_from_requires /^python3(paddle)/d
%filter_from_requires /^python3(mlx\.core)/d

%description
Safetensors is a simple format for storing tensors safely (as
opposed to pickle), while still being fast. Tensors are stored as
flat byte buffers with JSON header metadata describing shapes,
dtypes, and offsets, so files can be loaded with zero-copy and
without arbitrary code execution.

%prep
%setup -a2
cp %SOURCE3 %py_dir/Cargo.lock

cd %py_dir
mkdir -p .cargo
cat > .cargo/config.toml <<-'EOF'
	[source.crates-io]
	replace-with = "vendored-sources"

	[source.vendored-sources]
	directory = "vendor"
	EOF
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
cd %py_dir
export CARGO_HOME=${PWD}/cargo
export CARGO_NET_OFFLINE=true
%python3_set_limited_api 3.10
%pyproject_build

%install
cd %py_dir
%pyproject_install

%check
cd %py_dir
# test_flax_comparison.py, test_tf_comparison.py,
# test_paddle_comparison.py, test_mlx_comparison.py need flax/jax,
# tensorflow, paddlepaddle, and mlx respectively; test_multithreaded.py,
# test_pread_backend.py, test_pt_comparison.py, test_pt_model.py,
# test_simple.py need torch -- none of these frameworks are packaged
# in Sisyphus, so all of them are skipped. Only test_handle.py and
# test_threadable.py (numpy-only) actually run.
%pyproject_run_pytest tests \
	--ignore=tests/test_flax_comparison.py \
	--ignore=tests/test_tf_comparison.py \
	--ignore=tests/test_paddle_comparison.py \
	--ignore=tests/test_mlx_comparison.py \
	--ignore=tests/test_multithreaded.py \
	--ignore=tests/test_pread_backend.py \
	--ignore=tests/test_pt_comparison.py \
	--ignore=tests/test_pt_model.py \
	--ignore=tests/test_simple.py

%files
%doc LICENSE
%doc %py_dir/README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Sep 12 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.8.0-alt1
- Initial build for ALT Sisyphus.
