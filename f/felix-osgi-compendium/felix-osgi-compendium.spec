Name: felix-osgi-compendium
Version: 1.4.0
Summary: Felix OSGi R4 Compendium Bundle
License: ASL 2.0
Url: http://felix.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: felix-osgi-compendium = 1.4.0-21.fc23
Provides: mvn(org.apache.felix:org.osgi.compendium) = 1.4.0
Provides: mvn(org.apache.felix:org.osgi.compendium:pom:) = 1.4.0
Provides: mvn(org.osgi:org.osgi.compendium) = 1.4.0
Provides: mvn(org.osgi:org.osgi.compendium:pom:) = 1.4.0
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(javax.servlet:javax.servlet-api)
Requires: mvn(org.apache.felix:org.osgi.core)
Requires: mvn(org.apache.felix:org.osgi.foundation)

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: felix-osgi-compendium-1.4.0-21.fc23.cpio

%description
OSGi Service Platform Release 4 Compendium Interfaces and Classes.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_16jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_14jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_12jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_12jpp7
- new release

* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_3jpp6
- dropped tomcat6-servlet-2.5-api dep to fix apache-commons-chain

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp6
- new jpp release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

