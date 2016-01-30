Name: maven-plugin-bundle
Version: 2.5.4
Summary: Maven Bundle Plugin
License: ASL 2.0
Url: http://felix.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-bundle = 2.5.4-1.fc23
Provides: mvn(org.apache.felix:maven-bundle-plugin) = 2.5.4
Provides: mvn(org.apache.felix:maven-bundle-plugin:pom:) = 2.5.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(biz.aQute.bnd:biz.aQute.bndlib)
Requires: mvn(net.sf.kxml:kxml2)
Requires: mvn(org.apache.felix:org.apache.felix.bundlerepository)
Requires: mvn(org.apache.felix:org.apache.felix.framework)
Requires: mvn(org.apache.felix:org.apache.felix.utils)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)
Requires: mvn(org.apache.maven.reporting:maven-reporting-impl)
Requires: mvn(org.apache.maven.shared:maven-dependency-tree)
Requires: mvn(org.apache.maven:maven-archiver)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.osgi:org.osgi.core)
Requires: mvn(org.sonatype.plexus:plexus-build-api)
Requires: glassfish-servlet-api

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-bundle-2.5.4-1.fc23.cpio

%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt3_10jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_4jpp7
- new version

* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_12jpp6
- fixed buildrequires

* Fri Oct 15 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_4jpp6
- new version

