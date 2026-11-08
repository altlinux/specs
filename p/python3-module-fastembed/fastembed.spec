Name: python3-module-fastembed
Version: 0.9.1
Release: alt1

Summary: Python library built for embedding generation
License: Apache-2.0
Group: Development/Python

URL: https://pypi.org/project/fastembed
VCS: https://github.com/qdrant/fastembed

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup test

%build
%pyproject_build

%install
%pyproject_install

%check
# The rest of the suite downloads embedding models from HuggingFace,
# which is impossible on the build farm.
%pyproject_run_pytest -o=addopts= \
    tests/test_image_transform.py \
    tests/test_model_management.py \
    tests/test_parallel_processor.py \
    tests/test_text_onnx_embeddings.py::test_quantized_model_reports_onnxruntime_requirement \
    tests/test_text_onnx_embeddings.py::test_post_processing_keeps_model_dtype \
    tests/test_text_onnx_embeddings.py::test_get_embedding_size \
    tests/test_custom_models.py::test_mock_add_custom_models \
    tests/test_custom_models.py::test_custom_text_model_lookup_is_case_insensitive \
    tests/test_custom_models.py::test_custom_cross_encoder_lookup_is_case_insensitive \
    tests/test_custom_models.py::test_do_not_add_existing_model \
    tests/test_custom_models.py::test_do_not_add_existing_cross_encoder

%files
%python3_sitelibdir/fastembed
%python3_sitelibdir/fastembed-%version.dist-info

%changelog
* Sat Nov 07 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.1-alt1
- 0.9.1 released
