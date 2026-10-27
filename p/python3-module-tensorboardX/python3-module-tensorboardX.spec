%define pypi_name tensorboardX

%def_with check

Name:    python3-module-%pypi_name
Version: 2.6.5
Release: alt1

Summary: tensorboard for pytorch (and chainer, mxnet, numpy, ...)
License: MIT
Group:   Development/Python3
Url: 	 https://tensorboardx.readthedocs.io
Vcs:     https://github.com/lanpa/tensorboardX

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-setuptools_scm

%if_with check
# Upstream test dependencies are provided via the "dev" dependency group,
# not as a metadata extra; keep dependencies for enabled tests explicit.
BuildRequires: python3-module-torch-cpu
BuildRequires: python3-module-boto3
BuildRequires: python3-module-moto
BuildRequires: python3-module-soundfile
%endif

%pyproject_runtimedeps_metadata

# PyTorch test dependencies are available only on x86_64 and aarch64.
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

Source1: %pyproject_deps_config_name

%description
Write TensorBoard events with simple function call.

%prep
%setup

export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_metadata

# Moto 5 replaced service-specific mock decorators with mock_aws.
grep -q '^from moto import mock_s3$' tests/test_embedding.py
grep -q '^from moto import mock_s3$' tests/test_record_writer.py

sed -i 's/^from moto import mock_s3$/from moto import mock_aws as mock_s3/' \
    tests/test_embedding.py \
    tests/test_record_writer.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

# Move the pure-Python payload to platlib for the arch-specific RPM.
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
   %buildroot%python3_sitelibdir/
%endif

%check
# Skip TensorBoard/ONNX-dependent tests and upstream lint checks.
%pyproject_run_pytest \
    --ignore=tests/event_file_writer_test.py \
    --ignore=tests/record_writer_test.py \
    --ignore=tests/test_multiprocess_write.py \
    --ignore=tests/test_pytorch_graph.py \
    --ignore=tests/test_onnx_graph.py \
    --ignore=tests/test_writer.py \
    --ignore=tests/test_lint.py

%files
%doc *.md LICENSE HISTORY.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 26 2026 Nikita Shmatko <nash@altlinux.org> 2.6.5-alt1
- Initial build for Sisyphus.
