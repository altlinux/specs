Name: meritous
Version: 1.2
Release: alt2
%define fver 12
Summary: Action-adventure dungeon crawl game
License: GPLv3
Group: Games/Adventure
Source: http://www.asceai.net/files/meritous_v%{fver}_src.tar.bz2
Source1: %name.sh
URL: http://www.asceai.net/meritous/
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Dec 04 2008
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel zlib-devel

%description
Far below the surface of the planet is a secret.
A place of limitless power. Those that seek to
control such a utopia will soon bring an end
to themselves.

Seeking an end to the troubles that plague him,
PSI user MERIT journeys into the hallowed Orcus
Dome in search of answers.

%prep
%setup -n meritous_v%{fver}_src
find . -type f \( -name \*.txt -o -name \*.c -o -name \*.h \) -exec sed -i 's///' {} \;
sed -i 's/ -lz/ -lz -lm/' Makefile

%build
%make_build

%install
install -Ds %name %buildroot%_gamesbindir/%name.bin
install -D %SOURCE1 %buildroot%_gamesbindir/%name
mkdir -p %buildroot%_gamesdatadir/%name
cp -a dat %buildroot%_gamesdatadir/%name/

%files
%doc readme.txt
%_gamesdatadir/%name/*
%_gamesbindir/*

%changelog
* Mon May 28 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- DSO list completion

* Thu Dec 04 2008 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from scratch

