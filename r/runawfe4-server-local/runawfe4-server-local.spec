Name: runawfe4-server-local
Version: 4.2.0
Release: alt13

Summary: Runawfe local server

License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

Source: %name-%version.tar
Source1: standalone-runa-local.xml
Source2: runawfe4-server-local
Source3: jboss-as-runawfe4-server-local.conf
Source4: runawfe4-server-local.service
Source5: runawfe4-server-local-start.desktop
Source6: runawfe4-server-local.png
Source7: runawfe4-server-local-stop.desktop

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: jboss-as-vanilla
#Conflicts: runawfe4-server

#BuildPreReq:
# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: apache-commons-cli atinject google-guice guava java java-devel jpackage-utils maven maven-wagon nekohtml plexus-cipher plexus-classworlds plexus-containers-component-annotations plexus-interpolation plexus-sec-dispatcher plexus-utils python3-base sisu tzdata tzdata-java xbean xerces-j2 xml-commons-jaxp-1.4-apis
BuildRequires: aether

BuildRequires: jboss-as-vanilla
BuildArch: noarch

%define jbossuser jboss-as
%define runauser _runa
%define runadir /var/lib/%name
%define jbossdir %_datadir/jboss-as/standalone

%description
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on JBoss jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

%build

%install
mkdir -p %buildroot/%jbossdir/{bin,data,deployments,log,tmp,configuration}
mkdir -p %buildroot/etc/jboss-as/
mkdir -p %buildroot/lib/systemd/system/
mkdir -p %buildroot%_desktopdir/
mkdir -p %buildroot%_pixmapsdir/
mkdir -p %buildroot%jbossdir/../docs/examples/configs/
mkdir -p %buildroot%runadir/
mkdir -p %buildroot/var/run/
mkdir -p %buildroot/%_bindir/

#FIX correct path to jboss-as/bin
cp %SOURCE1 %buildroot%jbossdir/../docs/examples/configs/
cp %SOURCE1 %buildroot%jbossdir/configuration/
cp %SOURCE3 %buildroot/etc/jboss-as/
cp %SOURCE4 %buildroot/lib/systemd/system/
cp %SOURCE5 %buildroot%_desktopdir/
cp %SOURCE6 %buildroot%_pixmapsdir/
cp %SOURCE7 %buildroot%_desktopdir/
cp -a simulation/* %buildroot%jbossdir/../
cp -a simulation_cache/ %buildroot%runadir/
touch %buildroot/var/run/%name.pid
chmod a+rw %buildroot/var/run/%name.pid


cat >%buildroot/%_bindir/%name <<EOF
#!/bin/sh
localdir=~/%name/

#rm -f /var/run/%name.pid
ln -sf /var/run/jboss-as/jboss-as-standalone.pid /var/run/%name.pid &> /dev/null
#TODO after start
#cat /var/run/jboss-as/jboss-as-standalone.pid > /var/run/%name.pid 

if [ ! -e "\$localdir" ] ; then
jboss-as-cp -c standalone-runa-local.xml -l "\$localdir"
ln -s %jbossdir/deployments/runawfe.ear "\$localdir"/deployments/
cp -a %runadir/simulation_cache/* "\$localdir"
cp -a %jbossdir/../adminkit/ %jbossdir/../samples/ %jbossdir/../standalone/wfe.custom/ "\$localdir"
fi

rm -f "\$localdir"/deployments/runawfe.ear.*

cd "\$localdir"
JBOSS_BASE_DIR=/usr/share/jboss-as/standalone "\$localdir"/bin/standalone.sh -c standalone-runa-local.xml > "\$localdir"/%name.log 2>&1 &

count=0
launched=false

until [ \$count -gt 200 ]
  do
    if [ -e "\$localdir"/deployments/runawfe.ear.deployed ] ; then
      launched=true
      break
    fi
    sleep 1
    let count=\$count+1;
done

xdg-open http://127.0.0.1:28080/wfe/

EOF

cat >%buildroot/%_bindir/%name-stop <<EOF
#!/bin/sh
localdir=~/%name/

/usr/share/jboss-as/bin/jboss-cli.sh --connect command=:shutdown
#killall java

EOF

#Uses one ear for server and local server
mkdir -p %buildroot/%jbossdir/deployments/
cp -a wfe-ear/target/runawfe.ear %buildroot/%jbossdir/deployments/

install -D -m754 %SOURCE2 %buildroot%_initdir/%name

%check
#check that port listening

%pre

%files
/etc/jboss-as/jboss-as-%name.conf
%_pixmapsdir/*
%_desktopdir/*
%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_bindir/%name-stop

%jbossdir/../adminkit/
%jbossdir/../samples/
%jbossdir/../standalone/wfe.custom/
%jbossdir/configuration/*
%jbossdir/../docs/examples/configs/*
%attr(755,%jbossuser,root) %jbossdir/deployments/*

%runadir/simulation_cache/
%_runtimedir/%name.pid
%_bindir/%name-stop

%attr(644,root,root) /lib/systemd/system/%name.service
%_initdir/%name

%changelog
* Thu Jul 02 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt13
- Update to trunk code@6444

* Wed Jul 01 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt12
- Fixed bugs 1068, added runawfe4-server-local-stop for stopping server

* Thu Jun 25 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt11
- Updated ear to code@6397

* Wed Jun 24 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt10
- Added simulation cache, change stop server

* Wed Jun 24 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt9
- Change samples dir, rebuild ear from code@6345

* Wed Jun 17 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt8
- Remove requires runawfe4-server

* Tue Jun 16 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt7
- Added samples

* Wed Jun 10 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt6
- Revert save db to dir

* Tue Jun 09 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt5
- Update standalone-runa-local.xml, save db in memory, added mvcc=true

* Thu Apr 23 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt4
- Added log saving, fix browser opening

* Thu Apr 02 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt3
- fix ear copy

* Wed Apr 01 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt2
- Fix start, stop destop files

* Thu Mar 26 2015 Danil Mikhailov <danil@altlinux.org> 4.2.0-alt1
- Initial release

