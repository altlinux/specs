Name: b-em
Version: 2.2
Release: alt1
Summary: An open source Acorn BBC Micro emulator
Group: Emulators
License: GPLv2
Url: http://stardot.org.uk/forums/viewtopic.php?f=4&t=10823

Source: %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: liballegro5.2-devel
BuildRequires: zlib-devel
BuildRequires: libopenal-devel
BuildRequires: automake autoconf

%description
An open source Acorn BBC Micro emulator

%prep
%setup -n %name-%version

%build
autoreconf -i
%configure
%make_build

%install
%makeinstall

mkdir -p %buildroot/%_datadir/%name
cp -R roms %buildroot/%_datadir/%name
cp -R tapes %buildroot/%_datadir/%name
cp -R discs %buildroot/%_datadir/%name
cp -R ddnoise %buildroot/%_datadir/%name


%files
%doc README.md COPYING
%_bindir/%name
%_bindir/gtest
%_bindir/hdfmt
%_bindir/jstest
%_bindir/m7makechars
%_bindir/sdf2imd

%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sat Jul 24 2022 Artyom Bystrov <arbars@altlinux.org> 2.2-alt1
 - initial release
