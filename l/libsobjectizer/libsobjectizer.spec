Name: libsobjectizer
Version: 5.5.18
Release: alt0.2

Summary: SObjectizer is an in-process message dispatching framework with implementation of Actor Model (C++)

License: GPL
Group: Development/C++
Url: https://sourceforge.net/projects/sobjectizer/

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://sourceforge.net/projects/sobjectizer/files/latest/download
Source: %name-%version.tar


BuildPreReq: rpm-macros-cmake

# Automatically added by buildreq on Wed Feb 22 2017
# optimized out: cmake-modules libstdc++-devel python-base python-modules python3 python3-base
BuildRequires: cmake gcc-c++

%description
SObjectizer is an in-process message dispatching framework with 
implementation of Actor Model, Publish-Subscribe Model and CSP-like channels.

%package devel
Group: Development/C++
Summary: SObjectizer is an in-process message dispatching framework with implementation of Actor Model (C++)

%description devel
SObjectizer is an in-process message dispatching framework with 
implementation of Actor Model, Publish-Subscribe Model and CSP-like channels.

%prep
%setup

%build
cd dev
%cmake_insource
%make_build

%install
cd dev/
%makeinstall_std

%if %_lib == lib64
    mv %buildroot/usr/lib %buildroot%_libdir
%endif

rm -r %buildroot%_libdir/*.a

%files
%_libdir/*.so

%files devel
%dir %_includedir/so_5
%_includedir/*

%changelog
* Wed Feb 22 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.18-alt0.2
- update build requires

* Wed Feb 22 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.18-alt0.1
- initial commit 
