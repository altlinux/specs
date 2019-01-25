%define _unpackaged_files_terminate_build 1
%define oname importlib_metadata

%def_with check

Name: python-module-%oname
Version: 0.8
Release: alt1
Summary: Library to access the metadata for a Python package
License: ASL2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/importlib-metadata/

# Source-git: https://gitlab.com/python-devs/importlib_metadata
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python-module-configparser
BuildRequires: python-module-contextlib2
BuildRequires: python-module-importlib_resources
BuildRequires: python-modules-json
BuildRequires: python-module-packaging
BuildRequires: python-module-zipp
BuildRequires: python3-module-importlib_resources
BuildRequires: python3-module-packaging
BuildRequires: python3-module-tox
BuildRequires: python3-module-zipp
%endif

# not autodetected
%py_requires pathlib2
%py_requires contextlib2
%py_requires configparser

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

%package -n python3-module-%oname
Summary: Library to access the metadata for a Python package
Group: Development/Python3

%description -n python3-module-%oname
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

rm -rf ../python3
cp -a . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

pushd ../python3
python3 -c "import sys; sys.exit(\"It's time to remove Python3 module because this one is in standard library\" if sys.version_info[0:2] >= (3, 8) else 0)"
%python3_install
popd

for i in tests docs;
do
    [ -d "%buildroot%python3_sitelibdir/%oname/$i" ] && \
    { echo "There should be no packaged $i"; exit 1; }
done

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
%define pynodots py%{python_version_nodots python}
%define py3nodots py%{python_version_nodots python3}
export TOXENV=%pynodots-nocov,%py3nodots-nocov
tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE README.rst
%python_sitelibdir/importlib_metadata-%version-py%_python_version.egg-info/
%python_sitelibdir/importlib_metadata/

%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/importlib_metadata-%version-py%_python3_version.egg-info/
%python3_sitelibdir/importlib_metadata/

%changelog
* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 0.8-alt1
- Initial build.
