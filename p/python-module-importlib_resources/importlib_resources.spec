%define _unpackaged_files_terminate_build 1
%define oname importlib_resources

%def_with check

Name: python-module-%oname
Version: 1.0.2
Release: alt2
Summary: Library which provides for access to resources in Python packages
License: ASL2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/importlib_resources/

# Source-git: https://gitlab.com/python-devs/importlib_resources
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: python2.7(wheel)

%if_with check
BuildRequires: python2.7(pathlib2)
BuildRequires: python2.7(tox)
BuildRequires: python2.7(typing)
%endif

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

%prep
%setup
%patch -p1
# currently disable PEP517/518
rm -f pyproject.toml

# Python3 module causes errors in Python2
rm -f importlib_resources/_py3.py

%build
%python_build

%install
%python_install

for i in tests docs;
do
    [ -d "%buildroot%python3_sitelibdir/%oname/$i" ] && \
    { echo "There should be no packaged $i"; exit 1; }
done

%check
export PIP_NO_INDEX=YES
%define pynodots py%{python_version_nodots python}
export TOXENV=%pynodots-nocov
tox --sitepackages -p auto -o -v

%files
%doc LICENSE README.rst
%python_sitelibdir/importlib_resources-%version-py%_python_version.egg-info/
%python_sitelibdir/importlib_resources/

%changelog
* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2
- Dropped Python3 package (closes: #36645).

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- Initial build.
