# TODO: compile from source, fix systray4jd
# TODO: use system jar libs

Name: memoranda
Version: 1.0
Release: alt0.1rc3.1.qa2

License: GPL
Group: Office
Url: http://memoranda.sourceforge.net/

Summary: Open source cross-platform diary manager and a tool for scheduling personal project

Packager: Vitaly Lipatov <lav@altlinux.ru>

%define oversion 1.0-rc3.1-20070407
Source: http://dl.sf.net/memoranda/%name%oversion.tar.bz2

Requires: java >= 1.6.0-4

%description
Memoranda is a personal tool designed to help someone to organize his/her
work and actual projects.
Memoranda is intended for the people, whose daily work is shared between
a few different projects. This is a tool helping to keep your projects,
irrespective of their nature.

%prep
%setup -q -n %name%oversion

%install
mkdir -p %buildroot/%_libdir/%name-%version/
cp -af * %buildroot/%_libdir/%name-%version/
rm -rf %buildroot/%_libdir/%name-%version/lib/{kde,win32}

mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Open Project
Comment=Java based diary manager
Exec=%_bindir/%name
Icon=taskmanagement_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Office;Development;ProjectManagement;
EOF

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name << EOF
cd %_libdir/%name-%version
sh %name.sh
cd ..
EOF

chmod 0755 %buildroot%_bindir/%name

%files
%_bindir/%name
%_libdir/%name-%version/
%_desktopdir/%name.desktop

%changelog
* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt0.1rc3.1.qa2
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for memoranda
  * postun_ldconfig for memoranda
  * update_menus for memoranda
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1rc3.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for memoranda

* Mon Oct 29 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1rc3.1
- initial build for ALT Linux Sisyphus
