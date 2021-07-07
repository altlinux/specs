
%define _unpackaged_files_terminate_build 1
%define _customdocdir %_defaultdocdir/%name


Name:     dragonfly-reverb
Version:  3.2.5
Release:  alt1

Summary:  A set of free reverb effects
License:  GPL-3.0
Group:    Sound
# VCS:    https://github.com/michaelwillis/dragonfly-reverb
URL:      https://michaelwillis.github.io/dragonfly-reverb/

Source:   %name-%version.tar

# https://github.com/DISTRHO/DPF.git
Source10: DPF-226f219c4d35ca8fa6e82b69d87be823cb785a0d.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(x11)

%description
Dragonfly Reverb is a free reverb bundle including Hall,
Room, Plate, and Early Reflections.


%package standalone
Group: Sound
Summary: A set of free reverb effects -- standalone versions

%description standalone
Dragonfly Reverb is a free reverb bundle including Hall,
Room, Plate, and Early Reflections.

This package contains these effects built as standalone
applications, intended for use with JACK.


%package -n lv2-%name-plugins
Group: Sound
Summary: A set of free reverb effects -- LV2 versions

%description -n lv2-%name-plugins
Dragonfly Reverb is a free reverb bundle including Hall,
Room, Plate, and Early Reflections.

This package contains these effects built as LV2 plugins.


%package docs
Group: Documentation
Summary: The documentation for Dragonfly Reverb

%description docs
%summary


%prep
%setup
tar -xf %SOURCE10 -C 'dpf' --strip-components 1

%build
%make_build BASE_OPTS='%optflags' SHELL='sh -x' SKIP_STRIPPING=true

%install
names='DragonflyEarlyReflections DragonflyHallReverb DragonflyPlateReverb DragonflyRoomReverb'

mkdir -p %buildroot%_bindir

for name in $names; do
  install -m755 bin/$name %buildroot%_bindir
done

mkdir -p %buildroot%_libdir/lv2
for name in $names; do
  cp -R bin/$name.lv2 %buildroot%_libdir/lv2
done
find %buildroot%_libdir/lv2 -type f -exec chmod 644 '{}' ';'


%files standalone
%_bindir/*

%files -n lv2-%name-plugins
%_libdir/lv2/*

%files docs
%doc docs


%changelog
* Wed Jul 07 2021 Ivan A. Melnikov <iv@altlinux.org> 3.2.5-alt1
- Initial build for Sisyphus
