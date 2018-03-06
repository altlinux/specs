%define oname check-manifest

%def_with python3

Name: python-module-%oname
Version: 0.36
Release: alt1
Summary: Check MANIFEST.in in a Python source package for completeness
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/check-manifest
BuildArch: noarch

# https://github.com/mgedmin/check-manifest.git
Source: %name-%version.tar

BuildRequires: git-core
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(mock)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(mock)
%endif

%description
Are you a Python developer?
Have you uploaded packages to the Python Package Index?
Have you accidentally uploaded broken packages with some files missing?
If so, check-manifest is for you.

%if_with python3
%package -n python3-module-%oname
Summary: Check MANIFEST.in in a Python source package for completeness
Group: Development/Python3

%description -n python3-module-%oname
Are you a Python developer?
Have you uploaded packages to the Python Package Index?
Have you accidentally uploaded broken packages with some files missing?
If so, check-manifest is for you.
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
%python3_build_install
popd
pushd %buildroot%_bindir
for i in $(ls) ; do
mv $i $i.py3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.36-alt1
- Initial build for ALT.
