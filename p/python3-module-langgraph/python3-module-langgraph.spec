%define _unpackaged_files_terminate_build 1

BuildRequires(pre): rpm-build-pyproject
Source99: %pyproject_deps_config_name

Name: python3-module-langgraph
Version: 1.2.11
Release: alt2
Summary: Building stateful, multi-actor applications with LLMs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langgraph/
Vcs: https://github.com/langchain-ai/langgraph
BuildArch: noarch
Source0: langgraph.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langgraph_metadata
%pyproject_builddeps -- langgraph_pep518
%pyproject_builddeps -- langgraph_pep517
%files -n python3-module-langgraph -f langgraph.files

%description
Building stateful, multi-actor applications with LLMs


%package -n python3-module-langgraph-cli
Version: 0.4.31
Release: alt2
Summary: CLI for interacting with LangGraph API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langgraph-cli/
Vcs: https://github.com/langchain-ai/langgraph
BuildArch: noarch
Source1: langgraph-cli.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langgraph_cli_metadata
%pyproject_builddeps -- langgraph_cli_pep518
%pyproject_builddeps -- langgraph_cli_pep517
%files -n python3-module-langgraph-cli -f langgraph_cli.files

%description -n python3-module-langgraph-cli
%summary.


%package -n python3-module-langgraph-sdk
Version: 0.4.2
Release: alt2
Summary: SDK for interacting with LangGraph API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langgraph-sdk/
Vcs: https://github.com/langchain-ai/langgraph
BuildArch: noarch
Source2: langgraph-sdk.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langgraph_sdk_metadata
%pyproject_builddeps -- langgraph_sdk_pep518
%pyproject_builddeps -- langgraph_sdk_pep517
%files -n python3-module-langgraph-sdk -f langgraph_sdk.files

%description -n python3-module-langgraph-sdk
%summary.


%package -n python3-module-langgraph-prebuilt
Version: 1.1.0
Release: alt2
Summary: Library with high-level APIs for creating and executing LangGraph agents and tools.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langgraph-prebuilt/
Vcs: https://github.com/langchain-ai/langgraph
BuildArch: noarch
Source3: langgraph-prebuilt.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langgraph_prebuilt_metadata
%pyproject_builddeps -- langgraph_prebuilt_pep518
%pyproject_builddeps -- langgraph_prebuilt_pep517
%files -n python3-module-langgraph-prebuilt -f langgraph_prebuilt.files

%description -n python3-module-langgraph-prebuilt
%summary.


%package -n python3-module-langgraph-checkpoint
Version: 4.2.0
Release: alt2
Summary: Library with base interfaces for LangGraph checkpoint savers.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langgraph-checkpoint/
Vcs: https://github.com/langchain-ai/langgraph
BuildArch: noarch
Source4: langgraph-checkpoint.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langgraph_checkpoint_metadata
%pyproject_builddeps -- langgraph_checkpoint_pep518
%pyproject_builddeps -- langgraph_checkpoint_pep517
%files -n python3-module-langgraph-checkpoint -f langgraph_checkpoint.files

%description -n python3-module-langgraph-checkpoint
%summary.


%package -n python3-module-langgraph-checkpoint-sqlite
Version: 3.1.1
Release: alt2
Summary: Library with a SQLite implementation of LangGraph checkpoint saver.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langgraph-checkpoint-sqlite/
Vcs: https://github.com/langchain-ai/langgraph
BuildArch: noarch
Source5: langgraph-checkpoint-sqlite.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langgraph_checkpoint_sqlite_metadata
%pyproject_builddeps -- langgraph_checkpoint_sqlite_pep518
%pyproject_builddeps -- langgraph_checkpoint_sqlite_pep517
%files -n python3-module-langgraph-checkpoint-sqlite -f langgraph_checkpoint_sqlite.files

%description -n python3-module-langgraph-checkpoint-sqlite
%summary.


%package -n python3-module-langgraph-checkpoint-postgres
Version: 3.1.2
Release: alt2
Summary: Library with a Postgres implementation of LangGraph checkpoint saver.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langgraph-checkpoint-postgres/
Vcs: https://github.com/langchain-ai/langgraph
BuildArch: noarch
Source6: langgraph-checkpoint-postgres.tar
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- langgraph_checkpoint_postgres_metadata
%pyproject_builddeps -- langgraph_checkpoint_postgres_pep518
%pyproject_builddeps -- langgraph_checkpoint_postgres_pep517
%files -n python3-module-langgraph-checkpoint-postgres -f langgraph_checkpoint_postgres.files

%description -n python3-module-langgraph-checkpoint-postgres
%summary.


%prep
%setup -c -T -n packages
%setup -D -T -n packages -a0 -a1 -a2 -a3 -a4 -a5 -a6

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
* Fri Sep 11 2026 Anton Zhukharev <ancieg@altlinux.org> 1.2.11-alt2
- Used --rpm-filelist to generate filelists for %%files

* Mon Aug 31 2026 Anton Zhukharev <ancieg@altlinux.org> 1.2.11-alt1
- Packaged for ALT Sisyphus.
