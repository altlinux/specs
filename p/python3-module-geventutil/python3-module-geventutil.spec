%define _unpackaged_files_terminate_build 1
%define modulename geventutil

Name: python3-module-geventutil
Version: 0.0.1
Release: alt2.hg20120114

Summary: Random utilities for gevent

Group: Development/Python3

License: MIT
Url: https://bitbucket.org/denis/gevent-playground/overview
# hg clone https://bitbucket.org/denis/gevent-playground

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python-tools-2to3
BuildRequires: time
BuildArch: noarch

%description
Random utilities for gevent.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Thu Jan 16 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.0.1-alt2.hg20120114
- NMU: remove python2 module build
- Cleanup spec

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.1-alt1.hg20120114.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.hg20120114.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.hg20120114.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.hg20120114
- Snapshot from mercurial
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus
