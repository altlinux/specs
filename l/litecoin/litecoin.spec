%define		_giconsdir %_iconsdir/hicolor/128x128/apps

Name:		litecoin
Version:	0.15.0.1
Release:	alt2
Summary:	Litecoin Core
Url:		https://litecoin.org/
Group:		Office
License:	MIT
Source0:	litecoin.tar.xz
Source1:	%name.desktop
Source2:	%name.png

Patch1: litecoin-0.15.0.1-upstream-boost-compat.patch

BuildRequires: boost-filesystem-devel boost-interprocess-devel boost-program_options-devel boost-signals-devel
BuildRequires: gcc-c++ libdb4.8_cxx-devel libevent-devel libminiupnpc-devel libprotobuf-devel libqrencode-devel
BuildRequires: libzeromq-devel protobuf-compiler libqt4-devel

BuildRequires: /usr/bin/convert

%description
Litecoin is an experimental digital currency that enables instant payments to anyone,
anywhere in the world. Litecoin uses peer-to-peer technology to operate with no central
authority: managing transactions and issuing money are carried out collectively by the
network. Litecoin Core is the name of open source software which enables the use of this
currency.

For more information, as well as an immediately useable, binary version of the Litecoin
Core software, see https://litecoin.org.

%prep
%setup -n litecoin
%patch1 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure --with-gui=qt4 --libdir=%_libdir/%name
%make_build

%install
make DESTDIR=%buildroot install
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_giconsdir}
convert -resize 48x48 %SOURCE2 %buildroot%_liconsdir/%name-core.png
convert -resize 32x32 %SOURCE2 %buildroot%_niconsdir/%name-core.png
convert -resize 16x16 %SOURCE2 %buildroot%_miconsdir/%name-core.png
convert -resize 128x128 %SOURCE2 %buildroot%_giconsdir/%name-core.png

%files
%_bindir/*
%_libdir/%name/*.so*
%_desktopdir/*.desktop
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%_giconsdir/*.png
%_man1dir/*

%changelog
* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0.1-alt2
- NMU: rebuilt with boost-1.67.0.

* Thu Sep 21 2017 Motsyo Gennadi <drool@altlinux.ru> 0.15.0.1-alt1
- initial build for ALT Linux
