%define oname toredis

%def_disable check

Name: python3-module-%oname
Version: 0.1.2
Release: alt2

Summary: Really simple async Redis client for Tornado
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/toredis/
BuildArch: noarch

# https://github.com/mrjoes/toredis.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pycares python3-module-pytest
BuildRequires: python3-module-zope

%py3_provides %oname
%py3_requires tornado hiredis


%description
This is minimalistic, but feature rich redis client for Tornado built on
top of hiredis protocol parser.

Supports all redis commands, which are auto-generated from the redis
JSON documentation file.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc AUTHORS *.rst examples
%doc *.json gen_commands.py
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt1.git20140515.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20140515.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20140515.1
- NMU: Use buildreq for BR.

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20140515
- Initial build for Sisyphus

