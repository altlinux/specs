Name: jboss-as-vanilla
Version: 7.1.1
Release: alt1

Summary: jboss-as-vanilla - Vanilla Edition Of JBoss Application Server

License: LGPLv2 and ASL 2.0
Group: System/Servers
Url: http://www.jboss.org/jbossas

#how create git repo from zip
#wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-as-7.1.1.Final.zip
#unzip jboss-as-7.1.1.Final.zip
Source: %name-%version.tar
Source1: jboss-as-cp

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: java >= 1.7
#Provides:
#Conflicts:

#BuildPreReq:
BuildArch: noarch

%define jbossuser jboss-as
#jboss-as:x:185:185:JBoss AS:%_datadir/jboss-as:/bin/nologin
%define jbossdir %_datadir/jboss-as

%description
JBoss Application Server 7 is the latest release in a series of JBoss
Application Server offerings. JBoss Application Server 7, is a fast,
powerful, implementation of the Java Enterprise Edition 6 specification.
The state-of-the-art architecture built on the Modular Service Container
enables services on-demand when your application requires them.

%prep
%setup

%build
#nothing to do

%install
#in jboss-as
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%jbossdir/
cp %SOURCE1 %buildroot/%_bindir/

cp -a ./* %buildroot/%jbossdir/
rm -f %buildroot/%jbossdir/bin/*\.bat
mkdir -p %buildroot/%jbossdir/docs/examples/properties/
cp %buildroot/%jbossdir/standalone/configuration/logging.properties %buildroot/%jbossdir/docs/examples/properties/
cp %buildroot/%jbossdir/standalone/configuration/mgmt-users.properties %buildroot/%jbossdir/docs/examples/properties/
cp %SOURCE1 %buildroot/%jbossdir/docs/examples/properties/standalone-web.xml
#TODO FIX remove cp and add ln -s
cp %buildroot/%jbossdir/bin/jboss-cli.sh %buildroot/%_bindir/jboss-cli

#remove library
rm -rf %buildroot/%jbossdir/modules/org/jboss/as/web/main/lib/*
rm -rf %buildroot/%jbossdir/modules/org/hornetq/main/lib/*
chmod 755 %buildroot/%jbossdir/bin/*\.sh

%check

%pre
useradd -d %jbossdir -r -s /bin/nologin %jbossuser >/dev/null 2>&1 || :
#mkdir -p %jbossdir/

%files
%jbossdir/

%attr(755,root,root) %_bindir/jboss-cli
%attr(755,root,root) %_bindir/jboss-as-cp

%changelog
* Mon Mar 31 2014 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt1
- jboss-as binary from jboss.org without build
