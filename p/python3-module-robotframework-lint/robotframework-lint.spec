%define _unpackaged_files_terminate_build 1

%define oname robotframework-lint

Name: python3-module-%oname
Version: 0.7
Release: alt2

Summary: Static analysis tool for robotframework plain text files
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/robotframework-lint
BuildArch: noarch

# https://github.com/boakley/robotframework-lint.git
Source0: https://pypi.python.org/packages/27/bf/9caeefff91e49aab3ed8262172251b623fe529674424c86bf2a1345aa801/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-robotframework
BuildRequires: python-tools-2to3

%py3_provides rflint


%description
Linter for robot framework plain text files.

This is a static analysis tool for robot framework plain text files.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt2
- porting on python3

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

