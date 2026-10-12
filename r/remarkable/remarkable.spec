Name: remarkable
Version: 1.95
Release: alt1

Summary: A free fully featured markdown editor

Group: Editors
Url: http://remarkableapp.github.io
License: MIT

# Source-url: https://github.com/jamiemcg/Remarkable/archive/v%version.tar.gz
Source: %name-%version.tar

Patch1: remarkable-1.95-sysconfig-path.patch

AutoProv:no

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires: python3-module-setuptools
BuildRequires: python3(setuptools_scm)

BuildArch: noarch

# local implementation uses wkhtmltopdf, but have a wrong placement
# findBar and styles are internal modules of the package (found via sys.path)
%add_python3_req_skip pdfkit findBar styles

# gi.require_version('WebKit2', '4.1') (typelib is not detected by autoreq)
Requires: libwebkit2gtk4.1-gir
# typelib(GtkSource) = 3.0
Requires: libgtksourceview3-gir

%description
A Fully Featured Markdown Editor for Linux.

%prep
%setup
%patch1 -p1
subst 's|^import pdfkit||' remarkable/RemarkableWindow.py
sed -i 's/\r$//' remarkable/undobuffer.py

%install
# Check https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=remarkable
install -Dm 755 bin/remarkable %buildroot/usr/bin/remarkable
#install -D debian/remarkable.mime %buildroot%_datadir/mime/packages/remarkable
install -Dm 644 data/media/remarkable.svg %buildroot/usr/share/icons/hicolor/scalable/apps/remarkable.svg
install -Dm 644 remarkable.desktop %buildroot/usr/share/applications/remarkable.desktop

install -Dm 644 data/glib-2.0/schemas/net.launchpad.remarkable.gschema.xml %buildroot/usr/share/glib-2.0/schemas/net.launchpad.remarkable.gschema.xml

mkdir -p %buildroot%python3_sitelibdir/
cp -a remarkable remarkable_lib %buildroot%python3_sitelibdir/
mkdir -p %buildroot%_datadir/%name/
cp -a data/media data/ui %buildroot%_datadir/%name/

%files
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/*/*/*/%name.svg
/usr/share/glib-2.0/schemas/net.launchpad.remarkable.gschema.xml
%python3_sitelibdir/%name/
%python3_sitelibdir/%{name}_lib/
#python3_sitelibdir/%name-*.egg-info

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.95-alt1
- new version 1.95
- fix startup: use the ALT site-packages path for internal modules
- require WebKit2 4.1 typelib

* Mon May 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.87-alt1
- initial build for Sisyphus
