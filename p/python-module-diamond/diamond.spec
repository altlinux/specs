%define oname diamond

%def_disable check

Name: python-module-%oname
Version: 4.0.14
Release: alt2.git20150101.1
Summary: Smart data producer for graphite graphing package
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/diamond/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-diamond/Diamond.git
Source: %name-%version.tar
# git://github.com/python-diamond/Diamond.wiki.git
Source1: Diamond.wiki.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-configobj python-module-psutil
BuildPreReq: python-module-mock
BuildPreReq: python-module-sphinx-devel /proc

%py_provides %oname

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

%description docs
Diamond is a python daemon that collects system metrics and publishes
them to Graphite (and others). It is capable of collecting cpu, memory,
network, i/o, load and disk metrics. Additionally, it features an API
for implementing custom collectors for gathering metrics from almost any
source.

This package contains documentation for %oname.

%prep
%setup

tar -xf %SOURCE1

%build
%python_build_debug

%install
%python_install

#install -d %buildroot%_initdir
#install -p -m755 bin/init.d/diamond %buildroot%_initdir/
install -d %buildroot/var/log/%oname
touch %buildroot/var/log/%oname/.dont_delete

%check
python test.py

%files
%doc CHANGELOG *.md
%_bindir/*
%config %_sysconfdir/*
#_initdir/*
%python_sitelibdir/*
%_datadir/%oname
%dir /var/log/%oname

%files docs
%doc doc/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.14-alt2.git20150101.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.14-alt2.git20150101
- Set %_sysconfigdir/%oname as config file

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.14-alt1.git20150101
- Initial build for Sisyphus

