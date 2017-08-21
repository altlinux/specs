Name: munt
Version: 2.2.0
Release: alt1.git.5.gb414aeb
Summary: MT-32, CM-32L and LAPC-I synthesiser modules emulator
Group: Sound
Url: http://munt.sourceforge.net/
License: GPL2

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name.tar

# Automatically added by buildreq on Mon Aug 21 2017
# optimized out: cmake-modules libstdc++-devel pkg-config python-base python-modules
BuildRequires: cmake gcc-c++ glib2-devel libalsa-devel

%description
mt32emu
=======
mt32emu is a C/C++ library which allows to emulate (approximately) the Roland
MT-32, CM-32L and LAPC-I synthesiser modules.

mt32emu_alsadrv
===============
ALSA MIDI driver uses mt32emu to provide ALSA MIDI interface for Linux applications (now obsolete).

mt32emu_smf2wav
===============
mt32emu-smf2wav makes use of mt32emu to produce a WAVE file from an SMF file.
The output file corresponds a digital recording from a Roland MT-32, CM-32L and LAPC-I
synthesiser module.

%prep
%setup -n %name

%build
%cmake \
	-Dmunt_WITH_MT32EMU_QT=FALSE \

make -C BUILD
make -C mt32emu_alsadrv/ mt32d \
	INCLUDES=-I../BUILD/mt32emu/include \
	CXXFLAGS="-O2 -Wno-write-strings -Wno-unused-result -Wno-deprecated-declarations \
		-L../BUILD/mt32emu"

%install
%makeinstall_std -C BUILD
mv %buildroot%_docdir/munt doc
mkdir doc/alsadrv/
cp -a mt32emu_alsadrv/*.txt doc/alsadrv/
install -m755 mt32emu_alsadrv/mt32d %buildroot%_bindir/

%files
%_bindir/*
%doc doc/*
%exclude %_includedir/mt32emu
%exclude %_libdir

%changelog
* Mon Aug 21 2017 Ildar Mulyukov <ildar@altlinux.ru> 2.2.0-alt1.git.5.gb414aeb
- initial build for ALT Linux Sisyphus
- only smf2wav and alsadrv are built, no QT, no GUI

