BuildRequires: xvfb-run
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config /usr/bin/python
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-dropbox
%define pygtk2_version 2.24.0

Summary: 		Dropbox extension for caja
Name: 			mate-file-manager-dropbox
Version: 		0.7.1
Release: 		alt1_4
License: 		GNU
Group: 			Graphical desktop/MATE
URL: 			http://pub.mate-desktop.org
Source: 		http://pub.mate-desktop.org/releases/1.4/%{oldname}-%{version}.tar.xz

BuildRequires: 	gtk2-devel
BuildRequires: 	glib2-devel
BuildRequires: 	mate-file-manager-devel
BuildRequires: 	mate-file-manager-extensions
BuildRequires: 	mate-vfs-devel
BuildRequires: 	python-module-pygtk-devel >= %{pygtk2_version}
BuildRequires: 	pygtk2 >= %{pygtk2_version}
BuildRequires: 	python-module-docutils
BuildRequires: 	ImageMagick
BuildRequires: 	libmatenotify-devel
BuildRequires:  mate-common
BuildRequires:  xorg-utils
BuildRequires:  python-module-docutils
BuildRequires:  python-devel

Requires: 		mate-file-manager
Requires: 		glib2
Requires: 		gtk2
Requires: 		libmatenotify
Requires: 		mate-vfs
Requires: 		pygtk2
Requires: 		python-module-docutils
Source44: import.info

%description
Dropbox extension for caja
Dropbox allows you to sync your files online and across your computers automatically.

%prep
%setup -q -n %{oldname}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build
cat > c <<'EOF'
#!/bin/sh
%configure
EOF
chmod 755 ./c
xvfb-run ./c

make %{?_smp_mflags}
# resize icons
for icon in emblem-dropbox-syncing.png emblem-dropbox-unsyncable.png emblem-dropbox-uptodate.png
do
	convert data/emblems/$icon -resize 16x data/emblems/$icon
done

%install
DESTDIR=$RPM_BUILD_ROOT make install
libtool --finish %{_libdir}/caja/extensions-2.0

%files
%doc AUTHORS COPYING INSTALL NEWS README 
%{_bindir}/dropbox
%{_datadir}/caja-dropbox
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/dropbox.*
%{_datadir}/applications/dropbox.desktop
%{_libdir}/caja/extensions-2.0/libcaja-dropbox.*

%changelog
* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_4
- initial release

