%global         majorver 2.2
%global         minorver 1.1
%global         debug_package %nil

Name:           docky
Version:        %majorver.%minorver
Release:        alt1

Summary:        Advanced dock application written in Mono
Group:		Graphical desktop/GNOME
License:        GPLv3+
URL:            http://wiki.go-docky.com

Source0:        https://launchpad.net/docky/%majorver/%version/+download/%{name}-%{version}.tar.xz
# The "Icon Magnification" was removed from "Docky" due 
# to a potential violation of US Patent 7434177
Patch0:         docky-nozoom.patch
Patch1:         docky-startscript-path.patch
BuildRequires:  mono-web
BuildRequires:  libgnome-sharp-devel libgtk-sharp2-devel libgnome-desktop-sharp-devel
BuildRequires:  libgnome-keyring-sharp-devel libgtk-sharp2-gapi mono-addins-devel
BuildRequires:  mono-devel ndesk-dbus-devel ndesk-dbus-glib-devel
BuildRequires:  libnotify-sharp-devel libGConf-devel
# Docky does not use gio-sharp library yet (it has its own for now)
BuildRequires:  libgio-sharp-devel dbus-sharp-devel dbus-sharp-glib-devel
# native deps
BuildRequires:  python-devel
BuildRequires:  glib2-devel libgtk+2-devel
BuildRequires:  libgkeyfile-sharp-devel
BuildRequires:  libwnck-devel
BuildRequires:  gettext-tools
BuildRequires:  perl-XML-Parser
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
Requires:       libgio-sharp
Requires:       icon-theme-hicolor
Requires:       dbus-tools-gui

%description
Docky is an advanced shortcut bar that sits at the bottom, top, and/or
sides of your screen. It provides easy access to some of the files,
folders, and applications on your computer, displays which applications
are currently running, holds windows in their minimized state, and more.

%package        devel
Summary:        Development files for %name
Group:		Development/GNOME and GTK+
Requires:       %name = %version-%release

%description    devel
This package contains libraries and header files for developing
applications that use %name.

%prep
%setup -q
%patch0 -p1
%patch1 -p2

%build
%configure --disable-schemas-install \
           --with-gconf-schema-file-dir=%_sysconfdir/gconf/schemas
%make_build

%install
%makeinstall_std

# put in autostart
install -Dm 0644 %buildroot/%_desktopdir/%name.desktop %buildroot%_sysconfdir/xdg/autostart/%name.desktop

#gapi_codegen.exe is not distributed (licence is GNU GPL v2)
rm -f %buildroot%_libdir/%name/gapi_codegen*

# use system libgio-sharp
rm -rf %buildroot%_libdir/%name/gio-sharp.dll

# autostart is disabled by default
echo "X-GNOME-Autostart-enabled=false" >> \
    %buildroot%_sysconfdir/xdg/autostart/%name.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING COPYRIGHT NEWS
%_bindir/%name
%_libdir/%name
%_datadir/%name/
%_iconsdir/hicolor/*/apps/%name.*
%_iconsdir/hicolor/*/apps/gmail.png
%_iconsdir/hicolor/*/mimetypes/*
%_desktopdir/*.desktop
%_sysconfdir/gconf/schemas/docky.schemas
%config(noreplace) %_sysconfdir/xdg/autostart/%name.desktop
%_man1dir/%name.1*

%files devel
%_libdir/pkgconfig/docky.*.pc

%changelog
* Thu Mar 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.2.1.1-alt1
- New version
- Use dbus-launch in startup script to run with DBus

* Tue May 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt2
- Use system libgio-sharp library
- Leave desktop files original
- Spec cleanup

* Mon May 11 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- Initial build in Sisyphus (thanks Fedora for the spec and patches)

