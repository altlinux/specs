%define _unpackaged_files_terminate_build 1
%define pypi_name pdm-pep517
%def_without vendored

%define python_deps() %(for mod in %{*}; do echo -n "python3(${mod}) "; done; )

%if_without vendored
%define vendored_list \\\
boolean \\\
cerberus \\\
license_expression \\\
packaging \\\
tomli \\\
tomli_w \\\
%nil
%endif

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.2
Release: alt1
Summary: A PEP 517 backend for PDM that supports PEP 621 metadata
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pdm-pep517
VCS: https://github.com/pdm-project/pdm-pep517.git
BuildArch: noarch
Source: %name-%version.tar
%if_without vendored
Source1: debundler.py.in
%endif
Patch: %name-%version-alt.patch

# namespace root
%py3_requires pdm
%if_without vendored
# unvendored packages that are not found as deps automatically
%py3_requires cerberus
%py3_requires license-expression
%py3_requires packaging
%py3_requires tomli
%py3_requires tomli_w
%endif

%py3_provides %pypi_name

# self-dependencies
%filter_from_requires /python3(pdm\.pep517\._vendor\..*)/d

%if_with vendored
# self-contained deps
%add_findreq_skiplist %python3_sitelibdir/pdm/pep517/_vendor/*
%add_findprov_skiplist %python3_sitelibdir/pdm/pep517/_vendor/*
%endif

BuildRequires(pre): rpm-build-python3

%if_without vendored
BuildRequires: %python_deps %vendored_list
%endif

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(setuptools)
BuildRequires: python3-devel
BuildRequires: /usr/bin/git
%endif

%description
This is the backend for PDM projects, while you can also use it alone. It reads
the metadata of PEP 621 format and coverts it to Core metadata.

%prep
%setup
%autopatch -p1

%if_without vendored
# check if actual bundled modules list is synced to expected one
set -o pipefail
PYTHONPATH="$(pwd)" %__python3 - <<-'EOF' | sort -u > actual.pkg.list
import pkgutil
for mod in pkgutil.iter_modules(["./pdm/pep517/_vendor"]):
    if not mod.name.startswith("_"):
        print(mod.name)
EOF

echo "%vendored_list" | sed 's/[ ]*$//' | tr ' ' '\n' | sort -u > expected.pkg.list
diff -y expected.pkg.list actual.pkg.list

# unbundle packages
VENDORED_PATH='pdm/pep517/_vendor'
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"pdm.pep517._vendor"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/pdm/pep517/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- 1.1.1 -> 1.1.2.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.6 -> 1.1.1.

* Thu Nov 24 2022 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1
- 1.0.5 -> 1.0.6.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.4 -> 1.0.5.

* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus.
