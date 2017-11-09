Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          truezip
Version:       7.7.9
Release:       alt1_5jpp8
Summary:       Java based VFS for treating archive files as virtual directories

License:       EPL
URL:           http://truezip.java.net/

# hg clone https://hg.java.net/hg/truezip~v7 && cd truezip~v7/
# hg archive -r truezip-7.7.9 truezip-7.7.9.tar.gz -X ".hg*"
Source0:       %{name}-%{version}.tar.gz
Source1:       http://www.eclipse.org/legal/epl-v10.html

BuildArch:     noarch
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(junit:junit)
# Use truecommons-parent:107
BuildRequires: mvn(net.java.truecommons:truecommons-parent:pom:)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.jsr-305:ri)
BuildRequires: mvn(org.netbeans:jemmy)
BuildRequires: mvn(org.tukaani:xz)

Requires:      %{name}-driver-parent = %{version}-%{release}
Requires:      %{name}-driver-file = %{version}-%{release}
Requires:      %{name}-driver-http = %{version}-%{release}
Requires:      %{name}-driver-tar = %{version}-%{release}
Requires:      %{name}-driver-tzp = %{version}-%{release}
Requires:      %{name}-driver-zip = %{version}-%{release}
Requires:      %{name}-extension-parent = %{version}-%{release}
Requires:      %{name}-extension-jmx-jul = %{version}-%{release}
Requires:      %{name}-extension-pace = %{version}-%{release}
Requires:      %{name}-file = %{version}-%{release}
Requires:      %{name}-kernel = %{version}-%{release}
Requires:      %{name}-path = %{version}-%{release}
Requires:      %{name}-samples = %{version}-%{release}
Requires:      %{name}-swing = %{version}-%{release}
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
Summary:       Parent POM for TrueZip modules

%description parent
Parent POM for TrueZip modules.

%package driver-parent
Group: Development/Java
Summary:       Parent POM for TrueZip pluggable file system drivers

%description driver-parent
Parent POM for TrueZip pluggable file system drivers.

%package driver-file
Group: Development/Java
Summary:       TrueZip driver for the FILE scheme

%description driver-file
The file system driver family for the FILE scheme.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-http
Group: Development/Java
Summary:       TrueZip driver for the HTTP(S) scheme

%description driver-http
The file system driver for the HTTP(S) scheme.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-tar
Group: Development/Java
Summary:       TrueZip driver for TAR archives

%description driver-tar
The file system driver family for TAR and related archive file types.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-tzp
Group: Development/Java
Summary:       TrueZip driver for ZIP.RAES (TZP) encrypted archives

%description driver-tzp
The file system driver family for RAES encrypted ZIP alias
ZIP.RAES alias TZP files.

Add the JAR artifact of this module to the run time class path to
make its file system drivers available for service location in the
client API modules.

%package driver-zip
Group: Development/Java
Summary:       TrueZip driver for ZIP archives

%description driver-zip
TrueZIP Path module application - requires JSE 7.

%package extension-parent
Group: Development/Java
Summary:       Parent POM for TrueZip pluggable extensions

%description extension-parent
Parent POM for TrueZip pluggable extensions.

%package extension-jmx-jul
Group: Development/Java
Summary:       TrueZip JMX/JUL Extension

%description extension-jmx-jul
This module provides a file system manager and an I/O pool service
for managing and monitoring TrueZIP via JMX and java.util.logging.

Add the JAR artifact of this module to the run time class path to
make its file system manager and I/O pool service available for
service location in the client API modules.

%package extension-pace
Group: Development/Java
Summary:       TrueZip PaceManager Extension

%description extension-pace
This module constrains the number of mounted archive files in order to
save some heap space. It provides a JMX interface for monitoring and
management. Add the JAR artifact of this module to the run time class
path to make its services available for service location in the client
API modules.

%package file
Group: Development/Java
Summary:       TrueZip File*

%description file
This module provides the TFile* classes for simple, uniform,
transparent, thread-safe, read/write access to archive files
as if they were virtual directories in a file system path.

This module also provides Swing GUI classes for viewing file
trees and choosing entries in archive files.

%package kernel
Group: Development/Java
Summary:       Implements and manages virtual file systems for %{name}


%description kernel
This module implements virtual file systems from arbitrary resources,
manages their state and commits unsynchronized changes if required or
requested.

The TrueZIP Kernel uses file system drivers to access these resources.
It provides multithreading, multiplexing, caching and buffering so that
the file system drivers do not need to take care of this.

%package path
Group: Development/Java
Summary:       TrueZip Path

%description path
This module provides the TPath class for simple, uniform,
transparent, thread-safe, read/write access to archive
files as if they were virtual directories in a file system path.
It also provides the TFileSystemProvider class to implement a file
system provider for the NIO.2 API (JSR 203) in JSE 7.

%package samples
Group: Development/Java
Summary:       TrueZip Samples

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
Summary:       TrueZip general Swing GUI classes

%description swing
General Swing GUI classes.

This module does not depend on other TrueZIP modules.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -type f -name *.zip -delete
find -type f -name *.jar -delete
find -type f -name *.class -delete

# Add jsr-305 as dependency for javax.annotation.concurrent
%pom_add_dep org.jsr-305:ri

# ${project.groupId} doesn't seem to get expanded properly here
%pom_remove_dep :%{name}-kernel %{name}-extension
%pom_add_dep de.schlichtherle.%{name}:%{name}-kernel:%{version} %{name}-extension
%pom_remove_dep :%{name}-kernel %{name}-driver
%pom_add_dep de.schlichtherle.%{name}:%{name}-kernel:%{version} %{name}-driver

find -name pom.xml -exec \
 sed -i -e "s/\${project.groupId}/de.schlichtherle.truezip/g" -e "s/\${project.version}/%{version}/g" {} \;

%pom_disable_module %{name}-archetype

%pom_remove_plugin -r :maven-assembly-plugin

# javascript not allowed in javadoc
%pom_xpath_remove "pom:properties/pom:header"

cp -p %{SOURCE1} .

%build
# Skipping tests because some fail with 'Bad test setup' error
%mvn_build -s --skip-tests

%install
%mvn_install

%files parent -f .mfiles-%{name}
%files javadoc -f .mfiles-javadoc
%doc epl-v10.html
%files driver-parent -f .mfiles-%{name}-driver
%files driver-file -f .mfiles-%{name}-driver-file
%files driver-http -f .mfiles-%{name}-driver-http
%files driver-tar -f .mfiles-%{name}-driver-tar
%files driver-tzp -f .mfiles-%{name}-driver-tzp
%files driver-zip -f .mfiles-%{name}-driver-zip
%files extension-parent -f .mfiles-%{name}-extension
%files extension-jmx-jul -f .mfiles-%{name}-extension-jmx-jul
%files extension-pace -f .mfiles-%{name}-extension-pace
%files file -f .mfiles-%{name}-file
%files kernel -f .mfiles-%{name}-kernel
%doc epl-v10.html
%files path -f .mfiles-%{name}-path
%files samples -f .mfiles-%{name}-samples
%files swing -f .mfiles-%{name}-swing

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 7.7.9-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 7.7.9-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 7.7.9-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 7.7.9-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 7.7.5-alt1_7jpp8
- java 8 mass update

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 7.6.6-alt2_4jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 7.6.6-alt2_1jpp7
- rebuild with maven-local

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 7.6.6-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 7.5.5-alt1_6jpp7
- new version

