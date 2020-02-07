%define _unpackaged_files_terminate_build 1

%define oname glob2

Name: python3-module-%oname
Version: 0.7
Release: alt1

Summary: Extended version of Python's builtin glob module
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/glob2/
BuildArch: noarch

# https://github.com/miracle2k/python-glob2.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%py3_provides %oname


%description
Version of the glob module that can capture patterns and supports
recursive wildcards.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3

%files
%doc CHANGES *.rst PKG-INFO
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt1
- Version updated to 0.7
- build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140122
- Initial build for Sisyphus

