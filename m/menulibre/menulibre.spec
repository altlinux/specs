Name: menulibre
Version: 13.04.17
Release: alt1

Summary: Advanced menu editor with quicklist support
License: %gpl3only
Group: Graphical desktop/Other
BuildArch: noarch

URL: https://launchpad.net/menulibre
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses intltool
BuildRequires: python-devel python-module-distutils-extra python-module-pygtk
BuildRequires: python-module-pyxdg python-module-pygobject3 libgtk+3-gir libgtksourceview3-gir

Requires: libgtk+3-gir libgtksourceview3-gir

%description
An advanced menu editor that provides modern features in a clean,
easy-to-use interface. All without GNOME dependencies, so even
lightweight systems can benefit from the sanity that MenuLibre offers.
MenuLibre is your one-stop shop for menus in Linux, whether you use
Gnome, LXDE, XFCE, or Unity.

%prep
%setup
%patch0 -p1

%build
%python_build

%install
install -Dm0644 build/share/applications/menulibre.desktop %buildroot%_desktopdir/%name.desktop
%python_install

# Drop Ubuntu-specific
sed -i '/^$/,$d' %buildroot%_desktopdir/%name.desktop

# Install localizations
mkdir -p %buildroot%_datadir/locale
cp -a build/mo/* %buildroot%_datadir/locale/

# Install help
mkdir -p  %buildroot%_datadir/gnome/help/%name
cp -a help/* %buildroot%_datadir/gnome/help/%name/

%find_lang %name

%files -f %name.lang
%doc AUTHORS TODO
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%python_sitelibdir_noarch/%{name}*
%_datadir/gnome/help/%name/

%changelog
* Mon Jul 08 2013 Mikhail Efremov <sem@altlinux.org> 13.04.17-alt1
- Updated to 13.04.17.

* Wed Apr 24 2013 Mikhail Efremov <sem@altlinux.org> 13.04.12-alt1
- Fix directory creation.
- Initial build.

