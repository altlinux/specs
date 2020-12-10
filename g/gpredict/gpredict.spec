%define _localstatedir %_var
Name: gpredict
Version: 2.2.1
Release: alt2
Summary: Real-time satellite tracking and orbit prediction program
Group: Communications
License: GPLv2+
Url: https://github.com/csete/gpredict
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: gpredict.desktop
Source2: gpredict.appdata.xml
Patch0: build_fix.patch

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(goocanvas-2.0)
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool >= 0.21
BuildRequires: %_bindir/desktop-file-install

%description
Gpredict is a real time satellite tracking and orbit prediction
program written using the Gtk+ widgets. Gpredict is targeted mainly
towards ham radio operators but others interested in satellite
tracking may find it useful as well. Gpredict uses the SGP4/SDP4
algorithms, which are compatible with the NORAD Keplerian elements.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

rm -fr %buildroot%_desktopdir/gpredict.desktop

desktop-file-install \
    --dir %buildroot%_desktopdir \
    %SOURCE1

mkdir -p %buildroot%_datadir/appdata/
install -m 644 %SOURCE2 %buildroot%_datadir/appdata/%name.appdata.xml

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_datadir/appdata/*%name.appdata.xml
%_datadir/%name
%_desktopdir/*%name.desktop
%_pixmapsdir/gpredict
%_pixmapsdir/gpredict-icon.png
%_man1dir/gpredict*

%changelog
* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.1-alt2
- Fix build with gcc10
- Add appdata metafile

* Wed Mar 28 2018 Anton Midyukov <antohami@altlinux.org> 2.2.1-alt1
- New version 2.2.1

* Sun Sep 03 2017 Anton Midyukov <antohami@altlinux.org> 1.3-alt1.20170617.1
- Initial build for ALT Sisyphus.
