%define subver 0

Name: goom
Version: 2k4
Release: alt5

Summary: A neat sound visualization program
License: GPL
Group: Sound

Url: http://goom.sourceforge.net
Source: %name-%version-%subver-src.tar.gz
Patch0: goom2k4-0-as-needed.patch
Patch1: goom2k4-0-acin.patch
Patch2: goom2k4-0-alt-makefile.patch
Patch3: goom2k4-0-alt-gdk.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon May 25 2009
BuildRequires: flex libSDL-devel libxmms-devel

%description
Standalone Goom 2k4 visualization eye-candy

TAB - Enter/Leave Fullscreen
Numpad +/- - Change resolution
F1-F8 - Set Background FX
F - Display Frame Rate
Q - Quit

%package -n xmms-vis-%name
Summary: A neat visual plugin for XMMS
Group: Sound

%description -n xmms-vis-%name
Very nice vis plugin for XMMS!

TAB - Enter/Leave Fullscreen
Numpad +/- - Change resolution
F1-F8 - Set Background FX
F - Display Frame Rate
Q - Quit

%package -n lib%name
Summary: Goom library
Group: System/Libraries

%description -n lib%name
Shared library needed for Goom visualization

%package -n lib%name-devel
Summary: Goom library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for Goom visualization

%prep
%setup -n %name%version-%subver
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall xmms_libdir=%buildroot%xmms_visualizationdir

%files
%_bindir/*

%files -n xmms-vis-%name
%xmms_visualizationdir/*

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS ChangeLog README

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name/
%_pkgconfigdir/*

# TODO:
# - enable MMX on x86*
# - enable PPC on ppc

%changelog
* Wed May 30 2012 Michael Shigorin <mike@altlinux.org> 2k4-alt5
- fixed FTBFS with binutils-2.22

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 2k4-alt4.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 2k4-alt4
- fixed build with recent coreutils
- buildreq

* Sun Feb 15 2009 Michael Shigorin <mike@altlinux.org> 2k4-alt3
- presumably fixed build on ppc (thx sbolshakov@)
  + patch0 rewritten too

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 2k4-alt2
- applied repocop patch
- added Packager:
- minor spec cleanup
- buildreq

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 2k4-alt1
- Fixed build (linking with -lm).

* Tue Jan 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 2k4-alt0.3
- NMU.
- Removed ExclusiveArch.

* Sun Dec 11 2005 Michael Shigorin <mike@altlinux.org> 2k4-alt0.2
- 2k4-rc2
- removed gcc3 patch
- split package into a whole bunch following upstream

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 1.99.4-alt1
- built for ALT Linux (how did we miss out on THIS??)

