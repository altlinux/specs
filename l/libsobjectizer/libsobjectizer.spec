Name: libsobjectizer
Version: 5.5.21
Release: alt1

Summary: SObjectizer is an in-process message dispatching framework with implementation of Actor Model (C++)

License: BSD-3-CLAUSE
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
mkdir -p %buildroot%_docdir/%name
cp LICENSE %buildroot%_docdir/%name/
cp README %buildroot%_docdir/%name/
cp THANKS %buildroot%_docdir/%name/

cd dev/
%makeinstall_std

%if %_lib == lib64
    mv %buildroot/usr/lib %buildroot%_libdir
%endif

rm -r %buildroot%_libdir/*.a
ln -s libso.%version.so %buildroot%_libdir/libso.so

%files
%_libdir/*so.*
%_docdir/%name/

%files devel
%_includedir/so_5/
%_libdir/*.so

%changelog
* Thu Feb 08 2018 Pavel Vainerman <pv@altlinux.ru> 5.5.21-alt1
- new version (5.5.21) with rpmgs script

* Sat Dec 09 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.20-alt1
- new version (5.5.20) with rpmgs script

* Thu Nov 02 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.19-alt5
- new version (5.5.19) with rpmgs script

* Wed Nov 01 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.19-alt4.2
- test build (beta2)

* Mon Oct 30 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.19-alt4.1
- test build (beta1)

* Sun Oct 29 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.19-alt4
- update license information 

* Sun Oct 29 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.19-alt3
- update license information

* Tue Oct 24 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.19-alt2
- added link for so-file

* Wed Jun 14 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.19-alt1
- new version (5.5.19) with rpmgs script

* Wed Feb 22 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.18-alt0.2
- update build requires

* Wed Feb 22 2017 Pavel Vainerman <pv@altlinux.ru> 5.5.18-alt0.1
- initial commit 
