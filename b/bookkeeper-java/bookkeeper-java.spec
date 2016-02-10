Name: bookkeeper-java
Version: 4.2.1
Summary: BookKeeper/Hedwig Java libraries
License: ASL 2.0
Url: http://zookeeper.apache.org/bookkeeper/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: bookkeeper-java = 4.2.1-18.fc23
Provides: mvn(org.apache.bookkeeper:bookkeeper-server) = 4.2.1
Provides: mvn(org.apache.bookkeeper:bookkeeper-server:pom:) = 4.2.1
Provides: mvn(org.apache.bookkeeper:bookkeeper:pom:) = 4.2.1
Provides: mvn(org.apache.bookkeeper:hedwig-client) = 4.2.1
Provides: mvn(org.apache.bookkeeper:hedwig-client:pom:) = 4.2.1
Provides: mvn(org.apache.bookkeeper:hedwig-protocol) = 4.2.1
Provides: mvn(org.apache.bookkeeper:hedwig-protocol:pom:) = 4.2.1
Provides: mvn(org.apache.bookkeeper:hedwig-server) = 4.2.1
Provides: mvn(org.apache.bookkeeper:hedwig-server:pom:) = 4.2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.google.guava:guava)
Requires: mvn(com.google.protobuf:protobuf-java)
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(commons-codec:commons-codec)
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-configuration:commons-configuration)
Requires: mvn(commons-io:commons-io)
Requires: mvn(io.netty:netty:3.9.3.Final)
Requires: mvn(jline:jline)
Requires: mvn(log4j:log4j:1.2.17)
Requires: mvn(org.apache.derby:derby)
Requires: mvn(org.apache.zookeeper:zookeeper)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.slf4j:slf4j-log4j12)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: bookkeeper-java-4.2.1-18.fc23.cpio

%description
This package contains BookKeeper/Hedwig Java libraries.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

