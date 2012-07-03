%define qtdir %_libdir/qt4

Name: dssi
Version: 1.1.1
Release: alt1

Summary: Disposable Soft Synth Interface specification & examples
License: LGPL
Group: Sound
Url: http://%name.sourceforge.net
Packager: Alex Karpov <karpov@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
# Patch: %name-0.4-alt-textrel.patch

# Automatically added by buildreq on Mon Apr 06 2009
BuildRequires: gcc-c++ gcc-fortran glibc-devel-static jackit-devel ladspa_sdk libalsa-devel liblo-devel libqt4-devel libsamplerate-devel libsndfile-devel

%description
This is the Disposable Soft Synth Interface specification.

%package examples
Summary: Simple applications that use %name
Group: Development/C++

%description examples
This package contains simple apps that use lib%name.
dssi_osc_update -- simple DSSI OSC test programs
dssi_example_host -- a basic example host implementation
trivial_synth -- a quite useless but fairly clear illustrative synth plugin
less_trivial_synth -- a synth that actually does some basic synthesis
less_trivial_synth_qt_gui -- a very simple Qt GUI for the above

%package devel
Summary: Development stuff for %name
Group: Development/C++
Requires: %name = %version

%description devel
This package contents development stuff for %name.

%prep
%setup -q
%autoreconf

%build
export QTDIR=%qtdir
%configure
%make_build

%install
%makeinstall 
%make -C examples distclean

%files
%dir %_libdir/%name/
%_bindir/*
%doc README
%doc doc/*
%_mandir/man1/*

%files examples
%_libdir/%name/*
%doc examples

%files devel
%_includedir/*
%_libdir/pkgconfig/*

%changelog
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
