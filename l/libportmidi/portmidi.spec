Name: libportmidi
Version: 217
Release: alt2
Summary: Platform Independent Library for MIDI I/O
License: MIT
Group: Sound
Url: http://portmedia.sourceforge.net/portmidi/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
BuildPreReq: cmake
BuildRequires: gcc-c++ libalsa-devel

%description
PortMidi is a library for software developers. It supports real-time
input and output of MIDI data using a system-independent interface.

%package devel
Summary: Development files for PortMidi
Group: Development/C
BuildArch: noarch

%description devel
Development files for PortMidi.

%prep
%setup
sed -i -e 's|/usr/local/lib|%_libdir|g' \
    -e 's|/usr/local/include|%_includedir|g' \
    pm_common/CMakeLists.txt pm_dylib/CMakeLists.txt

%build
cmake . \
        -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %_lib == lib64
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS:STRING="%optflags" \
        -DCMAKE_BUILD_TYPE="Release" \
        -DCMAKE_ARCHIVE_OUTPUT_DIRECTORY="Release" \
        -DCMAKE_LIBRARY_OUTPUT_DIRECTORY="Release" \
        -DCMAKE_RUNTIME_OUTPUT_DIRECTORY="Release" \
        -DCMAKE_SKIP_RPATH=YES
%make_build

%install
%makeinstall_std

%files
%exclude %_libdir/libportmidi_s.a
%_libdir/libportmidi.so

%files devel
%_includedir/*

%changelog
* Tue Feb 08 2011 Egor Glukhov <kaman@altlinux.org> 217-alt2
- Fixed specfile

* Fri Nov 5 2010 Egor Glukhov <kaman@altlinux.org> 217-alt1
- Initial build for Sisyphus
