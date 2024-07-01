%define _unpackaged_files_terminate_build 1
%define pypi_name tldr
%define mod_name tldr

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: Python command-line client for tldr pages
License: MIT
Group: Documentation

Url: https://pypi.org/project/tldr/
Vcs: https://github.com/tldr-pages/tldr-python-client
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# previous name
Provides: tldr = %EVR
Obsoletes: tldr <= 3.1.0-alt1

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif
BuildRequires: python3-module-termcolor
BuildRequires: python3-module-colorama
BuildRequires: python3-module-shtab
# man page
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-argparse

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
# First make docs or else error
make SPHINXBUILD="sphinx-build-3" -C docs
%pyproject_build
# generate autocompletions
%pyproject_run -- tldr --print-completion bash > tldr.bash
%pyproject_run -- tldr --print-completion zsh > tldr.zsh

%install
%pyproject_install
install -Dpm644 %mod_name.bash %buildroot%_datadir/bash-completion/completions/%mod_name
install -Dpm644 %mod_name.zsh %buildroot%_datadir/zsh/site-functions/_%mod_name

%check
%pyproject_run_pytest -ra -Wignore

%files
%_bindir/tldr
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md
%_man1dir/tldr.1*
%_datadir/bash-completion/completions/%mod_name
%_datadir/zsh/site-functions/_%mod_name

# TODO: package http://github.com/tldr-pages/tldr itself

%changelog
* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.2.0 -> 3.3.0.

* Fri May 26 2023 Michael Shigorin <mike@altlinux.org> 3.2.0-alt2
- fix build --without check
- minor spec cleanup

* Wed May 17 2023 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.1.0 -> 3.2.0.

* Mon Dec 26 2022 Alexander Stepchenko <geochip@altlinux.org> 3.1.0-alt1
- Initial build for ALT.
