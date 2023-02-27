%define oname codepy

%def_with check

Name: python3-module-%oname
Version: 2019.1
Release: alt1

Summary: C metaprogramming toolkit for Python
License: MIT
Group: Development/Python3
Url: https://documen.tician.de/codepy/

VCS: https://github.com/inducer/codepy

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytools
BuildRequires: gcc-c++
BuildRequires: python3-module-appdirs
%endif

Requires: gcc-c++
Requires: python3-module-appdirs

%description
CodePy is a C metaprogramming toolkit for Python. It handles two aspects
of metaprogramming:

* Generating C source code.

* Compiling this source code and dynamically loading it into the Python
interpreter.

Both capabilities are meant to be used together, but also work on their
own. In particular, the code generation facilities work well in
conjunction with PyCuda. Dynamic compilation and linking are so far only
supported in Linux with the GNU toolchain.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test-3

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info


%changelog
* Mon Feb 27 2023 Anton Vyatkin <toni@altlinux.org> 2019.1-alt1
- new version 2019.1

* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 2013.1.2-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2013.1.2-alt1.git20140620.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.1.2-alt1.git20140620.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.1.2-alt1.git20140620.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1.git20140620
- New snapshot

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1.git20131126
- New snapshot

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1.git20130718
- Version 2013.1.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1.git20130314
- Version 2013.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2012.1.2-alt1.git20120607.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1.2-alt1.git20120607
- New snapshot

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1.2-alt1.git20120424
- Version 2012.1.2
- Added module for Python 3

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20111010
- Initial build for Sisyphus

