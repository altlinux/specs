%define _unpackaged_files_terminate_build 1
%define oname importlib_resources

%def_with check

Name: python-module-%oname
Version: 1.0.2
Release: alt1
Summary: Library which provides for access to resources in Python packages
License: ASL2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/importlib_resources/

# Source-git: https://gitlab.com/python-devs/importlib_resources
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-wheel
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python-module-pathlib2
BuildRequires: python-module-typing
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
%endif

# Python3 file
%add_findreq_skiplist %python_sitelibdir/importlib_resources/_py3.py
%add_findprov_skiplist %python_sitelibdir/importlib_resources/_py3.py

%py_requires typing

%description
%oname is a library which provides for access to resources in Python packages.
It provides functionality similar to pkg_resources Basic Resource Access API,
but without all of the overhead and performance problems of pkg_resources.

In our terminology, a resource is a file that is located within an importable
Python package. Resources can live on the file system, in a zip file, or in
any place that has a loader supporting the appropriate API for reading
resources. Directories are not resources.

importlib_resources is a backport of Python 3.7's standard library
importlib.resources module for Python 2.7, and 3.4 through 3.6. Users of
Python 3.7 and beyond are encouraged to use the standard library module, and in
fact for these versions, importlib_resources just shadows that module.
Developers looking for detailed API descriptions should refer to the Python 3.7
standard library documentation.

%package -n python3-module-%oname
Summary: Library which provides for access to resources in Python packages
Group: Development/Python3

# Python2 file
%add_findreq_skiplist %python3_sitelibdir/importlib_resources/_py2.py
%add_findprov_skiplist %python3_sitelibdir/importlib_resources/_py2.py

# typing is in standard library
%add_python3_req_skip typing.io

%description -n python3-module-%oname
%oname is a library which provides for access to resources in Python packages.
It provides functionality similar to pkg_resources Basic Resource Access API,
but without all of the overhead and performance problems of pkg_resources.

In our terminology, a resource is a file that is located within an importable
Python package. Resources can live on the file system, in a zip file, or in
any place that has a loader supporting the appropriate API for reading
resources. Directories are not resources.

importlib_resources is a backport of Python 3.7's standard library
importlib.resources module for Python 2.7, and 3.4 through 3.6. Users of
Python 3.7 and beyond are encouraged to use the standard library module, and in
fact for these versions, importlib_resources just shadows that module.
Developers looking for detailed API descriptions should refer to the Python 3.7
standard library documentation.

%prep
%setup
%patch -p1
# currently disable PEP517/518
rm -f pyproject.toml

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
python3 -c "import sys; sys.exit(\"It's time to remove Python3 module because this one is in standard library\" if sys.version_info[0:2] >= (3, 7) else 0)"
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

for i in tests docs;
do
    [ -d "%buildroot%python3_sitelibdir/%oname/$i" ] && \
    { echo "There should be no packaged $i"; exit 1; }
done

%check
export PIP_NO_INDEX=YES
%define pynodots py%{python_version_nodots python}
%define py3nodots py%{python_version_nodots python3}
export TOXENV=%pynodots-nocov,%py3nodots-nocov
tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE README.rst
%python_sitelibdir/importlib_resources-%version-py%_python_version.egg-info/
%python_sitelibdir/importlib_resources/

%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/importlib_resources-%version-py%_python3_version.egg-info/
%python3_sitelibdir/importlib_resources/

%changelog
* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- Initial build.
