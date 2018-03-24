%define modname mygpoclient

Name: python-module-%modname
Version: 1.8
Release: alt2

Summary: Python interface to the my.gpodder.org webservices
License: GPLv3+
Group: Development/Python
Url: https://github.com/gpodder/%modname

Source: %url/archive/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: python-devel python-module-setuptools
BuildRequires: python3-devel python3-module-distribute

%description
This Python library provides an easy and structured way to access the
my.gpodder.org web services. In addition to subscription list
synchronization and storage, the advanced API support allows to upload
and download episode status changes.

%package -n python3-module-%modname
Summary: Python3 interface to the my.gpodder.org webservices
Group: Development/Python3

%description -n python3-module-%modname
This Python3 library provides an easy and structured way to access the
my.gpodder.org web services. In addition to subscription list
synchronization and storage, the advanced API support allows to upload
and download episode status changes.


%prep
%setup -n %modname-%version -a0
cp -a %modname-%version py3build

%build
%python_build

pushd py3build
%python3_build
popd

%install
%python_install

pushd py3build
%python3_install
popd

%files
%python_sitelibdir/*

%files -n python3-module-%modname
%_bindir/mygpo-bpsync
%_bindir/mygpo-list-devices
%_bindir/mygpo-simple-client
%python3_sitelibdir/*
%_man1dir/mygpo-bpsync.1.*
%doc AUTHORS README*


%changelog
* Fri Mar 23 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt2
- added python3 subpackage

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- 1.7

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-2.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- first build for Sisyphus

