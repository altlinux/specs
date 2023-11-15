%define _unpackaged_files_terminate_build 1
%define pypi_name yesqa

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: Automatically remove unnecessary `# noqa` comments
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/yesqa/
Vcs: https://github.com/asottile/yesqa

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-flake8
%endif

%description
A tool (and pre-commit hook) to automatically remove unnecessary # noqa
comments, for example: a check that's no longer applicable (say you
increased your max line length), a mistake (# noqa added to a line that
wasn't failing), or other code in the file caused it to no longer need
a # noqa (such as an unused import).

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__/%pypi_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 15 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- Built for ALT Sisyphus.

