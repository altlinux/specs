Name: maven-doxia-tools
Version: 1.6
Summary: Maven Doxia Integration Tools
License: ASL 2.0
Url: http://maven.apache.org/doxia/doxia-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-doxia-tools = 1.6-3.fc23
Provides: mvn(org.apache.maven.doxia:doxia-integration-tools) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-integration-tools:pom:) = 1.6
Provides: mvn(org.apache.maven.shared:maven-doxia-tools) = 1.6
Provides: mvn(org.apache.maven.shared:maven-doxia-tools:pom:) = 1.6
Provides: mvn(org.apache.maven:doxia-integration-tools) = 1.6
Provides: mvn(org.apache.maven:doxia-integration-tools:pom:) = 1.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(org.apache.maven.doxia:doxia-decoration-model)
Requires: mvn(org.apache.maven.doxia:doxia-logging-api)
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-i18n)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-doxia-tools-1.6-3.fc23.cpio

%description
A collection of tools to help the integration of Doxia in Maven plugins.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_12jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_11jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_5jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

