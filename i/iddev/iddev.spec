#-*-rpm-spec-*-

%define cvs_date 20050330
%define flavour std26-up

Name: iddev
Version: 0.0.cvs%{cvs_date}
Release: alt1
License: GPL
Group: System/Libraries
Summary: iddev is a library that identifies device contents.
Url: http://sources.redhat.com/cluster

Packager: Pavel Mironchik <tibor@altlinux.ru>


Source0: %{name}-%{cvs_date}.tar.bz2

%description
iddev is a library that identifies device contents.  It will
tell you what file system (or logical volume manager) has
formatted the device.  This package contains the shared libraries.

%package devel
Group: System/Libraries
Summary: iddev is a library that identifies device contents.

%description devel
iddev is a library that identifies device contents.  It will
tell you what file system (or logical volume manager) has
formatted the device.  This package contains the static
libraries and header files.

%prep
%setup -q -n %name

%build
./configure --libdir=%{_libdir} --incdir=%{_includedir}
make

%install
make install DESTDIR=%buildroot


%files

%files devel
%{_libdir}/libiddev.a
%{_includedir}/iddev.h

%changelog
* Wed Mar 30 2005 Pavel Mironchik <tibor@altlinux.ru> 0.0.cvs20050330-alt1
- updated from cvs

* Wed Mar 16 2005 Pavel Mironchik <tibor@altlinux.ru> 0.0.cvs20050316-alt1
- updated from cvs

* Tue Mar 01 2005 Pavel Mironchik <tibor@altlinux.ru> 0.0.cvs20050301-alt1
- updated from cvs

* Tue Feb 22 2005 Pavel Mironchik <tibor@altlinux.ru> 0.0.cvs20050222-alt1
- updated from cvs

* Mon Feb 14 2005 Pavel Mironchik <tibor@altlinux.ru> 0.0.cvs20050214-alt1
- updated from cvs

* Tue Feb 08 2005 Pavel Mironchik <tibor@altlinux.ru> 0.0.cvs20050208-alt1
- updated from cvs

* Fri Feb 04 2005 Pavel Mironchik <tibor@altlinux.ru> 0-alt20050204
- updated from cvs

* Tue Feb 01 2005 Pavel Mironchik <tibor@altlinux.ru> 0-alt20050201
- updated from cvs

* Thu Jan 27 2005 Pavel Mironchik <tibor@altlinux.ru> 0-alt20050127
- updated from cvs

* Thu Jan 20 2005 Pavel Mironchik <tibor@altlinux.ru> 0-alt20050120
- updated from cvs

* Wed Jan 19 2005 Pavel Mironchik <tibor@altlinux.ru> 0-alt20050119
- updated from cvs

* Mon Jan 17 2005 Pavel Mironchik <tibor@altlinux.ru> 0-alt20050117
- updated from cvs

* Mon Jan 10 2005 Pavel Mironchik <tibor@altlinux.ru> 0-alt20050110
- updated from cvs

* Wed Jan  5 2005 Pavel S. Mironchik <tibor@altlinux.ru> 0-alt20050107
- initial build


