%def_enable snapshot

Name: zam-plugins
Version: 3.10
Release: alt1.1

Summary: A collection of LV2/LADSPA/JACK audio plugins
Group: Sound
License: GPLv2+ and ISC
Url: http://www.zamaudio.com/

%if_disabled snapshot
Source: https://github.com/zamaudio/%name/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

# https://github.com/zamaudio/zam-plugins/pull/62
Patch: %name-unbundle-zita-convolver.patch
Patch1: dpf-generate-ttl.sh.patch

BuildRequires: gcc-c++
BuildRequires: libjack-devel liblo-devel
BuildRequires: lv2-devel >= 1.8.1 ladspa_sdk
BuildRequires: libfftw3-devel >= 3.3.5
BuildRequires: libsamplerate-devel
BuildRequires: zita-convolver-devel >= 3.1.0
BuildRequires: libX11-devel libGL-devel

%description
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.

%package -n lv2-zam-plugins
Summary: A collection of LV2/LADSPA/JACK audio plugins. LV2 version
Group: Sound
Requires: lv2 >= 1.8.1

%description -n lv2-zam-plugins
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.
This is the LV2 version.

%package -n ladspa-zam-plugins
Summary: A collection of LV2/LADSPA/JACK audio plugins. LADSPA version
Group: Sound
Requires: ladspa_sdk

%description -n ladspa-zam-plugins
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.
This is the LADSPA version.

%prep
%setup
%patch -p1 -b .unbundle-zita
%patch1 -b "~"

%build
%add_optflags %optflags_fastmath

%ifarch %ix86
%add_optflags -msse -mfpmath=sse
%endif

%ifarch x86_64
%add_optflags -msse2 -mfpmath=sse
%endif

%define opts PREFIX=%prefix LIBDIR=%_lib USE_SYSTEM_LIBS=1

%make_build %opts BASE_OPTS="%optflags"

%install
%makeinstall_std %opts

# remove VST and DSSI plugins
rm -rf %buildroot%_libdir/vst %buildroot/*-dssi*

%files
%_bindir/*
%doc README.md

%files -n lv2-zam-plugins
%_libdir/lv2/*
%doc README.md

%files -n ladspa-zam-plugins
%_libdir/ladspa/*
%doc README.md

%changelog
* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1.1
- rebuilt for aarch64

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- first build on Sisyphus (based on fc 3.10-3)

