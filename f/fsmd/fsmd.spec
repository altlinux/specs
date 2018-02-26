Name: fsmd
Version: 0.5
Release: alt4

Summary: Finite State Machine Debugger
Group: Development/C++
License: GPL
Packager: Pavel Vainerman <pv@altlinux.ru>

Url: http://fsme.sourceforge.net
Source: %name-%version.tar.bz2
Patch: %name-%version.patch

# Automatically added by buildreq on Mon Jul 19 2010
BuildRequires: gcc-c++ qt3-designer

%description
Finite State Machine Debugger

%prep
%setup -q -n %name
%patch -p0
export QTDIR=%_libdir/qt3
$QTDIR/bin/qmake fsmd.pro

%build
export QTDIR=%_libdir/qt3
export PATH=$QTDIR/bin:$PATH
%make_build


%install
%makeinstall
install -d -p -m755 $RPM_BUILD_ROOT%_bindir
install -p -s -m755 bin/fsmd $RPM_BUILD_ROOT%_bindir

%files
%_bindir/*


%changelog
* Mon Jul 19 2010 Pavel Vainerman <pv@altlinux.ru> 0.5-alt4
- update BuildRequires

* Mon Jan 01 2007 Pavel Vainerman <pv@altlinux.ru> 0.5-alt3
- update for g++-4.1
- update BuildRequires

* Wed Dec 07 2005 Pavel Vainerman <pv@altlinux.ru> 0.5-alt2
- update BuildRequires

* Fri Feb 18 2005 Pavel Vainerman <pv@altlinux.ru> 0.5-alt1
- first build


