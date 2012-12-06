%define api_ver 3.0

Name:           nemo-share
Version:        1.0.0
Release:        alt1
Packager:       Vladimir Didenko <cow@altlinux.org>
License:        GPLv2+
Summary:        Nemo Share allows you to quickly share a folder from the Cinnamon Nemo file manager without requiring root access.
Url:            https://github.com/linuxmint/nemo-extensions/
Group:          Graphical desktop/GNOME
Source:         %name-%version.tar
Requires:       nemo >= 1.1.2-alt2
Requires:       samba >= 3.0.23
Requires:       %name-common = %version-%release
BuildRequires:  glibc-devel-static intltool libnemo-devel

%description
Application for the Cinnamon desktop integrated in Nemo, that allows
simple use of Nemo shares without signing in as root.

Features:
* A new entry in your Nemo right-click menu with a
   nice icon.

* A simple dialog to share your folder, which allows you to choose a
   name and decide whether to make it read-only.

* Possibility to access it from the Properties tab of your folder.

* Possibility to see whether a share name already exists by simply
   typing it.

* Nemo displays a palm icon to visually show you which folders are
   shared.

%package common
Summary: Common files for nemo-share.
Group: Graphical desktop/GNOME
BuildArch: noarch

%description common
Provides common files for nemo-share.

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
%_datadir/nemo-share/*

%files
%defattr (-, root, root)
%_libdir/nemo/extensions-%api_ver/*

%changelog
* Thu Dec 6 2012 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- Initial build, 1.0.0-alt1 (closes: #27996).
