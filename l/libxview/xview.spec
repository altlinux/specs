%def_disable static
%define origname xview
%define rel %nil
#define rel -18c

Name: lib%origname
Version: 3.2p1.4
Release: alt7.qa1

Summary: XView libraries for X11
License: Distributable
Url: http://step.polymtl.ca/~coyote/xview_main.html
# http://physionet.caregroup.harvard.edu/physiotools/xview/
Group: System/Libraries
Packager: Igor Vlasenko <viy@altlinux.ru>

#Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/X/xview/xview-3.2p1.4.src.tar.gz
Source0: %{origname}_%version.orig.tar.gz
# Gentoo
#Source0: %{origname}-%version%rel.tar.gz
# debian
Patch0: %{origname}_%version-23.diff.gz
Patch1: %{origname}_%version-alt-xorg7.patch
Patch2: xview_3.2p1.4-alt-gcc41.patch

# gentoo patches; are mainly included in debian patch;
# not applied (we use debian)
Patch3: CAN-2005-0076.patch
Patch4: lseek.diff
Patch5: xview-3.2-gcc-4.1-v0.1.patch.bz2

Provides: %origname = %version

# Automatically added by buildreq on Tue Jul 22 2008 (-bi)
BuildRequires: gccmakedep imake libXext-devel xorg-cf-files libX11-devel

#imake
#set_gcc_version 3.3

%description
XView provides a set of pre-built, user-interface objects such as
canvases, scrollbars, menus, and control panels. The appearance and
functionality of these objects follow the OPEN LOOK Graphical User
Interface (GUI) specification.

This is the Sun implementation of the OpenLook interface standard,
using the xview libraries. While somewhat outdated and superseded by
Motif, or gtk, it is still very useful, especially in providing
compatibility with older installations.

It is possible that the openwin desktop takes up much less disk space
to install and memory to run than modern desktops, which would make it
a good candidate for old hardware.

%package devel
Summary: Header files for XView development
Group: Development/C
Requires: %name = %version

%description devel
All the files needed to develop applications that, using the XView
libraries, meet the OpenLook interface specifications.

%if_enabled static
%package devel-static
Summary: Static libraries for XView development
Group: Development/C
Requires: %name = %version

%description devel-static
Static libraries for XView development
%endif

%prep
%setup -q -n %origname-%version%rel

%patch0 -p1
%patch1 -p0
%patch2 -p1

# gentoo patches
#%patch3 -p0
#%patch4 -p0
#%patch5 -p1

# gentoo
# Do not build xgettext and msgfmt since they are provided by the gettext
# package. Using the programs provided by xview breaks many packages
# including vim, grep and binutils.
sed -e 's/MSG_UTIL = xgettext msgfmt/#MSG_UTIL = xgettext msgfmt/' \
	-i util/Imakefile

# gentoo (#120910) Look for imake in the right place
#sed -i -e 's:\/X11::g' imake 
#sed -i -e 's:/usr/X11R6:/usr:' config/XView.cf Build-LinuxXView.bash

#Patch6: xview-3.2-alt-glibc28.patch
subst s,__linux__,__old_linux__,g lib/libxview/file_chooser/file_list.c

%build
%__rm -f make
# Create the makefile
export IMAKEINCLUDE="-I"`pwd`"/config -I%_datadir/X11/config"
cd config
imake -DUseInstalled 
cd ..
xmkmf -a
%__make \
	CC=%__cc \
	CCOPTIONS="%optflags"

#export OPENWINHOME="/usr"
#export X11DIR="/usr"
#bash Build-LinuxXView.bash libs 
#bash Build-LinuxXView.bash clients 
#bash Build-LinuxXView.bash contrib
#bash Build-LinuxXView.bash olvwm

%install
%__install -d %buildroot{%_libdir,%_man7dir,%_includedir}

for name in olgx xview; do
	%__cp lib/lib$name/lib$name.a %buildroot%_libdir
	%__cp -d lib/lib$name/lib$name.so.* %buildroot%_libdir
done

%__install xview.man %buildroot%_mandir/man7/xview.7

for dir in olgx olgx_private xview xview_private pixrect; do
	%__cp -aL build/include/$dir %buildroot%_includedir
done

ln -sf libolgx.so.3.2.4 %buildroot%_libdir/libolgx.so.3
ln -sf libxview.so.3.2.4 %buildroot%_libdir/libxview.so.3

ln -sf libolgx.so.3.2.4 %buildroot%_libdir/libolgx.so
ln -sf libxview.so.3.2.4 %buildroot%_libdir/libxview.so

%files
%_libdir/libolgx.so.*
%_libdir/libxview.so.*

%files devel
%doc contrib/examples/
%_libdir/libolgx.so
%_libdir/libxview.so
%_man7dir/xview.7.*
%_includedir/olgx
%_includedir/olgx_private
%_includedir/pixrect
%_includedir/xview
%_includedir/xview_private

%if_enabled static
%files lib%origname-devel-static
%_libdir/libolgx.a
%_libdir/libxview.a
%else 
%exclude %_libdir/libolgx.a
%exclude %_libdir/libxview.a
%endif

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 3.2p1.4-alt7.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Dec 15 2008 Igor Vlasenko <viy@altlinux.ru> 3.2p1.4-alt7
- fixed build with new glibc

* Tue Jul 22 2008 Igor Vlasenko <viy@altlinux.ru> 3.2p1.4-alt6
- fixed repocop warnings

* Tue Oct 24 2006 Igor Vlasenko <viy@altlinux.ru> 3.2p1.4-alt5
- gcc41 build fix (added patch)

* Fri Jun 02 2006 Igor Vlasenko <viy@altlinux.ru> 3.2p1.4-alt4
- resynced with Debian -21.1

* Sun Jan 29 2006 Igor Vlasenko <viy@altlinux.ru> 3.2p1.4-alt3
- rebuild with gcc3.4.4 (compact 3.0)

* Mon Nov 21 2005 Igor Vlasenko <viy@altlinux.ru> 3.2p1.4-alt2.1
- picked up from orphaned; 
- resynced with Debian
- CAN-2005-0076 patch and ansi patch are now in debian patch

* Sat Jan 22 2005 Michael Shigorin <mike@altlinux.ru> 3.2p1.4-alt2
- CAN-2005-0076: multiple buffer overflows;
  added patch by Dmitry V. Levin (ldv@)
- doesn't build with gcc3.4 (OK with 3.2/3.3) => unsupported

* Sat Aug 16 2003 Michael Shigorin <mike@altlinux.ru> 3.2p1.4-alt1
- built for ALT Linux
- these PLD people worked on it:
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  ankry, blues, filon, kloczek, marcus, qboosh, waszi
- original package (Mandrake) by:
  Chmouel Boudjnah <chmouel@mandrakesoft.com>
  Quôc-Viêt Hà <viet@mandrakesoft.com>
