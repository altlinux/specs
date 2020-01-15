%define oname nose_ittr

Name: python3-module-%oname
Version: 0.0.4
Release: alt2

Summary: nose extension for supporting parametrized testing
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/nose_ittr
BuildArch: noarch

# https://github.com/taykey/nose-ittr.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-nose

%py3_provides %oname


%description
Allows developer to run the same test over and over again using
different values.

Main Features:

* Very easy to integrate with existing tests
* Saves a lot of boilerplate code, and code replication
* Work with all nose plugins (including multiprocessing)

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.txt *.rst
%python3_sitelibdir/*


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.0.4-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.4-alt1.git20141202.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141202
- Version 0.0.4

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141127
- Version 0.0.3

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141127
- Version 0.0.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141126
- Initial build for Sisyphus

