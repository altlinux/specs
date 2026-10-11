%define _unpackaged_files_terminate_build 1
%define oname hermes-agent
%define mname hermes_agent

Name: hermes-agent
Version: 2026.9.24
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

# application: keep its modules private and provide nothing but itself
AutoProv: yes,nopython3
%add_python3_path %_datadir/%name
%add_python3_self_prov_path %buildroot%_datadir/%name

# optional mem0ai memory plugin (extra "mem0", not in Sisyphus)
%add_python3_req_skip mem0.configs.llms.base mem0.configs.llms.openai mem0.llms.base mem0.llms.openai

%description
hermes-agent is a self-improving AI agent that creates skills from
experience, improves them during use, and runs anywhere. It supports tool
use, web browsing, automation, voice, messaging, and many integrations.

%prep
%setup

# Bump pyproject version to match git tag (upstream forgets to sync)
sed -i 's/^version = ".*"/version = "%version"/' pyproject.toml
# Strip non-ASCII description (em-dash) that breaks sisyphus_check
sed -i 's/ - / - /g; s/—/-/g' pyproject.toml

# Remove npm/yarn/web dashboard parts (not built here)
rm -rv web ui-tui scripts/whatsapp-bridge package-lock.json

%build
# upstream setup.py blocks wheel builds unless this flag is set
export HERMES_NIX_BUILD=1
%pyproject_build

%install
%pyproject_install
# move the application modules to a private directory
mkdir -p %buildroot%_datadir
mv %buildroot%python3_sitelibdir %buildroot%_datadir/%name
# upstream wheel no longer ships these data dirs; runtime looks for them next to the packages
cp -a locales optional-mcps %buildroot%_datadir/%name/

# entry point scripts use the private module directory
for s in hermes:hermes_cli.main hermes-agent:agent.legacy_cli hermes-acp:acp_adapter.entry ; do
    cat >%buildroot%_bindir/${s%%%%:*} <<EOF
#!%__python3
import sys
sys.path.insert(0, "%_datadir/%name")
from ${s#*:} import main
sys.exit(main())
EOF
done

%files
%doc README.md LICENSE SECURITY.md
%_bindir/hermes
%_bindir/hermes-agent
%_bindir/hermes-acp
%_datadir/%name/

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.9.24-alt1
- new version 2026.9.24
- move application modules out of python3 site-packages to %%_datadir/%%name
  (provide only the package itself)

* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.7.7.2-alt1
- new version 2026.7.7.2

* Mon May 04 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.4.30-alt1
- initial build for ALT Sisyphus
