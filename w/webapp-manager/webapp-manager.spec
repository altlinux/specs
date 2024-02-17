Name:     webapp-manager
Version:  1.3.4
Release:  alt1

Summary:  Run websites as if they were apps
License:  GPLv3
Group:    Networking/Other
Url:      https://github.com/linuxmint/webapp-manager

BuildArch: noarch

# Source-url: https://github.com/linuxmint/webapp-manager/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

AutoProv: no

BuildRequires(pre): rpm-build-python3 rpm-build-gir rpm-build-kf5
BuildRequires: altlinux-menus

%description
%summary.

%prep
%setup
subst 's|/usr/lib|%python3_sitelibdir|' usr/bin/%name

%build
%make

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%python3_sitelibdir/
mkdir -p %buildroot%_datadir/

cp -a usr/bin/* %buildroot%_bindir/
cp -a usr/lib/* %buildroot%python3_sitelibdir/
cp -a usr/share/* %buildroot%_datadir/

cp -a etc %buildroot%_sysconfdir/

%find_lang %name

%post
glib-compile-schemas /usr/share/glib-2.0/schemas

%files -f %name.lang
%doc README.md
%_bindir/%name
%python3_sitelibdir/%name/

%_iconsdir/*/*/*/*.svg
%_desktopdir/*

%_datadir/%name/
%_datadir/glib-2.0/schemas/org.x.webapp-manager.gschema.xml
%_K5xdgdir/webapps-webapps.directory

%config %_sysconfdir/xdg/menus/applications-merged/webapps.menu

%changelog
* Fri Feb 16 2024 Roman Alifanov <ximper@altlinux.org> 1.3.4-alt1
- Initial build for Sisyphus.
