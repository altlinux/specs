%def_with bootstrap

%define oname lxml

Name: python3-module-lxml
Version: 4.9.2
Release: alt1

Summary: Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API

License: BSD-3-Clause AND GPL-2.0-or-later
Group: Development/Python3
URL: https://pypi.org/project/lxml

# https://github.com/lxml/lxml
Source: %name-%version.tar

%if_without bootstrap
# Used for tests only, but depends on lxml itself,
# which is not yet built in a bootstrap environment.
BuildRequires: python3-module-cssselect
# needed for: from lxml.cssselect import CSSSelector
Requires: python3-module-cssselect
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: libxslt-devel zlib-devel
# see doc/build.txt
BuildRequires: python3-module-Cython >= 0.18

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.
It provides safe and convenient access to these libraries using the ElementTree API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

%package doc
Summary: Documentation for lxml
Group: Development/Documentation
BuildArch: noarch

%description doc
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

This package contains documentation for lxml.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
# see Makefile
sed -i 's|/usr/bin/env python.*|/usr/bin/env python3|' \
	update-error-constants.py test.py
sed -i 's|/usr/bin/python|/usr/bin/python3|' \
	doc/rest2latex.py doc/rest2html.py
%python3_build --with-cython

%install
%python3_install

%check
export LC_ALL=en_US.UTF-8
# see Makefile
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;
cp -l build/lib.linux-*/lxml/*.so src/lxml/
python3 test.py -p -v
PYTHONPATH=src python3 src/lxml/tests/selftest.py
PYTHONPATH=src python3 src/lxml/tests/selftest2.py

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%files doc
%doc doc samples

%changelog
* Tue Jan 17 2023 Grigory Ustinov <grenka@altlinux.org> 4.9.2-alt1
- Automatically updated to 4.9.2.
- Bootstrap for python3.11.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 4.9.1-alt1
- Automatically updated to 4.9.1.

* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 4.9.0-alt1
- Automatically updated to 4.9.0.

* Thu Mar 17 2022 Grigory Ustinov <grenka@altlinux.org> 4.8.0-alt1
- Automatically updated to 4.8.0.

* Sat Feb 05 2022 Grigory Ustinov <grenka@altlinux.org> 4.7.1-alt1
- Build new version.
- Disable bootstrap.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 4.6.4-alt2
- Bootstrap for python3.10.

* Tue Nov 23 2021 Grigory Ustinov <grenka@altlinux.org> 4.6.4-alt1
- Build new version.

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 4.6.3.0.16.git5ecb40bc-alt1
- Fixed FTBFS.

* Mon Mar 22 2021 Grigory Ustinov <grenka@altlinux.org> 4.6.3-alt1
- Build new version.

* Tue Mar 02 2021 Grigory Ustinov <grenka@altlinux.org> 4.6.2-alt1
- Build new version.
- Disable bootstrap.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 4.6.1-alt3
- Bootstrap for python3.9.

* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 4.6.1-alt2
- restore missed cssselect requires

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 4.6.1-alt1
- new version 4.6.1 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt3
- build python3 package separately, cleanup spec

* Wed Apr 29 2020 Stanislav Levin <slev@altlinux.org> 4.5.0-alt2
- Fixed FTBFS.

* Tue Mar 17 2020 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Build new version
- Disable bootstrap knob.

* Wed Jan 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.4.2-alt2
- Bootstrap for python3.8.

* Mon Dec 09 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.2-alt1
- Build new version
- Fix license

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.1-alt1
- Build new version
- Disable bootstrap knob.

* Wed Apr 03 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.3-alt1.1
- Bootstrap for python3.7.

* Wed Mar 27 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.3-alt1
- Build new version

* Mon Mar 04 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1
- Build new version

* Mon Feb 11 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt1
- Build new version

* Sun Jan 06 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt1
- Build new version

* Tue Dec 25 2018 Grigory Ustinov <grenka@altlinux.org> 4.2.5-alt1
- Build new version

* Tue Mar 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt1
- Updated to upstream version 4.2.1.

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- build new version

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- build new version

* Fri Apr 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt2.beta1.git20150727
- (.spec) Described the actually necessary simplification for %%if_with bootstrap
  (namely: make it skip some tests employing cssselect which depends on lxml itself).

* Tue Apr 12 2016 Denis Medvedev <nbr@altlinux.org> 3.5.0-alt1.beta1.git20150727.3
- NMU: added documentation back.

* Wed Mar 23 2016 Denis Medvedev <nbr@altlinux.org> 3.5.0-alt1.beta1.git20150727.2
- NMU: temporarily removed documentation for python3.5 cycle removal.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.5.0-alt1.beta1.git20150727.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.beta1.git20150727
- Version 3.5.0.beta1

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.dev.git20150417
- Version 3.5.dev

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.git20141226
- New snapshot

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.git20141120
- Version 3.4.1

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.5-alt1.git20140418
- Version 3.3.5

* Sat Mar 30 2013 Aleksey Avdeev <solo@altlinux.ru> 3.1.1-alt1.git20130330
- Version 3.1.1 (d7ea8fd4bb60e8e0799b1cb4a3ef0f79da8f3530)

* Thu Mar 28 2013 Aleksey Avdeev <solo@altlinux.ru> 3.1.0-alt1
- Version 3.1.0

* Sun Mar 17 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.6-alt1
- Version 2.3.6

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt2
- Added module for Python 3

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.8-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt2
- Added zlib-devel into BuildPreReq
- Rebuilt for debuginfo

* Tue Nov 30 2010 Ivan Fedorov <ns@altlinux.org> 2.2.8-alt1
- Version 2.2.8

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt1
- Version 2.2.7
- Added docs

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- cleanup spec
- new version 2.2.4 (with rpmrb script)

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.1-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-lxml
  * postclean-05-filetriggers for spec file

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Rebuilt with python 2.6

* Wed Jul 30 2008 Ivan Fedorov <ns@altlinux.org> 2.1.1-alt1
- 2.1.1

* Wed May 28 2008 Ivan Fedorov <ns@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Apr 09 2008 Ivan Fedorov <ns@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt1
- initial build for ALT Linux Sisyphus
