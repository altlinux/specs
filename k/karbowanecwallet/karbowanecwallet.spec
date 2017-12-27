Name:		karbowanecwallet
Version:	1.2.0
Release:	alt1
Summary:	Karbowanec KRB wallet
Url:		http://karbowanec.com
Group:		Office
License:	MIT
Source0:	%name.tar.xz
Source1:	cryptonote.tar.xz
Source2:	libqrencode.tar.xz
Source3:	karbowanec.png

# Automatically added by buildreq on Mon Jul 03 2017 (-bi)
# optimized out: GraphicsMagick GraphicsMagick-common boost-filesystem-devel boost-program_options-devel cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-network libqt5-widgets libstdc++-devel perl python-base python-modules python3 python3-base python3-dev rpm-build-python3 xz
BuildRequires: boost-asio-devel boost-devel-headers boost-devel-static cmake qt5-base-devel

BuildRequires: /usr/bin/convert

%description
  Karbowanec is Ukrainian decentralized, privacy oriented peer-to-peer
  cryptocurrency. It is open-source, nobody owns or controls Karbowanec
  and everyone can take part.

%prep
%setup -n %name
tar -xf %SOURCE1
tar -xf %SOURCE2

%build
subst 's|Categories=Office;Finance;|Categories=Qt;Office;Finance;|g' ./src/%name.desktop
rm -f ./src/gui/macdockiconhandler.{h,mm}
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
%_miconsdir/karbowanec.png
%_niconsdir/karbowanec.png
%_liconsdir/karbowanec.png

%changelog
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
