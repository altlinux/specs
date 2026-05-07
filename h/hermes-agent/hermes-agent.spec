%define _unpackaged_files_terminate_build 1
%define oname hermes-agent
%define mname hermes_agent

Name: hermes-agent
Version: 2026.4.30
Release: alt1

Summary: Locally-run AI agent with tool use, web browsing, and automation
Group: Development/Other
License: MIT
Url: https://github.com/NousResearch/hermes-agent
Vcs: https://github.com/NousResearch/hermes-agent.git

# Source-url: https://github.com/NousResearch/hermes-agent/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools python3-module-wheel

%description
hermes-agent is a self-improving AI agent that creates skills from
experience, improves them during use, and runs anywhere. It supports tool
use, web browsing, automation, voice, messaging, and many integrations.

%prep
%setup

# Bump pyproject version to match git tag (upstream forgets to sync)
sed -i 's/^version = "0\.12\.0"/version = "%version"/' pyproject.toml
# Strip non-ASCII description (em-dash) that breaks sisyphus_check
sed -i 's/ - / - /g; s/—/-/g' pyproject.toml

# Remove npm/yarn/web dashboard parts (not built here)
rm -rv web ui-tui scripts/whatsapp-bridge package-lock.json

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE SECURITY.md
%_bindir/hermes
%_bindir/hermes-agent
%_bindir/hermes-acp
%python3_sitelibdir/acp_adapter/
%python3_sitelibdir/agent/
%python3_sitelibdir/cron/
%python3_sitelibdir/gateway/
%python3_sitelibdir/hermes_cli/
%python3_sitelibdir/plugins/
%python3_sitelibdir/tools/
%python3_sitelibdir/tui_gateway/
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/%{pyproject_distinfo %mname}/

%changelog
* Mon May 04 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.4.30-alt1
- initial build for ALT Sisyphus
