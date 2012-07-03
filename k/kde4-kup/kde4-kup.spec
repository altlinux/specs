%define _name kup

Name:     kde4-kup
Version:  0.2
Release:  alt1

Summary:  Kup is a KDE-based frontend for the very excellent bup backup software, that gives you easy and fast incremental backups!
License:  GPLv2+
Group:    Archiving/Backup
URL:      http://kde-apps.org/content/show.php/Kup+Backup+System?content=147465

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   147465-%_name-%version.tar.bz2

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++
Requires: bup

%description
Kup is a KDE-based frontend for the very excellent bup backup software,
that gives you easy and fast incremental backups!

%prep
%setup -q -n %_name-%version

%build
%add_optflags -fPIC
%K4build

%install
%K4install
%K4find_lang --with-kde %_name

%files -f %_name.lang
%doc README TODO
%_K4bindir/kupdaemon
%_K4lib/kcm_kup.so
%_K4apps/kupdaemon/kupdaemon.notifyrc
%_K4start/kupdaemon.desktop
%_K4srv/kcm_kup.desktop
%_iconsdir/hicolor/32x32/actions/kuprunning.mng
%_iconsdir/hicolor/scalable/apps/kup.svgz

%changelog
* Wed Feb 15 2012 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- New version 0.2

* Sun Jan 29 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- Add requirement of bup

* Fri Jan 27 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus

