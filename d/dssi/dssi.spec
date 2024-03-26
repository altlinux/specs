Name: dssi
Version: 1.1.1
Release: alt3

Summary: Disposable Soft Synth Interface specification & examples
License: LGPL-2.1
Group: Sound
Url: https://dssi.sourceforge.net

Provides: dssi-examples = %version-%release
Obsoletes: dssi-examples

Source: %name-%version.tar

BuildRequires: gcc-c++ ladspa_sdk
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)

%package devel
Summary: Development stuff for DSSI
Group: Development/C

%description
This package contains simple apps that use DSSI
dssi_osc_update -- simple DSSI OSC test programs
dssi_example_host -- a basic example host implementation
trivial_synth -- a quite useless but fairly clear illustrative synth plugin
less_trivial_synth -- a synth that actually does some basic synthesis

%description devel
This package contents development stuff for DSSI

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README doc/RFC.txt
%_bindir/*
%_libdir/dssi
%_man1dir/*.1*

%files devel
%_includedir/dssi.h
%_libdir/pkgconfig/dssi.pc

%changelog
* Tue Mar 26 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.1-alt3
- rebuilt without qt-based examples

* Tue Jun 29 2021 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt2
- port to Qt5

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1.1
- Rebuild with new version liblo

* Tue Dec 13 2011 Alex Karpov <karpov@altlinux.ru> 1.1.1-alt1
- new version

* Wed Nov 03 2010 Alex Karpov <karpov@altlinux.ru> 1.1.0-alt1
- new version

* Mon Apr 06 2009 Alex Karpov <karpov@altlinux.ru> 1.0.0-alt1
- 1.0.0 release
    + updated build requirements

* Fri Sep 12 2008 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt2.1
- fixed dssi-devel requirements

* Wed Sep 10 2008 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt2
- separated devel stuff

* Tue Dec 12 2006 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt1
- new version

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.4-alt1.1
- Rebuilt with libstdc++.so.6.

* Sat Jul 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- First build for Sisyphus.
