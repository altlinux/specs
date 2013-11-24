%set_verify_elf_method rpath=relaxed

Name: plank
Version: 0.5.0
Release: alt4

Summary: Elegant, simple, clean dock
License: GPLv3+
Group: Graphical desktop/Other
Url: https://launchpad.net/plank

Source0: %name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu Oct 10 2013
BuildRequires: gnome-common intltool libbamf3-devel libgee0.8-devel vala-tools
BuildRequires: xvfb-run dbus-tools-gui libgtk+3-devel libwnck3-devel

%description
Plank is a dock enabling you to start applications and manage your windows.

%package -n libplank0
Summary: Library to build a elegant, simple, clean dock
Group: System/Libraries

Requires: libplank-common = %version-%release

%description -n libplank0
Plank is a dock enabling you to start applications and manage your windows.

%package -n libplank-devel
Summary: Library to build a elegant, simple, clean dock (development files)
Group: Development/C

%description -n libplank-devel
Plank is a dock enabling you to start applications and manage your windows.

%package -n libplank-common
Summary: Library to build a elegant, simple, clean dock
Group: Graphical desktop/Other

BuildArch: noarch

# TODO:
# Depends: plank-theme-pantheon

%description -n libplank-common
Plank is a dock enabling you to start applications and manage your windows.

%package -n libplank-doc
Summary: Library to build a elegant, simple, clean dock - documentation
Group: Documentation

BuildArch: noarch

# TODO: re-check
# Suggests: devhelp

%description -n libplank-doc
Plank is a dock enabling you to start applications and manage your windows.

This package contains the documentation.

%package -n libplank-vala
Summary: Vala language bindings for plank library
Group: Development/Other
BuildArch: noarch
Requires: libplank0 = %version-%release

%description -n libplank-vala
This package provides Vala language bindings for plank library.

%prep
%setup -q

%build
%configure \
  --enable-headless-tests
#  --enable-docs
%make_build V=1

#%check
#make check || exit 1

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_sysconfdir/apport/crashdb.conf.d/plank-crashdb.conf
%_bindir/plank
%_datadir/icons/hicolor/*/apps/plank.*
%_man1dir/plank.*
%_desktopdir/plank.desktop
%exclude %_datadir/apport/package-hooks/source_plank.py

%files -n libplank0
%_libdir/libplank.so.*

%files -n libplank-devel
%_libdir/libplank.so
%_includedir/plank
%_pkgconfigdir/plank.pc

%files -n libplank-common
%_datadir/plank/themes

%files -n libplank-doc

%files -n libplank-vala
%_datadir/vala/vapi/plank.deps
%_datadir/vala/vapi/plank.vapi

%changelog
* Sat Nov 23 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt4
- Add vala bindings

* Thu Nov 21 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt3
- Rebuilt with libbamf3.so.2

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt2
- Enable headless tests

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt1
- 0.5.0

* Mon Oct 21 2013 Igor Zubkov <icesik@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Oct 09 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1.bzr857
- build for Sisyphus

