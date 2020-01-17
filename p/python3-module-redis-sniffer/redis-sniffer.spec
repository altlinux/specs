%define oname redis-sniffer

Name: python3-module-%oname
Version: 1.1.0
Release: alt4

Summary: A redis sniffing & event logging utility
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/redis-sniffer/
BuildArch: noarch

# https://github.com/eternalprojects/redis-sniffer.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pcap python3-module-dpkt
BuildRequires: python-tools-2to3

%py3_provides redis_sniffer
%py3_requires pcap dpkt


%description
This tool will monitor a specific port and interface for redis traffic
and captures the commands being sent to Redis and/or formatted full TCP
dump data. This can be used for analysis for debugging or for replaying
the transactions as a way of doing real load/performance testing.

Redis Hound must be run locally on a Redis server or a server that is
sending commands to Redis.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt4
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt3.git20150318.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt3.git20150318
- Fixed build.

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.git20150318
- Fixed build

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150318
- Initial build for Sisyphus

