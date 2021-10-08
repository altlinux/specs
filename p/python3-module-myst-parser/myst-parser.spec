%define _unpackaged_files_terminate_build 1

%define oname myst-parser
%define mname myst_parser

Name: python3-module-%oname
Version: 0.15.2
Release: alt1
Summary: An extended commonmark compliant parser, with bridges to docutils/sphinx
License: MIT
Group: Development/Python3
Url: https://myst-parser.readthedocs.io/

BuildArch: noarch

# https://github.com/executablebooks/MyST-Parser
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: /usr/bin/py.test3
BuildRequires: python3(sphinx) python3(sphinx.testing) python3(bs4) python3(markdown_it)
BuildRequires: python3(yaml) python3(mdit_py_plugins)

%description
MyST is a rich and extensible flavor of Markdown
meant for technical documentation and publishing.

MyST is a flavor of markdown that is designed for simplicity,
flexibility, and extensibility. This repository serves
as the reference implementation of MyST Markdown, as well
as a collection of tools to support working with MyST in Python and Sphinx.
It contains an extended CommonMark-compliant parser using markdown-it-py,
as well as a Sphinx extension that allows you to write MyST Markdown in Sphinx.

See the MyST Parser documentation for more information.

%package -n %oname
Summary: An extended commonmark compliant parser, with bridges to docutils/sphinx
Group: Development/Python3
Requires: %name = %EVR

%description -n %oname
MyST is a rich and extensible flavor of Markdown
meant for technical documentation and publishing.

MyST is a flavor of markdown that is designed for simplicity,
flexibility, and extensibility. This repository serves
as the reference implementation of MyST Markdown, as well
as a collection of tools to support working with MyST in Python and Sphinx.
It contains an extended CommonMark-compliant parser using markdown-it-py,
as well as a Sphinx extension that allows you to write MyST Markdown in Sphinx.

See the MyST Parser documentation for more information.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv \
	--deselect=tests/test_renderers/test_myst_refs.py::test_parse \
	--deselect=tests/test_renderers/test_parse_directives.py::test_parsing \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_basic \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_references \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_references_singlehtml \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_heading_slug_func \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_extended_syntaxes \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_includes \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_footnotes \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_commonmark_only \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_substitutions \
	--deselect=tests/test_sphinx/test_sphinx_builds.py::test_gettext \
	--deselect=tests/test_renderers/test_fixtures.py::test_sphinx_directives \
	%nil

%files
%doc LICENSE
%doc README.md
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py3*.egg-info

%files -n %oname
%_bindir/myst-anchors

%changelog
* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.2-alt1
- Initial build for ALT.
