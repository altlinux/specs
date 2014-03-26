Name: runawfe4-gpd
Version: 4.1.0
Release: alt1

Summary: Runawfe Graphic Process Designer

License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

#how create git repo from svn
#git svn clone --prefix=svn/ -r4036:HEAD svn://svn.code.sf.net/p/runawfe/code/ . #clone svn repo
#export in eclipse like eclipse product, read http://wf.runa.ru/rus/doc/DesignerDeveloperGuide
#cp -a ~/workspace/target/eclipse/ runawfe4-gpd/gpd/        #copy to git dir
Source: %name-%version.tar
Source1: runawfe4-gpd.desktop
Source2: runawfe4-gpd.png

Packager: Danil Mikhailov <danil@altlinux.org>

AutoReq: yes,noperl,nopython
Requires: java >= 1.7 libwebkitgtk2
Provides: osgi(ru.runa.gpd.form.ftl)
BuildRequires: chrpath

%define runauser _runa
%define runadir /usr/lib/runawfe4-gpd

%description
RunaWFE is a free OpenSource business process management system. It is delivered 
under LGPL licence. RunaWFE is based on JBoss jBPM and Activiti. It provides rich 
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

%build
#take binary from http://sourceforge.net/projects/runawfe/files/SRC%20and%20BIN%20files/4.1.0/RunaWFE%20Developer%20Studio/

%install 
mkdir -p %buildroot/%runadir/
mkdir -p %buildroot/usr/share/pixmaps/
mkdir -p %buildroot/usr/share/applications/

#in gpd/ dir
cp %SOURCE1 %buildroot/usr/share/applications/
cp %SOURCE2 %buildroot/usr/share/pixmaps/
#cp -a ./* %buildroot/%runadir/ #default gpd copy path for x86 arch

#gpd copy path for multi arch 
%ifarch x86_64
chrpath -d gpd_x86_64/libcairo-swt.so
cp -a gpd_x86_64/* %buildroot/%runadir/
%else
cp -a gpd/* %buildroot/%runadir/
%endif

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/runawfe4-gpd <<EOF
#!/bin/sh
gpddir="\$HOME/runawfe4-gpd"
mkdir -p "\$gpddir"
cd "\$gpddir"
%runadir/runawfe4-gpd
EOF

%check

%pre

%files
%attr(755,root,root) %dir %runadir/
%runadir/*
/usr/share/pixmaps/*
/usr/share/applications/*
%attr(755,root,root) %_bindir/runawfe4-gpd
#%attr(755,root,root) %runadir/workspace/

%changelog
* Wed Mar 26 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt1
- GPD 4.1.0 binary

