Name: emotion_generic_players
Version: 1.8.0
Release: alt1

Summary: A set of players for Emotion
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: efl-libs-devel libvlc-devel

%description
These are additional "generic" players for Evas that are stand-alone
executables that Emotion may run from its generic loader module. This means
that if they crash, the application loading the image does not crash
also. In addition the licensing of these binaries will not affect the
license of any application that uses Evas as this uses a completely
generic execution system that allows anything to be plugged in as a
loader.


%prep
%setup

%build
%configure
%make_build

%check
%make check

%install
%makeinstall_std

%files
%_libdir/emotion/generic_players/*
%doc AUTHORS COPYING README

%changelog
* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus

