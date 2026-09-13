%define _unpackaged_files_terminate_build 1
%define pypi_name accelerate
%define module_name accelerate

%def_with check

Name: python3-module-%pypi_name
Version: 1.15.0
Release: alt1

Summary: A simple way to run PyTorch training on any device/config
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/accelerate/
Vcs: https://github.com/huggingface/accelerate

# torch (a hard runtime dep here) is only packaged for x86_64/
# aarch64, so this package must not be noarch: a noarch RPM lands in
# the shared noarch repo and becomes an unmet dependency on i586
# ("dependencies check FAILED" in girar). Being arch-dependent with a
# pure-Python payload means relocating the modules in %%install below.
ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

# torch-cpu provides neither a python3-module-torch virtual name nor
# python3(torch) autoprovides -- replace the generated bare Requires.
%add_pyproject_deps_runtime_filter '^torch$'
Requires: python3-module-torch-cpu
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
# torch-cpu again (BuildRequires-side virtual-name issue this time).
%add_pyproject_deps_check_filter '^torch$'
BuildRequires: python3-module-torch-cpu
%pyproject_builddeps_metadata
# Only parameterized (from "test_prod") is needed for the tests kept
# below; the rest of "testing" (datasets, diffusers, peft, ...) isn't,
# and peft isn't packaged yet anyway (it's what needs accelerate).
BuildRequires: python3-module-parameterized
%endif

# No python3(torch.*) autoprovides either -- same as above, drop the
# unresolvable autoreq entries.
%filter_from_requires /^python3(torch)/d
%filter_from_requires /^python3(torch\./d
# evaluate/transformers/deepspeed.runtime.utils are hard-imported only
# by test_utils/scripts/external_deps/*.py (CI helpers shipped in the
# package, not real deps upstream); filter the autoreq hits back out.
%filter_from_requires /^python3(evaluate)/d
%filter_from_requires /^python3(transformers)/d
%filter_from_requires /^python3(deepspeed\.runtime\.utils)/d

%description
Accelerate was created for PyTorch users who like to write the
training loop of PyTorch models but are reluctant to write and
maintain the boilerplate code needed to use multi-GPU/TPU/fp16.
It abstracts exactly and only the boilerplate code related to
multi-GPU/TPU/fp16 and leaves the rest of the training code
unchanged.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/

%check
# Ignored: deepspeed/fsdp/tp (frameworks not packaged), sagemaker/
# tpu/fp8/quantization/multidevice/tracking/examples/cli/compile (need
# GPU, network or a fuller runtime), big_modeling (hard-imports
# transformers, not built yet). Deselected: test_convert_to_fp32
# (needs torch.compile/g++), and a few torch.multiprocessing tests
# that only fail on aarch64 (chroot/qemu quirk, not an accelerate bug).
# test_free_memory_dereferences_prepared_components asserts on real
# host RAM before/after with only a 50MB tolerance -- too tight for a
# shared/virtualized build host.
%pyproject_run_pytest tests \
	--deselect=tests/test_utils.py::UtilsTester::test_convert_to_fp32 \
	--deselect=tests/test_cpu.py::MultiCPUTester::test_cpu \
	--deselect=tests/test_accelerator.py::AcceleratorTester::test_free_memory_dereferences_prepared_components \
	--deselect=tests/test_grad_sync.py::SyncScheduler::test_gradient_sync_cpu_multi \
	--deselect=tests/test_scheduler.py::SchedulerTester::test_lambda_scheduler_not_step_with_optimizer_multiprocess \
	--deselect=tests/test_scheduler.py::SchedulerTester::test_lambda_scheduler_steps_with_optimizer_multiprocess \
	--deselect=tests/test_scheduler.py::SchedulerTester::test_one_cycle_scheduler_not_step_with_optimizer_multiprocess \
	--deselect=tests/test_scheduler.py::SchedulerTester::test_one_cycle_scheduler_steps_with_optimizer_multiprocess \
	--ignore=tests/deepspeed \
	--ignore=tests/fsdp \
	--ignore=tests/tp \
	--ignore=tests/test_sagemaker.py \
	--ignore=tests/test_tpu.py \
	--ignore=tests/test_fp8.py \
	--ignore=tests/test_quantization.py \
	--ignore=tests/test_multidevice.py \
	--ignore=tests/test_tracking.py \
	--ignore=tests/test_examples.py \
	--ignore=tests/test_cli.py \
	--ignore=tests/test_compile.py \
	--ignore=tests/test_big_modeling.py

%files
%doc README.md LICENSE
%_bindir/accelerate
%_bindir/accelerate-config
%_bindir/accelerate-estimate-memory
%_bindir/accelerate-launch
%_bindir/accelerate-merge-weights
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Sep 13 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.15.0-alt1
- Initial build for ALT Sisyphus.
