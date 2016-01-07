Name:           bleachbit
Version:        1.10
Release:        alt1

Summary:        Remove unnecessary files, free space, and maintain privacy
License:        GPLv3+
Group:          Archiving/Other
URL:            http://bleachbit.sourceforge.net/

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        http://downloads.sourceforge.net/%name/%name-%version.tar.lzma
Source1:	%name.watch

Patch1:		%name-apt-rpm-specific.patch

BuildArch:      noarch

BuildRequires(pre): rpm-build-gnome python-devel

%add_python_req_skip Windows

%description
BleachBit deletes unnecessary files to free valuable disk space,
maintain privacy, and remove junk. Rid your system of old clutter
including cache, cookies, Internet history, localizations, logs,
temporary files, and broken shortcuts. It wipes clean the cache
and history list of many common programs.

%prep
%setup -q
%patch1 -p2

%build
make -C po local 
%python_build

%install
%makeinstall_std prefix=%_prefix

sed -i -e '/^#!\//, 1d' %buildroot%_datadir/bleachbit/CLI.py
sed -i -e '/^#!\//, 1d' %buildroot%_datadir/bleachbit/GUI.py
rm -f %buildroot%_datadir/%name/Windows.py*

%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_pixmapsdir/%name.png

%changelog
* Thu Jan 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.10-alt1
- New version

* Sun Jun 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.8-alt1
- New version

* Sat Feb 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt3
- Fix apt cleaner for apt-rpm support (ALT #30736)

* Mon Jan 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt2
- Package watch file to check for new version

* Wed Jan 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- New version

* Tue Sep 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- New version

* Wed Jul 09 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- New version

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- New version

* Mon Nov 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version

* Tue Feb 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt1
- New version 0.9.5

* Fri Sep 07 2012 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- Initial build in Sisyphus (ALT #23106)

