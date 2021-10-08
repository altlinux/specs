%define _unpackaged_files_terminate_build 1

%define oname markdown-it
%define mname markdown_it

Name: python3-module-%oname
Version: 1.1.0
Release: alt1
Summary: Markdown parser, done right. 100%% CommonMark support, extensions, syntax plugins & high speed. Now in Python!
License: MIT
Group: Development/Python3
Url: https://markdown-it-py.readthedocs.io/

BuildArch: noarch

# https://github.com/executablebooks/markdown-it-py
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: /usr/bin/py.test3
BuildRequires: python3(pytest_benchmark)

%description
Markdown parser done right.

* Follows the CommonMark spec for baseline parsing
* Configurable syntax: you can add new rules and even replace existing ones.
* Pluggable: Adds syntax extensions to extend the parser (see the plugin list).
* High speed (see our benchmarking tests)
* Safe by default

This is a Python port of markdown-it, and some of its associated plugins.
For more details see: https://markdown-it-py.readthedocs.io.

%package -n %oname
Summary: Markdown parser, done right. 100%% CommonMark support, extensions, syntax plugins & high speed. Now in Python!
Group: Development/Python3
Requires: %name = %EVR

%description -n %oname
Markdown parser done right.

* Follows the CommonMark spec for baseline parsing
* Configurable syntax: you can add new rules and even replace existing ones.
* Pluggable: Adds syntax extensions to extend the parser (see the plugin list).
* High speed (see our benchmarking tests)
* Safe by default

This is a Python port of markdown-it, and some of its associated plugins.
For more details see: https://markdown-it-py.readthedocs.io.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv \
	--deselect=tests/test_linkify.py::test_token_levels \
	--deselect=tests/test_port/test_fixtures.py::test_linkify \
	--deselect=tests/test_tree.py::test_pretty \
	--deselect=tests/test_api/test_main.py::test_table_tokens \
	--deselect=tests/test_cmark_spec/test_spec.py::test_file \
	--deselect=tests/test_port/test_references.py::test_use_existing_env \
	--deselect=tests/test_port/test_references.py::test_store_labels \
	%nil

%files
%doc LICENSE LICENSE.markdown-it
%doc README.md
%python3_sitelibdir/%mname
%python3_sitelibdir/%{mname}_py-%version-py3*.egg-info

%files -n %oname
%_bindir/%oname

%changelog
* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Initial build for ALT.
