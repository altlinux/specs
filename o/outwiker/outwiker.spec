Name: outwiker
Version: 1.6.0
Release: alt1

Summary: OutWiker is designed to store notes in a tree

License: GPL3
Group: Text tools
Url: http://jenyay.net/Soft/Outwiker

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://jenyay.net/uploads/Soft/Outwiker/%name-%version-src.tar

BuildArch: noarch

%description
OutWiker is designed to store notes in a tree. Such programs are called
"outliner", personal wiki, or tree-like editors. OutWiker's main difference
from the other similar programs is keeping the tree of notes in the form of
directories on disk, and encouraging changing the base by external sources
and programs. Also any number of files can be attached to the page. OutWiker
can contain pages of different types, currently supports two types of pages:
plain text and HTML, but the number of types of pages will increase in future.


%prep
%setup -n %name-%version-src

%build
%make_build
%__subst "s|\r$||g" src/runoutwiker.py

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_datadir/pixmaps/%name.xpm

%changelog
* Wed May 30 2012 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- initial build for ALT Linux Sisyphus

