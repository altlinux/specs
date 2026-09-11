%define _unpackaged_files_terminate_build 1
%define pypi_name langchain

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

BuildRequires(pre): rpm-build-pyproject
Source99: %pyproject_deps_config_name

Name: python3-module-langchain
Version: 1.4.0
Release: alt2
Summary: Building applications with LLMs through composability
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langchain/
Vcs: https://github.com/langchain-ai/langchain
BuildArch: noarch
Source0: langchain.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langchain_metadata
%pyproject_builddeps -- langchain_pep518
%pyproject_builddeps -- langchain_pep517
%files -n python3-module-langchain -f langchain.files

%add_python_extra mcp
%add_python_extra anthropic
%add_python_extra deepseek
%add_python_extra openai

%description
LangChain is the easiest way to start building agents and applications powered
by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic,
Google, and more. LangChain provides a pre-built agent architecture and model
integrations to help you get started quickly and seamlessly incorporate LLMs
into your agents and applications.


%package -n python3-module-langchain-core
Version: 1.6.1
Release: alt2
Summary: Building applications with LLMs through composability
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langchain-core/
Vcs: https://github.com/langchain-ai/langchain
BuildArch: noarch
Source1: langchain-core.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langchain_core_metadata
%pyproject_builddeps -- langchain_core_pep518
%pyproject_builddeps -- langchain_core_pep517
%files -n python3-module-langchain-core -f langchain_core.files

%description -n python3-module-langchain-core
%summary.


%package -n python3-module-langchain-openai
Version: 1.6.0
Release: alt2
Summary: An integration package connecting OpenAI and LangChain
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langchain-openai/
Vcs: https://github.com/langchain-ai/langchain
BuildArch: noarch
Source2: langchain-openai.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langchain_openai_metadata
%pyproject_builddeps -- langchain_openai_pep518
%pyproject_builddeps -- langchain_openai_pep517
%files -n python3-module-langchain-openai -f langchain_openai.files

%description -n python3-module-langchain-openai
%summary.


%package -n python3-module-langchain-deepseek
Version: 1.1.0
Release: alt2
Summary: An integration package connecting DeepSeek and LangChain
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langchain-deepseek/
Vcs: https://github.com/langchain-ai/langchain
BuildArch: noarch
Source3: langchain-deepseek.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langchain_deepseek_metadata
%pyproject_builddeps -- langchain_deepseek_pep518
%pyproject_builddeps -- langchain_deepseek_pep517
%files -n python3-module-langchain-deepseek -f langchain_deepseek.files

%description -n python3-module-langchain-deepseek
%summary.


%package -n python3-module-langchain-anthropic
Version: 1.7.1
Release: alt2
Summary: Integration package connecting Claude (Anthropic) APIs and LangChain
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langchain-anthropic/
Vcs: https://github.com/langchain-ai/langchain
BuildArch: noarch
Source4: langchain-anthropic.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langchain_anthropic_metadata
%pyproject_builddeps -- langchain_anthropic_pep518
%pyproject_builddeps -- langchain_anthropic_pep517
%files -n python3-module-langchain-anthropic -f langchain_anthropic.files

%description -n python3-module-langchain-anthropic
%summary.


%package -n python3-module-langchain-text-splitters
Version: 1.1.2
Release: alt2
Summary: LangChain text splitting utilities
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langchain-text-splitters/
Vcs: https://github.com/langchain-ai/langchain
BuildArch: noarch
Source5: langchain-text-splitters.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langchain_text_splitters_metadata
%pyproject_builddeps -- langchain_text_splitters_pep518
%pyproject_builddeps -- langchain_text_splitters_pep517
%files -n python3-module-langchain-text-splitters -f langchain_text_splitters.files

%description -n python3-module-langchain-text-splitters
%summary.


%prep
%setup -c -T -n packages
%setup -D -T -n packages -a0 -a1 -a2 -a3 -a4 -a5

for target in $(ls -d *) ; do
    pushd $target
        %pyproject_deps_resync ${target}_pep518 pep518
        %pyproject_deps_resync ${target}_pep517 pep517
        %pyproject_deps_resync ${target}_metadata metadata
    popd
done

%build
for target in $(ls -d *) ; do
    pushd $target
        %pyproject_build
    popd
done

%install
builddir=$PWD
for target in $(ls -d *) ; do
    pushd $target
        %pyproject_install --rpm-filelist $builddir/$target.files
    popd
done

%changelog
* Fri Sep 11 2026 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt2
- Used --rpm-filelist to generate filelists for %%files.

* Tue Sep 08 2026 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated langchain to 1.4.0.
- Updated langchain-core to 1.6.1.
- Updated langchain-anthropic to 1.7.1.

* Mon Aug 31 2026 Anton Zhukharev <ancieg@altlinux.org> 1.3.17-alt1
- Updated langchain to 1.3.17.
- Updated langchain-anthropic to 1.6.1.
- Updated langchain-openai to 1.6.0.
- Updated langchain-core to 1.6.0.
- Updated langchain-deepseek to 1.1.0.
- Updated langchain-text-splitters to 1.1.2.

* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.23-alt1
- Initial build
