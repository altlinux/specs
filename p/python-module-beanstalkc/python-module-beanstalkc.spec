%define module_name beanstalkc

Name: python-module-%module_name
Version: 0.2.0
Release: alt1
Group: System/Base
License: Apache License
Summary: beanstalkc is a simple beanstalkd client library for Python
URL: https://github.com/earl/beanstalkc.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
beanstalkc is a simple beanstalkd client library for Python. [beanstalkd][1] is
a fast, distributed, in-memory workqueue service

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc LICENSE README TUTORIAL
%python_sitelibdir/beanstalkc*

%changelog
* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.0-alt1
- build for ALT
