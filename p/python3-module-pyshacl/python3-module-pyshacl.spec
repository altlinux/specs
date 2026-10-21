%define pypi_name pyshacl

%def_with check

Name:    python3-module-%pypi_name
Version: 0.40.1
Release: alt1

Summary: A Python validator for SHACL
License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/pyshacl/
VCS:     https://github.com/RDFLib/pySHACL

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-rdflib
BuildREquires: python3-module-owlrl
BuildRequires: python3-module-pyduktape2
BuildRequires: python3-module-prettytable
%endif

Requires: python3-module-sanic-cors

BuildArch: noarch

Source: %name-%version.tar

%description
This is a pure Python module which allows for the validation of RDF graphs
against Shapes Constraint Language (SHACL) graphs. This module uses the rdflib
Python library for working with RDF and is dependent on the OWL-RL Python
module for OWL2 RL Profile based expansion of data graphs.

%prep
%setup

# Fix the HTTP server entry point
sed -i 's/pyshacl\.http:cli/pyshacl.sh_http:main/' pyproject.toml

# Remove the obsolete Sanic server argument (drop when fixed upstream)
sed -i '/^[[:space:]]*legacy=False,[[:space:]]*$/d' pyshacl/sh_http.py

%build
%pyproject_build

%install
%pyproject_install

%check
# some tests requires internet connection
%pyproject_run_pytest -v \
    --deselect=test/issues/test_154.py::test_154 \
    --deselect=test/test_cmdline.py::test_cmdline_web \
    --deselect=test/test_cmdline.py::test_cmdline_jsonld \
    --deselect=test/test_extra.py::test_web_retrieve \
    --deselect=test/test_extra.py::test_web_retrieve_fail \
    --deselect=test/test_extra.py::test_owl_imports \
    --deselect=test/test_extra.py::test_owl_imports_fail

%files
%doc LICENSE.txt *.md
%_bindir/pyshacl
%_bindir/pyshacl_rules
%_bindir/pyshacl_server
%_bindir/pyshacl_validate
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 07 2026 Evgeniy Serov <scala@altlinux.org> 0.40.1-alt1
- Initial build for Sisyphus.
