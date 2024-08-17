Name: outwiker
Version: 3.3.0
Release: alt1

Summary: OutWiker is designed to store notes in a tree

License: GPL-3.0
Group: Text tools
Url: https://github.com/Jenyay/outwiker

# Source-url: https://github.com/Jenyay/outwiker/archive/refs/tags/%version-stable.tar.gz
Source: %name-%version.tar

BuildRequires: rpm-build-python3

BuildArch: noarch

%add_python3_path %_datadir/%name/

AutoProv: nopython3

# See https://bugzilla.altlinux.org/40796
Requires: python3-module-cyhunspell

%description
OutWiker is designed to store notes in a tree. Such programs are called
"outliner", personal wiki, or tree-like editors. OutWiker's main difference
from the other similar programs is keeping the tree of notes in the form of
directories on disk, and encouraging changing the base by external sources
and programs. Also any number of files can be attached to the page. OutWiker
can contain pages of different types, currently supports two types of pages:
plain text and HTML, but the number of types of pages will increase in future.


%prep
%setup

%build
%make_build

%install
%makeinstall_std

# fix shebang
find %buildroot%_datadir/%name -name '*.py' | xargs sed -i \
	-e 's:/usr/bin/env python$:%__python3:'

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_mandir/ru/man1/*
%_pixmapsdir/*

%changelog
* Sat Aug 17 2024 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1
- new version (3.3.0) with rpmgs script
- do not provides python3 modules

* Thu Aug 10 2023 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt1
- New version 3.2.0

* Sun Aug 22 2021 Anton Midyukov <antohami@altlinux.org> 3.0.0.888-alt2
- Add Requires: python3-module-cyhunspell (ALT bug #40796)

* Fri May 14 2021 Anton Midyukov <antohami@altlinux.org> 3.0.0.888-alt1
- new version 3.0.0.888

* Tue Sep 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.0.790-alt1
- new version 1.9.0.790 (with rpmrb script) (ALT bug #32526)

* Tue Sep 27 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.0.800-alt1
- new version 2.0.0.800 (with rpmrb script) (ALT bug #32526)

* Wed May 30 2012 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- initial build for ALT Linux Sisyphus

