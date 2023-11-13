# dpf required
%def_enable snapshot

Name: zam-plugins
Version: 4.2
Release: alt1

Summary: A collection of LV2/LADSPA/JACK audio plugins
Group: Sound
License: GPL-2.0-or-later and ISC
Url: http://www.zamaudio.com/

%if_disabled snapshot
Source: https://github.com/zamaudio/%name/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires: gcc-c++
BuildRequires: libjack-devel liblo-devel
BuildRequires: lv2-devel >= 1.8.1 ladspa_sdk
BuildRequires: libfftw3-devel >= 3.3.5
BuildRequires: libsamplerate-devel
BuildRequires: zita-convolver-devel >= 3.1.0
BuildRequires: libX11-devel libglvnd-devel

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

%package -n vst-zam-plugins
Summary: A collection of LV2/LADSPA/JACK audio plugins. VST* version
Group: Sound

%description -n vst-zam-plugins
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.
This is the VST/VST3 version.

%package -n clap-zam-plugins
Summary: A collection of LV2/LADSPA/JACK audio plugins. CLAP version
Group: Sound

%description -n clap-zam-plugins
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.
This is the CLAP (CLever Audio Plug-in API) version.

%prep
%setup

%build
base_opts=" -ffast-math -fdata-sections -ffunction-sections %(getconf LFS_CFLAGS)"

%ifarch %ix86
base_opts+=" -msse -mfpmath=sse"
%endif

%ifarch x86_64
base_opts+=" -msse2 -mfpmath=sse"
%endif

export HAVE_ZITA_CONVOLVER=true
%define opts PREFIX=%_prefix LIBDIR=%_lib SKIP_STRIPPING=true
%make_build BASE_OPTS="$base_opts" %opts

%install
export HAVE_ZITA_CONVOLVER=true
%makeinstall_std %opts

%files
%_bindir/*
%doc README.md NOTICE.*

%files -n lv2-zam-plugins
%_libdir/lv2/*
%doc README.md NOTICE.*

%files -n ladspa-zam-plugins
%_libdir/ladspa/*
%doc README.md NOTICE.*

%files -n vst-zam-plugins
%_libdir/vst/*
%_libdir/vst3/*
%doc README.md NOTICE.*

%files -n clap-zam-plugins
%_libdir/clap/*
%doc README.md NOTICE.*

%changelog
* Mon Nov 13 2023 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2
- new vst- and clap- subpackages

* Mon Dec 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.14-alt1
- 3.14

* Sun Jul 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.13-alt1
- 3.13

* Mon Dec 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.12-alt1
- 3.12

* Wed Jul 24 2019 Yuri N. Sedunov <aris@altlinux.org> 3.11-alt1
- updated to 3.11-7-gd211bff

* Sun Nov 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt2
- rebuilt against libzita-convolver.so.4

* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1.1
- rebuilt for aarch64

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- first build on Sisyphus (based on fc 3.10-3)

