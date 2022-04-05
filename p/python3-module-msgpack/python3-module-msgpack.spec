%define oname msgpack

Name: python3-module-%oname
Version: 1.0.3
Release: alt1

Summary: A Python 3 MessagePack (de)serializer

Group: Development/Python3
License: ASL 2.0
URL: https://pypi.org/project/msgpack/

# Source-url: https://pypi.io/packages/source/m/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++

BuildRequires: rpm-build-python3
BuildRequires: python3-module-Cython

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%files
%doc COPYING
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Tue Sep 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)
- build python3 package

* Fri Mar 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version (0.6.1) with rpmgs script
- package name on PyPI was changed to msgpack from 0.5
- drop extra buildreqs

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.6-alt1
- new version 0.5.6 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.8-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.8-alt1
- move to build from tarball
- new version 0.4.8 (with rpmrb script)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6-alt1.git20150323.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1.git20150323.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20150323
- Version 0.4.6

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.git20150126
- Version 0.4.5

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140326
- Version 0.4.2

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.2.2-alt1.1
- Rebuild with Python-3.3

* Thu Dec 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.2-alt1
- New version

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.12-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.12-alt1
- initial
