%define _unpackaged_files_terminate_build 1
%define module_name opentelemetry
%define version_beta b0

# Upstream versions the wheels X.YbN; the spec keeps the beta in Release.
%define pyproject_distinfo() %{pep427_name: %1}-%version%{version_beta}.dist-info

# Each packaged component is described by macros sharing a KEY prefix
# (util, gg). The helper macros below take only KEY and look the rest
# up, so adding a component means adding one more block like these.
#   KEY_dir     source directory of the component in the upstream tree
#   KEY_name    distribution name without the opentelemetry- prefix,
#               used in the subpackage and dist-info names
#   KEY_module  module path below the opentelemetry namespace, for %%files
#   KEY_summary summary and description of the subpackage
#   KEY_extra   optional extra whose deps are added to the runtime ones

# util: GenAI utilities shared by the instrumentations
%define util_dir util/%module_name-util-genai
%define util_name util-genai
%define util_module util/genai
%define util_summary OpenTelemetry GenAI utilities

# gg: Google GenAI instrumentation
%define gg_dir instrumentation/%module_name-instrumentation-google-genai
%define gg_name instrumentation-google-genai
%define gg_module instrumentation/google_genai
%define gg_summary OpenTelemetry Google GenAI instrumentation
# The instrumented library itself comes in through this extra.
%define gg_extra instruments

# Common
%define genai_dirs %util_dir %gg_dir
# Upstream pytest plugin for the GenAI suites, used only by the tests.
%define test_util_dir util/%module_name-test-util-genai

# %%add_genai_package KEY: subpackage of KEY with runtime deps from the
# KEY_metadata source instead of the import scanner.
%define add_genai_package() \
%{expand:%%package -n python3-module-%%module_name-%%%{1}_name \
Summary: %%%{1}_summary \
Group: Development/Python3 \
AutoReq: yes, nopython3 \
%%pyproject_runtimedeps -- %{1}_metadata %%{?%{1}_extra:--extra %%%{1}_extra} \
%%description -n python3-module-%%module_name-%%%{1}_name \
%%%{1}_summary. \
}

# %%add_genai_files KEY: %%files section of the KEY subpackage.
%define add_genai_files() \
%{expand:%%files -n python3-module-%%module_name-%%%{1}_name \
%%doc %%%{1}_dir/README.rst %%%{1}_dir/LICENSE \
%%python3_sitelibdir/%%module_name/%%%{1}_module/ \
%%python3_sitelibdir/%%{pyproject_distinfo %%module_name-%%%{1}_name}/ \
}

# %%genai_deps_resync KEY: verify or sync the deps sources of KEY_dir.
%define genai_deps_resync() \
%{expand:cd %%%{1}_dir \
%%pyproject_deps_resync %{1}_pep518 pep518 \
%%pyproject_deps_resync %{1}_metadata metadata \
cd - \
}

%def_with check

Name: python3-module-opentelemetry-python-genai
Version: 1.2
Release: alt1.%version_beta

Summary: OpenTelemetry instrumentation for generative AI libraries
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/open-telemetry/opentelemetry-python-genai
Vcs: https://github.com/open-telemetry/opentelemetry-python-genai
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps -- util_pep518
%pyproject_builddeps -- gg_pep518
%if_with check
# The rest of the tox pytest_deps; test_util_metadata brings pytest.
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-vcr
%pyproject_builddeps -- util_metadata
%pyproject_builddeps -- util_check
%pyproject_builddeps -- gg_check
# opentelemetry-util-genai is built here.
%pyproject_builddeps -- test_util_metadata --exclude 'opentelemetry-util-genai$'
%endif

%description
%summary.

%add_genai_package util
%add_genai_package gg

%prep
%setup
%autopatch -p1
%genai_deps_resync util
%genai_deps_resync gg
%pyproject_deps_resync util_check pip_reqfile %util_dir/test-requirements.txt
%pyproject_deps_resync gg_check pip_reqfile %gg_dir/tests/requirements.latest.txt
cd %test_util_dir
%pyproject_deps_resync test_util_metadata metadata
cd -

%build
for dir in %genai_dirs; do
	cd $dir
	%pyproject_build
	cd -
done

%install
for dir in %genai_dirs; do
	cd $dir
	%pyproject_install
	cd -
done

%check
%pyproject_run --wheel %util_dir/dist/$(cat %util_dir/dist/.wheeltracker) -- bash -s <<-'ENDTESTS'
set -eu
# The venv holds the util-genai wheel; add the instrumentation one and
# load the upstream test plugin from its source tree, it is not shipped.
python3 -m pyproject_installer install %gg_dir/dist/$(cat %gg_dir/dist/.wheeltracker)
export PYTHONPATH=$PWD/%test_util_dir/src
# Both suites are packages named "tests", so they run one at a time.
python3 -m pytest -ra %util_dir/tests
# Replay the recorded cassettes only: hasher has no network, and the
# fixtures switch to fake credentials just in that mode.
# test_conformance.py drives the external OpenTelemetry Weaver binary.
python3 -m pytest -ra --vcr-record=none %gg_dir/tests \
	--ignore %gg_dir/tests/test_conformance.py
ENDTESTS

%add_genai_files util
%add_genai_files gg

%changelog
* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.2-alt1.b0
- Initial build for ALT Sisyphus.
