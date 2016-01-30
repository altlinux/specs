Name: maven-javadoc-plugin
Version: 2.10.3
Summary: Maven Javadoc Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-javadoc-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-javadoc-plugin = 2.10.3-2.fc23
Provides: mvn(org.apache.maven.plugins:maven-javadoc-plugin) = 2.10.3
Provides: mvn(org.apache.maven.plugins:maven-javadoc-plugin:pom:) = 2.10.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(commons-logging:commons-logging)
Requires: mvn(log4j:log4j)
Requires: mvn(org.apache.httpcomponents:httpclient)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
Requires: mvn(org.apache.maven.shared:maven-invoker)
Requires: mvn(org.apache.maven.wagon:wagon-provider-api)
Requires: mvn(org.apache.maven:maven-archiver)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-settings)
Requires: mvn(org.codehaus.plexus:plexus-archiver)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-interactivity-api)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-javadoc-plugin-2.10.3-2.fc23.cpio

%description
The Maven Javadoc Plugin is a plugin that uses the javadoc tool for
generating javadocs for the specified project.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_1.1jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt2_2jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

