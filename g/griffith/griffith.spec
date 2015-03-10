# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)
Name: griffith
Version: 0.12.1
Release: alt2
Summary: Media collection manager
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: Databases
License: GPLv2+
Url: http://www.griffith.cc
Source0: http://launchpad.net/%name/trunk/%version/+download/%name-%version.tar.gz
BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: gettext
Requires: pygtk2
Patch1: tree_view_fix.patch
Patch2: sqlalchemy_0.7_upgrade.patch
Source44: import.info

%description
Griffith is a media collection manager application. Adding items to the
collection is as quick and easy as typing the film title and selecting a
supported source. Griffith will then try to fetch all the related information
from the Web.

This Version comes with SQLite support. You need to install
 * the package "MySQL-python" for MySQL-support
 * the package "python-psycopg2" for PostgreSQL-support

%prep
%setup
%patch1 -p1 -b .orig
%patch2 -p1 -b .orig

find -iname "*.mo" -exec rm -f {} \;

iconv -f iso-8859-1 -t utf-8 docs/pl/%name.1 |sed 's|\r||g' > docs/pl/%name.1.utf8
touch -c -r docs/pl/%name.1 docs/pl/%name.1.utf8
mv docs/pl/%name.1.utf8 docs/pl/%name.1

%build
make -C po dist %{?_smp_mflags}

%install
make install \
     INSTALL="install -p" \
     DESTDIR=%buildroot

rm -f %buildroot%_bindir/%name

cat > %buildroot/%_bindir/%name << EOF
#!/bin/bash
%_datadir/%name/lib/%name
EOF

chmod +x %buildroot/%_bindir/%name

desktop-file-install \
       --dir=%buildroot/%_datadir/applications/ \
%buildroot/%_datadir/applications/%name.desktop
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%{name}*
%_datadir/pixmaps/%{name}*
%_mandir/man1/%{name}*
%_mandir/*/man1/%{name}*
%config(noreplace) %_sysconfdir/bash_completion.d/%name

%changelog
* Tue Mar 10 2015 Ilya Mashkin <oddity@altlinux.ru> 0.12.1-alt2
- build for Sisyphus

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1_7
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1_6
- initial fc import

