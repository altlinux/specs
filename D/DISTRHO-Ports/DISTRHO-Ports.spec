
%global _unpackaged_files_terminate_build 1
%global _optlevel 3
%global optflags_optimization -O3

%ifarch loongarch64
%global optflags_optimization -Ofast -mlsx -mlasx -flax-vector-conversions
%endif

%global distrho LV2 port by DISTRHO

Name:    DISTRHO-Ports
Version: 20210315
Release: alt0.2.gitd3b62da2

Summary: Linux audio plugins and LV2 ports by DISTRHO
License: GPL-2.0+ AND GPL-3.0+ AND LGPL-2.0+ AND MIT AND Apache-2.0
Group:   Sound
Url:     https://distrho.sourceforge.io/ports.php
Vcs:     https://github.com/DISTRHO/DISTRHO-Ports.git

# Exclude i586 just because I can
ExcludeArch: %ix86

Source: %name-snapshot.tar
Patch:  %name-%version-%release.patch

Source1: sub-merge.sources.txt
Source2: sub-merge.unpack.sh

# Import sub-merge sources right here
%(cat %SOURCE1)


BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: ccache

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%ifarch loongarch64 riscv64
BuildRequires: simde-devel
%endif

%description
%summary.


%package -n lv2-arctican-plugins
Summary: Arctican Plugins -- %distrho
Group: Sound

%description -n lv2-arctican-plugins
%distrho of open-source audio plugins from Arctican:
* The Function -- stereo signal manipulation;
* The Pilgrim -- a highpass & lowpass filter programmed into one dial,
  MIDI controllable.


%package -n lv2-dRowAudio-plugins
Summary: dRowAudio plugins -- %distrho
Group: Sound

%description -n lv2-dRowAudio-plugins
%distrho of audio plugins from dRowAudio, including:
* Distortion
* DistortionShaper
* Flanger
* Reverb
* Tremolo


%package -n lv2-EasySSP-plugin
Summary: Audio visualization tool -- %distrho
Group: Sound

%description -n lv2-EasySSP-plugin
%distrho of EasySSP (Easy Sound Space Perception)
-- small and lightweight audio visualization tool, which provides
spectrometer and goniometer views.


%package -n lv2-LUFSMeter-plugin
Summary: Loudness meter plugin -- %distrho
Group: Sound

%description -n lv2-LUFSMeter-plugin
%distrho of the LUFS Meter plugin by Klangfreund.
Compliant with EBU R 128, ATSC A/85 and more.

See https://www.klangfreund.com/lufsmeter/ for more info.

%package -n lv2-luftikus-plugin
Summary: An analog modeled equalizer -- %distrho
Group: Sound

%description -n lv2-luftikus-plugin
%distrho of Luftikus plugin from lkjb.

Luftikus is a digital adaptation of an analog EQ with fixed half-octave
bands and additional high frequency boost. As an improvement to the hardware
it allows deeper cuts and supports a keep-gain mode where overall gain
changes are avoided.


%package -n lv2-PitchedDelay-plugin
Summary: A pitch-shifting delay -- %distrho
Group: Sound

%description -n lv2-PitchedDelay-plugin
%distrho of PitchedDelay plugin from lkjb.

PitchedDelay is a delay that allows the pitching the delayed signal.
This can be done within or outside the feedback loop.

Besides the pitch shifting it has feedback, a basic filter in the
feedback path for signal manipulation and mono, stereo and ping-pong
mode per delay.


%package -n lv2-ReFine-plugin
Summary: ReFine audio plugin -- %distrho
Group: Sound

%description -n lv2-ReFine-plugin
%distrho of ReFine plugin from lkjb.

ReFine is a plugin that allows to add a final polishing to your
tracks, busses and masters. It extracts psycho-acoustic parameters
from the source and thus allows to add warmth, space and punch to
your mixes. This is done level dependent and rather subtle; you
probably won't be able to create heavy distortion effects with this
plugin.


%package -n lv2-Roth-Air-plugin
Summary:  Roth-Air audio plugin -- %distrho
Group: Sound

%description -n lv2-Roth-Air-plugin
%distrho of Roth-Air plugin from Daniel Rothmann.

Roth-Air is a mixing tool for easily adding airy, crispy presence
to your audio. This is achieved by a combination of multiband
compression and gentle saturation of the highs. It enables for a
stronger, more consistent presence of high frequency material and
works particularly well with vocals, synths and strings. The process
is made easy by a simple user interface, automatic makeup gain and a
combined function "AIR" knob.


%package -n lv2-StereoSourceSeparation-plugin
Summary: Stereo Source Separator -- %distrho
Group: Sound

%description -n lv2-StereoSourceSeparation-plugin
%distrho of Stereo Source Separator --
a plugin that uses the spatial information hidden in the stereo
signal to accomplish source separation.


%package -n lv2-SwankyAmp-plugin
Summary: A tube amplifier simulation plugin -- %distrho
Group: Sound

%description -n lv2-SwankyAmp-plugin
%distrho of Swanky Amp -- a tube amplifier simulation
DSP plugin which aims to capture the details in the dynamics of
tube amplifiers.


%package -n lv2-TAL-plugins
Summary: Togu Audio Line Plugins -- %distrho
Group: Sound

%description -n lv2-TAL-plugins
%distrho of opensource audio plugins from Togu Audio Line:
* Dub-3
* Filter and Filter-2
* NoiseMaker
* Reverb, Reverb-2 and Reverb-3


%package -n lv2-Temper-plugin
Summary: A digital distortion plugin -- %distrho
Group: Sound

%description -n lv2-Temper-plugin
%distrho of Temper -- a digital distortion audio plugin.
It builds upon traditional waveshaping techniques using modulated
filter coefficients to produce a unique phase distortion.


%package -n lv2-vitalium-plugin
Summary: Spectral warping wavetable synth -- %distrho
Group: Sound

%description -n lv2-vitalium-plugin
Vitalium is a DISTRHO fork of Vital, a spectral warping wavetable synth.
Authentication, log-in, downloads and other online related stuff has
been removed from this plugin version.


%package -n lv2-Wolpertinger-plugin
Summary: A subtractive synth plugin -- %distrho
Group: Sound

%description -n lv2-Wolpertinger-plugin
%distrho of Wolpertinger.

Wolpertinger is a subtractive synth with a sharp bandpass filter whose
center frequency "bounces" around the frequency of the playing notes.


%prep
%setup -n %name-snapshot
# unpack sub-merged sources
sh -eux "%SOURCE2"

%autopatch -p1

%ifnarch x86_64
# mute JUCE assertions
find libs -type f  -name *.h -print0 \
  | xargs -0 sed -i '/define\s\+JUCE_LOG_ASSERTIONS/ s/\b1\b/0/'
%endif

%build
export GCC_USE_CCACHE=1

plugins="

# arctican
arctican-function
arctican-pilgrim

# drowaudio
drowaudio-distortion
drowaudio-distortionshaper
drowaudio-flanger
drowaudio-reverb
drowaudio-tremolo

# tal
tal-dub-3
tal-filter
tal-filter-2
tal-noisemaker
tal-reverb
tal-reverb-2
tal-reverb-3
tal-vocoder-2

# LUFSMeter
LUFSMeter
LUFSMeter-Multi

# individual
easySSP
luftikus
%ifnarch loongarch64 riscv64
pitchedDelay
%endif
refine
roth-air
stereosourceseparation
swankyamp
temper
vitalium
wolpertinger"

%meson \
  --buildtype release \
  --libdir=lib64 \
  -Dbuild-vst2=false \
  -Dbuild-vst3=false \
  -Dplugins="$(echo -n "$plugins" | sed -e 's/#.*//' -e '/^\s*$/d' | tr '\n' ',')" \
  %nil

%meson_build -v

%install
%meson_install


%files -n lv2-arctican-plugins
%_libdir/lv2/ThePilgrim.lv2
%_libdir/lv2/TheFunction.lv2

%files -n lv2-dRowAudio-plugins
%_libdir/lv2/drowaudio*.lv2

%files -n lv2-EasySSP-plugin
%_libdir/lv2/EasySSP.lv2

%files -n lv2-LUFSMeter-plugin
%_libdir/lv2/LUFSMeter*.lv2

%files -n lv2-luftikus-plugin
%_libdir/lv2/Luftikus.lv2

%ifnarch loongarch64 riscv64
%files -n lv2-PitchedDelay-plugin
%_libdir/lv2/PitchedDelay.lv2
%endif

%files -n lv2-ReFine-plugin
%_libdir/lv2/ReFine.lv2

%files -n lv2-Roth-Air-plugin
%_libdir/lv2/Roth-Air.lv2

%files -n lv2-StereoSourceSeparation-plugin
%_libdir/lv2/StereoSourceSeparation.lv2

%files -n lv2-TAL-plugins
%_libdir/lv2/TAL*.lv2

%files -n lv2-SwankyAmp-plugin
%_libdir/lv2/SwankyAmp.lv2

%files -n lv2-Temper-plugin
%_libdir/lv2/Temper.lv2

%files -n lv2-vitalium-plugin
%_libdir/lv2/Vitalium*.lv2
%_libdir/lv2/vitalium*.lv2

%files -n lv2-Wolpertinger-plugin
%_libdir/lv2/Wolpertinger.lv2


%changelog
* Wed Jan 14 2026 Ivan A. Melnikov <iv@altlinux.org> 20210315-alt0.2.gitd3b62da2
- build and package roth-air;
- build on loongarch64 and riscv64:
  + build fixes for these architectures;
  + make vitalium cross-platform via simde.
  + mute JUCE assertions on non-Intel architectures

* Wed Dec 31 2025 Ivan A. Melnikov <iv@altlinux.org> 20210315-alt0.1.gitd3b62da2
- build for sisyphus
