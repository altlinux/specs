Name: libportmidi
Version: 217
Release: alt3

Summary: Platform Independent Library for MIDI I/O

License: MIT
Group: Sound
Url: http://portmedia.sourceforge.net/portmidi/

Packager: Egor Glukhov <kaman@altlinux.org>

# Source-url: http://prdownloads.sourceforge.net/portmedia/portmidi-src-%{version}.zip
Source: %name-%version.tar

BuildPreReq: cmake
BuildRequires: gcc-c++ libalsa-devel

%description
PortMidi is a library for software developers. It supports real-time
input and output of MIDI data using a system-independent interface.

%package devel
Summary: Development files for PortMidi
Group: Development/C
Requires: %name = %version-%release

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

# Why don't they install this header file?
install -pm 644 pm_common/pmutil.h %{buildroot}%{_includedir}/
rm -f %buildroot%_libdir/libportmidi_s.a
rm -f %buildroot%_libdir/libpmjni.so

%files
%_libdir/libportmidi.so.*

%files devel
%_includedir/*
%_libdir/libportmidi.so

%changelog
* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 217-alt3
- build from 217 official tarball
- add patches from Fedora project

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 217-alt2.qa1
- NMU: rebuilt for updated dependencies.

* Tue Feb 08 2011 Egor Glukhov <kaman@altlinux.org> 217-alt2
- Fixed specfile

* Fri Nov 5 2010 Egor Glukhov <kaman@altlinux.org> 217-alt1
- Initial build for Sisyphus
