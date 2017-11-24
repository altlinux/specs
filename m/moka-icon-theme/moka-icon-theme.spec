Name: moka-icon-theme
Version: 5.3.6
Release: alt1
Summary: Moka icon theme
Group: Graphical desktop/GNOME
License: CC-BY-SA-4.0, GPL-3.0+
Url: https://github.com/snwh/moka-icon-theme
Source: %name-%version.tar
Patch0: %name-%version-alt-add-xreader-icons.patch
BuildArch: noarch

%description
Moka is a stylized Linux desktop icon set, designed to be clear, simple and
consistent.

%prep
%setup
%patch0 -p1

%build
%define _configure_script ./autogen.sh
%configure

%install
%makeinstall_std

%files
%doc AUTHORS COPYING LICENSE_* README.md
%_datadir/icons/Moka

%changelog
* Fri Nov 24 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.3.6-alt1
- New version 5.3.6 and change build scheme to tag

* Mon Aug 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.3.5-alt2
- Add xreader icons (copy from qpdfview)

* Mon Mar 27 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.3.5-alt1
- First build for ALT Linux
