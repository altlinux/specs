%define _unpackaged_files_terminate_build 1
%define oname xmlschema

%def_with check

Name: python-module-%oname
Version: 1.0.13
Release: alt1

Summary: XML Schema validator and data conversion library
License: MIT
Group: Development/Python
# Source-git: https://github.com/sissaschool/xmlschema
Url: https://pypi.org/project/xmlschema/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(elementpath)
BuildRequires: python2.7(lxml)
BuildRequires: python2.7(pathlib2)
BuildRequires: python3(elementpath)
BuildRequires: python3(lxml)

%if_with check
BuildRequires: /proc
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
The xmlschema library is an implementation of XML Schema for Python.

%package -n python3-module-%oname
Summary: XML Schema validator and data conversion library
Group: Development/Python3

%description -n python3-module-%oname
The xmlschema library is an implementation of XML Schema for Python.

%prep
%setup
sed -i \
-e 's/elementpath~=/elementpath>=/g' \
-e '/memory_profiler/d' \
tox.ini setup.py
cp -a . ../python3

%build
export LANG=C.UTF-8
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
install -m 0644 ./xmlschema/unicode_categories.json \
%buildroot%python_sitelibdir/xmlschema/unicode_categories.json

pushd ../python3
%python3_install
install -m 0644 ./xmlschema/unicode_categories.json \
%buildroot%python3_sitelibdir/xmlschema/unicode_categories.json
popd

# don't ship tests
rm -r %buildroot{%python_sitelibdir,%python3_sitelibdir}/%oname/tests

%check
# since builds for Py2 and Py3 differ from each other
# we shouldn't run tests from Py2 dir as usual
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}
tox.py3 --sitepackages -vr -- -v

pushd ../python3
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vr -- -v
popd

%files
%doc LICENSE README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Sat Aug 17 2019 Stanislav Levin <slev@altlinux.org> 1.0.13-alt1
- Initial build.

