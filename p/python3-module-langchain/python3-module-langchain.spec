%define _unpackaged_files_terminate_build 1

BuildRequires(pre): rpm-build-pyproject
Source99: %pyproject_deps_config_name

Name: python3-module-langchain
Version: 1.3.17
Release: alt1
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

%files -n python3-module-langchain
%python3_sitelibdir/langchain/
%python3_sitelibdir/langchain-%version.dist-info/

%description
LangChain is the easiest way to start building agents and applications powered
by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic,
Google, and more. LangChain provides a pre-built agent architecture and model
integrations to help you get started quickly and seamlessly incorporate LLMs
into your agents and applications.


%package -n python3-module-langchain-core
Version: 1.6.0
Release: alt1
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

%files -n python3-module-langchain-core
%python3_sitelibdir/langchain_core/
%python3_sitelibdir/langchain_core-%version.dist-info/

%description -n python3-module-langchain-core
%summary.


%package -n python3-module-langchain-openai
Version: 1.6.0
Release: alt1
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

%files -n python3-module-langchain-openai
%python3_sitelibdir/langchain_openai/
%python3_sitelibdir/langchain_openai-%version.dist-info/

%description -n python3-module-langchain-openai
%summary.


%package -n python3-module-langchain-deepseek
Version: 1.1.0
Release: alt1
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

%files -n python3-module-langchain-deepseek
%python3_sitelibdir/langchain_deepseek/
%python3_sitelibdir/langchain_deepseek-%version.dist-info/

%description -n python3-module-langchain-deepseek
%summary.


%package -n python3-module-langchain-anthropic
Version: 1.6.1
Release: alt1
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

%files -n python3-module-langchain-anthropic
%python3_sitelibdir/langchain_anthropic/
%python3_sitelibdir/langchain_anthropic-%version.dist-info/

%description -n python3-module-langchain-anthropic
%summary.


%package -n python3-module-langchain-text-splitters
Version: 1.1.2
Release: alt1
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

%files -n python3-module-langchain-text-splitters
%python3_sitelibdir/langchain_text_splitters/
%python3_sitelibdir/langchain_text_splitters-%version.dist-info/

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
for target in $(ls -d *) ; do
    pushd $target
        %pyproject_install
    popd
done

%changelog
* Mon Aug 31 2026 Anton Zhukharev <ancieg@altlinux.org> 1.3.17-alt1
- Updated langchain to 1.3.17.
- Updated langchain-anthropic to 1.6.1.
- Updated langchain-openai to 1.6.0.
- Updated langchain-core to 1.6.0.
- Updated langchain-deepseek to 1.1.0.
- Updated langchain-text-splitters to 1.1.2.

* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.23-alt1
- Initial build
