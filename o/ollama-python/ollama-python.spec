# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: ollama-python
Version: 0.4.6
Release: alt1
Summary: Ollama Python library
License: MIT
Group: Sciences/Computer science
Url: https://ollama.com
Vcs: https://github.com/ollama/ollama-python

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(poetry-core)
%{?!_without_check:%{?!_disable_check:
BuildRequires: pytest3
BuildRequires: python3(anyio)
BuildRequires: python3(httpx)
BuildRequires: python3(PIL)
BuildRequires: python3(pydantic)
BuildRequires: python3(pytest_asyncio)
BuildRequires: python3(pytest_httpserver)
}}

%description
The Ollama Python library.

%package -n python3-module-ollama
Summary: %summary
Group: Sciences/Computer science
BuildArch: noarch
Requires: python3(anyio)

%description -n python3-module-ollama
The Ollama Python library provides the easiest way to integrate Python 3.8+
projects with Ollama.

%package checkinstall
Summary: CI for %name
Group: Development/Other
Requires(post): python3-module-ollama = %EVR
Requires(post): python3
%ifarch aarch64 x86_64
Requires(post): ollama
%endif

%description checkinstall
%summary.

%prep
%setup
sed -Ei '/^version\s*=/s/"[0.]+"/"%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%post checkinstall
set -xe
%__python3 -c 'import ollama'
%__python3 -c 'import ollama; ollama.list()' |& grep 'Connection refused'
type ollama || exit 0
ollama serve &
sleep 1
%__python3 -c 'import ollama; ollama.list(); ollama.ps()'
kill %%ollama
wait
rm -rf /root/.ollama

%files -n python3-module-ollama
%doc LICENSE README.md requirements.txt examples
%python3_sitelibdir_noarch/ollama
%python3_sitelibdir_noarch/ollama-%version.dist-info

%files checkinstall

%changelog
* Fri Jan 17 2025 Vitaly Chikunov <vt@altlinux.org> 0.4.6-alt1
- Update to v0.4.6 (2025-01-13).
- spec: Add checkinstall with basic smoke tests.
- spec: Rename the (noarch) top-level package python3-module-ollama to the
  (arch) ollama-python to allow creation of arch-specific sub-packages (for
  chackinstall, which requires arch-specific package ollama for tests).

* Mon Dec 09 2024 Vitaly Chikunov <vt@altlinux.org> 0.4.4-alt1
- First import v0.4.4-1-g70dd0b7 (2024-12-07).
