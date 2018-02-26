%define self ptcpas
Name:		fpc-units-%self
# svn info -r HEAD https://ptcpas.svn.sourceforge.net/svnroot/ptcpas/trunk | grep Revision
Version:	447
Release:	alt2
Group:		Development/Other
License:	Modified LGPL
Summary:	A free, portable framebuffer library, written in Free Pascal
# svn co https://ptcpas.svn.sourceforge.net/svnroot/ptcpas/trunk ptcpas-402
Source:		%self-%version.tar
URL:		http://ptcpas.sourceforge.net/

# Automatically added by buildreq on Mon Sep 06 2010
BuildRequires: fpc-units-gtk2 fpc-utils libX11-devel libXext-devel libXrandr-devel libXxf86dga-devel libXxf86vm-devel

Requires: libX11-devel libXext-devel libXrandr-devel libXxf86dga-devel libXxf86vm-devel
%description
PTCPas is a free, portable framebuffer library, written in Free Pascal.
It allows low-level high-speed graphics access on multiple platforms and
is distributed under the terms of a modified (to allow static linking)
GNU LGPL license. Currently supports DirectX, X11, VBE1.2+ and
fakemodes. It has been tested on Windows (all versions since Windows 95;
on i386 and x86_64), Linux (i386, x86_64 and ppc), FreeBSD and DOS.

%package demos
Group:		Development/Other
Summary:	Demo applications for %name
Requires:	fpc-utils fpc %name
%description demos
%summary

%prep
%setup -n %self-%version
find . -depth -name .svn -exec rm -rf {} \;

for N in core/*; do sed -i 's@/usr/share/ptcpas/ptcpas.conf@%_sysconfdir/%self.conf@' $N; done

%build
# fpc bug
%ifarch x86_64
export FPCDIR=%_libdir/fpc
%endif

./configure

%make_build
%make demos examples

%install
%ifarch %ix86
%define fpcarch i386
%else
%define fpcarch %_arch
%endif
%define unitdir %_libdir/fpc/units/%fpcarch-linux
mkdir -p %buildroot%unitdir/%self
install units/%fpcarch-linux/* %buildroot%unitdir/%self
mkdir -p %buildroot%_libdir/%name-demos
cp -a demos examples %buildroot%_libdir/%name-demos
rm -rf %buildroot%_libdir/%name-demos/*/units
install -D ptcpas.cfg %buildroot%_sysconfdir/%self.conf

%files
%doc docs
%unitdir/%self
%config %_sysconfdir/%self.conf

%files demos
%_libdir/%name-demos

%changelog
* Fri Dec 17 2010 Fr. Br. George <george@altlinux.ru> 447-alt2
- Demos package now depends on build environment

* Fri Dec 17 2010 Fr. Br. George <george@altlinux.ru> 447-alt1
- Bugfix update up to SVN

* Mon Sep 06 2010 Fr. Br. George <george@altlinux.ru> 402-alt1
- Initial build from scratch

