%define rname python-caja

Name: python3-module-caja
Version: 1.26.0
Release: alt1
Summary: Python bindings for Caja
Group: Development/Other
License: GPLv2+ and LGPLv2+
URL: http://mate-desktop.org

Source: %rname-%version.tar
Patch: %rname-%version.patch

Conflicts: python-module-caja

BuildRequires: gtk-doc mate-file-manager-devel python-module-pygobject3-common-devel python3-dev rpm-build-python3

%description
Python bindings for Caja

%package -n python3-module-caja-devel
Summary: Python bindings for Caja
Group: Development/Other
Requires: %name = %version-%release
Conflicts: python-module-caja-devel

%description -n python3-module-caja-devel
Python bindings for Caja

%prep
%setup -n %rname-%version -q
%patch -p1

%build
%autoreconf
%configure \
     --disable-static \
     --enable-gtk-doc

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %rname --with-gnome --all-name

%files -n python3-module-caja -f %rname.lang
%doc README AUTHORS COPYING NEWS
%_libdir/caja/extensions-2.0/libcaja-python.so
%_datadir/caja/extensions/libcaja-python.caja-extension

%files -n python3-module-caja-devel
%_docdir/python-caja
%_pkgconfigdir/caja-python.pc
%_datadir/gtk-doc/html/caja-python

%changelog
* Tue Aug 10 2021 Valery Inozemtsev <shrek@altlinux.ru> 1.26.0-alt1
- 1.26.0

* Wed Mar 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.24.0-alt1
- initial release

