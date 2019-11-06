%define oname gevent-socketio

Name: python3-module-%oname
Version: 0.3.6
Release: alt4

Summary: SocketIO server based on the Gevent pywsgi server, a Python network library
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/gevent-socketio/
# https://github.com/abourget/gevent-socketio.git
BuildArch: noarch

Source: %name-%version.tar
Patch: fix-django-utils-importlib-since-1.9.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx

BuildRequires: python-tools-2to3
BuildRequires: python3-module-versiontools
BuildRequires: python3-module-sphinx

%py3_provides %oname
%py3_requires gevent-websocket


%description
SocketIO server based on the Gevent pywsgi server, a Python network
library.

%package docs
Summary: Documentation for gevent-socketio
Group: Development/Documentation

%description docs
SocketIO server based on the Gevent pywsgi server, a Python network
library.

This package contains documentation for gevent-socketio.

%package pickles
Summary: Pickles for gevent-socketio
Group: Development/Python

%description pickles
SocketIO server based on the Gevent pywsgi server, a Python network
library.

This package contains pickles for gevent-socketio.

%prep
%setup
%patch -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build

%make -C docs pickle
%make -C docs html

%install
%python3_install

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/socketio/

%files
%doc AUTHORS LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.6-alt4
- disable python2

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.3.6-alt3.git20140202
- Adapt module for a new Django.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.6-alt2.git20140202.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt2.git20140202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt2.git20140202.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt2.git20140202
- New snapshot

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt2.git20130915
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt2.git20130201
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.3.6-alt1.git20130201.1
- Rebuild with Python-3.3

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20130201
- Version 0.3.6

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.beta.git20120514
- Version 0.3.5-beta
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

