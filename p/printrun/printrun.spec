Name:     printrun
Version:  2.1.0
Release:  alt1
Epoch:    1
Summary:  RepRap printer interface and tools

License:  GPL-3.0+ and FSFAP
Group:    Engineering
URL:      https://github.com/kliment/Printrun
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar

#BuildRequires:  Cython
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-Polygon
BuildRequires: python3-module-serial
BuildRequires: desktop-file-utils
BuildRequires: gettext
Requires: pronterface = %EVR
Requires: pronsole = %EVR
Requires: plater = %EVR

%description
Printrun is a set of G-code sending applications for RepRap.
It consists of printcore (dumb G-code sender), pronsole (featured command line
G-code sender), pronterface (featured G-code sender with graphical user
interface), and a small collection of helpful scripts.
This package installs whole Printrun.

%package common
Summary: Common files for Printrun
Group: Engineering

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

%package -n pronsole
Summary: CLI interface for RepRap
Group: Engineering
Requires: python3-module-serial
Requires: 3dprinter-udev-rules
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer. It is a part of Printrun.

%package -n pronterface
Summary: GUI interface for RepRap
Group: Engineering
Requires: python3-module-wx
Requires: simarrange
Requires: pronsole = %{version}-%{release}
Requires: 3dprinter-udev-rules
BuildArch: noarch

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer. It is a part of Printrun.

%package -n plater
Summary: RepRap STL plater
Group: Engineering
Requires: python3-module-wx
Requires: %{name}-common = %{version}-%{release}
Requires: simarrange
BuildArch: noarch

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.

%prep
%setup -q
# Remove unsupported module
rm -f printrun/power/osx.py

%build
%python3_build

# rebuild locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || :
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || :
done
cd ..

%install
%python3_install

# Remove .py extension from executable files
cd %buildroot%_bindir
for FILE in *.py; do
  mv -f "$FILE" "${FILE%.py}"
done
cd -

# Remove .py extension in desktop files (ALT #36763)
cd %buildroot%_desktopdir
for file in $(ls) ; do sed -i "s/\(.*\).py/\1/" $file; done
cd -

%if_without prontserve
rm -f %buildroot%_bindir/prontserve
rm -f %buildroot%python_sitelibdir/%name/prontserve.py
%endif

mv %buildroot%_datadir/{metainfo,appdata}

%find_lang pronterface
%find_lang plater

%files
%doc README* COPYING

%files common
%doc README* COPYING
%python3_sitelibdir/%name
%python3_sitelibdir/Printrun-*.egg-info
%_bindir/printcore*
%_pixmapsdir/plater.png

%files -n pronsole
%doc README* COPYING
%_bindir/pronsole*
%_pixmapsdir/pronsole.png
%_desktopdir/pronsole.desktop
%_datadir/appdata/pronsole.appdata.xml

%if_with prontserve
%files -n prontserve
%doc README* COPYING
%_bindir/prontserve*
%endif

%files -n pronterface -f pronterface.lang
%doc README* COPYING
%_bindir/pronterface*
%_datadir/pronterface
%_pixmapsdir/pronterface.png
%_desktopdir/pronterface.desktop
%_datadir/appdata/pronterface.appdata.xml

%files -n plater -f plater.lang
%doc README* COPYING
%_bindir/plater*
%_desktopdir/plater.desktop
%_datadir/appdata/plater.appdata.xml

%changelog
* Mon May 27 2024 Andrey Cherepanov <cas@altlinux.org> 1:2.1.0-alt1
- New version.

* Thu May 25 2023 Andrey Cherepanov <cas@altlinux.org> 1:2.0.1-alt1
- New version.

* Tue Apr 14 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.0.0-alt0.1.rc5
- New version (ALT #38351).
- Build with python3 and without skeinforge support.

* Thu Jun 06 2019 Grigory Ustinov <grenka@altlinux.org> 1:1.6.0-alt2
- Fix desktop files (Closes: #36763).

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.6.0-alt1.qa1
- NMU: applied repocop patch

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.0-alt1
- New version.

* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 20131019-alt1
- Import from Fedora

