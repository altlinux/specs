Name: ganttproject
Version: 2.0.10
Release: alt1

Summary: GanttProject is a tool for creating a project schedule by means of Gantt chart and resource load chart
License: GPLv2 with library exceptions
Group: Office

Url: http://www.ganttproject.biz/
Source: %name-%version.zip
Packager: Denis Medvedev <nbr@altlinux.ru> 

BuildArch: noarch
BuildRequires: unzip
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
GanttProject is a tool for creating a project schedule by means
of Gantt chart and resource load chart.
With GanttProject you can break down your project into a tree of tasks
and assign human resources that have to work on each task. You can also
establish dependencies between tasks, like "this task can't start
until this one is finished". GanttProject renders your project
using two charts: Gantt chart for tasks and resource load chart
for resources. You may print your charts, generate PDF and HTML
reports, exchange data with Microsoft(R) Project(TM)
and spreadsheet applications.

%prep
%setup

%build

%install
install -d %buildroot%_datadir/%name
install -d %buildroot%_bindir
mv * %buildroot%_datadir/%name/

cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
cd %_datadir/%name
./%name.sh \$@
EOF
chmod 755 %buildroot%_bindir/%name %buildroot%_datadir/%name/%name.sh

#Create the desktop entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=GanttProject
Comment=Project Management
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=Office;Development;ProjectManagement;X-MandrivaLinux-Office-TasksManagement;
EOF

#Create the mime-type for GanttProject
mkdir -p %buildroot%_datadir/mimelnk/application
cat > %buildroot%_datadir/mimelnk/application/x-%name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
MimeType=application/x-ganttproject
Comment=GanttProject File
Comment[es]=Archivo de GanttProject
Icon=%name
Type=MimeType
Patterns=*.gan;
X-KDE-AutoEmbed=false
[Property::X-KDE-NativeExtension]
Type=QString
Value=.gan
EOF

#Associate the mime-type with GanttProject
mkdir -p %buildroot%_datadir/application-registry
cat > %buildroot%_datadir/application-registry/%name.applications << EOF
ganttproject
        command=ganttproject
        name=GanttProject Project Managment Tool
        can_open_multiple_files=true
        expects_uris=non-file
        requires_terminal=false
        supported_uri_schemes=file,http,ftp
        mime_types=application/x-ganttproject
EOF

#Copy the icon
install -D %buildroot%_datadir/%name/plugins/net.sourceforge.ganttproject_2.0.0/data/resources/icons/ganttproject.png %buildroot%_datadir/icons/hicolor/32x32/apps/%name.png

%files
%_desktopdir/*
%_datadir/application-registry/*
%_datadir/mimelnk/application/*
%_datadir/icons/hicolor/32x32/apps/*
%_bindir/%name
#_datadir/%name/%name.sh
%_datadir/%name

%changelog
* Fri Dec 23 2011 Michael Shigorin <mike@altlinux.org> 2.0.10-alt1
- 2.0.10
- ensure that the wrapper script is executable

* Tue Feb 08 2011 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt3
- Removed colombia calendar and es desc from spec

* Fri Sep 10 2010 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt2
- Building by nbr, checked

* Thu Sep 09 2010 Sergey Kurakin <kurakin@altlinux.org> 2.0.2-alt1
- Fixed trivial but fatal bug in wrapper
- Fixed repocop issue desktop-file-validate
- License corrected
- Url corrected
- Spec cleanup

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.2-alt0.2.qa1
- NMU (by repocop): the following fixes applied:
  * shared-mime-info for ganttproject
  * update_menus for ganttproject
  * postclean-05-filetriggers for spec file

* Sat Feb 24 2007 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt0.2
- Added full source, after discovery that sources are missing.
  Sources were in ganttproject.cvs.sourceforge.net repository

* Tue Dec 12 2006 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt0.1
- ALT packaging

* Mon Aug 21 2006 Juan Luis Baptiste <jbaptiste@merlinux.org> 2.0.2-2mer
- Added creation of %_libdir/menu/ganttproject file so menus work
  in PCLinuxOS.

* Fri Aug 11 2006 Juan Luis Baptiste <jbaptiste@merlinux.org> 2.0.2-1mer
- Updated to 2.0.2.

* Thu Aug 10 2006 Juan Luis Baptiste <jbaptiste@merlinux.org> 2.0.1-1mer
- Initial version.
- Added patch to include Holydays calendar of Colombia for year 2006.

