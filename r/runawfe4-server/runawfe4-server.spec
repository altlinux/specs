Name: runawfe4-server
Version: 4.3.0
Release: alt20

Summary: Runawfe server

License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

#how create git repo from svn
#git svn clone --prefix=svn/ -r4036:HEAD svn://svn.code.sf.net/p/runawfe/code/ . #clone svn repo
#cp -a svn/runawfe-code/RunaWFE-4.x/trunk/projects/wfe runawfe4-server/wfe/      #copy to git dir
Source: %name-%version.tar
Source1: standalone-runa.xml
Source2: runawfe4-server
Source3: jboss-as-runawfe4-server.conf
Source4: runawfe4-server.service
Source5: runawfe4-server-start.desktop
Source6: runawfe4-server.png
Source7: runawfe4-server-stop.desktop

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: jboss-as-vanilla >= 7.1.1-alt9
#Provides:
#Conflicts:

#BuildPreReq:
# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: apache-commons-cli atinject google-guice guava java java-devel jpackage-utils maven maven-wagon nekohtml plexus-cipher plexus-classworlds plexus-containers-component-annotations plexus-interpolation plexus-sec-dispatcher plexus-utils python3-base sisu tzdata tzdata-java xbean xerces-j2 xml-commons-jaxp-1.4-apis
BuildRequires: aether rpm-build-compat guava
BuildRequires: xmvn maven maven-local maven-clean-plugin maven-install-plugin maven-deploy-plugin maven-site-plugin maven-antrun-plugin maven-assembly-plugin maven-dependency-plugin maven-release-plugin
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: jboss-as-vanilla
BuildArch: noarch

%define jbossuser jboss-as
%define runauser _runa
%define runadir /var/lib/%name
%define jbossdir %_datadir/jboss-as/standalone
%define distrname ALTLinux

%description
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on JBoss jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

%build
export MAVEN_OPTS="-Dmaven.repo.local=$(pwd)/.m2/repository/"
#export MAVEN_OPTS="-Dmaven2.offline.mode -Dmaven2.ignore.versions -Dmaven2.usejppjars"

cd wfe-app/repository/
./add_dependencies.sh
cd ..

%if %distrname == "Ubuntu" ||  %distrname == "Debian"
mvn clean package -Dappserver=jboss7
%else
%mvn_build -f -- -X -Dappserver=jboss7
#exit 1
%endif

%install
#jboss-as-cp -l %buildroot/%runadir
#rm -f %buildroot/%runadir/bin/standalone.sh
mkdir -p %buildroot/%jbossdir/{bin,data,deployments,log,tmp,configuration}
mkdir -p %buildroot/etc/jboss-as/
mkdir -p %buildroot/lib/systemd/system/
mkdir -p %buildroot%_desktopdir/
mkdir -p %buildroot%_pixmapsdir/

#FIX correct path to jboss-as/bin
cp %SOURCE1 %buildroot%jbossdir/configuration/
cp %SOURCE3 %buildroot/etc/jboss-as/
#cp %SOURCE4 %buildroot/lib/systemd/system/
cp %SOURCE5 %buildroot%_desktopdir/
cp %SOURCE6 %buildroot%_pixmapsdir/
cp %SOURCE7 %buildroot%_desktopdir/

mkdir -p %buildroot/%_sbindir/
mkdir -p %buildroot%_initdir/

%if %distrname == "Ubuntu" ||  %distrname == "Debian"

# Explain of server execution on:
# 1) deb we can runs like:
#  -  a program from bin dir
#  -  a very simple service - start is executing bin in a background (because we havent /etc/init.d/functions on this)
# 2) AltLinux and Fedora runs like:
#  -  a program (runs service start)
#  -  full supported service (starts jboss with runa config)

cat >%buildroot/%_sbindir/%name <<EOF
#!/bin/sh
JBOSS_BASE_DIR=%jbossdir su - jboss-as -s /bin/sh -c "/usr/share/jboss-as/bin/standalone.sh -c standalone-runa.xml"

EOF

cat >%buildroot%_initdir/%name <<EOF
#!/bin/sh
if [ "\$1" = "start" ] ; then
    #rm -f %_runtimedir/%name.pid
    #ln -s %_runtimedir/jboss-as/jboss-as-standalone.pid %_runtimedir/%name.pid
    #TODO BUG not work macros %_runtimedir !
    %_sbindir/%name > /var/log/%name 2>&1 &
fi
if [ "\$1" = "stop" ] ; then
    %jbossdir/../bin/jboss-cli.sh --connect --command=:shutdown
    #/usr/share/jboss-as/bin/
fi

EOF

%else

cat >%buildroot%_initdir/%name <<EOF

#
# %name - runawfe server
#
# chkconfig: 2345 99 1
# processname: runawfe
# config: /etc/runawfe
# pidfile: %_runtimedir/%name.pid
#
### BEGIN INIT INFO
# Provides: %name
# Default-Start: 2 3 4 5
# Short-Description: runawfe server
# Description: runawfe server or botstation daemon
### END INIT INFO

rm -f %_runtimedir/%name.pid
ln -s %_runtimedir/jboss-as/jboss-as-standalone.pid %_runtimedir/%name.pid

JBOSS_CONF=/etc/jboss-as/jboss-as-%name.conf %_initdir/jboss-as-standalone "\$1"

EOF

cat >%buildroot/%_sbindir/%name <<EOF
#!/bin/sh
%_initdir/%name "start"

EOF

%endif


cat >%buildroot/lib/systemd/system/%name.service <<EOF

[Unit]
Description=RunaWFE server daemon

[Service]
Type=simple
ExecStart=/usr/sbin/%name
PIDFile=%_runtimedir/%name.pid

EOF


cp -a wfe-ear/target/runawfe.ear %buildroot/%jbossdir/deployments/


#TEMPORARY!!!!
#install -D -m754 %SOURCE2 %buildroot%_initdir/%name


#chown -R %jbossuser %buildroot/%jbossdir/
#start jboss, copy ear to deploy dir and start deploy DONE
#Create user _runa and run
#sh standalone.sh -c standalone-runa.xml
#> deployments/runawfe.ear.dodeploy

%check
#check that port listening

%pre
useradd -d %runadir -r -s %_sbindir/%name %runauser >/dev/null 2>&1 || :

%files
/etc/jboss-as/jboss-as-%name.conf
%_pixmapsdir/*
%_desktopdir/*
%attr(755,%jbossuser,root) %jbossdir/configuration/*
%attr(755,%jbossuser,root) %jbossdir/deployments/*
%attr(755,root,root) %_sbindir/%name
%attr(755,root,root) %_initdir/%name
%attr(644,root,root) /lib/systemd/system/%name.service

%changelog
* Tue Feb 07 2017 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt20
- Updated to 4.3.0 code 

* Thu Jul 02 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt19
- Update to trunk code@6444

* Fri Jun 26 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt18
- Update to trunk code@6397

* Wed Jun 17 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt17
- Update to trunk code@6345

* Wed Jun 10 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt16
- Revert save db to dir

* Tue Jun 09 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt15
- Update standalone-runa-local.xml, save db in memory, added mvcc=true

* Wed Apr 22 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt14
- Change gksudo on gksu

* Wed Apr 22 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt13
- Fix start desktop

* Tue Apr 21 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt12
- Rewrite start service for deb 

* Mon Apr 20 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt11
- Added builde-req rpm-build-compat

* Mon Apr 20 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt10
- New rc version with offline maven build

* Thu Apr 16 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt9
- Added Ubuntu in %if distr

* Wed Apr 15 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt8
- Fixed bug in initscript for alt

* Wed Apr 15 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt7
- Change start script for debian

* Wed Mar 25 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt5
- Enable jboss listening from all network 0.0.0.0

* Tue Mar 24 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt4
- Added creation desktop and pixmap dir

* Mon Mar 23 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt3
- Change port, added desktop file with gksudo

* Thu Feb 19 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt2
- alt2

* Thu Feb 19 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt1
- initial build 4.2.0
