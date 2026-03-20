# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-freon
Version: 61
Release: alt1
Summary: Shows CPU temperature, disk temperature, video card temperature
# OFL-1.1 for material-icons
License: GPL-3.0-or-later AND OFL-1.1
Group:  Graphical desktop/GNOME
URL: gnome-shell-extension-freon
VCS: gnome-shell-extension-freon.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

%description
Freon is forked from gnome-shell-extension-sensors. Freon is an extension for displaying CPU
temperature, disk temperature, video card temperature (NVIDIA/Catalyst/Bumblebee&NVIDIA),
voltage and fan RPM in GNOME Shell.

%prep
%setup
%autopatch -p1

%build
pushd freon@UshakovVasilii_Github.yahoo.com
# build locale
for f in po/*.po; do
	name=${f:3:${#f}-6}
	mkdir -p locale/"$name"/LC_MESSAGES
	msgfmt "$f" --output-file=locale/"$name"/LC_MESSAGES/freon.mo
done
popd

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions
cp -a freon@UshakovVasilii_Github.yahoo.com %buildroot%_datadir/gnome-shell/extensions/
pushd %buildroot%_datadir/gnome-shell/extensions/freon@UshakovVasilii_Github.yahoo.com

# fix install translations
mv locale %buildroot%_datadir/
rm -r po

# fix install gsettings schemas
mkdir -p %buildroot%_datadir/glib-2.0
mv schemas %buildroot%_datadir/glib-2.0/
popd

# subdir license
cp freon@UshakovVasilii_Github.yahoo.com/icons/material-icons/LICENSE LICENSE-material-icons

%find_lang freon

%files -f freon.lang
%_datadir/gnome-shell/extensions/freon@UshakovVasilii_Github.yahoo.com
%_datadir/glib-2.0/schemas/*.gschema.xml
%doc README.md LICENSE LICENSE-material-icons

%changelog
* Fri Mar 20 2026 Anton Midyukov <antohami@altlinux.org> 61-alt1
- New version 61.

* Thu Oct 16 2025 Anton Midyukov <antohami@altlinux.org> 58-alt4
- metadata.json: add GNOME 49 support

* Tue May 20 2025 Anton Midyukov <antohami@altlinux.org> 58-alt3
- pack material-icons
- update License (add "AND OFL-1.1" for material-icons)

* Mon May 19 2025 Anton Midyukov <antohami@altlinux.org> 58-alt2
- Update Russian translation

* Mon May 19 2025 Anton Midyukov <antohami@altlinux.org> 58-alt1
- initial build
