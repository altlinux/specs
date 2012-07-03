Name: netty
Version: 3.2.4
Summary: An asynchronous event-driven network application framework and tools for Java
License: ASL 2.0
Url: http://www.jboss.org/netty
Packager: Igor Vlasenko <viy@altlinux.ru>
#Requires: java
#Requires: protobuf-java

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: netty-3.2.4-2.fc17.cpio

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
* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

