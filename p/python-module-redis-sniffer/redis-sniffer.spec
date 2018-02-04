%define oname redis-sniffer

%def_without python3

Name: python-module-%oname
Version: 1.1.0
Release: alt3.git20150318.1
Summary: A redis sniffing & event logging utility
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/redis-sniffer/

# https://github.com/eternalprojects/redis-sniffer.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pcap python-module-dpkt
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pcap
BuildRequires: python-tools-2to3
%endif

%py_provides redis_sniffer
%py_requires pcap dpkt

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
%py3_requires pcap

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt3.git20150318.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt3.git20150318
- Fixed build.

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.git20150318
- Fixed build

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150318
- Initial build for Sisyphus

