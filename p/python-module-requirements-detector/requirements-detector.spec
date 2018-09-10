%define _unpackaged_files_terminate_build 1
%define oname requirements-detector

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt1
Summary: Python tool to find and list requirements of a Python project
License: MIT
Group: Development/Python
Url: https://pypi.org/project/requirements-detector/
BuildArch: noarch

# https://github.com/landscapeio/requirements-detector.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-astroid python-module-nose
BuildRequires: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-astroid python3-module-nose
BuildRequires: python3-module-coverage
%endif

%py_provides requirements_detector
%py_requires astroid

%description
requirements-detector is a simple Python tool which attempts to find and
list the requirements of a Python project.

When run from the root of a Python project, it will try to ascertain
which libraries and the versions of those libraries that the project
depends on.

%if_with python3
%package -n python3-module-%oname
Summary: Python tool to find and list requirements of a Python project
Group: Development/Python3
%py3_provides requirements_detector
%py3_requires astroid

%description -n python3-module-%oname
requirements-detector is a simple Python tool which attempts to find and
list the requirements of a Python project.

When run from the root of a Python project, it will try to ascertain
which libraries and the versions of those libraries that the project
depends on.
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

%check
export LC_ALL=en_US.UTF-8
python setup.py test
nosetests -v -s --with-coverage \
	--cover-package requirements_detector \
	--cover-inclusive
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v -s --with-coverage \
	--cover-package requirements_detector \
	--cover-inclusive
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6-alt1
- Updated to upstream version 0.6.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1
- automated PyPI update

* Wed Mar 16 2016 Denis Medvedev <nbr@altlinux.org> 0.4.1-alt2.git20160316
- typo in summary fixed.

* Wed Mar 16 2016 Denis Medvedev <nbr@altlinux.org> 0.4.1-alt1.git20160316
- Merged upstream version 0.4.1.

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150323
- Initial build for Sisyphus

