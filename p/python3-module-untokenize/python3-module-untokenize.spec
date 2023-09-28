%define _unpackaged_files_terminate_build 1
%define pypi_name untokenize
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1.git2d7bcd6

Summary: Transforms tokens into original source code (while preserving whitespace)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/untokenize/
Vcs: https://github.com/myint/untokenize

BuildArch: noarch

Source0: %name-%version-%release.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
untokenize transforms tokens into source code. Unlike the standard
library's tokenize.untokenize(), it preserves the original whitespace
between tokens.

%prep
%setup -n %name-%version-%release
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1.git2d7bcd6
- Built for ALT Sisyphus.

