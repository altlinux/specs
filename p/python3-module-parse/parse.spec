%define _unpackaged_files_terminate_build 1
%define oname parse

%def_with check

Name: python3-module-%oname
Version: 1.19.0
Release: alt1
Summary: parse() is the opposite of format()
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/parse/

# https://github.com/r1chardj0n3s/parse.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
%endif

%description
Parse strings using a specification based on the Python format() syntax.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.19.0-alt1
- 1.8.2 -> 1.19.0.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt1
- Updated to upstream version 1.8.2.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.6-alt2
- Fixed tests.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.6-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1.git20141117
- Initial build for Sisyphus

