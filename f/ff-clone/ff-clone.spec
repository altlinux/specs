Name: ff-clone
Version: 1.1
Release: alt2
Summary: Get all (mostly two) fishes out
License: Public domain
Group: Games/Puzzles
Url: http://www.olsak.net/mirek/ff-clone/index_en.html
Source: %name-%version.tgz
# wget -nH -r -np http://www.olsak.net/mirek/ff-clone/manual_en.html
Source1: %name-docs.tar.gz

# Automatically added by buildreq on Fri Sep 02 2011
# optimized out: fontconfig libX11-devel pkg-config xorg-xproto-devel
BuildRequires: libcairo-devel liblua5-devel

%description
What is Fish Fillets Clone?

It is a czech puzzle game for X (Linux). The goal of each level is to
get all (mostly two) fishes out. It is a game inspirated by original
Fish Fillets.

Who has made this?

My name is Miroslav Olsak. I programmed this as my homework for school.
My brother Radek Olk has made most of levels. What is conection with
original Fish Fillets?

There is no conection with Altar (the company which made Fish Fillets
and Fish Fillets II). I have just made several new levels for Fish
Fillets - Next Generation. Program Fish Fillets Clone is written from
the begining, its rules are absolutely different from original Fish
Fillets and even images are mine.

%prep
%setup
tar xf %SOURCE1
sed -i 's/ -lX11/ -lm -lX11/' Makefile

%build
%make_build BINDIR=%_gamesbindir DATADIR=%_gamesdatadir/%name

%install
mkdir -p %buildroot%_gamesbindir %buildroot%_gamesdatadir/%name
%makeinstall BINDIR=%buildroot%_gamesbindir DATADIR=%buildroot%_gamesdatadir/%name

%files
%doc mirek/%name
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_gamesbindir/%name

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.1-alt2
- DSO list completion

* Mon Sep 12 2011 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Autobuild version bump to 1.1

* Fri Sep 02 2011 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from scratch

