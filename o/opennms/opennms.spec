# The install prefix becomes $OPENMS_HOME in the finished package
%define instprefix /usr/share/opennms
# This is where the OPENNMS_HOME variable will be set on the remote
# operating system. Not sure this is needed anymore.
%define profiledir /etc/profile.d
# This is where the "share" directory will link on RPM-based systems
%define sharedir /var/lib/opennms
# This is where the "logs" directory will link on RPM-based systems
%define logdir /var/log/opennms
# Where the OpenNMS webapp lives
%define webappsdir %instprefix/webapps
# Where the OpenNMS Jetty webapp lives
%define jettydir %instprefix/jetty-webapps
# The directory for the OpenNMS webapp
%define servletdir opennms
# Where OpenNMS binaries live
%define bindir %instprefix/bin

%define with_tests	0%nil
%define with_docs	1%nil

%define plain_release 1

Name: opennms
Summary: Enterprise-grade Network Management Platform (Easy Install)
Release: alt1
Version: 1.9.2
License: LGPL/GPL
Group: Monitoring

Source: %name-%version.tar
Source2: %name.init
Source3: %name-remote-poller.init
Source4: %name-maven-dependencies-%version.tar

Url: http://www.opennms.org/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Requires: opennms-webapp-jetty >= %version-%release
Requires: opennms-core = %version-%release
Requires: libiplike
Requires: postgresql-server >= 7.4

BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
#BuildRequires: jpackage-utils >= 0:1.7.2
#BuildRequires: ant >= 0:1.6
#BuildRequires: maven2-plugins
BuildRequires: junit

BuildRequires: librrd-devel postgresql-devel log4j jicmp
BuildRequires: perl-Net-Nessus perl-Class-DBI perl-Net-SNMP perl-Getopt-Mixed perl-libnet perl-libwww perl-POE perl-Authen-Radius perl-DBD-Pg perl-XML-Twig

%add_findreq_skiplist *maint_events.sh

%description
OpenNMS is an enterprise-grade network management platform.

This package used to contain what is now in the "opennms-core" package.
It now exists to give a reasonable default installation of OpenNMS.

When you install this package, you will also need to install one of the
opennms-webapp packages.  OpenNMS now provides 2 ways to install the
web UI:

* jetty

  A version of the web UI for OpenNMS which uses a built-in, embedded version
  of Jetty, which runs in the same JVM as OpenNMS.  This is the recommended
  version unless you have specific needs otherwise.

* standalone

  A standalone version of the web UI for OpenNMS, suitable for embedding inside
  tomcat or another servlet container, or on a server separate from the OpenNMS
  core server.

%package common
Summary: Common directories for OpenNMS
Group: Monitoring
BuildArch: noarch

%description common
Common directories for OpenNMS

%package -n lib%name
Summary: Arch dependent libs for OpenNMS
Group: Monitoring

%description -n lib%name
Arch dependent libs for OpenNMS

%package core
Summary: The core OpenNMS backend
Group: Monitoring
BuildArch: noarch
Requires: opennms-common = %version-%release libopennms = %version-%release
Requires: java jicmp libjrrd which rrd-utils
Obsoletes: opennms < %version-%release
AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description core
The core OpenNMS backend.  This package contains the main OpenNMS
daemon responsible for discovery, polling, data collection, and
notifications (ie, anything that is not part of the web UI).

If you want to be able to view your data, you will need to install
one of the opennms-webapp packages.

%if %with_docs
%package docs
Summary: Documentation for the OpenNMS network management platform
Group: Documentation
BuildArch: noarch

%description docs
This package contains the API and user documentation
for OpenNMS.
%endif

%package remote-poller
Summary: Remote (Distributed) Poller for OpenNMS
Group: Monitoring
BuildArch: noarch
Requires: opennms-common = %version-%release java
AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description remote-poller
The OpenNMS distributed monitor.  For details, see:
  http://www.opennms.org/index.php/Distributed_Monitoring

%package contrib
Summary: Enterprise-grade Open-source Network Management Platform (Contrib)
Group: Monitoring
BuildArch: noarch
Requires: opennms-core = %version-%release
AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description contrib
This package provides additional features and functionality that are not part
of OpenNMS proper.

%package webapp-jetty
Summary: Embedded web interface for OpenNMS
Group: Networking/Other
BuildArch: noarch
Requires: opennms-core = %version-%release
Provides: opennms-webui = %version-%release
Obsoletes: opennms-webapp < %version-%release
AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description webapp-jetty
The web UI for OpenNMS.  This is the Jetty version, which runs
embedded in the main OpenNMS core process.

%package webapp-standalone
Summary: Standalone web interface for OpenNMS
Group: Networking/Other
BuildArch: noarch
Requires: opennms-core = %version-%release 
Requires: tomcat6 java
Provides: opennms-webui = %version-%release
Obsoletes: opennms-webapp < %version-%release
AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description webapp-standalone
The web UI for OpenNMS.  This is the standalone version, suitable for
use with Tomcat or another servlet container.

%package plugins
Summary:	All Plugins for OpenNMS
Group:		Networking/Other
BuildArch: noarch
Requires:	opennms-plugin-provisioning-dns opennms-plugin-provisioning-link opennms-plugin-provisioning-map opennms-plugin-provisioning-rancid opennms-plugin-provisioning-snmp-asset

%description plugins
This installs all optional plugins for OpenNMS.

%package plugin-provisioning-dns
Summary:	DNS Provisioning Adapter for OpenNMS
Group:		Networking/Other
BuildArch: noarch
Requires:	opennms-core = %version-%release

%description plugin-provisioning-dns
The DNS provisioning adapter allows for updating dynamic DNS records based on
provisioned nodes.

%package plugin-provisioning-link
Summary:	Link Provisioning Adapter for OpenNMS
Group:		Networking/Other
BuildArch: noarch
Requires:	opennms-core = %version-%release

%description plugin-provisioning-link
The link provisioning adapter creates links between provisioned nodes based on naming
conventions defined in the link-adapter-configuration.xml file.  It also updates the
status of the map links based on data link events.

%package plugin-provisioning-map
Summary:	Map Provisioning Adapter for OpenNMS
Group:		Networking/Other
BuildArch: noarch
Requires:	opennms-core = %version-%release

%description plugin-provisioning-map
The map provisioning adapter will automatically create maps when nodes are provisioned
in OpenNMS.

%package plugin-provisioning-rancid
Summary:	RANCID Provisioning Adapter for OpenNMS
Group:		Networking/Other
BuildArch: noarch
Requires:	opennms-core = %version-%release

%description plugin-provisioning-rancid
The RANCID provisioning adapter coordinates with the RANCID Web Service by updating
RANCID's device database when OpenNMS provisions nodes.

%package plugin-provisioning-snmp-asset
Summary:	SNMP Asset Provisioning Adapter for OpenNMS
Group:		Networking/Other
BuildArch: noarch
Requires:	opennms-core = %version-%release

%description plugin-provisioning-snmp-asset
The SNMP asset provisioning adapter responds to provisioning events by updating asset
fields with data fetched from SNMP GET requests.

%prep
%setup -q
rm -fr $HOME/.m2
mkdir $HOME/.m2
%__tar xf %SOURCE4 -C $HOME/.m2

##############################################################################
# building
##############################################################################

%build
# nothing necessary

##############################################################################
# installation
##############################################################################

%install

%if %with_tests
EXTRA_TARGETS="$EXTRA_TARGETS test"
%endif

%if %with_docs
EXTRA_TARGETS="$EXTRA_TARGETS docs"
%endif

echo "=== RUNNING INSTALL ==="

export MAVEN_OPTS="-Xmx1g -XX:MaxPermSize=256m"

sh ./build.sh -o \
        -Ddist.dir=$(pwd)/alt -Ddist.name=temp \
        -Dopennms.home=%instprefix \
        -Dinstall.dir=%instprefix \
        -Dinstall.init.dir=%_sysconfdir/init.d \
        -Dinstall.etc.dir=%_sysconfdir/%name \
        -Dinstall.share.dir=%sharedir \
        -Dinstall.contrib.dir=%instprefix/contrib \
        -Dinstall.servlet.dir=%webappsdir \
        -Dinstall.webapps.dir=%webappsdir \
        -Dinstall.logs.dir=%logdir \
        -Dinstall.pid.file=/var/run/%name.pid \
        -Dproduct.release=%release \
        -Dinstall.rrdtool.bin=/usr/bin/rrdtool \
        -Dbuild.postgresql.include.dir=%_includedir/pgsql \
        -Dbuild.rrdtool.lib.dir=%_libdir \
        install  assembly:attached
#        install  assembly:directory-inline

echo "=== INSTALL COMPLETED ==="

mkdir -p alt/temp
%__tar xzf alt/temp.tar.gz -C alt/temp

mkdir -p $RPM_BUILD_ROOT%instprefix
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/%name
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/sysconfig
mkdir -p $RPM_BUILD_ROOT%_sbindir

### XXX is this needed?  (Most of) the current scripts don't use OPENNMS_HOME.
### /etc/profile.d

mkdir -p $RPM_BUILD_ROOT%profiledir
cat > $RPM_BUILD_ROOT%profiledir/%name.sh << __END__
#!/bin/bash

OPENNMS_HOME=%instprefix
if ! echo "\$PATH" | grep "\$OPENNMS_HOME/bin" >/dev/null 2>&1; then
	PATH="\$PATH:\$OPENNMS_HOME/bin"
fi

export OPENNMS_HOME PATH

__END__

cat > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/%name << __END__
# Number of times to do "opennms status" after starting OpenNMS to see
# if it comes up completely.  Set to "0" to disable.  Between each
# attempt we sleep for STATUS_WAIT seconds...
#START_TIMEOUT=10

# Number of seconds to wait between each "opennms status" check when
# START_TIMEOUT > 0.
#STATUS_WAIT=5

# Value of the -Xmx<size>m option passed to Java.
#JAVA_HEAP_SIZE=256

# Additional options that should be passed to Java when starting OpenNMS.
#ADDITIONAL_MANAGER_OPTIONS=""

# Classpath additions.  These go on the front of our classpath.
#ADDITIONAL_CLASSPATH=""

# Use incremental garbage collection.
#USE_INCGC=""

# Use the Java Hotspot server VM.
#HOTSPOT=""

# Enable verbose garbage collection debugging.
#VERBOSE_GC=""

# Additional options to pass to runjava.
#RUNJAVA_OPTIONS=""

__END__

cat > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/opennms-remote-poller << __END__
#JAVA_EXE="/usr/bin/java"
#RMI_LOCATION="RDU"
#RMI_HOST="127.0.0.1"
#RMI_PORT=1099

__END__

%if %with_docs

mkdir -p $RPM_BUILD_ROOT%_docdir/%name-%version
cp -fR opennms-doc/src/docbkx $RPM_BUILD_ROOT%_docdir/%name-%version/
install LICENSE README.notification $RPM_BUILD_ROOT%_docdir/%name-%version/
#rm -rf $RPM_BUILD_ROOT%instprefix/etc/README
#rm -rf $RPM_BUILD_ROOT%instprefix/etc/README.build
%endif

install -d -m 755 $RPM_BUILD_ROOT%logdir
cp -fR alt/temp/logs/* $RPM_BUILD_ROOT%logdir/

install -d -m 755 $RPM_BUILD_ROOT%sharedir
cp -fR alt/temp/share/* $RPM_BUILD_ROOT%sharedir/

install -d -m 755 $RPM_BUILD_ROOT%_sysconfdir/%name
cp -fR alt/temp/etc/* $RPM_BUILD_ROOT%_sysconfdir/%name/

install -d -m 755 $RPM_BUILD_ROOT%_initdir

install -d -m 755 $RPM_BUILD_ROOT%instprefix/bin
cp -fR alt/temp/bin/* $RPM_BUILD_ROOT%instprefix/bin/
cp -f %SOURCE2 $RPM_BUILD_ROOT%instprefix/bin/%name
chmod o+x $RPM_BUILD_ROOT%instprefix/bin/*

# remove ELF object for "noarch" architecture
rm -rf alt/temp/contrib/qosdaemon
rm -rf alt/temp/lib/mac
rm -rf alt/temp/lib/win32
rm -rf alt/temp/lib/win64

install -d -m 755 $RPM_BUILD_ROOT%_libdir/%name
%ifarch %ix86
cp -fR alt/temp/lib/linux32/* $RPM_BUILD_ROOT%_libdir/%name
%else
cp -fR alt/temp/lib/linux64/* $RPM_BUILD_ROOT%_libdir/%name
%endif
rm -rf alt/temp/lib/linux32
rm -rf alt/temp/lib/linux64

install -d -m 755 $RPM_BUILD_ROOT%instprefix/contrib
cp -fR alt/temp/contrib/* $RPM_BUILD_ROOT%instprefix/contrib/

install -d -m 755 $RPM_BUILD_ROOT%instprefix/lib
cp -fR alt/temp/lib/* $RPM_BUILD_ROOT%instprefix/lib/

install -d -m 755 $RPM_BUILD_ROOT%jettydir
cp -fR alt/temp/jetty-webapps/* $RPM_BUILD_ROOT%jettydir/

install -d -m 755 $RPM_BUILD_ROOT%webappsdir
cp -fR alt/temp/webapps/* $RPM_BUILD_ROOT%webappsdir/

# install the remote poller jar
#install -c -m 644 features/remote-poller/target/org.opennms.features.remote-poller-*-signed-jar-with-dependencies.jar $RPM_BUILD_ROOT%instprefix/lib/opennms-remote-poller.jar
#install -c -m 644 opennms-remote-poller/target/opennms-remote-poller*-jar-with-dependencies.jar $RPM_BUILD_ROOT%instprefix/lib/opennms-remote-poller.jar
mkdir -p  $RPM_BUILD_ROOT%_logdir/opennms-remote-poller
install %SOURCE3 $RPM_BUILD_ROOT%_initdir/opennms-remote-poller

ln -sf ../../..%logdir $RPM_BUILD_ROOT%instprefix/logs
ln -sf ../../..%sharedir $RPM_BUILD_ROOT%instprefix/share
ln -sf ../../..%_sysconfdir/%name $RPM_BUILD_ROOT%instprefix/etc
ln -sf ../../..%instprefix/bin/%name $RPM_BUILD_ROOT%_initdir/%name
ln -sf ../..%instprefix/bin/%name $RPM_BUILD_ROOT%_sbindir/%name

touch $RPM_BUILD_ROOT%_sysconfdir/%name/configured
cat > $RPM_BUILD_ROOT%_sysconfdir/%name/java.conf << END
/usr/bin/java
END
cat > $RPM_BUILD_ROOT%_sysconfdir/%name/libraries.properties << END
opennms.library.jrrd=%_libdir/libjrrd.so
opennms.library.jicmp=%_libdir/libjicmp.so
END

find $RPM_BUILD_ROOT -type f -name .readme -print0 | xargs -r0 rm -f

#Fix unmet
%__subst "s|/opt|%_datadir|g" $RPM_BUILD_ROOT%instprefix/contrib/alvarion/run_link_quality


# core package files
find $RPM_BUILD_ROOT/etc/%name ! -type d | \
    sed -e "s|^$RPM_BUILD_ROOT|%config(noreplace) %attr(664,root,_%name) |" | \
    sort > files.main
find $RPM_BUILD_ROOT/etc/%name -type d | \
    sed -e "s|^$RPM_BUILD_ROOT|%dir %attr(775,root,_%name) |" | \
    sort >> files.main
find $RPM_BUILD_ROOT%instprefix/bin ! -type d | \
    sed -e "s|^$RPM_BUILD_ROOT|%attr(755,root,root) |" | \
    grep -v '/remote-poller.sh' | \
    sort >> files.main
find $RPM_BUILD_ROOT%instprefix/lib ! -type d | \
    sed -e "s|^$RPM_BUILD_ROOT|%attr(644,root,root) |" | \
    grep -v '/remote-poller.jar' | \
    sort >> files.main

# jetty
find $RPM_BUILD_ROOT%jettydir ! -type d | \
    sed -e "s|^$RPM_BUILD_ROOT||" | \
    grep -v '/WEB-INF/web\.xml$' | \
    grep -v '/WEB-INF/configuration\.properties$' | \
    grep -v '.gitignore$' | \
    sort >> files.jetty
find $RPM_BUILD_ROOT%jettydir -type d | \
    sed -e "s|^$RPM_BUILD_ROOT|%dir |" | \
    sort >> files.jetty

# webapps
find $RPM_BUILD_ROOT%webappsdir ! -type d | \
    sed -e "s|^$RPM_BUILD_ROOT||" | \
    grep -v '/WEB-INF/web\.xml$' | \
    grep -v '/WEB-INF/configuration\.properties$' | \
    grep -v '.gitignore$' | \
    sort > files.webapp
find $RPM_BUILD_ROOT%webappsdir -type d | \
    sed -e "s|^$RPM_BUILD_ROOT|%dir |" | \
    sort >> files.webapp

# provisioning adapters
cp integrations/opennms-dns-provisioning-adapter/target/*.jar        $RPM_BUILD_ROOT%instprefix/lib/
cp integrations/opennms-link-provisioning-adapter/target/*.jar       $RPM_BUILD_ROOT%instprefix/lib/
cp integrations/opennms-map-provisioning-adapter/target/*.jar        $RPM_BUILD_ROOT%instprefix/lib/
cp integrations/opennms-rancid/target/*.jar                          $RPM_BUILD_ROOT%instprefix/lib/
cp integrations/opennms-snmp-asset-provisioning-adapter/target/*.jar $RPM_BUILD_ROOT%instprefix/lib/
rm -rf $RPM_BUILD_ROOT%instprefix/lib/*-sources.jar
rm -rf $RPM_BUILD_ROOT%instprefix/lib/*-tests.jar
rm -rf $RPM_BUILD_ROOT%instprefix/lib/*-xsds.jar

# config files, this should be more automated  :P
cp integrations/opennms-link-provisioning-adapter/src/main/resources/link-adapter-configuration.xml $RPM_BUILD_ROOT%_sysconfdir/%name/
cp integrations/opennms-link-provisioning-adapter/src/main/resources/endpoint-configuration.xml $RPM_BUILD_ROOT%_sysconfdir/%name/
cp integrations/opennms-map-provisioning-adapter/src/main/resources/mapsadapter-configuration.xml   $RPM_BUILD_ROOT%_sysconfdir/%name/


%pre core
groupadd -r -f _%name &> /dev/null ||:
##useradd -r -g _%name -d /dev/null -c 'An enterprise-grade network management platform' -s /dev/null -n _%name &> /dev/null ||:

%post core
echo "For setup DB start: /usr/share/opennms/bin/install -ids"
%post_service %name

%preun core
%preun_service %name

%post webapp-standalone
gpasswd -a tomcat _%name
echo "For install to Tomcat start: /usr/share/opennms/bin/install -y -w /etc/tomcat6/Catalina/localhost"

%post remote-poller
%post_service opennms-remote-poller

%preun remote-poller
%preun_service opennms-remote-poller

%files

%files common
%dir %instprefix
%dir %instprefix/lib

%files -n lib%name
%_libdir/%name

%files core -f files.main
%profiledir/%name.sh
%_sbindir/%name
%_initdir/%name
%_sysconfdir/sysconfig/%name
%instprefix/etc
%instprefix/logs
%instprefix/share
%sharedir
%logdir

%exclude %webappsdir
%exclude %jettydir
%exclude %instprefix/contrib

%exclude %instprefix/bin/remote-poller.jar

#%exclude %instprefix/lib/opennms-dns-provisioning-adapter*.jar

#%exclude %instprefix/lib/opennms-link-provisioning-adapter*.jar
#%exclude %instprefix/etc/link-adapter-configuration.xml

#%exclude %instprefix/etc/endpoint-configuration.xml
#%exclude %instprefix/lib/opennms-map-provisioning-adapter*.jar
%exclude %_sysconfdir/%name/mapsadapter-configuration.xml

#%exclude %instprefix/lib/opennms-rancid*.jar

#%exclude %instprefix/lib/opennms-snmp-asset-provisioning-adapter*.jar
%exclude %_sysconfdir/%name/snmp-asset-adapter-configuration.xml

%if %with_docs
%files docs
%_docdir/%name-%version
%endif

%files remote-poller
%config %_sysconfdir/sysconfig/opennms-remote-poller
%_initdir/opennms-remote-poller
%instprefix/bin/remote-poller.jar
%dir %_logdir/opennms-remote-poller

%files contrib
%attr(755,root,root) %instprefix/contrib

%files webapp-jetty -f files.jetty
%config %jettydir/%servletdir/WEB-INF/web.xml
%config %jettydir/%servletdir/WEB-INF/configuration.properties

%files webapp-standalone -f files.webapp
%config %webappsdir/%servletdir/WEB-INF/web.xml
%config %webappsdir/%servletdir/WEB-INF/configuration.properties

%files plugins

%files plugin-provisioning-dns
%instprefix/lib/opennms-dns-provisioning-adapter*.jar

%files plugin-provisioning-link
%instprefix/lib/opennms-link-provisioning-adapter*.jar
%config %_sysconfdir/%name//link-adapter-configuration.xml
%config %_sysconfdir/%name/endpoint-configuration.xml

%files plugin-provisioning-map
%instprefix/lib/opennms-map-provisioning-adapter*.jar
%config %_sysconfdir/%name/mapsadapter-configuration.xml

%files plugin-provisioning-rancid
%instprefix/lib/opennms-rancid*.jar

%files plugin-provisioning-snmp-asset
%instprefix/lib/opennms-snmp-asset-provisioning-adapter*.jar
%config %_sysconfdir/%name/snmp-asset-adapter-configuration.xml

%changelog
* Thu Nov 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.9.2-alt1
- New version
- Update spec. Add subpackages opennms-plugin*

* Tue Dec 15 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.8-alt1
- New version

* Fri Nov 27 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.7-alt1
- New unstable version
- Add subpakage libopennms

* Mon Sep 07 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.5-alt2
- Fix path to sharedir
- Add post_service and preun_service

* Tue Apr 14 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.5-alt1
- New version

* Fri Feb 13 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.2-alt1
- New version
- Bugfix release
- Add new subpackage opennms-common
- Add initscript for opennms-remote-poller
- Update initscript for opennms
- Update opennms-maven-dependencies-1.6.2.tar.bz2 as SOURCE4
- Add AutoReq: yes, noosgi and AutoProv: yes, noosgi
- Remove noarch for subpackage webapp-jetty
- Change Requires from tomca5 to tomcat6 for webapp-standalone subpackage

* Wed Nov 26 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.1-alt1
- New version
- Bugfix release
- Add %_sysconfdir/sysconfig/%name
- Move requires of libiplike from core to main package
- Update BuildRequires
- Add initscript for remote-poller

* Wed Oct 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.0-alt1
- New version
- Fix unmets
- Use %name-maven-dependencies for build

* Mon Aug 04 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.5.93-alt1
- Build for ALT
