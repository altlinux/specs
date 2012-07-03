Name: emelfm2
Version: 0.8.0
Release: alt1
Summary: file manager for UNIX-like operating systems

Group: File tools
License: GPLv3+
Url: http://emelfm2.net

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libgimp-devel libacl-devel libgtk+2-devel libgtkspell-devel udisks-devel libdbus-glib-devel libmagic-devel

%description
emelFM2 is a file manager for UNIX-like operating systems. It uses a
simple and efficient interface pioneered by Norton Commander, in the
1980s. The main window is divided into three parts, described as "panes"
or "panels". Two of those (side-by-side or top-to-bottom) show the
contents of selected filesystem directories. The third pane, at the
bottom of the window, shows the output of commands executed within the
program. Those panes can be resized, and any one or two of them can be
hidden and unhidden, on request. A built-in command-line, toolbar
buttons or assigned keys can be used to initiate commands.

%prep
%setup -q
mkdir src/build

%build
make PREFIX=%_prefix LIB_DIR=%_libdir    CFLAGS="--pipe -Wall -g -O2" STRIP=0 \
     DOCS_VERSION=1  WITH_TRANSPARENCY=1 WITH_KERNELFAM=1 EDITOR_SPELLCHECK=1 \
     NEW_COMMAND=1   WITH_DEVKIT=1       WITH_THUMBS=1    WITH_TRACKER=1 \
     WITH_ACL=1      WITH_POLKIT=1

%install
make install install_i18n \
             DOCS_VERSION=1 \
             PREFIX=%buildroot%_prefix \
             PLUGINS_DIR=%buildroot%_libdir/%name/plugins
for size in 24 32 48; do
    mkdir -p %buildroot/%_iconsdir/hicolor/${size}x$size/apps
    cp  %buildroot%_pixmapsdir/%name/%{name}_$size.png \
        %buildroot/%_iconsdir/hicolor/${size}x$size/apps/%name.png
done

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/application-registry/%name.applications
%_libdir/%name
%_man1dir/%name.1*
%_pixmapsdir/%name
%_iconsdir/hicolor/24x24/apps/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_datadir/doc/%name-%version

%changelog
* Thu Oct 20 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Feb 08 2011 Vladimir Lettiev <crux@altlinux.ru> 0.7.5-alt1
- initial build

