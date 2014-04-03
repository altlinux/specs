Name: runawfe4-server
Version: 4.1.0
Release: alt3

Summary: Runawfe server

License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

#how create git repo from svn
#git svn clone --prefix=svn/ -r4036:HEAD svn://svn.code.sf.net/p/runawfe/code/ . #clone svn repo
#cp -a svn/runawfe-code/RunaWFE-4.x/trunk/projects/wfe runawfe4-server/wfe/      #copy to git dir
Source: %name-%version.tar
Source1: standalone-runa.xml

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: jboss-as-vanilla
#Provides:
#Conflicts:

#BuildPreReq:
# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: apache-commons-cli atinject google-guice guava java java-devel jpackage-utils maven maven-wagon nekohtml plexus-cipher plexus-classworlds plexus-containers-component-annotations plexus-interpolation plexus-sec-dispatcher plexus-utils python3-base sisu tzdata tzdata-java xbean xerces-j2 xml-commons-jaxp-1.4-apis
BuildRequires: aether

BuildRequires: maven jboss-as-vanilla
BuildArch: noarch

%define runauser _runa
%define runadir /var/lib/runawfe4-server
%define jbossdir %_datadir/jboss-as/standalone

%description
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on JBoss jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

%build

cp -a .m2/ /tmp/.m2/
export MAVEN_OPTS="-Dmaven.repo.local=/tmp/.m2"

cd wfe-app/repository/
./add_dependencies.sh
cd ..
mvn -o clean package -Dappserver=jboss7

%install
#jboss-as-cp -l %buildroot/%runadir
#rm -f %buildroot/%runadir/bin/standalone.sh
mkdir -p %buildroot/%jbossdir/{bin,data,deployments,log,tmp,configuration}

#FIX correct path to jboss-as/bin
cp %SOURCE1 %buildroot%jbossdir/configuration/
mkdir -p %buildroot/%_sbindir/
#FIX JBOSS_BASE_DIR not work in jboss from zip, unused
cat >%buildroot/%_sbindir/runawfe4-server <<EOF
JBOSS_BASE_DIR=%jbossdir %_datadir/jboss-as/bin/standalone.sh -c standalone-runa.xml \
& echo $! > /var/run/runawfe4-server.pid;
EOF

mkdir -p %buildroot/%jbossdir/deployments/
cp -a wfe-ear/target/runawfe.ear %buildroot/%jbossdir/deployments/

#start jboss, copy ear to deploy dir and start deploy DONE
#Create user _runa and run
#sh standalone.sh -c standalone-runa.xml
#> deployments/runawfe.ear.dodeploy

%check
#check that port listening

%pre
useradd -d %runadir -r -s %_sbindir/runawfe4-server %runauser >/dev/null 2>&1 || :

%files
%jbossdir/
%attr(755,root,root) %dir %jbossdir/
#%dir %runadir/configuration/
#%config(noreplace) %runadir/configuration/*
#%attr(755,%runauser,root) %dir %runadir/data/
#%runadir/deployments/
#%attr(755,%runauser,root) %dir %runadir/log/
#%attr(755,%runauser,root) %dir %runadir/tmp/

%attr(755,root,root) %_sbindir/runawfe4-server

%changelog
* Thu Apr 03 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt3
- set maven offline build

* Mon Mar 31 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-alt2
- added maven cache for ofline build

* Mon Mar 24 2014 Danil Mikhailov <danil@altlinux.org> 4.1.0-eter1
- initial build 4.1.0
