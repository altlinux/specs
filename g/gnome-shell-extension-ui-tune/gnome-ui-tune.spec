%define _unpackaged_files_terminate_build 1

%define extdir %_datadir/gnome-shell/extensions
%define _name gnome-ui-tune
%define uuid %_name@itstime.tech
%define schema_file schemas/org.gnome.shell.extensions.%_name.gschema.xml

Name: gnome-shell-extension-ui-tune
Version: 1.10.0
Release: alt2
Summary: Tunes overview UI of the gnome 40 a bit
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/axxapy/gnome-ui-tune
Vcs: https://github.com/axxapy/gnome-ui-tune
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 45
BuildRequires: %_bindir/glib-compile-schemas

%description
Simple gnome-shell (v4x) extension that tunes overview UI to make it more
usable.

%prep
%setup
%autopatch -p1

%build
%make_build gettext uuid=%uuid

%install
install -Dpm0644 metadata.json %buildroot%extdir/%uuid/metadata.json
install -Dpm0644 extension.js %buildroot%extdir/%uuid/extension.js
install -Dpm0644 prefs.js %buildroot%extdir/%uuid/prefs.js
cp -pr src %buildroot%extdir/%uuid
install -Dm0644 %schema_file -t %buildroot%_datadir/glib-2.0/schemas/

# Install locales without po files
find locale -maxdepth 1 -type f -delete
cp -pr locale %buildroot%_datadir
%find_lang --with-gnome %uuid

%files -f %uuid.lang
%_datadir/glib-2.0/%schema_file
%extdir/%uuid
%doc README.md

%changelog
* Mon Aug 25 2025 Alexander Davydzik <paladindev@altlinux.org> 1.10.0-alt2
- fixed gschema & locale paths

* Tue Mar 25 2025 Alexander Davydzik <paladindev@altlinux.org> 1.10.0-alt1
- initial build
