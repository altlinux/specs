Name:	 winewizard
Version: 3.0.2
Release: alt1
Summary: Wine Wizard is a new GUI for Wine written in Qt

License: GPLv3+
Group:	 Emulators
URL:	 http://wwizard.net/

Source0: %name-%version.tar
#VCS:	 https://github.com/LLIAKAJL/WineWizard
Patch1:	 WineWizard-2.0.0-desktop.patch

BuildRequires:  gcc-c++
BuildRequires:  qt5-base-devel
BuildRequires:  qt5-tools

Requires: bzip2
Requires: cabextract
Requires: qt5-translations
Requires: unzip
Requires: wget

%description
Wine Wizard is a new GUI for Wine written in Qt.

General feature of Wine Wizard - solutions, that users can create and
edit directly from the application. Solution is a instruction what
libraries, settings and versions of Wine are required for installation
and running MS Windows application. If the solution already created, a
user only choose the solution and run the installation file, Wine Wizard
makes all work automatically.

Unlike PlayOnLinux, a knowledge of the Shell language is not required
for creation of solutions, everything is done with the mouse. Solutions
are not required confirmation and verification, it makes possible to
quickly build database of solutions. In the last resort, a user can
write custom script that will be shown to the user before
executing(disabled by default).


%prep
%setup -q
%patch1 -p1

%build
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%install_qt5_base

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*

%changelog
* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- new version 3.0.2

* Sun Oct 16 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- new version 3.0.1

* Fri Jul 08 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build in Sisyphus (based on spec form ROSA)
