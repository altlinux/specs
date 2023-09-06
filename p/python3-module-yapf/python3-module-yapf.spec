%define _unpackaged_files_terminate_build 1
%define pypi_name yapf

%def_with check

Name: python3-module-%pypi_name
Version: 0.40.1
Release: alt1
Summary: A formatter for Python files
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/yapf/
Vcs: https://github.com/google/yapf
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
%filter_from_requires /python3(yapf_third_party._ylib2to3.pgen2.pgen2)/d
BuildRequires(pre): rpm-build-pyproject
BuildRequires(pre): rpm-build-vim
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
Most of the current formatters for Python --- e.g., autopep8, and
pep8ify --- are made to remove lint errors from code. This has some
obvious limitations. For instance, code that conforms to the PEP 8
guidelines may not be reformatted. But it doesn't mean that the code
looks good.

YAPF takes a different approach. It's based off of 'clang-format',
developed by Daniel Jasper. In essence, the algorithm takes the code
and reformats it to the best formatting that conforms to the style
guide, even if the original code didn't violate the style guide. The
idea is also similar to the 'gofmt' tool for the Go programming
language: end all holy wars about formatting - if the whole codebase of
a project is simply piped through YAPF whenever modifications are made,
the style remains consistent throughout the project and there's no point
arguing about style in every code review.

The ultimate goal is that the code YAPF produces is as good as the code
that a programmer would write if they were following the style guide. It
takes away some of the drudgery of maintaining your code.

%package -n vim-plugin-yapf
Summary: The vim plugin allows you to reformat a range of code
Group: Editors

%description -n vim-plugin-yapf
%summary.

%prep
%setup

# fix local imports
sed -i "/from pgen2 import/s/pgen2/.pgen2/" \
    third_party/yapf_third_party/_ylib2to3/pgen2/conv.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%vim_autoload_dir/
mkdir -p %buildroot%vim_plugin_dir/

pushd plugins/vim
    install -p -m644 autoload/yapf.vim %buildroot%vim_autoload_dir/
    install -p -m644 plugin/yapf.vim %buildroot%vim_plugin_dir/
popd

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst CHANGELOG
%_bindir/yapf*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/yapf_third_party/
%exclude %python3_sitelibdir/%{pypi_name}tests/

%files -n vim-plugin-yapf
%vim_autoload_dir/*
%vim_plugin_dir/*

%changelog
* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.40.1-alt1
- Updated to 0.40.1.

* Wed May 17 2023 Stanislav Levin <slev@altlinux.org> 0.33.0-alt1
- 0.32.0 -> 0.33.0.

* Sun Oct 02 2022 Anton Zhukharev <ancieg@altlinux.org> 0.32.0-alt1
- initial build for Sisyphus

