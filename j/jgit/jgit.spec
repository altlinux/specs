%filter_from_requires /^java-headless/d
Name: jgit
Version: 4.3.0
Summary: Java-based command line Git interface
License: BSD
Url: http://www.eclipse.org/egit/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jgit = 4.3.0-2.fc24
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit-parent:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ant) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ant.test) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ant.test:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ant:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.archive) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.archive:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.apache) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.apache:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.server) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.server:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.test) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.http.test:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit.http) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit.http:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.junit:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.server) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.server.test) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.server.test:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.server:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.test) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs.test:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.lfs:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.pgm) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.pgm.test) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.pgm.test:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.pgm:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.test) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.test:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ui) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit.ui:pom:) = 4.3.0.201604071810.r
Provides: mvn(org.eclipse.jgit:org.eclipse.jgit:pom:) = 4.3.0.201604071810.r
Provides: osgi(org.eclipse.jgit) = 4.3.0
Provides: osgi(org.eclipse.jgit.ant) = 4.3.0
Provides: osgi(org.eclipse.jgit.archive) = 4.3.0
Provides: osgi(org.eclipse.jgit.http.apache) = 4.3.0
Provides: osgi(org.eclipse.jgit.http.server) = 4.3.0
Provides: osgi(org.eclipse.jgit.junit) = 4.3.0
Provides: osgi(org.eclipse.jgit.junit.http) = 4.3.0
Provides: osgi(org.eclipse.jgit.lfs) = 4.3.0
Provides: osgi(org.eclipse.jgit.lfs.server) = 4.3.0
Provides: osgi(org.eclipse.jgit.pgm) = 4.3.0
Provides: osgi(org.eclipse.jgit.ui) = 4.3.0
Requires: /bin/sh
Requires: jpackage-utils
Requires: mvn(args4j:args4j)
Requires: mvn(com.google.code.gson:gson)
Requires: mvn(com.googlecode.javaewah:JavaEWAH)
Requires: mvn(com.jcraft:jsch)
Requires: mvn(junit:junit)
Requires: mvn(org.apache.ant:ant)
Requires: mvn(org.apache.commons:commons-compress)
Requires: mvn(org.apache.httpcomponents:httpclient)
Requires: mvn(org.eclipse.jetty:jetty-servlet)
Requires: mvn(org.eclipse.osgi:org.eclipse.osgi)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.slf4j:slf4j-simple)
Requires: osgi(com.jcraft.jsch)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jgit-4.3.0-2.fc24.cpio

%description
Command line Git tool built entirely in Java.

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
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

