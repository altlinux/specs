Name: fsmc
Version: 1.0.4
Release: alt3.1

Summary: Finite State Machine Compiler
Group: Development/C++
License: GPL
Packager: Pavel Vainerman <pv@altlinux.ru>

Url: http://fsme.sourceforge.net
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Mon Jul 19 2010
BuildRequires: gcc-c++ libqt3-devel

%description
Finite State Machine Compiler

%prep
%setup -q 
export QTDIR=%_libdir/qt3
$QTDIR/bin/qmake fsmc.pro

%build
export QTDIR=%_libdir/qt3
export PATH=$QTDIR/bin:$PATH
%make

%install
%makeinstall
install -d -p -m755 $RPM_BUILD_ROOT%_bindir
install -p -s -m755 fsmc $RPM_BUILD_ROOT%_bindir
install -p -s -m755 pyfsmc $RPM_BUILD_ROOT%_bindir
install -p -m755 mkfsm $RPM_BUILD_ROOT%_bindir

%files
%_bindir/*


%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.4-alt3.1
- Rebuild with Python-2.7

* Mon Jul 19 2010 Pavel Vainerman <pv@altlinux.ru> 1.0.4-alt3
- update BuildRequires

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt2.1
- Rebuilt with python 2.6

* Wed Apr 23 2008 Pavel Vainerman <pv@altlinux.ru> 1.0.4-alt2
- spec fixed 

* Tue Oct 16 2007 Pavel Vainerman <pv@altlinux.ru> 1.0.4-alt1
- new version

* Mon Jan 01 2007 Pavel Vainerman <pv@altlinux.ru> 1.0.1-alt4
- update for g++-4.1
- update BuildRequires

* Wed Dec 07 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.1-alt3
- update BuildRequires

* Sun Feb 20 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.1-alt2
- change make_build --> make

* Fri Feb 18 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.1-alt1
- first build


