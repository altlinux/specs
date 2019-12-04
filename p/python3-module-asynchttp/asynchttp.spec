%define oname asynchttp

Name: python3-module-%oname
Version: 0.0.4
Release: alt2

Summary: A simple httplib2 based asynchronous HTTP library for python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/asynchttp/
BuildArch: noarch

# https://github.com/ross/python-asynchttp.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-httplib2 python3-module-coverage
BuildRequires: python3-module-mockito python3-module-nose
BuildRequires: python3-module-unittest2 python3-tools-pep8
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires httplib2


%description
asynchttp is an almost drop in replacement for httplib2 that provides
asynchronous http request behavior.

asynchttp uses python threading and Queues and provides callback
mechanisms to allow de-serialization and process to happen in the
background (worker threads) as well. You can queue up arbitrary numbers
of requests and a specified maximum number of workers will process each
request in turn.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|coverage|coverage3|' ./coverage.sh

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
%__python3 test.py
./coverage.sh

%files
%doc *.rst examples
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.4-alt1.git20120701.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20120701.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20120701
- Initial build for Sisyphus

