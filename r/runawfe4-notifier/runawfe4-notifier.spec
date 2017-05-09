Name: runawfe4-notifier
Version: 4.3.0
Release: alt1

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

Requires: java libwebkitgtk2

BuildPreReq: rpm-build-compat
BuildRequires: java-devel maven maven-local xmvn maven-clean-plugin maven-install-plugin maven-deploy-plugin maven-site-plugin maven-dependency-plugin maven-release-plugin
#BuildRequires: 
#BuildArch: noarch

%define runauser _runa
%define runadir /var/lib/runawfe4-notifier
%define distrname ALTLinux

%description
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on JBoss jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

%build
export MAVEN_OPTS="-Dmaven.repo.local=$(pwd)/.m2/repository/"

xmvn install:install-file -Dfile=wfe-webservice-client.jar -DartifactId=wfe-webservice-client -DgroupId=ru.runa.wfe -Dversion=4.3.0-SNAPSHOT -Dpackaging=jar -DgeneratePom=true
xmvn package

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


%if %distrname == "Debian"
#removed special version for debian
%define rtn_path target/rtn
%else
%define rtn_path target/rtn
%endif

#gpd copy path for multi arch
%define rtn_path_arch %{rtn_path}.jar

#in notifier/ dir
cp %rtn_path_arch %buildroot/%runadir/rtn.jar

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
* Tue May 09 2017 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt1
- Updated to 3.4.0 code

* Fri Jul 03 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt4
- Update to trunk code@6444 stable 4.2.0

* Tue Apr 21 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt3
- Update server port to 28080

* Fri Feb 20 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt2
- patched, change swt to 4.233 for alt

* Thu Feb 19 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt1
- initial build 4.2.0

* Fri Jul 18 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt16
- Added pre build req rpm-build-compat for distr_vendor

* Fri Jul 18 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt13
- Fixed SWTError: No more handles, Ubuntu binary

* Tue Jul 15 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt12
- Fix alt x86

* Thu Jul 10 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt11
- Remove noarch

* Thu Jul 10 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt10
- Fix arch

* Thu Jul 10 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt9
- Fix target path

* Thu Jul 10 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt8
- Added Debian support

* Sun Jul 06 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt7
- Change arch to noarch

* Fri Jul 04 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt6
- Fix restore from taskbar

* Wed Jun 25 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt5
- Workaround pixmaps, fix with new swt

* Tue Apr 22 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt3
- Fixed application.properties

* Tue Apr 22 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt2
- Fixed rtn.log

* Mon Mar 31 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt1
- initial build 4.1.0
