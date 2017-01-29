Name: xmacro

Version: 0.3
Release: alt3.pre

Summary: Recording and replaying keyboard and mouse events
Summary(ru_RU.UTF-8): Записывает и воспроизводит события клавиатуры и мыши
License: GPLv2
Group: System/X11
Url: http://xmacro.sourceforge.net/

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-pre0.3.tar.bz2
Patch: gcc6-FTBFS.patch

# Automatically added by buildreq on Mon Jul 13 2015
# optimized out: libX11-devel libXi-devel libstdc++-devel xorg-inputproto-devel xorg-recordproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ libXtst-devel

%description
The XMacro package contains two simple, C++ programs (xmacrorec and xmacroplay)
for recording and replaying keyboard and mouse events on an X server. This
functionality is achieved through the XTest extension. (BTW it would be better
to use the XTrap extension but it's not widespread in precompiled X servers...)
The programs are heavily based on the xremote utility of Jan Ekholm (chakie at
infa.abo.fi).

%description -l ru_RU.UTF-8
Пакет XMacro содержит две простых программы, написанных на С++ (xmacrorec и
xmacroplay) для записи и воспроизведения событий клавиатуры и мыши на X-сервере.
Эта функциональность достигается за счет расширения XTEST. (Кстати, было бы
лучше использовать расширение XTRAP, но оно не распространено в скомпилированных
X серверах...) Программы в значительной степени основаны на утилите xremote
Jan Ekholm (chakie at infa.abo.fi).

%prep
%setup -n %name-pre0.3
%patch -p2

%build
subst 's|g++ -O2|g++ %optflags|g' ./Makefile
%make_build

%install
mkdir -p %buildroot/%_bindir
cp xmacrorec xmacrorec2 xmacroplay %buildroot/%_bindir

%files
%doc COPYING README README.SUSE
%_bindir/xmacro*

%changelog
* Sun Jan 29 2017 Anton Midyukov <antohami@altlinux.org> 0.3-alt3.pre
- Fix build with gcc6

* Thu Aug 27 2015 Anton Midyukov <antohami@altlinux.org> 0.3-alt2.pre
- Fix encoding in description

* Fri Jul 17 2015 Anton Midyukov <antohami@altlinux.org> 0.3-alt1.pre
- Initial build for ALT Linux Sisyphus.
