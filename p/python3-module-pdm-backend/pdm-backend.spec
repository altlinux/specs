%define _unpackaged_files_terminate_build 1
%define pypi_name pdm-backend
%def_without vendored

%define python_deps() %(for mod in %{*}; do echo -n "python3(${mod}) "; done; )

%if_without vendored
%define vendored_list \\\
packaging \\\
tomli \\\
tomli_w \\\
validate_pyproject \\\
pyproject_metadata \\\
%nil
%endif

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.5
Release: alt1
Summary: The build backend used by PDM that supports latest packaging standards
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pdm-backend/
VCS: https://github.com/pdm-project/pdm-backend
BuildArch: noarch
Source: %name-%version.tar
%if_without vendored
Source1: debundler.py.in
%endif
Patch: %name-%version-alt.patch

# namespace root
%py3_requires pdm
%if_without vendored
%py3_requires %%vendored_list
%endif

%py3_provides %pypi_name

# self-dependencies
%filter_from_requires /python3(pdm\.backend\._vendor\..*)/d

%if_with vendored
# self-contained deps
%add_findreq_skiplist %python3_sitelibdir/pdm/backend/_vendor/*
%add_findprov_skiplist %python3_sitelibdir/pdm/backend/_vendor/*
%endif

BuildRequires(pre): rpm-build-python3

%if_without vendored
BuildRequires: %python_deps %vendored_list
%endif

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(setuptools)
BuildRequires: python3(editables)
BuildRequires: python3-devel
BuildRequires: /usr/bin/git
%endif

%description
This is the backend for PDM projects that is fully-compatible with PEP 517 spec,
but you can also use it alone. It reads the metadata of PEP 621 format and
coverts it to Core metadata.

%prep
%setup
%autopatch -p1

%if_without vendored
# check if actual bundled modules list is synced to expected one
set -o pipefail
PYTHONPATH="$(pwd)" %__python3 - <<-'EOF' | sort -u > actual.pkg.list
import pkgutil
for mod in pkgutil.iter_modules(["./src/pdm/backend/_vendor"]):
    if not mod.name.startswith("_"):
        print(mod.name)
EOF

echo "%vendored_list" | sed 's/[ ]*$//' | tr ' ' '\n' | sort -u > expected.pkg.list
diff -y expected.pkg.list actual.pkg.list

# unbundle packages
VENDORED_PATH='src/pdm/backend/_vendor'
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"pdm.backend._vendor"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"
%endif

# for pdm scm version
# https://pdm.fming.dev/latest/pyproject/build/#dynamic-version-from-scm
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/pdm/backend/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 28 2023 Stanislav Levin <slev@altlinux.org> 2.0.5-alt1
- 2.0.3 -> 2.0.5.

* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 2.0.3-alt1
- 2.0.2 -> 2.0.3.

* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.1.2 -> 2.0.2.

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
