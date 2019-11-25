%define oname ultra_rest_client

Name: python3-module-%oname
Version: 0.1.4
Release: alt2

Summary: A sample Python client for communicating with the UltraDNS REST API
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/ultra_rest_client
# https://github.com/ultradns/python_rest_api_client.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-requests

%py3_provides %oname
%py3_requires requests


%description
The sample code does not attempt to implement a client for all available
UltraDNS REST API functionality. It provides access to basic
functionality. Adding additional functionality should be relatively
straightforward, and any contributions from the UltraDNS community would
be greatly appreciated. See sample.py for an example of how to use this
library in your own code.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.md *.txt sample.py
%python3_sitelibdir/*


%changelog
* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt1.git20150515.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150515.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150515
- Initial build for Sisyphus

