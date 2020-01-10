%define oname tcpwatch

Name: python3-module-%oname
Version: 1.3.1
Release: alt2

Summary: TCP monitoring and logging tool with support for HTTP 1.1
License: ZPLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/tcpwatch/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-modules-tkinter

%py3_provides %oname


%description
TCPWatch is a utility written in Python that lets you monitor forwarded
TCP connections or HTTP proxy connections. It displays the sessions in a
window with a history of past connections. It is useful for developing
and debugging protocol implementations and web services.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Jan 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

