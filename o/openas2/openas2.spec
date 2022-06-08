Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name openas2
# Set bundled to copy needed jars to lib dir to run on el7
%bcond_with bundled

# Patch to use hsqldb instead of h2 for local database
%bcond_without hsqldb

# Enable Sentry logging plugin (http://sentry.io) - proprietary jar needed.
%bcond_with sentry

# Enable tests at build time.  
# Tests require mockito >= 2.6.8 and localhost networking.
%bcond_without tests

%global openas2dir %{_sharedstatedir}/%{name}
%global factory_passwd ChangeMe

%if %{with tests}
%global skip_test ''
%else
%global skip_test -Dmaven.test.skip=true
%endif

Name:           openas2
Version:        2.10.0
Release:        alt2_9jpp11
Summary:        Java-based implementation of the EDIINT AS2 standard

License:        BSD
URL:            https://github.com/OpenAS2/OpenAs2App
Source0:        https://github.com/OpenAS2/OpenAs2App/archive/v%{version}.tar.gz#/OpenAs2App-%{version}.tar.gz
#
# antfile to create initial hsqldb message log database
# NOTE: this is used only when building --with=hsqldb.  
# 
Source1:        hsqldb.xml

# Patch for using hsqldb instead of h2 for embedded database.  
# Code changes to use hsqldb
Patch0:         openas2-hsqldb.patch

# Use OPENAS2_BASE since start script can't be in /var/lib
Patch3:         openas2-fedora.patch
# openas2.service modified for this package's file layout
Source2:        openas2.service
# Logrotate to delete old logs (openas2 rotates on its own)
Source3:        openas2.logrotate

BuildRequires:  maven-local dom4j javamail bouncycastle glassfish-servlet-api
BuildRequires:  hamcrest dos2unix jsr-305
%if %{with hsqldb}
BuildRequires:  hsqldb-lib ant
%else
BuildRequires:  mvn(com.h2database:h2)
%endif
BuildRequires:  bouncycastle-mail bouncycastle-pkix bouncycastle-pg
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(commons-logging:commons-logging)
%if %{with tests}
# FIXME: adding to try to make unit tests work in mock
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.commons:commons-lang)
#BuildRequires:  mvn(org.apache.commons:commons-lang3)
#BuildRequires:  mvn(org.apache.maven.plugins:maven-toolchains-plugin)
BuildRequires:  mvn(org.apache.maven:maven-toolchain)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
#BuildRequires:  mvn(org.apache.commons:commons-dbcp)
BuildRequires:  mvn(org.apache.commons:commons-pool)
%endif
#
BuildRequires:  libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-homed systemd-networkd systemd-portable systemd-services systemd-stateless systemd-sysvinit systemd-utils
BuildArch:      noarch

%{?systemd_requires}
Requires:       systemd systemd-analyze systemd-coredump systemd-homed systemd-networkd systemd-portable systemd-services systemd-stateless systemd-sysvinit systemd-utils
Requires:       %{name}-lib = %{version}-%{release}
Obsoletes:      openas2-server <= 2.6.2-2
Source44: import.info
%filter_from_requires /^mvn[(].*[)]$/d

%description
OpenAS2 is a java-based implementation of the EDIINT AS2 standard. It is
intended to be used as a server. It is extremely configurable and supports a
wide variety of signing and encryption algorithms.

%if %{with hsqldb}
This package has a mostly preconfigured openas2 server, using hsqldb by default
%else
This package has a mostly preconfigured openas2 server, using h2 by default 
%endif
for a standalone package.  It can be configured to use postgresql instead.

%package lib
Group: Development/Java
Summary:        OpenAS2 core libraries
BuildArch:      noarch
Requires:       java >= 1.8
%if %{with bundled}
# Filter mvn autorequires since they are mostly bundled.

# EL7 has these compatible packages
Requires:       mvn(dom4j:dom4j)
# Remaining requires are bundled in the main package
Requires:       %{name} = %{version}-%{release}
%endif

%description lib
OpenAS2 is a java-based implementation of the EDIINT AS2 standard. It is
intended to be used as a server. It is extremely configurable and supports a
wide variety of signing and encryption algorithms.

This package contains core libraries.

%package javadoc
Group: Development/Java
Summary:        OpenAS2 API documentation
BuildArch: noarch

%description javadoc
API documentation for OpenAS2

%prep
%setup -qn OpenAs2App-%{version}
%if %{with hsqldb}
%patch0 -b .hsqldb
%endif
%patch3 -b .fedora

# Point default config to embedded database dir.
sed -i -e '/db_directory="/ s,".*","%{openas2dir}/db",' Server/src/config/config.xml

# Point default config to message data directory.
sed -i -e '/storageBaseDir="/ s,".*","%{_var}/spool/%{name}",' Server/src/config/config.xml

# Disable tcp_server in default config.  It is a security risk in
# workstation install with factory password.
sed -i -e '/tcp_server_start="/ s,".*","false",' Server/src/config/config.xml

# Set factory password
sed -i -e '/db_pwd="/ s,".*","%{factory_passwd}",' \
	-e '/tcp_server_password="/ s,".*","%{factory_passwd}",' \
	-e '/ password="/ s,password=".*",password="%{factory_passwd}",' \
	Server/src/config/config.xml

# Use latest OSGi implementation
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core

%if %{with hsqldb}
%pom_remove_dep com.h2database: Server
%pom_add_dep org.hsqldb:hsqldb:%{version} Server
%endif

%if %{with bundled}
# This is needed to match the POM on el7
%pom_change_dep org.dom4j: dom4j:dom4j:1.6.1 Server
%pom_change_dep org.dom4j: dom4j:dom4j:1.6.1 
%endif

%if !%{with sentry}
%pom_remove_dep io.sentry: Server
%endif

%pom_remove_dep com.google.code.findbugs: Server

%pom_add_dep com.sun.activation:jakarta.activation
%pom_add_dep org.slf4j:slf4j-api:1.7.25 Server
%pom_add_dep com.google.code.findbugs:jsr305 Server

%if %{with tests}
#pom_add_dep com.apache.commons:commons-lang Server
#pom_add_dep com.apache.commons:commons-lang3 Server
%pom_add_dep commons-lang:commons-lang Server
%endif

# Make submodule parents match actual parent
%pom_set_parent net.sf.openas2:OpenAS2:%{version} Remote
%pom_set_parent net.sf.openas2:OpenAS2:%{version} Bundle
%pom_set_parent net.sf.openas2:OpenAS2:%{version} Server

%if %{with hsqldb}
# initial hsqldb database
if test -s %{SOURCE1}; then
	:
else
  echo "**********"
  echo "Exec ../db_ddl.sql in Server/src/config/DB/ sqltool from maven,"
  echo " or org.hsqldb.util.DatabaseManager (which requires X)."
  echo "Run tar cvfz %{SOURCE1} Server/src/config/DB and rebuild."
  echo "**********"
  exit 1
fi
%endif
# remove binaries that came with the "source"
find . -name "*.jar" -delete
# remove h2 preloaded databases - we'll recreate from db_ddl.sql below
find . -name "openas2.mv.db" -delete
# remove proprietary jks key containers
# rename SentryLogger when not enabled
%if !%{with sentry}
cd Server/src/main/java/org/openas2/logging
mv SentryLogger.java SentryLogger.java.sentry
cd -
%endif

# Fix misc DOS eols
dos2unix changes.txt RELEASE-NOTES.md Remote/docs/Readme.txt

%build
%if %{with tests}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8 -Dorg.apache.commons.logging.Log=org.openas2.logging.Log
%else
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8
%endif


%install
%mvn_install

# systemd service
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{SOURCE2} %{buildroot}%{_unitdir}

# server application runs from /var/lib/openas2
mkdir -p %{buildroot}%{openas2dir}/{bin,db,config}
ln -sf %{_libexecdir}/%{name}/start-openas2.sh %{buildroot}%{openas2dir}/bin

# spooled messages in /var/spool/openas2
mkdir -p %{buildroot}%{_var}/spool/openas2
ln -sf %{_var}/spool/%{name} %{buildroot}%{openas2dir}/data

# logs in /var/log/openas2
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
ln -sf %{_localstatedir}/log/%{name} %{buildroot}%{openas2dir}/logs

# put scripts in /usr/libexec/openas2
mkdir -p %{buildroot}%{_libexecdir}/%{name}
install -pm755 Server/target/dist/bin/start-openas2.sh \
        %{buildroot}%{_libexecdir}/%{name}

# symlink library jars to /usr/share/java
cp -pr Server/target/dist/lib %{buildroot}%{openas2dir}
%if !%{with bundled}
xmvn-subst %{buildroot}%{openas2dir}/lib # replace system jars with symlinks
%endif
ln -sf %{_javadir}/openas2/openas2-server.jar \
        %{buildroot}%{openas2dir}/lib/openas2-server*

# sample configurations in /etc/openas2
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -p Server/target/dist/config/*.* %{buildroot}%{_sysconfdir}/%{name}
cd %{buildroot}%{_sysconfdir}/%{name}

%if %{with hsqldb}
# config.xml.hsqldb is the backup from the hsqldb patch
mv config.xml.hsqldb config.xml.h2
%endif

# symlink sample configurations to run dir where config expects them
# QUESTION: should we modify the config to use absolute paths to
# our run dir instead?
for i in *.*; do
  ln -sf %{_sysconfdir}/%{name}/"$i" %{buildroot}%{openas2dir}/config
done
cd -

cd Server/target/dist/config
%if %{with hsqldb}
sed -e 's/VARCHAR /VARCHAR(255) /' -e 's/VARCHAR,/VARCHAR(255),/' db_ddl.sql \
	>hsqldb_ddl.sql
ant -f %{SOURCE1}
%else
# recreate from source the initial h2 database that we removed above
java -cp ../lib/h2* org.h2.tools.RunScript -url "jdbc:h2:./DB/openas2" \
	-user sa -password "%{factory_passwd}" -script db_ddl.sql
%endif
cd -

# template h2/hsqldb database 
cp -pr Server/target/dist/config/DB %{buildroot}%{openas2dir}/config

# logrotate config to delete old logs
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp -p %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%files lib -f .mfiles
%doc --no-dereference LICENSE.txt Remote/docs/license.txt
%doc changes.txt README.md RELEASE-NOTES.md docs/* Remote/docs/Readme.txt

%pre
getent group openas2 > /dev/null || /usr/sbin/groupadd -r openas2
getent passwd openas2 > /dev/null || /usr/sbin/useradd -g openas2 \
        -c "Java EDIINT AS2 Server" \
        -r -d %{openas2dir} -s /sbin/nologin openas2
exit 0

%files javadoc 
%doc --no-dereference LICENSE.txt
%{_javadocdir}/*

%files 
%{_libexecdir}/%{name}
%attr(0644,root,root) %{_unitdir}/*
%attr(0755,root,root) %dir %{openas2dir}
%attr(0755,root,root) %{openas2dir}/bin
%attr(0755,root,root) %dir %{openas2dir}/lib
%{openas2dir}/lib/*
%attr(0755,root,root) %dir %{openas2dir}/config
%{openas2dir}/config/*
%attr(0750,root,openas2) %dir %{_sysconfdir}/%{name}
%attr(0640,root,openas2) %config(noreplace) %{_sysconfdir}/%{name}/*
%attr(0755,openas2,openas2) %dir %{openas2dir}/db
%{openas2dir}/data
%attr(0755,openas2,openas2) %dir %{_var}/spool/%{name}
%{openas2dir}/logs
%attr(0755,openas2,openas2) %dir %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/*

%post 
%post_service %{name}

%postun 
%if %{with bundled}
# EL7 needs explicit reload
systemctl daemon-reload >/dev/null 2>&1 || :
%endif
: 

%preun 
%preun_service %{name}


%changelog
* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 2.10.0-alt2_9jpp11
- fixed build with new guava

* Sun Jun 13 2021 Igor Vlasenko <viy@altlinux.org> 2.10.0-alt1_9jpp11
- new version

