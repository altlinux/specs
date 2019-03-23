%define _unpackaged_files_terminate_build 1
%define oname pycodestyle

%def_with check

Name: python-module-%oname
Version: 2.5.0
Release: alt1
Summary: Python style guide checker
Group: Development/Python
License: Expat
BuildArch: noarch
Url: https://pypi.org/project/pycodestyle/

# https://github.com/PyCQA/pycodestyle.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(json)
BuildRequires: python3(tox)
%endif

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8.

%package -n python3-module-%oname
Summary: Python style guide checker
Group: Development/Python3

%description -n python3-module-%oname
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8.

%prep
%setup

cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc README.rst LICENSE CONTRIBUTING.rst CHANGES.txt
%_bindir/pycodestyle
%python_sitelibdir/pycodestyle.py*
%python_sitelibdir/pycodestyle-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc README.rst LICENSE CONTRIBUTING.rst CHANGES.txt
%_bindir/pycodestyle.py3
%python3_sitelibdir/pycodestyle.py
%python3_sitelibdir/__pycache__/pycodestyle.cpython-*
%python3_sitelibdir/pycodestyle-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Fri Oct 26 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Initial build for ALT.
