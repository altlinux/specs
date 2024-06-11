%define _unpackaged_files_terminate_build 1

%define modulename textual
%def_with check

Name: python3-module-%modulename
Version: 0.67.0
Release: alt1

Summary: Textual is a Rapid Application Development framework for Python
License: MIT
Group: Terminals
Url: https://textual.textualize.io/
Vcs: https://github.com/Textualize/textual.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-rich
BuildRequires: python3-module-markdown
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-linkify-it-py
BuildRequires: python3-module-pytest-textual-snapshot
%endif

%description
Textual is a Rapid Application Development framework for Python.
Build sophisticated user interfaces with a simple Python API. Run
your apps in the terminal or a web browser!

%prep
%setup
# for windows
rm src/textual/drivers/win32.py

%build
%pyproject_build

%install
%pyproject_install

# test_snapshots needs GUI mode, tested locally
# In test_input_value_visibility broken "value"
# test_textual_env_var assert None is not None
# test_register_language, test_register_language_existing_language,
# test_language_binary_missing no module tree_sitter_languages
# https://github.com/grantjenks/py-tree-sitter-languages

%check
%pyproject_run_pytest -ra -Wignore \
    -ra tests -k "\
    not test_textual_env_var and \
    not test_register_language and \
    not test_register_language_existing_language and \
    not test_language_binary_missing" \
    --ignore="tests/snapshot_tests/test_snapshots.py" \
    --ignore="tests/input/test_input_value_visibility.py"

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc README.md docs/* examples/

%changelog
* Tue Jun 11 2024 Elena Dyatlenko <lenka@altlinux.org> 0.67.0-alt1
- Updated to upstream version v0.67.0.

* Mon Jun 03 2024 Elena Dyatlenko <lenka@altlinux.org> 0.64.0-alt1
- Initial build for Sisyphus.

