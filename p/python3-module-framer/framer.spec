%define _unpackaged_files_terminate_build 1
%define oname framer

Name: python3-module-%oname
Version: 0.1.1
Release: alt3

Summary: Network Framer Library
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/framer/
BuildArch: noarch

# https://github.com/klmitch/framer.git
Source: %{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-cobs python3-module-six
BuildRequires: python3-module-mock python3(asyncio)
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires cobs six asyncio


%description
The Framer library is a network communications library, built on top of
asyncio, for managing these units, which it calls frames. The Framer
library is built as an asyncio protocol which also happens to implement
the behavior of an asyncio transport. The protocol object can have
framers set on both directions of the communication; these framers
translate between the stream interface provided by TCP and the sequence
of frames desired by the application.

A framer is simply an object implementing a couple of methods which
implement the transformation from a stream to a frame and from a frame
to a sequence of bytes to transmit on the stream. These framers can
range from rather trivial--as in a text-oriented protocol like SMTP--all
the way to a complex binary data transmission protocol such as some
forms of RPC.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test3 -vv

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt3
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20140531.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140531
- Initial build for Sisyphus

