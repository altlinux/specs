%define pypi_name aider-chat
%define dist_name aider_chat
%define mod_name aider

Name: aider-chat
Version: 0.86.2
Release: alt1

Summary: AI pair programming in your terminal

License: Apache-2.0
Group: Development/Tools
Url: https://aider.chat/
Vcs: https://github.com/Aider-AI/aider

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://files.pythonhosted.org/packages/source/a/%pypi_name/%dist_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-setuptools_scm

%add_python3_req_skip mslex

%description
Aider lets you pair program with LLMs to start a new project or build on
your existing codebase. It works best with Claude, GPT-4o, DeepSeek, and
other top-tier LLMs that excel at editing source code.

Aider can write code, edit existing code in multiple files at once, fix
bugs, write tests, refactor code, and update documentation while
maintaining git history.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_AIDER_CHAT=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_AIDER_CHAT=%version
%pyproject_install

%files
%doc README.md HISTORY.md
%_bindir/aider
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.86.2-alt1
- initial build for ALT Sisyphus
