%define _unpackaged_files_terminate_build 1
%define oname robotframework-lint

%def_without python3

Name: python-module-%oname
Version: 0.7
Release: alt1.1
Summary: Static analysis tool for robotframework plain text files
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-lint
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boakley/robotframework-lint.git
Source0: https://pypi.python.org/packages/27/bf/9caeefff91e49aab3ed8262172251b623fe529674424c86bf2a1345aa801/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-robotframework
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-robotframework
BuildPreReq: python-tools-2to3
%endif

%py_provides rflint

%description
Linter for robot framework plain text files.

This is a static analysis tool for robot framework plain text files.

%if_with python3
%package -n python3-module-%oname
Summary: Static analysis tool for robotframework plain text files
Group: Development/Python3
%py3_provides rflint

%description -n python3-module-%oname
Linter for robot framework plain text files.

This is a static analysis tool for robot framework plain text files.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%python3_build_debug
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150205
- Version 0.5

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141222
- Version 0.4

* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141130
- New snapshot

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141125
- Initial build for Sisyphus

