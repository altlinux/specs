
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: jgit
Version: 5.6.0
Summary: A pure java implementation of git
License: BSD
Url: https://www.eclipse.org/jgit/
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jgit = 5.6.0-2.fc32
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit-parent:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ant) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ant:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.archive) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.archive:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.apache) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.apache:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.server) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.server:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit.http) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit.http:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit.ssh) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit.ssh:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.server) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.server:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.pgm) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.pgm:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ssh.apache) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ssh.apache:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ui) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ui:pom:) = 5.6.0.201912101111.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit:pom:) = 5.6.0.201912101111.r
Provides: osgi(org.eclipse.jgit) = 5.6.0
Provides: osgi(org.eclipse.jgit.ant) = 5.6.0
Provides: osgi(org.eclipse.jgit.archive) = 5.6.0
Provides: osgi(org.eclipse.jgit.http.apache) = 5.6.0
Provides: osgi(org.eclipse.jgit.http.server) = 5.6.0
Provides: osgi(org.eclipse.jgit.junit) = 5.6.0
Provides: osgi(org.eclipse.jgit.junit.http) = 5.6.0
Provides: osgi(org.eclipse.jgit.junit.ssh) = 5.6.0
Provides: osgi(org.eclipse.jgit.lfs) = 5.6.0
Provides: osgi(org.eclipse.jgit.lfs.server) = 5.6.0
Provides: osgi(org.eclipse.jgit.pgm) = 5.6.0
Provides: osgi(org.eclipse.jgit.ssh.apache) = 5.6.0
Provides: osgi(org.eclipse.jgit.ui) = 5.6.0
Requires: apache-sshd
Requires: bouncycastle
Requires: mvn(args4j:args4j)
Requires: mvn(com.google.code.gson:gson)
Requires: mvn(com.googlecode.javaewah:JavaEWAH)
Requires: mvn(com.jcraft:jsch)
Requires: mvn(com.jcraft:jzlib)
Requires: mvn(net.i2p.crypto:eddsa)
Requires: mvn(org.apache.ant:ant)
Requires: mvn(org.apache.commons:commons-compress)
Requires: mvn(org.apache.httpcomponents:httpclient)
Requires: mvn(org.apache.httpcomponents:httpcore)
#Requires: mvn(org.apache.sshd:sshd-osgi)
Requires: mvn(org.apache.sshd:sshd-sftp)
Requires: mvn(org.bouncycastle:bcpg-jdk15on)
Requires: mvn(org.bouncycastle:bcpkix-jdk15on)
Requires: mvn(org.bouncycastle:bcprov-jdk15on)
Requires: mvn(org.eclipse.jetty:jetty-servlet)
Requires: mvn(org.osgi:osgi.core)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.slf4j:slf4j-simple)

BuildArch: noarch
Source: jgit-5.6.0-2.fc32.cpio


%description
A pure Java implementation of the Git version control system and command
line interface.

%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}
sed -i s,/usr/bin/sh,/bin/sh, usr/bin/jgit

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

