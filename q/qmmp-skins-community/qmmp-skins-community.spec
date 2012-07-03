Version:	0.1
Name:		qmmp-skins-community
Release:	alt1
Summary:	Collection skins for QMMP from community
License: 	Distributable
Group: 		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>

Source0:	parskin-v.2.tar.gz
Source1:	parskin.tar.gz
Source2:	qmmp_black.tar.bz2
Source3:	qmmp_black_mod1.tar.bz2

BuildArch:	noarch
Requires:	winamplike-skins

BuildRequires:	rpm-build-wlskins

Conflicts:	qmmp < 0.2.3-alt1.M40.1

%description
Collection skins from community for QMMP audio-player:

parskin-v.2
parskin
qmmp_black
qmmp_black_mod1

%prep
%setup -q -c

%install
%__mkdir -p %buildroot%_wlskindir
cp %SOURCE0 %buildroot%_wlskindir/
cp %SOURCE1 %buildroot%_wlskindir/
cp %SOURCE2 %buildroot%_wlskindir/
cp %SOURCE3 %buildroot%_wlskindir/

%files
%_wlskindir/*

%changelog
* Sat Jan 31 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial packing
