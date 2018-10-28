Name:		karbowanecwallet
Version:	1.3.1
Release:	alt1
Summary:	Karbowanec KRB wallet
Url:		https://karbo.io/
Group:		Office
License:	MIT
ExclusiveArch:	%ix86 x86_64
Source0:	%name.tar.xz
Source1:	cryptonote.tar.xz
Source2:	libqrencode.tar.xz
Source3:	karbowanec.png

Patch0:		%name-1.2.6-alt_lang_dir.patch

BuildRequires: boost-asio-devel boost-devel-headers boost-devel-static cmake qt5-base-devel
BuildRequires: /usr/bin/convert

%description
  Karbowanec (Karbo) is Ukrainian decentralized, privacy oriented peer-to-peer
  cryptocurrency. It is open-source, nobody owns or controls Karbowanec
  and everyone can take part.

%prep
%setup -n %name
tar -xf %SOURCE1
tar -xf %SOURCE2
%patch0 -p1

%build
subst 's|Categories=Office;Finance;|Categories=Qt;Office;Finance;|g' ./src/%name.desktop
mkdir ./build
cd ./build
cmake ../. \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build VERBOSE=1

%install
cd ./build
make DESTDIR=%buildroot install

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %SOURCE3 %buildroot%_liconsdir/karbowanec.png
convert -resize 32x32 %SOURCE3 %buildroot%_niconsdir/karbowanec.png
convert -resize 16x16 %SOURCE3 %buildroot%_miconsdir/karbowanec.png

%files
%_bindir/*
%_desktopdir/%name.desktop
%_docdir/%name
%_datadir/%name
%_miconsdir/karbowanec.png
%_niconsdir/karbowanec.png
%_liconsdir/karbowanec.png

%changelog
* Sun Oct 28 2018 Motsyo Gennadi <drool@altlinux.ru> 1.3.1-alt1
- 1.3.1
- disable aarch64

* Sun Aug 26 2018 Motsyo Gennadi <drool@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Mon Aug 13 2018 Motsyo Gennadi <drool@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Thu Apr 05 2018 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Sat Mar 31 2018 Motsyo Gennadi <drool@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Wed Dec 27 2017 Motsyo Gennadi <drool@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Tue Oct 24 2017 Motsyo Gennadi <drool@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Thu Sep 28 2017 Motsyo Gennadi <drool@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Sun Jul 09 2017 Motsyo Gennadi <drool@altlinux.ru> 1.1.7-alt2
- fix cryptonote for build for Sisyphus

* Mon Jul 03 2017 Motsyo Gennadi <drool@altlinux.ru> 1.1.7-alt1
- initial build for ALT Linux
