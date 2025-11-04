%define _unpackaged_files_terminate_build 1
%define pypi_name voyageai

Name: python3-module-%pypi_name
Version: 0.3.2
Release: alt1

Summary: Voyage AI Official Python Library
License: MIT
Group: Development/Python3

Url: https://github.com/voyage-ai/voyageai-python
Vcs: https://github.com/voyage-ai/voyageai-python
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry.core)

BuildArch: noarch

%description
Embedding models are neural net models (e.g., transformers) that convert
unstructured and complex data, such as documents, images, audios, videos, or
tabular data, into dense numerical vectors (i.e. embeddings) that capture their
semantic meanings. These vectors serve as representations/indices for
datapoints and are essential building blocks for semantic search and
retrieval-augmented generation (RAG), which is the predominant approach for
domain-specific or company-specific chatbots and other AI applications.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info

%changelog
* Mon Apr 14 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.2-alt1
- Initial build
