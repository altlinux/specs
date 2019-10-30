%define oname gevent-loops

Name: python3-module-%oname
Version: 0.0.2
Release: alt2

Summary: A collection of improved loop classes to use with gevent
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/gevent-loops/
# https://github.com/mattlong/gevent-loops.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-gevent

%py3_provides gevent_loops


%description
This is a collection of custom gevent loop classes meant to override
gevent.core.loop. The original motivation was to prevent a big ugly
stack trace from being printed to stdout whenever a websocket client
disconnects from a Gunicorn server.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
#doc *.md
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt2
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Version 0.0.2

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141114
- Initial build for Sisyphus

