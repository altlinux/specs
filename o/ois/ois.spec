Name:           ois
Version:        1.3.0
Release:        alt2
Summary:        Open Input System, OO gaming input library
Group:          System/Libraries
License:        zlib
URL:            http://sourceforge.net/projects/wgois
Packager: 	Alexey Shentzev <ashen@altlinux.ru>
Source0:        %name-%version.tar
# Automatically added by buildreq on Wed Jun 17 2009
BuildRequires: gcc-c++ glibc-devel-static libXaw-devel

%description
Object Oriented Input System (OIS) is meant to be a cross platform, simple
solution for using all kinds of Input Devices (KeyBoards, Mice, Joysticks, etc)
and feedback devices (e.g. forcefeedback). Written in C++ using Object Oriented
Design patterns.

%package -n	lib%name
Summary:        Open Input System, OO gaming input library
Group:          System/Libraries
Provides:	ois

%description -n lib%name
Object Oriented Input System (OIS) is meant to be a cross platform, simple
solution for using all kinds of Input Devices (KeyBoards, Mice, Joysticks, etc)
and feedback devices (e.g. forcefeedback). Written in C++ using Object Oriented
Design patterns.

%package -n 	lib%name-devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, lib%name = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q -n %name

%build
sh bootstrap
export LIBS=-lX11
%configure --disable-static
%make_build


%install
%makeinstall_std

%files -n lib%name
%doc ReadMe.txt
%_libdir/libOIS-%version.so

%files -n lib%name-devel
%_libdir/libOIS.so
%_includedir/OIS
%_libdir/pkgconfig/OIS.pc

%changelog
* Sat May 26 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt2
- Fix DSO linking

* Thu Jan 13 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1
- New version

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Thu Jun 18 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.2.0-alt3
- Update spec

* Thu Jun 18 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.2.0-alt2
- Update spec

* Wed Jun 17 2009 Alexey Shentzev <ashen@altlinux.ru> 1.2.0-alt1.1
- first build for ALT Linux

