Name: teachercp
Version: 0.1
Release: alt2.qa1
Packager: Denis Medvedev <nbr@altlinux.ru>
Source: %name-%version.tar

Summary: Vnc session aggregator and demo transmitter for teacher/student interactions
License: GPL
Group: Education
Url: http://sourceforge.net/projects/teachercp

BuildArch: noarch
#Requires:	x11
Requires(post): desktop-file-utils tightvnc java
Requires(postun): desktop-file-utils

%description
Teacher Control Panel allows a teacher to monitor, lock, and operate student computers and broadcast the teacher's screen to the students. It can work with a mix of Windows and Linux workstations. The screens are captured using VNC, and the teacher's screen is broadcast using multicast.

%prep
%setup -q

%build
%install
mkdir -p %buildroot%_datadir/teachercp
cp -r *  %buildroot%_datadir/teachercp

#Create the desktop entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/Teacher.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Teacher
Comment=Teacher vnc aggregator
Exec=java -jar %_datadir/teachercp/teacher.jar
Terminal=false
Type=Application
StartupNotify=true
Categories=Education;
EOF

cat > %buildroot%_desktopdir/Student.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=Student part for vnc screen aggregator
Exec=java -jar %_datadir/teachercp/student.jar
Terminal=false
Type=Application
StartupNotify=true
Categories=Education;
EOF

#Update menus
%clean
#Install files
%files
%_datadir/teachercp/*
%_datadir/applications/*

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for teachercp
  * postclean-05-filetriggers for spec file

* Mon Jul 30 2007 Denis Medvedev <nbr@altlinux.ru> 0.1-alt2
 Russian HOWTO added 

* Thu Jul 26 2007 Denis Medvedev <nbr@altlinux.ru> 0.1-alt1
Initial ALT release

