%define _unpackaged_files_terminate_build 1
%define pypi_name yapf

%def_with check

Name: python3-module-%pypi_name
Version: 0.32.0
Release: alt1

Summary: A formatter for Python files
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/yapf/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-vim

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

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
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst CHANGELOG
%_bindir/yapf*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%{pypi_name}tests/

%files -n vim-plugin-yapf
%vim_autoload_dir/*
%vim_plugin_dir/*

%changelog
* Sun Oct 02 2022 Anton Zhukharev <ancieg@altlinux.org> 0.32.0-alt1
- initial build for Sisyphus

