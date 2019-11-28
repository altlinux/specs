%define _unpackaged_files_terminate_build 1
%define oname pies

%def_disable check

Name: python3-module-%oname
Version: 2.6.7
Release: alt4

Summary: The simplest way to write one program that runs on both Python 2 and Python 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pies/
BuildArch: noarch

# https://github.com/timothycrosley/pies.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(enum) python3-module-pytest

%py3_provides %oname


%description
The simplest (and tastiest) way to write one program that runs on both
Python 2 and Python 3.

%prep
%setup -n %oname-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
py.test3

%files
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.6.7-alt4
- python2 disabled

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.7-alt3
- Updated build and runtime dependencies.

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.7-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.3-alt2.git20141225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.3-alt2.git20141225
- cleanup buildreq

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.3-alt1.git20141225
- Version 2.6.3

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1.git20140224
- Initial build for Sisyphus

