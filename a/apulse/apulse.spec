Name: apulse
Summary: %name
Version: 0.1.0
Release: alt1
License: MIT
Group: System/Libraries
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

Patch: %name-%version-%release.patch

Source100: %name.watch

Url: https://download.libsodium.org/libsodium/releases/

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: cmake-modules libstdc++-devel pkg-config
BuildRequires: cmake gcc-c++ glib2-devel libalsa-devel

%description
%summary

%prep
%setup
%patch -p1

%build
%cmake_insource -DNODEBUG=1 -DAPULSEPATH=%_libdir/apulse
%make_build NODEBUG=1 # VERBOSE=1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/apulse
%_libdir/apulse/

%changelog
* Tue Sep 23 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.0-alt1
- first build for Sisyphus
