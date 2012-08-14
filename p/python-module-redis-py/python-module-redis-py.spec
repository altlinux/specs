%define module_name redis-py

Name: python-module-%module_name
Version: 2.6.0
Release: alt1
Group: System/Base
License: MIT License
Summary: The Python interface to the Redis key-value store
URL: http://github.com/andymccurdy/redis-py
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
The Python interface to the Redis key-value store

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
%doc CHANGES LICENSE README.md
%python_sitelibdir/redis*

%changelog
* Tue Aug 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.6.0-alt1
- new version

* Sat May 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.13-alt1
- build for ALT
