Name: netty3
Version: 3.9.3
Summary: An asynchronous event-driven network application framework and tools for Java
License: ASL 2.0 and BSD
Url: https://netty.io/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(io.netty:netty:3) = 3.9.3.Final
Provides: mvn(io.netty:netty:3.9.3) = 3.9.3.Final
Provides: mvn(io.netty:netty:3.9.3.Final) = 3.9.3.Final
Provides: mvn(io.netty:netty:pom:3) = 3.9.3.Final
Provides: mvn(io.netty:netty:pom:3.9.3) = 3.9.3.Final
Provides: mvn(io.netty:netty:pom:3.9.3.Final) = 3.9.3.Final
Provides: mvn(org.jboss.netty:netty:3) = 3.9.3.Final
Provides: mvn(org.jboss.netty:netty:3.9.3) = 3.9.3.Final
Provides: mvn(org.jboss.netty:netty:3.9.3.Final) = 3.9.3.Final
Provides: mvn(org.jboss.netty:netty:pom:3) = 3.9.3.Final
Provides: mvn(org.jboss.netty:netty:pom:3.9.3) = 3.9.3.Final
Provides: mvn(org.jboss.netty:netty:pom:3.9.3.Final) = 3.9.3.Final
Provides: netty3 = 3.9.3-1.fc23
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.jcraft:jzlib)
Requires: mvn(io.netty:netty-tcnative)
Requires: netty-tcnative

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: netty3-3.9.3-1.fc23.cpio

%description
Netty is a NIO client server framework which enables quick and easy
development of network applications such as protocol servers and
clients. It greatly simplifies and streamlines network programming
such as TCP and UDP socket server.

'Quick and easy' doesn't mean that a resulting application will suffer
from a maintainability or a performance issue. Netty has been designed
carefully with the experiences earned from the implementation of a lot
of protocols such as FTP, SMTP, HTTP, and various binary and
text-based legacy protocols. As a result, Netty has succeeded to find
a way to achieve ease of development, performance, stability, and
flexibility without a compromise.

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
* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 3.9.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

