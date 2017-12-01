%define _unpackaged_files_terminate_build 1

%def_with python3

%define oname pycodestyle

Name: python-module-%oname
Version: 2.3.1
Release: alt1
Summary: Python style guide checker
Group: Development/Python
License: Expat
BuildArch: noarch
URL: https://pypi.python.org/pypi/pycodestyle

# https://github.com/PyCQA/pycodestyle.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-pytest-runner
%if_with python3
BuildRequires: python3-module-setuptools rpm-build-python3
BuildRequires: python3-module-pytest-runner
%endif

%description
pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.

%if_with python3
%package -n python3-module-%oname
Summary: Python style guide checker
Group: Development/Python3

%description -n python3-module-%oname
pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc README.rst LICENSE CONTRIBUTING.rst CHANGES.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE CONTRIBUTING.rst CHANGES.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Initial build for ALT.
