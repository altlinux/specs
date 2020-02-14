%define _unpackaged_files_terminate_build 1
%define oname importlib_metadata

%def_with check

Name: python3-module-%oname
Version: 1.5.0
Release: alt1
Summary: Library to access the metadata for a Python package
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/importlib-metadata/

# Source-git: https://gitlab.com/python-devs/importlib_metadata
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(packaging)
BuildRequires: python3(pyfakefs)
BuildRequires: python3(tox)
BuildRequires: python3(zipp)
%endif

%description
%oname is a library which provides an API for accessing an installed package's
metadata, such as its entry points or its top-level name. This functionality
intends to replace most uses of pkg_resources entry point API and metadata API.
Along with importlib.resources in Python 3.7 and newer (backported as
importlib_resources for older versions of Python), this can eliminate the need
to use the older and less efficient pkg_resources package.

%oname is a backport of Python 3.8's standard library importlib.metadata module
for Python 2.7, and 3.4 through 3.7. Users of Python 3.8 and beyond are
encouraged to use the standard library module, and in fact for these versions,
importlib_metadata just shadows that module. Developers looking for detailed
API descriptions should refer to the Python 3.8 standard library documentation.

%prep
%setup
%patch -p1
# currently disable PEP517/518
rm -f pyproject.toml

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
python3 -c "import sys; sys.exit(\"It's time to remove Python3 module because this one is in standard library\" if sys.version_info[0:2] >= (3, 8) else 0)"
%python3_install

for i in tests docs;
do
    [ -d "%buildroot%python3_sitelibdir/%oname/$i" ] && \
    { echo "There should be no packaged $i"; exit 1; }
done

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vv

%files
%doc LICENSE README.rst
%python3_sitelibdir/importlib_metadata-%version-py%_python3_version.egg-info/
%python3_sitelibdir/importlib_metadata/

%changelog
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
