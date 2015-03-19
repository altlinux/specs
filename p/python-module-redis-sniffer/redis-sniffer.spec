%define oname redis-sniffer

%def_without python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.git20150318
Summary: A redis sniffing & event logging utility
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/redis-sniffer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eternalprojects/redis-sniffer.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pypcap python-module-dpkt
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pcap
BuildPreReq: python-tools-2to3
%endif

%py_provides redis_sniffer
%py_requires pypcap dpkt

%description
This tool will monitor a specific port and interface for redis traffic
and captures the commands being sent to Redis and/or formatted full TCP
dump data. This can be used for analysis for debugging or for replaying
the transactions as a way of doing real load/performance testing.

Redis Hound must be run locally on a Redis server or a server that is
sending commands to Redis.

%if_with python3
%package -n python3-module-%oname
Summary: A redis sniffing & event logging utility
Group: Development/Python3
%py3_provides redis_sniffer
%py3_requires pypcap

%description -n python3-module-%oname
This tool will monitor a specific port and interface for redis traffic
and captures the commands being sent to Redis and/or formatted full TCP
dump data. This can be used for analysis for debugging or for replaying
the transactions as a way of doing real load/performance testing.

Redis Hound must be run locally on a Redis server or a server that is
sending commands to Redis.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
py.test -vv redis_sniffer/*.py
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv redis_sniffer/*.py
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150318
- Initial build for Sisyphus

