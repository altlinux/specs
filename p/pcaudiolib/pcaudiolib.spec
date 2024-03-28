# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major      0
%define libname    libpcaudio%{major}
%define libnamedev libpcaudiolib-devel

Name:           pcaudiolib
Version:        1.2
Release:        alt1_1
Summary:        Portable C Audio Library
Group:          System/Libraries
# pcaudiolib bundles TPCircularBuffer with Cube license, which is only used
# by coreaudio support, which we do not build. The rest is GPLv3+.
License:        GPLv3+
URL:            https://github.com/espeak-ng/pcaudiolib/
Source0:        https://github.com/espeak-ng/pcaudiolib/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
Source44: import.info

%description
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.

#------------------------------------------------

%package -n     %{libname}
Summary:        Portable C Audio Library
Group:          System/Libraries

%description -n %{libname}
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.

#------------------------------------------------

%package -n     %{libnamedev}
Summary:        Development files for %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
Development files for the Portable C Audio Library.

#------------------------------------------------

%prep
%setup -q


rm -rf src/TPCircularBuffer

%build
./autogen.sh
%configure --disable-static \
           --without-coreaudio
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc --no-dereference COPYING
%doc AUTHORS CHANGELOG.md README.md
%{_libdir}/libpcaudio.so.%{major}
%{_libdir}/libpcaudio.so.%{major}.*

%files -n %{libnamedev}
%{_libdir}/libpcaudio.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/audio.h


%changelog
* Thu Mar 28 2024 Igor Vlasenko <viy@altlinux.org> 1.2-alt1_1
- new version

