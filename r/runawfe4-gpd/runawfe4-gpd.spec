Name: runawfe4-gpd
Version: 4.3.0
Release: alt1

Summary: Runawfe Graphic Process Designer

License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

Source: %name-%version.tar
Source1: runawfe4-gpd.desktop
Source2: runawfe4-gpd.png

Packager: Danil Mikhailov <danil@altlinux.org>

AutoReq: yes,noperl,nopython
Requires: java >= 1.7, libwebkitgtk2
#Requires: libsoup >= 2.48.1

BuildPreReq: rpm-build-compat maven
Provides: osgi(ru.runa.gpd.form.ftl)
BuildRequires: chrpath

%define runauser _runa
%define runadir %_libdir/runawfe4-gpd
%define distrname %(distr_vendor -d)

#Define for Fedora build http://forums.fedoraforum.org/showthread.php?t=182293
%define debug_package %{nil}
#
%define gpd_path gpd_source/plugins/ru.runa.gpd.maven/target/products/RunaWFE_DeveloperStudio/linux/gtk

#gpd copy path for multi arch
%ifarch x86_64
%define gpd_path_arch %{gpd_path}/x86_64/
%else
%define gpd_path_arch %{gpd_path}/x86/
%endif


%description
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on JBoss jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

#how create git repo from svn
#git svn clone --prefix=svn/ -r4036:HEAD svn://svn.code.sf.net/p/runawfe/code/ . #clone svn repo

%build
#use local maven repo
export MAVEN_OPTS="-Dmaven.repo.local=$(pwd)/.m2/repository/" 

cd gpd_source/plugins/
#Online build
#mvn clean package 
#Offline build but not working
#For altlinux need local online build and copy binary files
#mvn -o package #for offline build in git.alt

%install
mkdir -p %buildroot/%runadir/
mkdir -p %buildroot%_pixmapsdir/
mkdir -p %buildroot%_desktopdir/

#in gpd/ dir
cp %SOURCE1 %buildroot%_desktopdir/
cp %SOURCE2 %buildroot%_pixmapsdir/
#cp -a ./* %buildroot/%runadir/ #default gpd copy path for x86 arch

mv %gpd_path_arch/runa-gpd %gpd_path_arch/runawfe4-gpd
chmod 755 %gpd_path_arch/runawfe4-gpd
chrpath -d %gpd_path_arch/libcairo-swt.so
cp -a %gpd_path_arch/* %buildroot/%runadir/
cp -a gpd_source/workspace/ %buildroot/%runadir/

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/runawfe4-gpd <<EOF
#!/bin/sh
gpddir="\$HOME/runawfe4-gpd"

if [ ! -e ""\$gpddir/"" ] ; then
    gpdconfdir="\$HOME/runawfe4-gpd/workspace/.metadata/.plugins/org.eclipse.core.runtime/.settings"
    gpdconf="\$gpdconfdir/ru.runa.gpd.prefs"
    mkdir -p "\$gpddir"
    mkdir -p \$gpdconfdir
    cp -na %runadir/workspace/ "\$gpddir/"
    chown -R \$USER "\$gpddir/"/workspace/

fi

cd "\$gpddir"
%runadir/runawfe4-gpd

EOF

#Enable CKEditor4 by default #TODO remove this hack than released 4.2.0


%check

%pre
%files
%attr(755,root,root) %dir %runadir/
%runadir/*
%_pixmapsdir/*
%_desktopdir/*
%attr(755,root,root) %_bindir/runawfe4-gpd
#%attr(755,root,root) %runadir/workspace/

%changelog
* Tue May 09 2017 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt1
- Updated to 4.3.0 code

* Wed Jul 08 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt13
- Change port to 28080 by runtime .settings

* Thu Jul 02 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt12
- Fix workspace, update to 4.2.0 stable branch code@6444

* Tue Jun 30 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt11
- Remove hash project

* Fri Jun 26 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt10
- Fix error after creating new project

* Mon Jun 15 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt9
- Update workspace

* Thu Jun 11 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt8
- Added binary builds

* Tue Jun 09 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt7
- Fixed https://sourceforge.net/p/runawfe/bugs/905/

* Fri Apr 24 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt5
- Enable binary packing for alt repo

* Fri Apr 24 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt4
- Enable offline maven build

* Fri Mar 13 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt3
- rename patched swt lib from alt

* Fri Mar 13 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt2
- fix forms, use one swt version, need libsoup >= 2.48.1-alt1

* Thu Feb 19 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt1
- initial 4.2 build

* Wed Feb 18 2015 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt5
- alt5 added demo workspace

* Fri Feb 06 2015 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt3
- added my original pom.xml, svn repo pom based on this
- new 4.2rc version for deb
- new 4.2rc version for alt
- added ru.runa.gpd.prefs file

* Wed Aug 20 2014 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt1
- Initial 4.1.2 build

