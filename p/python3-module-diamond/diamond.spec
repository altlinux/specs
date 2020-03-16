%define oname diamond
%define _sysconfigdir /etc

Name: python3-module-%oname
Version: 4.0.515
Release: alt2

Summary: Smart data producer for graphite graphing package
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/diamond/

BuildArch: noarch

# https://github.com/python-diamond/Diamond.git
Source: %name-%version.tar
# git://github.com/python-diamond/Diamond.wiki.git
Source1: Diamond.wiki.tar

Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-configobj
BuildRequires: python3-module-mock

%py3_provides %oname


%description
Diamond is a python daemon that collects system metrics and publishes
them to Graphite (and others). It is capable of collecting cpu, memory,
network, i/o, load and disk metrics. Additionally, it features an API
for implementing custom collectors for gathering metrics from almost any
source.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Diamond is a python daemon that collects system metrics and publishes
them to Graphite (and others). It is capable of collecting cpu, memory,
network, i/o, load and disk metrics. Additionally, it features an API
for implementing custom collectors for gathering metrics from almost any
source.

This package contains documentation for %oname.

%prep
%setup
%patch0 -p1

sed -i 's|platform.dist|platform.libc_ver|' setup.py

tar -xf %SOURCE1

%build
%python3_build_debug

%install
%python3_install

install -d %buildroot/var/log/%oname
touch %buildroot/var/log/%oname/.dont_delete

%check
%if 0
%__python3 test.py
%endif

%files
%doc CHANGELOG LICENSE
%_bindir/*
%config %_sysconfdir/*
%python3_sitelibdir/*
# %%_datadir/%oname
%dir /var/log/%oname

%files docs
%doc doc/*


%changelog
* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0.515-alt2
- Detect dist fixed according with python3.8

* Wed Feb 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0.515-alt1
- Version updated to 4.0.515
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.14-alt2.git20150101.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.14-alt2.git20150101
- Set %_sysconfigdir/%oname as config file

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.14-alt1.git20150101
- Initial build for Sisyphus

