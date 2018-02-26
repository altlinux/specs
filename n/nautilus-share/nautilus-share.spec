Name:           nautilus-share
Version:        0.7.3
Release:        alt1
Packager:       Alex Negulescu <alecs@altlinux.org>
License:        GPLv2+
Summary:        Nautilus Share allows you to quickly share a folder from the GNOME Nautilus file manager without requiring root access.
Url:            http://git.gnome.org/nautilus-share
Group:          Graphical desktop/GNOME
Source:         http://download.gnome.org/sources/nautilus-share/0.7/%{name}-%{version}.tar.bz2
Requires:       nautilus >= 2.10
Requires:       samba >= 3.0.23
Requires:       %name-common = %version-%release
BuildRequires:  glibc-devel-static intltool libnautilus-devel

%description
Application for the GNOME desktop integrated in Nautilus, that allows
simple use of Nautilus shares without signing in as root.

Features:
* A new entry in your Nautilus right-click menu with a
   nice icon.

* A simple dialog to share your folder, which allows you to choose a
   name and decide whether to make it read-only.

* Possibility to access it from the Properties tab of your folder.

* Possibility to see whether a share name already exists by simply
   typing it.

* Nautilus displays a palm icon to visually show you which folders are
   shared.

%package common
Summary: Common files for nautilus-share.
Group: Graphical desktop/GNOME
BuildArch: noarch

%description common
Provides common files for nautilus-share.

%prep
%setup -q

%build
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot
%find_lang %name

%files common -f %name.lang
%defattr (-, root, root)
%doc AUTHORS COPYING README
%_datadir/nautilus-share/*

%files
%defattr (-, root, root)
%_libdir/nautilus/extensions-3.0/*

%changelog
* Fri Sep 2 2011 Alex Negulescu <alecs@altlinux.org> 0.7.3-alt1
- Initial build, 0.7.3-alt1.
