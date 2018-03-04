Name: wildfly-as
Version: 10.1.0
Release: alt1

Summary: wildfly-as - Wildfly Application Server

License: LGPLv2 and ASL 2.0
Group: System/Servers
Url: http://www.wildfly.org/

Source: %name-%version.tar
Source1: wildfly-as-cp
Source2: wildfly-as.service

Packager: Konstantinov Aleksey <kana@altlinux.org>

#PreReq:
Requires: java >= 1.8
AutoReq: yes, nomingw, nomingw32
Requires(post): %post_service
Requires(preun): %preun_service
#Provides:
#Conflicts:

#BuildPreReq:
BuildArch: noarch

%define wildflyuser wildfly-as
%define wildflydir %_datadir/wildfly-as

%description
wildfly Application Server 10 is the latest release in a series of wildfly
Application Server offerings. Wildfly Application Server 10, is a fast,
powerful, implementation of the Java Enterprise Edition 6 specification.
The state-of-the-art architecture built on the Modular Service Container
enables services on-demand when your application requires them.

%prep
%setup

%build
#nothing to do

%install
#in wildfly-as
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%wildflydir/
mkdir -p %buildroot/%_initdir/
mkdir -p %buildroot/etc/wildfly-as/
mkdir -p %buildroot/lib/systemd/system/

cp %SOURCE1 %buildroot/%_bindir/
cp %SOURCE2 %buildroot/lib/systemd/system/

cp ./bin/init.d/wildfly-as-standalone %buildroot/%_initdir/
cp ./bin/init.d/wildfly-as.conf %buildroot/etc/wildfly-as/wildfly-as.conf

cp -a ./* %buildroot/%wildflydir/
rm -f %buildroot/%wildflydir/bin/*\.bat
mkdir -p %buildroot/%wildflydir/docs/examples/properties/
mkdir -p %buildroot/%wildflydir/standalone/data/
mkdir -p %buildroot/%wildflydir/standalone/log/

cp %buildroot/%wildflydir/standalone/configuration/logging.properties %buildroot/%wildflydir/docs/examples/properties/
cp %buildroot/%wildflydir/standalone/configuration/mgmt-users.properties %buildroot/%wildflydir/docs/examples/properties/
cp %SOURCE1 %buildroot/%wildflydir/docs/examples/properties/standalone-web.xml
#TODO FIX remove cp and add ln -s
cp %buildroot/%wildflydir/bin/jboss-cli.sh %buildroot/%_bindir/jboss-cli


#remove library
#rm -rf %buildroot/%wildflydir/modules/org/jboss/as/web/main/lib/*
rm -rf %buildroot/%wildflydir/modules/system/layers/base/org/apache/activemq/artemis/main/lib/*
chmod 755 %buildroot/%wildflydir/bin/*\.sh

#alt10 fixup
touch %buildroot/%wildflydir/standalone/log/boot.log
#chmod 755 %buildroot/%wildflydir/standalone/log/boot.log
#chown wildfly-as %buildroot/%wildflydir/standalone/log/boot.log

#TODO remove it #why wildfly need this dir?
#mkdir /usr/src/GNUstep

#TODO rewrite with user cpecified dir or add all users in wildfly-as group and chmod 775
#chmod 777 %buildroot/%wildflydir/standalone/data/content
#chown wildfly-as %buildroot/%wildflydir/standalone/data/content


%check

%pre
useradd -d %wildflydir -r -s /bin/nologin %wildflyuser >/dev/null 2>&1 || :
#chown -R %wildflyuser %wildflydir

%post
%post_service wildfly-as

%preun
%preun_service wildfly-as

%files
%attr(755,%wildflyuser,root) %wildflydir/
%attr(755,root,root) %_bindir/jboss-cli
%attr(755,root,root) %_bindir/wildfly-as-cp
%attr(755,root,root) /etc/wildfly-as/wildfly-as.conf
%attr(755,root,root) %_initdir/*
%attr(644,root,root) /lib/systemd/system/wildfly-as.service

%changelog
* Sun Mar 04 2018 Konstantinov Aleksey <kana@altlinux.org> 10.1.0-alt1
- Initial version for wildfly applicatio server

