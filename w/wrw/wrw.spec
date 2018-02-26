Name: wrw
Version: 0.2.6
Release: alt2.2.1

Summary: Car racing game for one or two players

License: GPL
Group: Games/Arcade
#Url: http://kvik.sh.cvut.cz/~opi/python/
Url: http://nixbit.com/cat/games/simulation/wrong-way/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://kvik.sh.cvut.cz/~opi/python/%name/%name.tar.bz2
Patch: %name-config.patch
Requires: python-module-pygame

# manually removed: rpm-build-mono
# Automatically added by buildreq on Mon Jul 30 2007 (-bi)
BuildRequires: python-modules-encodings
BuildArch: noarch

%description
Wrong Way is car racing game for one or two players.
You can choose one of six cars in three different tracks.

%prep
%setup -q -n %name
%patch

%install
mkdir -p %buildroot/{%_datadir/%name,%_bindir}
cp -rp * %buildroot/%_datadir/%name/
echo "cd %_datadir/%name && %_datadir/%name/run.py" >%buildroot/%_bindir/%name
chmod 0755 %buildroot/%_bindir/%name

%files
%_bindir/*
%_datadir/%name/

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.6-alt2.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt2.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.2.6-alt2.1
- Rebuilt with python-2.5.

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.6-alt2
- fix option file saving (bug #10817), thanks to Slava Semushin

* Mon Jul 30 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.6-alt1
- fix URL, update buildreq

* Tue May 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.6-alt0.1
- initial build for ALT Linux Sisyphus
