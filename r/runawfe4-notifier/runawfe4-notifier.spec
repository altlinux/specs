Name: runawfe4-notifier
Version: 4.1.0
Release: alt5

Summary: Runawfe notifier client

License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

#how create git repo from svn
#git svn clone --prefix=svn/ -r4036:HEAD svn://svn.code.sf.net/p/runawfe/code/ . #clone svn repo
#cp -a svn/runawfe-code/RunaWFE-4.x/trunk/projects/notifier runawfe4-notifier/wfe/      #copy to git dir
Source: %name-%version.tar
Source1: runawfe4-notifier.desktop
Source2: runawfe4-notifier.png

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: java libwebkitgtk2
#runawfe4-server #remove server from deps for clients

#BuildPreReq:
#BuildRequires: maven
#BuildArch: noarch

%define runauser _runa
%define runadir /var/lib/runawfe4-notifier

%description
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on JBoss jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

%build
#Add in build requires runawfe4-server
#Run runawfe4-server
#Build and install wfe-web-client
#mvn clean install
#Build notifier
#mvn clean compile assembly:single

#or pre puild web-client mvn clean package
#copy and install
#mvn install:install-file \
# -Dfile=wfe-webservice-client-4.0.6.jar -DartifactId=wfe-webservice-client -DgroupId=ru.runa.wfe -Dversion=4.0.6 -Dpackaging=jar -DgeneratePom=true

%install
mkdir -p %buildroot/%runadir/
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot%_pixmapsdir/
mkdir -p %buildroot%_desktopdir/

cp %SOURCE1 %buildroot%_desktopdir/
cp %SOURCE2 %buildroot/usr/share/pixmaps/

cat >%buildroot/%_bindir/runawfe4-notifier <<EOF
cd %runadir/
java -Dorg.eclipse.swt.browser.UseWebKitGTK=true -cp ".:rtn.jar:swt-gtk.jar" ru.runa.notifier.PlatformLoader
EOF

mkdir -p %buildroot/var/log/runawfe4-notifier/
touch %buildroot/var/log/runawfe4-notifier/rtn.log
ln -s /var/log/runawfe4-notifier/rtn.log %buildroot/%runadir/rtn.log

#in notifier/ dir
%ifarch x86_64
cp target/rtn_x86_64.jar %buildroot/%runadir/rtn.jar
%else
cp target/rtn.jar %buildroot/%runadir/
%endif

#onAppShutdown.wav  onAppStart.wav  onNewTask.wav  unreadTasksNotification.wav
cp target/classes/*.wav %buildroot/%runadir/

#sh standalone.sh -c standalone-runa.xml
#> %buildroot/%runadir/deployments/runa.jar.dodeploy

%check
#check that port listening

%pre
%files
%attr(755,%runauser,root) %dir %runadir/
%_pixmapsdir/*
%_desktopdir/*
/var/log/runawfe4-notifier/*
%runadir/*
%attr(766,root,root) /var/log/runawfe4-notifier/rtn.log
%attr(755,root,root) %_bindir/runawfe4-notifier
%changelog
* Wed Jun 25 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt5
- Workaround pixmaps, fix with new swt

* Tue Apr 22 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt3
- Fixed application.properties

* Tue Apr 22 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt2
- Fixed rtn.log

* Mon Mar 31 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt1
- initial build 4.1.0
