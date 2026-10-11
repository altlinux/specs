# This package is built from the fork because upstream
# https://github.com/hslbck/gnome-shell-extension-radio
# hasn't been updated since August 12, 2024.

%define oname radio
%define uuid %oname@hslbck.gmail.com
%define xdg_name org.gnome.shell.extensions.%oname

Name: gnome-shell-extension-%oname
Version: 51
Release: alt1

Summary: A GNOME Shell extension for listening to internet radio streams

License: GPL-3.0
Group: Graphical desktop/GNOME
URL: https://github.com/enecciari/gnome-shell-extension-radio
VCS: https://github.com/enecciari/gnome-shell-extension-radio.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 45.0

%description
%summary.

%prep
%setup
%autopatch -p1

# fix README.md
sed -i 's|https://raw.githubusercontent.com/hslbck/gnome-shell-extension-radio/master/|./|g' README.md

%build

%install
mkdir -p %buildroot%_datadir/{gnome-shell/extensions/%uuid,glib-2.0/schemas}
cp -ar %uuid/{icons,*.css,*.js*} %buildroot%_datadir/gnome-shell/extensions/%uuid
cp -a %uuid/schemas/%xdg_name.gschema.xml %buildroot%_datadir/glib-2.0/schemas

# install locale files
pushd %uuid/po
for f in *.po; do
    mkdir -p %buildroot%_datadir/locale/${f%%.po}/LC_MESSAGES
    msgfmt -o %buildroot%_datadir/locale/${f%%.po}/LC_MESSAGES/%uuid.mo $f
done
popd

%find_lang %uuid

%files -f %uuid.lang
%doc COPYING *.md radio-extension.png
%_datadir/gnome-shell/extensions/%uuid
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml

%changelog
* Sun Oct 11 2026 Alexander Kovalev <alexvk@altlinux.org> 51-alt1
- Initial build for ALT.
