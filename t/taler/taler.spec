Name:		taler
Version:	0.15.0.1
Release:	alt1
Summary:	Taler - first Belarus cryptocurrency
Url:		https://taler.site/
Group:		Office
License:	MIT
Source0:	%name.tar.xz

Source1:	%name.png
Source2:	%name.desktop

BuildRequires: boost-devel-static boost-interprocess-devel git-core libdb4.8_cxx-devel
BuildRequires: libevent-devel libminiupnpc-devel libprotobuf-devel libqrencode-devel
BuildRequires: libssl-devel libstdc++-devel-static libzeromq-devel protobuf-compiler
BuildRequires: qt5-base-devel qt5-tools

BuildRequires: /usr/bin/convert

%description
Taler is an experimental digital currency that enables instant payments to anyone,
anywhere in the world. Taler uses peer-to-peer technology to operate with no central
authority: managing transactions and issuing money are carried out collectively by
the network. Taler Core is the name of open source software which enables the use of
this currency.

For more information, as well as an immediately useable, binary version of the Taler
Core software, see https://taler.site.

%prep
%setup -n %name

%build
%add_optflags -std=c++11
NOCONFIGURE=1 ./autogen.sh
autoreconf -fisv
%configure --libdir=%_libdir/%name --with-gui=qt5 --enable-static=no
%make_build

%install
make DESTDIR=%buildroot install
install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png

%files
%doc CONTRIBUTING.md COPYING README.md
%dir %_libdir/%name
%_bindir/*
%_libdir/%name/libbitcoinconsensus.so*
%_desktopdir/%name.desktop
%_man1dir/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed Feb 07 2018 Motsyo Gennadi <drool@altlinux.ru> 0.15.0.1-alt1
- initial build for ALT Linux
