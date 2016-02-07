Name: maven-checkstyle-plugin
Version: 2.12
Summary: Plugin that generates a report regarding the code style used by the developers
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-checkstyle-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-checkstyle-plugin = 2.12-2.fc21
Provides: maven2-plugin-checkstyle = 2.12-2.fc21
Provides: mvn(org.apache.maven.plugins:maven-checkstyle-plugin) = 2.12
Provides: mvn(org.apache.maven.plugins:maven-checkstyle-plugin:pom:) = 2.12
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.puppycrawl.tools:checkstyle)
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(org.apache.maven.doxia:doxia-decoration-model)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.reporting:maven-reporting-impl)
Requires: mvn(org.apache.maven.shared:maven-doxia-tools)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-resources)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.codehaus.plexus:plexus-velocity)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-checkstyle-plugin-2.12-2.fc21.cpio

%description
Generates a report on violations of code style and optionally fails the build
if violations are detected.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt4_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_2jpp7
- new version

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_2jpp7
- complete build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

