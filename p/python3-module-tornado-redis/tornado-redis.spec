%define oname tornado-redis

Name: python3-module-%oname
Version: 2.4.18
Release: alt3

Summary: Asynchronous Redis client that works within Tornado IO loop
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/tornado-redis/
BuildArch: noarch

# https://github.com/leporo/tornado-redis.git
Source: %name-%version.tar
Patch0: fix-filter-py3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-tornado

%py3_provides tornadoredis


%description
Asynchronous Redis client for the Tornado Web Server.

This is a fork of brukva redis client modified to be used via Tornado's
native 'tornado.gen' interface instead of 'adisp' call dispatcher.

%prep
%setup
%patch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py build_ext -i
%__python3 runtests.py

%files
%doc *.md demos
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.4.18-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.18-alt2.git20141002.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.18-alt2.git20141002
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.18-alt1.git20141002.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.18-alt1.git20141002
- Initial build for Sisyphus

