%define _unpackaged_files_terminate_build 1
%define oname nose-detecthttp

%def_disable check

Name: python3-module-%oname
Version: 1.1.0
Release: alt1

Summary: A nose plugin to detect tests making http calls
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/nose-detecthttp

# https://github.com/venmo/nose-detecthttp.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-vcrpy

%py3_provides detecthttp


%description
A nose plugin that can detect tests making external http calls.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt1
- Version updated to 1.1.0
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1
- Updated to upstream version 0.2.0.
- Disabled check phase due to no tests being present.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.dev.git20141124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.dev.git20141124
- Initial build for Sisyphus

