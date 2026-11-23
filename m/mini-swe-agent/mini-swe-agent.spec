%define _unpackaged_files_terminate_build 1
%def_enable check

%define pypi_name mini-swe-agent

Name: mini-swe-agent
Version: 2.4.6
Release: alt1

Summary: A simple software engineering agent for language models

License: MIT
Group: Development/Other
URL: https://mini-swe-agent.com

VCS: https://github.com/SWE-agent/mini-swe-agent
Source: %name-%version-%release.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3-module-datasets
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-litellm
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-prompt_toolkit
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-python-dotenv
BuildRequires: python3-module-requests
BuildRequires: python3-module-rich
BuildRequires: python3-module-swe-rex
BuildRequires: python3-module-tenacity
BuildRequires: python3-module-textual
BuildRequires: python3-module-typer
BuildRequires: python3-module-yaml
%endif

%description
mini-swe-agent is a simple, minimal and readable AI software engineering
agent that solves github issues and similar programming challenges.
Just 100 lines of python (+100 total for env): no fancy dependencies!
Supports local environments, docker/podman, singularity/apptainer,
bubblewrap, contree, and more.
Supports all models via litellm, openrouter, portkey, and more.
Supports /completion and /response API endpoints, interleaved thinking, etc.

Does not have any tools other than bash: it doesn't even use the tool-calling
interface of the LMs. Instead of implementing custom tools for every specific
thing the agent might want to do, the focus is fully on the LM utilizing the
shell to its full potential.
Has a completely linear history: every step of the agent just appends
to the messages that are passed to the LM in the next step and that's it.
This is great for debugging and understanding what the LM is prompted with.

%package -n python3-module-%pypi_name
Summary: The minisweagent Python module
Group: Development/Python3
URL: https://pypi.org/project/mini-swe-agent

%description -n python3-module-%pypi_name
mini-swe-agent is a simple, minimal and readable AI software engineering
agent that solves github issues and similar programming challenges.
Just 100 lines of python (+100 total for env): no fancy dependencies!
Supports local environments, docker/podman, singularity/apptainer,
bubblewrap, contree, and more.
Supports all models via litellm, openrouter, portkey, and more.
Supports /completion and /response API endpoints, interleaved thinking, etc.

This package contains the Python module "minisweagent".

%prep
%setup -n %name-%version-%release
rm src/minisweagent/environments/extra/{contree,swerex_modal}.py
subst '
/environments.extra.contree.ContreeEnvironment/d
/environments.extra.swerex_modal.SwerexModalEnvironment/d
' src/minisweagent/environments/__init__.py

%build
%pyproject_build

%install
%pyproject_install

%check
# contree_sdk, portkey and portkey_ai Python modules
# are missing from Sisyphus, as is swerex.deployment.modal.
# test_swebench tries to access huggingface; skipping.
%pyproject_run_pytest tests \
  --ignore=tests/environments/extra/test_contree.py \
  --ignore=tests/environments/extra/test_swerex_modal.py \
  --ignore=tests/models/test_portkey_model.py \
  --ignore=tests/models/test_portkey_response_model.py \
  -k 'not portkey' \
  --deselect tests/run/test_swebench.py::test_redo_existing_false_skips_existing

%files
%doc README.md LICENSE.md
%_bindir/mini
%_bindir/mini-e
%_bindir/mini-extra
%_bindir/mini-swe-agent

%files -n python3-module-%pypi_name
%python3_sitelibdir_noarch/minisweagent
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 20 2026 Arseny Maslennikov <arseny@altlinux.org> 2.4.6-alt1
- Initial build for ALT Sisyphus.
