%define plugin bonk
Name: xmms-in-%plugin
Version: 0.12
Release: alt1
Summary: Bonk input plugin for XMMS
Summary(uk_UA.CP1251): Плагін вводу Bonk для XMMS
Summary(ru_RU.CP1251): Плагин ввода Bonk для XMMS
License: GPL
Group: Sound
URL: http://www.proustmedia.de/bonk-xmms/
Source: %plugin-xmms-%version.tar.bz2

# Automatically added by buildreq on Wed Feb 01 2006
BuildRequires: gcc-c++ glib-devel gtk+-devel libstdc++-devel libxmms-devel pkg-config

%description
xmms-in-bonk is a plugin for the multimedia player XMMS that plays audio files in
the bonk format, a highly compressed audio format.


%prep
%setup -q -n %plugin-xmms-%version


%build
%define _optlevel 2
%add_optflags %optflags_shared
%make_build CFLAGS="%optflags -fno-exceptions -ffast-math -D_REENTRANT `pkg-config --cflags-only-I gtk+`"


%install
#define xmmsindir `xmms-config --input-plugin-dir`
%define xmmsindir %_libdir/xmms/Input
install -pD -m644 lib%plugin.so %buildroot%xmmsindir/lib%plugin.so


%files
%doc README ChangeLog
%xmmsindir/*


%changelog
* Wed Feb 01 2006 Led <led@altlinux.ru> 0.12-alt1
- initial build
