%define oname monetdb

%def_with python3
%def_without check

Name: pymonetdb
Epoch: 1
Version: 1.1.1
Release: alt1.1

Summary: MonetDB is an open source column-oriented database management system
License: Mozilla Public License 2.0
Group: Databases
BuildArch: noarch
URL: http://monetdb.org

Source: %name-%version.tar

BuildRequires: monetdb
BuildRequires: python-devel python-module-setuptools python-module-pytest-runner
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pytest-runner
%endif

%description
MonetDB is an open source column-oriented database management system. It was
designed to provide high performance on complex queries against large databases,
e.g. combining tables with hundreds of columns and multi-million rows.

%package -n python-module-%oname
Summary: MonetDB python interface
Group: Development/Python
BuildArch: noarch

%description -n python-module-%oname
%summary

%if_with python3
%package -n python3-module-%oname
Summary: MonetDB python interface
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%oname
%summary
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files -n python-module-%oname
%doc README.rst
%python_sitelibdir/%name
%python_sitelibdir/%name-%version-py*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-py*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.1-alt1
- Initial build for ALT.
