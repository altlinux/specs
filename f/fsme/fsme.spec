Name: fsme
Version: 1.0.4
Release: alt3

Summary: Finite State Machine Editor
Group: Development/C++
License: GPL
Packager: Pavel Vainerman <pv@altlinux.ru>

Url: http://fsme.sourceforge.net
Source: %name-%version.tar.bz2
Patch: %name-%version.gcc.patch

# Automatically added by buildreq on Mon Jul 19 2010
BuildRequires: gcc-c++ libcairo-devel qt3-designer

%description
A Finite State Machine Editor, written on QT. 
It allows to draw Finite State Machine with 
easy GUI and store it in XML file. 
There are Finite State Machine Compilers 
to translate this description 
to source code (technique like QT's UIC uses).

%prep
%setup -q 
%patch -p0

export QTDIR=%_libdir/qt3
#export QTINC=%_libdir/qt3/include
#export QTLIB=%_libdir/qt3/lib
$QTDIR/bin/qmake fsme.pro

%build
export QTDIR=%_libdir/qt3
#export QTINC=%_libdir/qt3/include
#export QTLIB=%_libdir/qt3/lib
export PATH=$QTDIR/bin:$PATH
%make

%install
%makeinstall
install -d -p -m755 $RPM_BUILD_ROOT%_bindir
install -p -s -m755 bin/fsme $RPM_BUILD_ROOT%_bindir

%post 

%postun 

%files
%_bindir/*


%changelog
* Mon Jul 19 2010 Pavel Vainerman <pv@altlinux.ru> 1.0.4-alt3
- update BuildRequires

* Wed Nov 05 2008 Pavel Vainerman <pv@altlinux.ru> 1.0.4-alt2
- build for new gcc

* Tue Oct 16 2007 Pavel Vainerman <pv@altlinux.ru> 1.0.4-alt1
- new version

* Mon Jan 01 2007 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt5
- update BuildRequires
- add patch for g++-4.1.x

* Fri Oct 06 2006 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt4
- update buildreq
- make_build --> make

* Mon Dec 12 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt3
- add patch for build for new Sysiphus
- back %make --> %make_build

* Wed Dec 07 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt2
- update BuildRequires
- change %make_build --> %make

* Fri Feb 18 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt1
- first build
