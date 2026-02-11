%define _unpackaged_files_terminate_build 1
%define sover 0

Name: sonic
Version: 0.2.0.13+b1
Release: alt1

Summary: Simple utility to speed up or slow down speech
License: Apache-2.0
Group: Sound
Url: https://github.com/espeak-ng/sonic
VCS: https://github.com/espeak-ng/sonic.git

Source: %name-%version.tar

#BuildRequires:

%description
Sonic is a very simple utility that reads and writes wav files,
 and speeds them up or slows them down, with low distortion.
 The key new feature in Sonic versus other libraries is very
 high quality at speed up factors well over 2X.

%package -n lib%name%sover
Summary: Lib files for %name
Group: System/Libraries

%description -n lib%name%sover
%summary

%package -n lib%name-devel
Summary: Devel files fore %name
Group: Development/C++
Provides: %name-devel = %EVR

%description -n lib%name-devel
%summary

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch 

%description doc
%summary

%prep
%setup
%__subst 's|LIBDIR=\$(PREFIX)/lib|LIBDIR=%_libdir|g' Makefile

%build
%make_build

%install
%makeinstall_std

rm %buildroot%_libdir/*.a

%check
%make_build check

%files
%_bindir/%name

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h

%files doc
%doc README TODO doc

%changelog
* Wed Feb 11 2026 Artem Semenov <savoptik@altlinux.org> 0.2.0.13+b1-alt1
- Initial build for Sisyphus
