# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		truezip
Version:	7.6.6
Release:	alt1_1jpp7
Summary:	Java based VFS for treating archive files as virtual directories

Group:		Development/Java
License:	EPL
URL:		http://truezip.java.net/

# hg clone https://hg.java.net/hg/truezip~v7 && cd truezip~v7/
# hg archive -r truezip-7.5.5 truezip-7.5.5.tar.gz -X ".hg*"
Source0:	%{name}-%{version}.tar.gz
Source1:	http://www.eclipse.org/legal/epl-v10.html


BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	apache-commons-compress
BuildRequires:	bouncycastle
BuildRequires:	findbugs
BuildRequires:	jemmy
BuildRequires:	jsr-305
BuildRequires:	junit
BuildRequires:	maven
BuildRequires:	schlichtherle-oss-parent

BuildRequires:	maven-antrun-plugin
BuildRequires:	maven-archetype-common
BuildRequires:	maven-archetype-packaging
BuildRequires:	maven-archetype-plugin
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-failsafe-plugin
BuildRequires:	maven-install-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	maven-plugin-jxr
BuildRequires:	maven-plugin-cobertura
BuildRequires:	maven-release-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-site-plugin
BuildRequires:	maven-surefire-plugin

Requires:	jpackage-utils
Requires:	%{name}-driver-parent = %{version}-%{release}
Requires:	%{name}-driver-file = %{version}-%{release}
Requires:	%{name}-driver-http = %{version}-%{release}
Requires:	%{name}-driver-tar = %{version}-%{release}
Requires:	%{name}-driver-tzp = %{version}-%{release}
Requires:	%{name}-driver-zip = %{version}-%{release}
Requires:	%{name}-extension-parent = %{version}-%{release}
Requires:	%{name}-extension-jmx-jul = %{version}-%{release}
Requires:	%{name}-extension-pace = %{version}-%{release}
Requires:	%{name}-file = %{version}-%{release}
Requires:	%{name}-kernel = %{version}-%{release}
Requires:	%{name}-path = %{version}-%{release}
Requires:	%{name}-samples = %{version}-%{release}
Requires:	%{name}-swing = %{version}-%{release}
Source44: import.info

%description
TrueVFS is a Java based virtual file system (VFS) which enables
client applications to perform CRUD (Create, Read, Update, Delete)
operations on archive files as if they were virtual directories,
even with nested archive files in multithreaded environments.

As a library, TrueVFS provides simple, uniform, transparent,
thread-safe, read/write access to archive files as if they were
virtual directories in a file system path.

As a framework, TrueVFS provides the interfaces and classes to
write file system drivers which plug-in to its federated file
system space.

%package parent
Group: Development/Java
Summary:	Parent POM for TrueZip modules
Requires:	jpackage-utils
Requires:	schlichtherle-oss-parent

%description parent
Parent POM for TrueZip modules.

%package driver-parent
Group: Development/Java
Summary:	Parent POM for TrueZip pluggable file system drivers
Requires:	jpackage-utils
Requires:	%{name}-parent = %{version}-%{release}

%description driver-parent
Parent POM for TrueZip pluggable file system drivers.

%package driver-file
Group: Development/Java
Summary:	TrueZip driver for the FILE scheme
Requires:	jpackage-utils
Requires:	%{name}-driver-parent = %{version}-%{release}
Requires:	%{name}-kernel = %{version}-%{release}

%description driver-file
The file system driver family for the FILE scheme.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-http
Group: Development/Java
Summary:	TrueZip driver for the HTTP(S) scheme
Requires:	jpackage-utils
Requires:	httpcomponents-client
Requires:	httpcomponents-core
Requires:	%{name}-driver-parent = %{version}-%{release}
Requires:	%{name}-kernel = %{version}-%{release}

%description driver-http
The file system driver for the HTTP(S) scheme.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-tar
Group: Development/Java
Summary:	TrueZip driver for TAR archives
Requires:	jpackage-utils
Requires:	apache-commons-compress
Requires:	%{name}-path = %{version}-%{release}

%description driver-tar
The file system driver family for TAR and related archive file types.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-tzp
Group: Development/Java
Summary:	TrueZip driver for ZIP.RAES (TZP) encrypted archives
Requires:	jpackage-utils
Requires:	bouncycastle
Requires:	%{name}-driver-zip = %{version}-%{release}
Requires:	%{name}-file = %{version}-%{release}

%description driver-tzp
The file system driver family for RAES encrypted ZIP alias
ZIP.RAES alias TZP files.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-zip
Group: Development/Java
Summary:	TrueZip driver for ZIP archives
Requires:	jpackage-utils
Requires:	apache-commons-compress
Requires:	bouncycastle
Requires:	%{name}-path = %{version}-%{release}
Requires:	%{name}-swing = %{version}-%{release}

%description driver-zip
TrueZIP Path module application - requires JSE 7.

%package extension-parent
Group: Development/Java
Summary:	Parent POM for TrueZip pluggable extensions
Requires:	jpackage-utils
Requires:	%{name}-parent = %{version}-%{release}

%description extension-parent
Parent POM for TrueZip pluggable extensions.

%package extension-jmx-jul
Group: Development/Java
Summary:	TrueZip JMX/JUL Extension
Requires:	jpackage-utils
Requires:	%{name}-extension-parent = %{version}-%{release}
Requires:	%{name}-driver-file = %{version}-%{release}

%description extension-jmx-jul
This module provides a file system manager and an I/O pool service
for managing and monitoring TrueZIP via JMX and java.util.logging.

Add the JAR artifact of this module to the run time class path to
make its file system manager and I/O pool service available for
service location in the client API modules.

%package extension-pace
Group: Development/Java
Summary:	TrueZip PaceManager Extension
Requires:	jpackage-utils
Requires:	%{name}-extension-parent = %{version}-%{release}
Requires:	%{name}-driver-file = %{version}-%{release}

%description extension-pace
This module constrains the number of mounted archive files in order to
save some heap space. It provides a JMX interface for monitoring and
management. Add the JAR artifact of this module to the run time class
path to make its services available for service location in the client
API modules.

%package file
Group: Development/Java
Summary:	TrueZip File*
Requires:	jpackage-utils
Requires:	jemmy
Requires:	%{name}-driver-file = %{version}-%{release}

%description file
This module provides the TFile* classes for simple, uniform,
transparent, thread-safe, read/write access to archive files
as if they were virtual directories in a file system path.

This module also provides Swing GUI classes for viewing file
trees and choosing entries in archive files.

%package kernel
Group: Development/Java
Summary:	Implements and manages virtual file systems for %{name}
Requires:	jpackage-utils
Requires:	%{name}-parent = %{version}-%{release}


%description kernel
This module implements virtual file systems from arbitrary resources,
manages their state and commits unsynchronized changes if required or
requested.

The TrueZIP Kernel uses file system drivers to access these resources.
It provides multithreading, multiplexing, caching and buffering so that
the file system drivers do not need to take care of this.

%package path
Group: Development/Java
Summary:	TrueZip Path
Requires:	jpackage-utils
Requires:	%{name}-file = %{version}-%{release}
Requires:	%{name}-parent = %{version}-%{release}

%description path
This module provides the TPath class for simple, uniform,
transparent, thread-safe, read/write access to archive
files as if they were virtual directories in a file system path.
It also provides the TFileSystemProvider class to implement a file
system provider for the NIO.2 API (JSR 203) in JSE 7.

%package samples
Group: Development/Java
Summary:	TrueZip Samples
Requires:	jpackage-utils
Requires:	%{name}-driver-tzp = %{version}-%{release}
Requires:	%{name}-extension-jmx-jul = %{version}-%{release}

%description samples
Sample applications to demonstrate the usage of various TrueZIP module
APIs.

Some of these samples use rather advanced or exotic features which
makes them more complex than necessary for a typical application.

By design, the sample applications use all file system drivers which
can be located at runtime.
Location of the available file system drivers is performed by
scanning the class path - see the Javaodoc for the TrueZIP Kernel class
de.schlichtherle.truezip.fs.sl.FsDriverLocator for more information.

%package swing
Group: Development/Java
Summary:	TrueZip general Swing GUI classes
Requires:	jpackage-utils
Requires:	jemmy
Requires:	%{name}-parent = %{version}-%{release}

%description swing
General Swing GUI classes.

This module does not depend on other TrueZIP modules.

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q

find -type f -name *.zip -delete
find -type f -name *.jar -delete
find -type f -name *.class -delete

# Parent has changed to net.java.truecommons:truecommons-parent
# which isn't in Fedora, but older parent is
%pom_set_parent de.schlichtherle:oss-parent:9

# Fix findbugs groupId (switch for new dep)
%pom_remove_dep com.google.code.findbugs:annotations
%pom_add_dep net.sourceforge.findbugs:annotations . "<optional>true</optional>"

# Add jsr-305 as dependency for javax.annotation.concurrent
%pom_add_dep org.jsr-305:ri


%build
# Skipping tests because some fail with 'Bad test setup' error
mvn-rpmbuild package javadoc:aggregate -Dmaven.test.skip=true

%install

install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# These modules all have same structure, so we loop through to install
for module in file kernel path samples swing; do
    install -m 644 %{name}-${module}/target/%{name}-${module}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${module}.jar

    install -pm 644 %{name}-${module}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${module}.pom

    %add_maven_depmap JPP.%{name}-%{name}-${module}.pom %{name}/%{name}-${module}.jar -f ${module}

done

# truezip-driver has submodules
install -pm 644 %{name}-driver/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-driver.pom
%add_maven_depmap JPP.%{name}-%{name}-driver.pom -f driver

for sub in file http tar tzp zip; do
    cp -p %{name}-driver/%{name}-driver-${sub}/target/%{name}-driver-${sub}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-driver-${sub}.jar

    install -pm 644 %{name}-driver/%{name}-driver-${sub}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-driver-${sub}.pom
    %add_maven_depmap JPP.%{name}-%{name}-driver-${sub}.pom %{name}/%{name}-driver-${sub}.jar -f driver-${sub}
done

# truezip-extensions are exceptional
install -pm 644 %{name}-extension/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-extension.pom
%add_maven_depmap JPP.%{name}-%{name}-extension.pom -f extension

for ext in extension-jmx-jul extension-pace; do
    cp -p %{name}-extension/%{name}-${ext}/target/%{name}-${ext}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${ext}.jar

    install -pm 644 %{name}-extension/%{name}-${ext}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${ext}.pom
    %add_maven_depmap JPP.%{name}-%{name}-${ext}.pom %{name}/%{name}-${ext}.jar -f ${ext}
done


#JAVADOCS
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# main POM
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom


%files parent
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%files driver-parent
%{_mavenpomdir}/JPP.%{name}-%{name}-driver.pom
%{_mavendepmapfragdir}/%{name}-driver

%files driver-file
%{_javadir}/%{name}/%{name}-driver-file.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-driver-file.pom
%{_mavendepmapfragdir}/%{name}-driver-file

%files driver-http
%{_javadir}/%{name}/%{name}-driver-http.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-driver-http.pom
%{_mavendepmapfragdir}/%{name}-driver-http

%files driver-tar
%{_javadir}/%{name}/%{name}-driver-tar.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-driver-tar.pom
%{_mavendepmapfragdir}/%{name}-driver-tar

%files driver-tzp
%{_javadir}/%{name}/%{name}-driver-tzp.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-driver-tzp.pom
%{_mavendepmapfragdir}/%{name}-driver-tzp

%files driver-zip
%{_javadir}/%{name}/%{name}-driver-zip.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-driver-zip.pom
%{_mavendepmapfragdir}/%{name}-driver-zip

%files extension-parent
%{_mavenpomdir}/JPP.%{name}-%{name}-extension.pom
%{_mavendepmapfragdir}/%{name}-extension

%files extension-jmx-jul
%{_javadir}/%{name}/%{name}-extension-jmx-jul.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-extension-jmx-jul.pom
%{_mavendepmapfragdir}/%{name}-extension-jmx-jul

%files extension-pace
%{_javadir}/%{name}/%{name}-extension-pace.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-extension-pace.pom
%{_mavendepmapfragdir}/%{name}-extension-pace

%files file
%{_javadir}/%{name}/%{name}-file.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-file.pom
%{_mavendepmapfragdir}/%{name}-file

%files kernel
%{_javadir}/%{name}/%{name}-kernel.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-kernel.pom
%{_mavendepmapfragdir}/%{name}-kernel

%files path
%{_javadir}/%{name}/%{name}-path.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-path.pom
%{_mavendepmapfragdir}/%{name}-path

%files samples
%{_javadir}/%{name}/%{name}-samples.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-samples.pom
%{_mavendepmapfragdir}/%{name}-samples

%files swing
%{_javadir}/%{name}/%{name}-swing.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-swing.pom
%{_mavendepmapfragdir}/%{name}-swing


%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 7.6.6-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 7.5.5-alt1_6jpp7
- new version

