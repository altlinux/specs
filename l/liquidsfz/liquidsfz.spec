Name: liquidsfz
Version: 0.3.2
Release: alt1

Summary: SFZ sampler
License: MPL-2.0
Group: Sound
Url: https://github.com/swesterfeld/liquidsfz

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(tinfo)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(fftw3f)

%package -n libliquidsfz
Summary: SFZ sampler
Group: System/Libraries

%package devel
Summary: SFZ sampler
Group: Development/C++

%package -n lv2-liquidsfz-plugin
Summary: SFZ sampler
Group: Sound

%define desc\
liquidsfz is a free and open source sampler that can load and play .sfz files.\
It can also load and play Hydrogen drumkits. We support JACK and LV2.\

%description %desc

%description -n libliquidsfz %desc
This package contains shared library only.

%description devel %desc
This package contains developmtnt part of liquidsfz.

%description -n lv2-liquidsfz-plugin %desc
This package contains liquidsfz as LV2 plugin.

%prep
%setup

%build
%autoreconf
%configure --enable-shared --disable-static
%make_build

%install
%makeinstall_std

%files
%doc LICENSE NEWS OPCODES.* README.*
%_bindir/liquidsfz

%files -n libliquidsfz
%_libdir/libliquidsfz.so.*

%files devel
%_libdir/libliquidsfz.so
%_pkgconfigdir/liquidsfz.pc
%_includedir/liquidsfz.hh

%files -n lv2-liquidsfz-plugin
%_libdir/lv2/liquidsfz.lv2

%changelog
* Fri Oct 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.2-alt1
- initial

