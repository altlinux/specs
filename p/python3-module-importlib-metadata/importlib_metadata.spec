%define _unpackaged_files_terminate_build 1
%define oname importlib-metadata

%def_with check

Name: python3-module-%oname
Version: 4.11.3
Release: alt1
Summary: Library to access the metadata for a Python package
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/importlib-metadata/

# Source-git: https://github.com/python/importlib_metadata.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires:
BuildRequires: python3(zipp)

BuildRequires: python3(pyfakefs)
BuildRequires: python3(test)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

# PyPI name(dash, underscore)
%py3_provides %oname
Provides: python3-module-importlib_metadata = %EVR
Obsoletes: python3-module-importlib_metadata <= 1.5.0-alt1

%description
Library to access the metadata for a Python package.

This package supplies third-party access to the functionality of
importlib.metadata including improvements added to subsequent Python versions.

New features are introduced in this third-party library and later merged into
CPython.

%prep
%setup
%patch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

# setup.py less project, PEP517 builds are not supported in sisyphus for now
cat > setup.py <<'EOF'
import setuptools

if __name__ == "__main__":
    setuptools.setup()
EOF
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false -- \
    --ignore exercises.py

%files
%doc LICENSE README.rst
%python3_sitelibdir/importlib_metadata-%version-py%_python3_version.egg-info/
%python3_sitelibdir/importlib_metadata/

%changelog
* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 4.11.3-alt1
- 4.11.2 -> 4.11.3.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 4.11.2-alt1
- 4.11.1 -> 4.11.2.

* Tue Feb 22 2022 Stanislav Levin <slev@altlinux.org> 4.11.1-alt1
- 4.10.1 -> 4.11.1.

* Wed Jan 19 2022 Stanislav Levin <slev@altlinux.org> 4.10.1-alt1
- 4.8.1 -> 4.10.1.

* Tue Nov 23 2021 Stanislav Levin <slev@altlinux.org> 4.8.1-alt2
- Obsoleted importlib_metadata (closes: #41400).

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 4.8.1-alt1
- 4.6.1 -> 4.8.1.

* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 4.6.1-alt1
- 1.5.0 -> 4.6.1 (restored for features from Python 3.10).

* Wed Feb 12 2020 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.3.0 -> 1.5.0.
- Moved Python3 subpackage to its own package.

* Mon Dec 16 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 0.23 -> 1.3.0.

* Fri Sep 27 2019 Stanislav Levin <slev@altlinux.org> 0.23-alt1
- 0.19 -> 0.23.

* Tue Aug 13 2019 Stanislav Levin <slev@altlinux.org> 0.19-alt1
- 0.17 -> 0.19.

* Wed Jun 05 2019 Stanislav Levin <slev@altlinux.org> 0.17-alt1
- 0.11 -> 0.17.

* Tue May 14 2019 Stanislav Levin <slev@altlinux.org> 0.11-alt1
- 0.9 -> 0.11.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 0.9-alt1
- 0.8 -> 0.9.
- Fixed testing.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 0.8-alt1
- Initial build.
