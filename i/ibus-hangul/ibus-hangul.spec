%global require_ibus_version 1.3.99
%global require_libhangul_version 0.1.0

Name:       ibus-hangul
Version:    1.5.5
Release:    alt1
Summary:    The Hangul engine for IBus input platform
License:    GPLv2+
Group:      System/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    %name-%version.tar
# VCS: git://github.com/choehwanjin/ibus-hangul.git
# upstreamed patches
#Patch0:     ibus-hangul-HEAD.patch
# not upstreamed patches
Patch1:     ibus-hangul-setup-abspath.patch

%add_python3_path %_datadir/%name
BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: libgtk+3-devel
BuildRequires: python3-devel
BuildRequires: gettext-devel, automake, libtool
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: libhangul-devel >= %{require_libhangul_version}
BuildRequires: pkgconfig
BuildRequires: libibus-devel >= %{require_ibus_version}
BuildRequires: desktop-file-utils

#Requires:   libibus >= %{require_ibus_version}
#Requires:   libhangul >= %{require_libhangul_version}

%description
The Hangul engine for IBus platform. It provides Korean input method from
libhangul.

%prep
%setup -q
%patch1 -p1 -b .setup-abspath

#№autopoint -f
#AUTOPOINT='intltoolize --automake --copy' autoreconf -fi
%autoreconf

%build
%configure --disable-static %{?_with_hotkeys} --with-python=python3
# make -C po update-gmo
make %{?_smp_mflags}

%install
%makeinstall_std

rm -f ${RPM_BUILD_ROOT}%{_bindir}/ibus-setup-hangul
sed -i 's!^Exec=ibus-setup-hangul!Exec=%{_libexecdir}/ibus-setup-hangul!' ${RPM_BUILD_ROOT}%{_datadir}/applications/ibus-setup-hangul.desktop

desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/ibus-setup-hangul.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-hangul
%{_libexecdir}/ibus-setup-hangul
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/*
%{_datadir}/glib-2.0/schemas/* 
%_desktopdir/ibus-setup-hangul.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/org.freedesktop.ibus.engine.hangul.metainfo.xml

%changelog
* Sun Apr 30 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- New version.

* Fri Oct 16 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.4-alt1
- New version.

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt1
- New version.

* Wed Aug 21 2019 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt2
- rebuild with python3

* Sun Aug 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- New version.

* Fri Nov 28 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- New version
- Build from upstream Git repository
  git://github.com/choehwanjin/ibus-hangul.git

* Fri May 30 2014 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Import from Fedora

