%define oname grep_ast
%define pypi_name grep-ast

Name: python3-module-grep-ast
Version: 0.9.0
Release: alt1

Summary: A tool to grep through the AST of a source file
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/paul-gauthier/grep-ast

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-pathspec

# tree-sitter-language-pack and tree-sitter-languages are not packaged in ALT yet.
# grep_ast/tsl.py imports one of them lazily; allow building without them.
%add_python3_req_skip tree_sitter_language_pack tree_sitter_languages

%description
Grep source code files and see matching lines with useful context that
show how they fit into the code. See the loops, functions, methods,
classes, etc that contain all the matching lines.

Get a sense of what's inside a matched class or function definition.
You see relevant code from every layer of the abstract syntax tree,
above and below the matches.

By default, grep-AST recurses the current directory to search all source
code files. It respects .gitignore, so it will usually "do the right
thing" in most repos.

grep-AST is built with tree-sitter.

%package -n grep-ast
Summary: A tool to grep through the AST of a source file
Group: Development/Tools
Requires: python3-module-%pypi_name = %EVR

%description -n grep-ast
Grep source code files and see matching lines with useful context that
show how they fit into the code (CLI tools: grep-ast, gast).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%files -n grep-ast
%_bindir/grep-ast
%_bindir/gast

%changelog
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- initial build for ALT Sisyphus

