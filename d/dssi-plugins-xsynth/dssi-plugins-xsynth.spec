%define _name xsynth
%define beta %nil

Name: dssi-plugins-%_name
Version: 0.9.0
Release: alt2%beta

Summary: Xsynth plugin for DSSI
License: GPL
Group: Sound
Url: http://dssi.sourceforge.net/
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source:http://prdownloads.sourceforge.net/dssi/%_name-dssi-%version%beta.tar.gz

%define dssi_ver 0.9.1
%define ladspa_ver 1.12-alt2

PreReq: ladspa_sdk >= %ladspa_ver
PreReq: dssi >= %dssi_ver

BuildPreReq: dssi >= %dssi_ver  
BuildPreReq: ladspa_sdk >= %ladspa_ver  

# Automatically added by buildreq on Tue Sep 16 2008
BuildRequires: dssi-devel glibc-devel-static ladspa_sdk libalsa-devel libgtk+2-devel liblo-devel

%description
Xsynth-DSSI is a classic-analog (VCOs-VCF-VCA) style software
synthesizer which operates as a plugin for the Disposable Soft Synth
Interface (DSSI).

%define _dssi_path %_libdir/dssi

%prep
%setup -q -n %_name-dssi-%version%beta

%build
%configure
%make_build

%install
%makeinstall

# remove none-packaged files
%__rm -f %buildroot%_dssi_path/*.la

%files
%_bindir/*
%_dssi_path/*.so
%_datadir/%_name-dssi
%doc AUTHORS ChangeLog README TODO

%changelog
* Tue Sep 16 2008 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt2
- updated build requirements

* Tue Dec 12 2006 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt1
- new version 

* Thu Sep 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.0-alt1
- First build for Sisyphus.
