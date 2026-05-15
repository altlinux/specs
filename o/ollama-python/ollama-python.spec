# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: ollama-python
Version: 0.6.2
Release: alt1
Summary: Ollama Python library
License: MIT
Group: Sciences/Computer science
Url: https://ollama.com
Vcs: https://github.com/ollama/ollama-python

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatch-vcs)
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
Requires(post): ollama-cpu
%endif

%description checkinstall
%summary.

%prep
%setup
sed -Ei '/^version\s*=/s/"[0.]+"/"%version"/' pyproject.toml

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --ignore=examples

%post checkinstall
set -xe
%__python3 -c 'import ollama'
%__python3 -c 'import ollama; ollama.list()' |& grep 'ConnectionError'
type ollama || exit 0
ollama serve &
sleep 1
%__python3 -c 'import ollama; ollama.list(); ollama.ps()'
kill %%ollama
wait
rm -rf /root/.ollama

%files -n python3-module-ollama
%define _customdocdir %_docdir/%name
%doc LICENSE *.md requirements.txt examples
%python3_sitelibdir_noarch/ollama
%python3_sitelibdir_noarch/ollama-%version.dist-info

%files checkinstall

%changelog
* Fri May 15 2026 Vitaly Chikunov <vt@altlinux.org> 0.6.2-alt1
- Update to v0.6.2 (2026-01-23).

* Fri Nov 14 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.1-alt1
- Update to v0.6.1 (2025-11-12).

* Thu Sep 25 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.0-alt1
- Update to v0.6.0 (2025-09-24).
- Documentation with examples moved to static location at
  /usr/share/doc/ollama-python.

* Wed Sep 17 2025 Vitaly Chikunov <vt@altlinux.org> 0.5.4-alt1
- Update to v0.5.4 (2025-09-15).

* Thu Aug 07 2025 Vitaly Chikunov <vt@altlinux.org> 0.5.3-alt1
- Update to v0.5.3 (2025-08-07).

* Sun Jun 01 2025 Vitaly Chikunov <vt@altlinux.org> 0.5.1-alt1
- Update to v0.5.1 (2025-05-30).

* Tue May 27 2025 Vitaly Chikunov <vt@altlinux.org> 0.4.9-alt1
- Update to v0.4.9 (2025-05-14).
- spec: Upstream switched from Poetry to Hatch.

* Tue Apr 22 2025 Vitaly Chikunov <vt@altlinux.org> 0.4.8-alt1
- Update to v0.4.8 (2025-04-16).

* Wed Feb 19 2025 Vitaly Chikunov <vt@altlinux.org> 0.4.7-alt1
- Update to v0.4.7 (2025-01-21).

* Fri Jan 17 2025 Vitaly Chikunov <vt@altlinux.org> 0.4.6-alt1
- Update to v0.4.6 (2025-01-13).
- spec: Add checkinstall with basic smoke tests.
- spec: Rename the (noarch) top-level package python3-module-ollama to the
  (arch) ollama-python to allow creation of arch-specific sub-packages (for
  chackinstall, which requires arch-specific package ollama for tests).

* Mon Dec 09 2024 Vitaly Chikunov <vt@altlinux.org> 0.4.4-alt1
- First import v0.4.4-1-g70dd0b7 (2024-12-07).
