Name: xmms-in-tta
Version: 1.2
Release: alt2

Summary: TTA input plugin for XMMS
License: LGPL
Group: Sound

Url: http://tta.sourceforge.net
Source: xmms-tta-plugin-%version-src.tar.bz2
Patch: xmms-tta-plugin-1.2-alt-libtool.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon May 25 2009
BuildRequires: glib2-devel libxmms-devel

Summary(uk_UA.CP1251): Плагін вводу TTA для XMMS
Summary(ru_RU.CP1251): Плагин ввода TTA для XMMS

%description
This is an input plugin for XMMS which can play TTA (.tta) files.

%description -l uk_UA.CP1251
Плагін вводу для XMMS для програвання файлів TTA (.tta).

%description -l ru_RU.CP1251
Плагин ввода для XMMS для проигрывания файлов TTA (.tta).

%prep
%setup -n xmms-tta-plugin-%version
%patch -p1

%build
%add_optflags %optflags_shared
%make_build CFLAGS="%optflags `pkg-config --cflags-only-I glib-2.0 gtk+`"

%install
#define xmmsindir `xmms-config --input-plugin-dir`
%define xmmsindir %_libdir/xmms/Input
install -d %buildroot%xmmsindir
install -pD -m755 libxmms-tta.la %buildroot%xmmsindir/
install -pD -m644 .libs/libxmms-tta.so.0.0.0 %buildroot%xmmsindir/
ln -s libxmms-tta.so.0.0.0 %buildroot%xmmsindir/libxmms-tta.so.0
ln -s libxmms-tta.so.0.0.0 %buildroot%xmmsindir/libxmms-tta.so

%files
%xmmsindir

%changelog
* Tue Jun 02 2009 Michael Shigorin <mike@altlinux.org> 1.2-alt2
- fixed FTBFS with recent libtool
- me as a Packager:

* Wed Feb 01 2006 Led <led@altlinux.ru> 1.2-alt1
- initial build
