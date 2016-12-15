%filter_from_requires /^java-headless/d
Name: eclipse-jdt
Version: 4.6.0
Summary: Eclipse Java Development Tools
License: EPL
Url: http://www.eclipse.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: eclipse = 1:4.6.0-0.6.git201605092000.fc24
Provides: eclipse-jdt = 1:4.6.0-0.6.git201605092000.fc24
Provides: mvn(org.eclipse.ant:org.eclipse.ant.launching) = 1.1.200.SNAPSHOT
Provides: mvn(org.eclipse.ant:org.eclipse.ant.ui) = 3.6.200.SNAPSHOT
Provides: mvn(org.eclipse.jdt.feature:org.eclipse.jdt) = 3.12.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt) = 3.12.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.annotation) = 1.1.100.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.annotation) = 2.1.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.apt.core) = 3.4.100.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.apt.pluggable.core) = 1.1.100.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.apt.ui) = 3.4.100.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.compiler.apt) = 1.2.100.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.compiler.tool) = 1.1.100.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.core) = 3.12.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.core.manipulation) = 1.7.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.debug) = 3.10.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.debug.ui) = 3.7.200.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.doc.user) = 3.12.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.junit) = 3.9.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.junit.core) = 3.8.0.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.junit.runtime) = 3.4.600.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.junit4.runtime) = 1.1.600.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.launching) = 3.8.100.SNAPSHOT
Provides: mvn(org.eclipse.jdt:org.eclipse.jdt.ui) = 3.12.0.SNAPSHOT
Provides: osgi(org.eclipse.ant.launching) = 1.1.200.v20160511.1000
Provides: osgi(org.eclipse.ant.ui) = 3.6.200.v20160511.1000
Provides: osgi(org.eclipse.jdt) = 3.12.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.annotation) = 1.1.100.v20160511.1000
Provides: osgi(org.eclipse.jdt.annotation) = 2.1.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.apt.core) = 3.4.100.v20160511.1000
Provides: osgi(org.eclipse.jdt.apt.pluggable.core) = 1.1.100.v20160511.1000
Provides: osgi(org.eclipse.jdt.apt.ui) = 3.4.100.v20160511.1000
Provides: osgi(org.eclipse.jdt.compiler.apt) = 1.2.100.v20160511.1000
Provides: osgi(org.eclipse.jdt.compiler.tool) = 1.1.100.v20160511.1000
Provides: osgi(org.eclipse.jdt.core) = 3.12.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.core.manipulation) = 1.7.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.debug) = 3.10.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.debug.ui) = 3.7.200.v20160511.1000
Provides: osgi(org.eclipse.jdt.doc.user) = 3.12.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.junit) = 3.9.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.junit.core) = 3.8.0.v20160511.1000
Provides: osgi(org.eclipse.jdt.junit.runtime) = 3.4.600.v20160511.1000
Provides: osgi(org.eclipse.jdt.junit4.runtime) = 1.1.600.v20160511.1000
Provides: osgi(org.eclipse.jdt.launching) = 3.8.100.v20160511.1000
Provides: osgi(org.eclipse.jdt.ui) = 3.12.0.v20160511.1000
Requires: /bin/sh
Requires: eclipse-platform
Requires: hamcrest-core
Requires: jpackage-utils
Requires: junit
Requires: osgi(org.junit)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: eclipse-jdt-4.6.0-0.6.git201605092000.fc24.cpio

%description
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

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
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

