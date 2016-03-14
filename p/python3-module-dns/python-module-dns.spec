%define modulename dns

# Testing requires network access
%def_without check

Name: python3-module-%modulename
Version: 1.12.0
Release: alt1.git20150613.1.1

Summary: DNS toolkit (Python 3)
License: BSD-like
Group: Development/Python
Url: http://www.dnspython.org

BuildArch: noarch

# http://www.dnspython.org/kits/%version/dnspython-%version.tar
# git://github.com/rthalley/dnspython.git
Source: %name-%version.tar

#BuildPreReq: rpm-build-python3
#BuildPreReq: python3-module-distribute
#BuildPreReq: python-module-epydoc

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-module-PyStemmer python-module-Pygments python-module-cssselect python-module-docutils python-module-pytz python-module-setuptools python-module-snowballstemmer python-modules python-modules-compiler python-modules-email python-modules-encodings python3 python3-base
BuildRequires: python-module-epydoc python-module-html5lib rpm-build-python3 time

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.

%prep
%setup
rm -f examples/._*

%build
%python3_build
%make_build doc

%install
%python3_install

%if_with check
%check
pushd tests
%make PYTHONPATH="../:$PYTHONPATH" check
popd
%endif

%files
%doc examples/ html/ ChangeLog LICENSE
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.12.0-alt1.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.12.0-alt1.git20150613.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.git20150613
- Version 1.12.0

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.1-alt1.git20140411
- New snapshot

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.1-alt1.git20130902
- Version 1.11.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt2
- Version 1.10.0 (py3)
- Build for Python-3
- Rename package to python3-module-dns

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt2
- Version 1.10.0
- Obsoletes python-module-dnspython (ALT #28727)

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.2-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1
- Version 1.9.2

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- cleanup spec
- new version (1.8.0) import in git

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt1.1
- Rebuilt with python-2.5.

* Mon Oct 03 2005 Andrey Orlov <cray@altlinux.ru> 1.3.4-alt1
- initial release

