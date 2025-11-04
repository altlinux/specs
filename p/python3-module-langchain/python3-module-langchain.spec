%define _unpackaged_files_terminate_build 1
%define pypi_name langchain
%define libs cli community core langchain text-splitters standard-tests
%define partners anthropic deepseek exa groq huggingface ollama openai perplexity prompty qdrant voyageai xai
# Couldn't build `python3(torch)` for `nomic`
# Couldn't build `python3(chromadb)` for `chroma`
# Couldn't build `python3(fireworks.client)` for `fireworks`
# Couldn't build `python3(tokenizers)` for `mistralai`

Name: python3-module-%pypi_name
Version: 0.3.23
Release: alt1

Summary: Building applications with LLMs through composability
License: MIT
Group: Development/Python3

Url: https://github.com/langchain-ai/langchain
Vcs: https://github.com/langchain-ai/langchain
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pdm.backend)

%add_python3_req_skip __module_name__.vectorstores
%add_python3_req_skip __module_name__.chain
%add_python3_req_skip __module_name__.chat_models
%add_python3_req_skip __module_name__.document_loaders
%add_python3_req_skip __module_name__.embeddings
%add_python3_req_skip __module_name__.retrievers
%add_python3_req_skip __module_name__.toolkits
%add_python3_req_skip __module_name__.tools

BuildArch: noarch

%description
Large language models (LLMs) are emerging as a transformative technology,
enabling developers to build applications that they previously could not.
However, using these LLMs in isolation is often insufficient for creating a
truly powerful app - the real power comes when you can combine them with other
sources of computation or knowledge.

%package -n %name-cli
Summary: CLI for interacting with LangChain
Group: Development/Python3

%description -n %name-cli
This package implements the official CLI for LangChain. Right now, it is most
useful for getting started with LangChain Templates!

%package -n %name-community
Summary: Community contributed LangChain integrations
Group: Development/Python3

%description -n %name-community
LangChain Community contains third-party integrations that implement the base
interfaces defined in LangChain Core, making them ready-to-use in any LangChain
application.

%package -n %name-core
Summary: Building applications with LLMs through composability
Group: Development/Python3

%description -n %name-core
LangChain Core contains the base abstractions that power the rest of the
LangChain ecosystem.

These abstractions are designed to be as modular and simple as possible.
Examples of these abstractions include those for language models, document
loaders, embedding models, vectorstores, retrievers, and more.

The benefit of having these abstractions is that any provider can implement the
required interface and then easily be used in the rest of the LangChain
ecosystem.

%package -n %name-tests
Summary: Standard tests for LangChain implementations
Group: Development/Python3

%description -n %name-tests
This is a testing library for LangChain integrations. It contains the base
classes for a standard set of tests.

%package -n %name-text-splitters
Summary: LangChain text splitting utilities
Group: Development/Python3

%description -n %name-text-splitters
LangChain Text Splitters contains utilities for splitting into chunks a wide
variety of text documents.

%package -n %name-anthropic
Summary: An integration package connecting AnthropicMessages and LangChain
Group: Development/Python3

%description -n %name-anthropic
This package contains the LangChain integration for Anthropic's generative
models.

# Couldn't build `python3(chromadb)` for `chroma`
# %package -n %name-chroma
# Summary: An integration package connecting Chroma and LangChain
# Group: Development/Python3
#
# %description -n %name-chroma
# This package contains the LangChain integration with Chroma.

%package -n %name-deepseek
Summary: An integration package connecting DeepSeek and LangChain
Group: Development/Python3

%description -n %name-deepseek
This package contains the LangChain integration with the DeepSeek API

%package -n %name-exa
Summary: An integration package connecting Exa and LangChain
Group: Development/Python3

%description -n %name-exa
This package contains the LangChain integrations for Exa Cloud generative
models.

# Couldn't build `python3(fireworks.client)` for `fireworks`
# %package -n %name-fireworks
# Summary: An integration package connecting Fireworks and LangChain
# Group: Development/Python3
#
# %description -n %name-fireworks
# This is the partner package for tying Fireworks.ai and LangChain. Fireworks
# really strive to provide good support for LangChain use cases, so if you run
# into any issues please let us know.

%package -n %name-groq
Summary: An integration package connecting Groq and LangChain
Group: Development/Python3

%description -n %name-groq
At Groq, we've developed the world's first Language Processing Unit, or LPU.
The Groq LPU has a deterministic, single core streaming architecture that sets
the standard for GenAI inference speed with predictable and repeatable
performance for any given workload.

Beyond the architecture, our software is designed to empower developers like
you with the tools you need to create innovative, powerful AI applications.
With Groq as your engine, you can:

- Achieve uncompromised low latency and performance for real-time AI and HPC
inferences
- Know the exact performance and compute time for any given workload
- Take advantage of our cutting-edge technology to stay ahead of the
competition

%package -n %name-huggingface
Summary: An integration package connecting Hugging Face and LangChain
Group: Development/Python3

%description -n %name-huggingface
This package contains the LangChain integrations for huggingface related
classes.

# Couldn't build `python3(tokenizers)` for `mistralai`
# %package -n %name-mistralai
# Summary: An integration package connecting Mistral and LangChain
# Group: Development/Python3
#
# %description -n %name-mistralai
# This package contains the LangChain integrations for MistralAI through their
# mistralai SDK.

# Couldn't build `python3(torch)` for `nomic`
# %package -n %name-nomic
# Summary: An integration package connecting Nomic and LangChain
# Group: Development/Python3
#
# %description -n %name-nomic
# This package contains the LangChain integration with Nomic

%package -n %name-ollama
Summary: An integration package connecting Ollama and LangChain
Group: Development/Python3

%description -n %name-ollama
This package contains the LangChain integration with Ollama

%package -n %name-openai
Summary: An integration package connecting OpenAI and LangChain
Group: Development/Python3

%description -n %name-openai
This package contains the LangChain integrations for OpenAI through their
`openai` SDK.

%package -n %name-perplexity
Summary: An integration package connecting Perplexity and LangChain
Group: Development/Python3

%description -n %name-perplexity
This package contains the LangChain integration with Perplexity.

%package -n %name-prompty
Summary: An integration package connecting Prompty and LangChain
Group: Development/Python3

%description -n %name-prompty
This package contains the LangChain integration with Microsoft Prompty.

%package -n %name-qdrant
Summary: An integration package connecting Qdrant and LangChain
Group: Development/Python3

%description -n %name-qdrant
This package contains the LangChain integration with Qdrant.

%package -n %name-voyageai
Summary: An integration package connecting VoyageAI and LangChain
Group: Development/Python3

%description -n %name-voyageai
This package contains the LangChain integrations for VoyageAI through their
`voyageai` client package.

%package -n %name-xai
Summary: An integration package connecting xAI and LangChain
Group: Development/Python3

%description -n %name-xai
This package contains the LangChain integrations for xAI through their APIs.

%prep
%setup

%build
cd libs
for dir in %libs; do
  %pyproject_build $dir
done

cd partners
for dir in %partners; do
  %pyproject_build $dir
done

%install
cd libs
for dir in %libs; do
  cd $dir
  %pyproject_install
  cd ..
done

cd partners
for dir in %partners; do
  cd $dir
  %pyproject_install
  cd ..
done

%files
%_bindir/%pypi_name
%python3_sitelibdir_noarch/%{pypi_name}
%python3_sitelibdir_noarch/%{pypi_name}-*
%exclude %python3_sitelibdir_noarch/scripts
%exclude %python3_sitelibdir_noarch/%pypi_name/__pycache__
%doc libs/%{pypi_name}/README.md

%files -n %name-cli
%_bindir/%pypi_name-cli
%python3_sitelibdir_noarch/%{pypi_name}_cli
%python3_sitelibdir_noarch/%{pypi_name}_cli-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_cli/__pycache__
%doc libs/cli/README.md

%files -n %name-community
%python3_sitelibdir_noarch/%{pypi_name}_community
%python3_sitelibdir_noarch/%{pypi_name}_community-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_community/__pycache__
%doc libs/community/README.md

%files -n %name-core
%python3_sitelibdir_noarch/%{pypi_name}_core
%python3_sitelibdir_noarch/%{pypi_name}_core-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_core/__pycache__
%doc libs/core/README.md

%files -n %name-tests
%python3_sitelibdir_noarch/%{pypi_name}_tests
%python3_sitelibdir_noarch/%{pypi_name}_tests-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_tests/__pycache__
%doc libs/standard-tests/README.md

%files -n %name-text-splitters
%python3_sitelibdir_noarch/%{pypi_name}_text_splitters
%python3_sitelibdir_noarch/%{pypi_name}_text_splitters-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_text_splitters/__pycache__
%doc libs/text-splitters/README.md

%files -n %name-anthropic
%python3_sitelibdir_noarch/%{pypi_name}_anthropic
%python3_sitelibdir_noarch/%{pypi_name}_anthropic-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_anthropic/__pycache__
%doc libs/partners/anthropic/README.md

# Couldn't build `python3(chromadb)` for `chroma`
# %files -n %name-chroma
# %python3_sitelibdir_noarch/%{pypi_name}_chroma
# %python3_sitelibdir_noarch/%{pypi_name}_chroma-*
# %exclude %python3_sitelibdir_noarch/%{pypi_name}_chroma/__pycache__
# %doc libs/partners/chroma/README.md

%files -n %name-deepseek
%python3_sitelibdir_noarch/%{pypi_name}_deepseek
%python3_sitelibdir_noarch/%{pypi_name}_deepseek-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_deepseek/__pycache__
%doc libs/partners/deepseek/README.md

%files -n %name-exa
%python3_sitelibdir_noarch/%{pypi_name}_exa
%python3_sitelibdir_noarch/%{pypi_name}_exa-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_exa/__pycache__
%doc libs/partners/exa/README.md

# Couldn't build `python3(fireworks.client)` for `fireworks`
# %files -n %name-fireworks
# %python3_sitelibdir_noarch/%{pypi_name}_fireworks
# %python3_sitelibdir_noarch/%{pypi_name}_fireworks-*
# %exclude %python3_sitelibdir_noarch/%{pypi_name}_fireworks/__pycache__
# %doc libs/partners/fireworks/README.md

%files -n %name-groq
%python3_sitelibdir_noarch/%{pypi_name}_groq
%python3_sitelibdir_noarch/%{pypi_name}_groq-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_groq/__pycache__
%doc libs/partners/groq/README.md

%files -n %name-huggingface
%python3_sitelibdir_noarch/%{pypi_name}_huggingface
%python3_sitelibdir_noarch/%{pypi_name}_huggingface-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_huggingface/__pycache__
%doc libs/partners/huggingface/README.md

# Couldn't build `python3(tokenizers)` for `mistralai`
# %files -n %name-mistralai
# %python3_sitelibdir_noarch/%{pypi_name}_mistralai
# %python3_sitelibdir_noarch/%{pypi_name}_mistralai-*
# %exclude %python3_sitelibdir_noarch/%{pypi_name}_mistralai/__pycache__
# %doc libs/partners/mistralai/README.md

# Couldn't build `python3(torch)` for `nomic`
# %files -n %name-nomic
# %python3_sitelibdir_noarch/%{pypi_name}_nomic
# %python3_sitelibdir_noarch/%{pypi_name}_nomic-*
# %exclude %python3_sitelibdir_noarch/%{pypi_name}_nomic/__pycache__
# %doc libs/partners/nomic/README.md

%files -n %name-ollama
%python3_sitelibdir_noarch/%{pypi_name}_ollama
%python3_sitelibdir_noarch/%{pypi_name}_ollama-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_ollama/__pycache__
%doc libs/partners/ollama/README.md

%files -n %name-openai
%python3_sitelibdir_noarch/%{pypi_name}_openai
%python3_sitelibdir_noarch/%{pypi_name}_openai-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_openai/__pycache__
%doc libs/partners/openai/README.md

%files -n %name-perplexity
%python3_sitelibdir_noarch/%{pypi_name}_perplexity
%python3_sitelibdir_noarch/%{pypi_name}_perplexity-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_perplexity/__pycache__
%doc libs/partners/perplexity/README.md

%files -n %name-prompty
%python3_sitelibdir_noarch/%{pypi_name}_prompty
%python3_sitelibdir_noarch/%{pypi_name}_prompty-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_prompty/__pycache__
%doc libs/partners/prompty/README.md

%files -n %name-qdrant
%python3_sitelibdir_noarch/%{pypi_name}_qdrant
%python3_sitelibdir_noarch/%{pypi_name}_qdrant-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_qdrant/__pycache__
%doc libs/partners/qdrant/README.md

%files -n %name-voyageai
%python3_sitelibdir_noarch/%{pypi_name}_voyageai
%python3_sitelibdir_noarch/%{pypi_name}_voyageai-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_voyageai/__pycache__
%doc libs/partners/voyageai/README.md

%files -n %name-xai
%python3_sitelibdir_noarch/%{pypi_name}_xai
%python3_sitelibdir_noarch/%{pypi_name}_xai-*
%exclude %python3_sitelibdir_noarch/%{pypi_name}_xai/__pycache__
%doc libs/partners/xai/README.md

%changelog
* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.23-alt1
- Initial build
