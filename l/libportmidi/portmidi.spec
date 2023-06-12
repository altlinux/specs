Name: libportmidi
Version: 2.0.4
Release: alt1
Epoch: 1

Summary: Platform Independent Library for MIDI I/O

License: MIT
Group: Sound
Url: http://portmedia.sourceforge.net/portmidi/

# Source-url: https://github.com/PortMidi/portmidi/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libalsa-devel

%description
PortMidi is a library for software developers. It supports real-time
input and output of MIDI data using a system-independent interface.

%package devel
Summary: Development files for PortMidi
Group: Development/C
Requires: %name = %EVR

%description devel
Development files for PortMidi.

%prep
%setup

rm -f portmidi_cdt.zip */*.exe */*/*.exe

# Fix permissons and encoding issues:
find . -name "*.c" -exec chmod -x {} \;
find . -name "*.h" -exec chmod -x {} \;
for i in *.txt */*.txt */*/*.txt ; do
   chmod -x $i
   sed 's|\r||' $i > $i.tmp
   touch -r $i $i.tmp
   mv -f $i.tmp $i
done

%build
%cmake_insource \
    -DVERSION=%version \
    -DCMAKE_CACHEFILE_DIR=%{_builddir}/%{name}-%{version}/build
%make_build

# Build the doxygen documentation:
#doxygen

# Skip python modules building

%install
%makeinstall_std

%files
%_libdir/libportmidi.so.*

%files devel
%doc README.md README.txt license.txt
%_includedir/portmidi.h
%_includedir/porttime.h
%_includedir/pmutil.h
%_libdir/cmake/PortMidi/
%_pkgconfigdir/portmidi.pc
%_libdir/libportmidi.so

%changelog
* Mon Jun 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1:2.0.4-alt1
- new version (2.0.4) with rpmgs script (ALT bug 41760)
- upstream changed version order, set epoch: 1

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 217-alt3
- build from 217 official tarball
- add patches from Fedora project

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 217-alt2.qa1
- NMU: rebuilt for updated dependencies.

* Tue Feb 08 2011 Egor Glukhov <kaman@altlinux.org> 217-alt2
- Fixed specfile

* Fri Nov 5 2010 Egor Glukhov <kaman@altlinux.org> 217-alt1
- Initial build for Sisyphus
