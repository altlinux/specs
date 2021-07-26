%define oname unittest2

%def_disable check

Name: python3-module-%oname
Version: 1.1.0
Release: alt4

Summary: Backport of Python 2.7 unittest module
License: Same as Python
Group: Development/Python3
Url: http://pypi.python.org/pypi/unittest2
# hg clone https://hg.python.org/unittest2
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-pytest python3-module-traceback2
BuildPreReq: python-tools-2to3

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
unittest2 is a backport of the new features added to the unittest
testing framework in Python 2.7. It is tested to run on Python 2.4 -
2.7.

%prep
%setup

%build
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.txt
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt4
- Drop python2 support.

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt2.hg20150630.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.1.0-alt2.hg20150630
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.hg20150630
- Version 1.1.0

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.a1.hg20120312
- Version 0.6.0a1

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Wed Sep 29 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.1-alt1
- initial build
