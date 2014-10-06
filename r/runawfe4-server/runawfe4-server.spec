Name: runawfe4-server
Version: 4.1.2
Release: alt6

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

%define jbossuser jboss-as
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
mvn clean package -Dappserver=jboss7
#mvn -o package -Dappserver=jboss7 #for offline build in git.alt


%install
#jboss-as-cp -l %buildroot/%runadir
#rm -f %buildroot/%runadir/bin/standalone.sh
mkdir -p %buildroot/%jbossdir/{bin,data,deployments,log,tmp,configuration}
mkdir -p %buildroot/etc/jboss-as/
#FIX correct path to jboss-as/bin
cp %SOURCE1 %buildroot%jbossdir/configuration/
cp %SOURCE3 %buildroot/etc/jboss-as/
mkdir -p %buildroot/%_sbindir/
#FIX JBOSS_BASE_DIR not work in jboss from zip, unused
cat >%buildroot/%_sbindir/runawfe4-server <<EOF
JBOSS_BASE_DIR=%jbossdir su - %jbossuser -s /bin/sh -c "%_datadir/jboss-as/bin/standalone.sh -c standalone-runa.xml" \
&& echo \$$ > /var/run/runawfe4-server.pid;
EOF

cp -a wfe-ear/target/runawfe.ear %buildroot/%jbossdir/deployments/

install -D -m754 %SOURCE2 %buildroot%_initdir/%name
#chown -R %jbossuser %buildroot/%jbossdir/
#start jboss, copy ear to deploy dir and start deploy DONE
#Create user _runa and run
#sh standalone.sh -c standalone-runa.xml
#> deployments/runawfe.ear.dodeploy

%check
#check that port listening

%pre
useradd -d %runadir -r -s %_sbindir/runawfe4-server %runauser >/dev/null 2>&1 || :

%files
/etc/jboss-as/jboss-as-runawfe4-server.conf
%attr(755,%jbossuser,root) %jbossdir/configuration/*
%attr(755,%jbossuser,root) %jbossdir/deployments/*
%attr(755,root,root) %_sbindir/runawfe4-server

%_initdir/%name

%changelog
* Mon Oct 06 2014 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt6
- added deployments dir
- change jbdc to keep db in file
- change jbdc to keep db in file

* Mon Sep 29 2014 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt5
- added new init realisatio
- create etc dir
- fix confict file standalone
- added files
- change standalone attribute
- remove sh -x in init
- fix permission
- added files
- fix files

* Fri Sep 26 2014 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt4
- remove depends from init

* Thu Sep 25 2014 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt3
- added new standalone.xml

* Tue Sep 23 2014 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt2
- initial init.d support

* Mon Aug 18 2014 Danil Mikhailov <danil@altlinux.org> 4.1.2-alt1
- initial build 4.1.2
