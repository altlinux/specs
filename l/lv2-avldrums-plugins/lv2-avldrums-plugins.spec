
%define _unpackaged_files_terminate_build 1
%define oname avldrums

Name:    lv2-%oname-plugins
Version: 0.5.2
Release: alt1
Summary: A simple drum sample player plugin

License: GPLv2+
Group:   Sound
Url:     http://x42-plugins.com/x42/x42-avldrums

Source:  %oname-%version.tar
Source1: sub-merge.sources.txt
Source2: sub-merge.unpack.sh

%(cat %SOURCE1)

BuildRequires: gcc-c++
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)


Requires: %oname-soundfonts = %EVR

%description
avldrums.lv2 is a drum sample player plugin dedicated to Glen
MacArthur's AVLdrums. This self-contained plugin provides a
convenient way to rapidly sequence and mix midi-drums.

The AVLdrums comes as two separate drumkits: Black Pearl and Red
Zeppelin. There are 5 velocity layers for each of the 28 kits
pieces or drum-zones for both kits.

The main benefits compared to loading the soundfont into a
generic sample player are:
* built-in MIDNAM: The plugin informs the host about note-names;
* semantic grouping of ports: fan-out separate mics to
  individual tracks;
* compatible stereo/multi-out variant: allows to in-place replace
  the stereo version with multi-out -- start with stereo when
  sequencing and when moving to the mixing stage use separate
  outputs to process or customize level and pan of individual drums.

%package -n %oname-soundfonts
Summary:   AVL Drumkits soundfonts
Group:     Sound
BuildArch: noarch

%description -n %oname-soundfonts
%summary.


%prep
%setup -n %oname-%version
sh %SOURCE2

%build
# Upstream adds x86-specific optimization flags by default.
# We're preserving most of them on x86_64, but we have other platforms.
%add_optflags -ffast-math -fno-finite-math-only
%ifarch x86_64
%add_optflags -msse2 -mfpmath=sse -O3
%endif

%make_build \
    OPTIMIZATIONS="%optflags" \
    STRIP=/bin/true \
    avldrums_VERSION=%version \
    PREFIX=%prefix \
    LV2DIR=%_libdir/lv2

%install
%makeinstall_std \
    OPTIMIZATIONS="%optflags" \
    STRIP=/bin/true \
    avldrums_VERSION=%version \
    PREFIX=%prefix \
    LV2DIR=%_libdir/lv2

# install soundfonts to arch-independent location:
mkdir -p %buildroot%_datadir/%oname/
cp -r sf2 %buildroot%_datadir/%oname/

# link foundfonts from lv2 dir
for f in %buildroot%_libdir/lv2/*/*.sf2; do
    rm -f "$f"
    ln -sr %buildroot%_datadir/%oname/sf2/$(basename "$f") "$f"
done


%files
%_libdir/lv2/*

%files -n %oname-soundfonts
%_datadir/%oname

%changelog
* Fri Jan 06 2023 Ivan A. Melnikov <iv@altlinux.org> 0.5.2-alt1
- 0.5.2

* Thu Jun 03 2021 Ivan A. Melnikov <iv@altlinux.org> 0.4.2-alt1
- initial build for Sisyphus
