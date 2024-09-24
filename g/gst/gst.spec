%define _unpackaged_files_terminate_build 1

Name: gst
Version: 0.7.6
Release: alt3

Summary: System utility designed to stress and monitor various hardware components
License: GPL-3.0
Group: Development/Tools
Url: https://gitlab.com/leinardi/gst

BuildArch: noarch

Source: %name-%version.tar
Patch0: gst-0.7.6-alt-remove-distutils-dependency.patch
Patch1: gst-0.7.6-alt-dmidecode.patch

# Runtime dependencies from upstream (Python dependencies listed in requirements.txt)
Requires: dmidecode
Requires: stress-ng
Requires: lm_sensors3
Requires: gobject-introspection
Requires: python3-module-humanfriendly
Requires: python3-module-injector
Requires: python3-module-peewee
Requires: python3-module-psutil
Requires: python3-module-pygobject3
Requires: python3-module-pyxdg
Requires: python3-module-yaml
Requires: python3-module-requests
Requires: python3-module-rx

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gobject-introspection-devel

%description
GST is a GTK system utility designed to stress and monitor various hardware
components like CPU and RAM.

%prep
%setup
%patch0 -p1
%patch1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md CHANGELOG.md
%_bindir/%name
%_desktopdir/com.leinardi.gst.desktop
%_datadir/%name/
%python3_sitelibdir/%name/
%_iconsdir/hicolor/*/apps/com.leinardi.gst*.*
%_datadir/metainfo/com.leinardi.gst.appdata.xml
%_datadir/dbus-1/services/com.leinardi.gst.service
%_datadir/glib-2.0/schemas/com.leinardi.gst.gschema.xml

%changelog
* Tue Jul 23 2024 Vladislav Glinkin <smasher@altlinux.org> 0.7.6-alt3
- Change path to dmidecode (Closes: #49226)

* Mon Nov 06 2023 Vladislav Glinkin <smasher@altlinux.org> 0.7.6-alt2
- Rebuild with 'gst-0.7.6-alt-remove-distutils-dependency.patch'

* Sat Oct 28 2023 Vladislav Glinkin <smasher@altlinux.org> 0.7.6-alt1
- Initial build for ALT

