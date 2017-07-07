%define		_giconsdir %_iconsdir/hicolor/128x128/apps

Name:		sibcoin
Version:	0.16.1.1
Release:	alt1
Summary:	Siberian Chervonets Wallet
Url:		http://sibcoin.org/en/
Group:		Office
License:	MIT
Source0:	%name.tar.xz

Source1:	%name.png
Source2:	%name.desktop


BuildRequires: boost-devel-static boost-interprocess-devel libdb4.8_cxx-devel protobuf-compiler
BuildRequires: libevent-devel libprotobuf-devel libqrencode-devel libssl-devel libzeromq-devel
BuildRequires: qt5-base-devel qt5-tools

BuildRequires: /usr/bin/convert

%description
"Siberian Chervonets" (SIB) is a decentralized payment system, free of useles
intermediaries, control function which performs a public mathematical algorithm.
All calculations are directly from user to user. And users, in turn, form a
distributed network in which information is stored for each transaction, constantly
updating and receiving an acknowledgment from the other participants.

%prep
%setup -n %name

%build
NOCONFIGURE=1 ./autogen.sh
autoreconf -fisv
%configure
%make_build

%install
make DESTDIR=%buildroot install
install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_giconsdir}
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png
convert -resize 128x128 %SOURCE1 %buildroot%_giconsdir/%name.png

%files
%doc CONTRIBUTING.md COPYING README.md
%_bindir/*
%_libdir/libbitcoinconsensus.so*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_giconsdir/%name.png

%changelog
* Fri Jul 07 2017 Motsyo Gennadi <drool@altlinux.ru> 0.16.1.1-alt1
- initial build for ALT Linux
