Name: moka-icon-theme
Version: 5.3.5
Release: alt2
Summary: Moka icon theme
Group: Graphical desktop/GNOME
License: GPL-3.0+
Url: https://github.com/snwh/moka-icon-theme
Source: %name-%version.tar
BuildArch: noarch

%description
Moka is a stylized Linux desktop icon set, designed to be clear, simple and
consistent.

%prep
%setup

# add xreader icons
for n in $(find Moka -name 'qpdfview.png'); do
    cp $n `dirname $n`/xreader.png
done

%build
%define _configure_script ./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING LICENSE_* README.md
%_datadir/icons/Moka

%changelog
* Mon Aug 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.3.5-alt2
- add xreader icons (copy from qpdfview)

* Mon Mar 27 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.3.5-alt1
- first build for ALT Linux
