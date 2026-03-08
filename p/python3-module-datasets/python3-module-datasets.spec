%define pypi_name datasets

Name: python3-module-%pypi_name
Version: 4.5.0
Release: alt1

Summary: HuggingFace community-driven open-source library of datasets

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/datasets
VCS: https://github.com/huggingface/datasets

BuildArchitectures: noarch

# Source-url: https://github.com/huggingface/datasets/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%add_python3_req_skip pyspark torchcodec.decoders

%description
HuggingFace Datasets is a lightweight library providing two main features:
one-line dataloaders for many public datasets and efficient data
pre-processing. It is designed to let the community easily add and share
new datasets.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%_bindir/datasets-cli
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Feb 25 2026 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt1
- initial build for ALT Sisyphus
