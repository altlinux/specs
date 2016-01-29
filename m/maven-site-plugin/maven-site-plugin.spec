Name: maven-site-plugin
Version: 3.4
Summary: Maven Site Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-site-plugin/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-site-plugin = 3.4-4.fc23
Provides: mvn(org.apache.maven.plugins:maven-site-plugin) = 3.4
Provides: mvn(org.apache.maven.plugins:maven-site-plugin:pom:) = 3.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(javax.servlet:servlet-api)
Requires: mvn(org.apache.maven.doxia:doxia-core)
Requires: mvn(org.apache.maven.doxia:doxia-decoration-model)
Requires: mvn(org.apache.maven.doxia:doxia-integration-tools)
Requires: mvn(org.apache.maven.doxia:doxia-logging-api)
Requires: mvn(org.apache.maven.doxia:doxia-module-apt)
Requires: mvn(org.apache.maven.doxia:doxia-module-fml)
Requires: mvn(org.apache.maven.doxia:doxia-module-markdown)
Requires: mvn(org.apache.maven.doxia:doxia-module-xdoc)
Requires: mvn(org.apache.maven.doxia:doxia-module-xhtml)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.reporting:maven-reporting-exec)
Requires: mvn(org.apache.maven.wagon:wagon-provider-api)
Requires: mvn(org.apache.maven:maven-archiver)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-settings)
Requires: mvn(org.apache.maven:maven-settings-builder)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.codehaus.plexus:plexus-archiver)
Requires: mvn(org.codehaus.plexus:plexus-i18n)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.codehaus.plexus:plexus-velocity)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-site-plugin-3.4-4.fc23.cpio

%description
The Maven Site Plugin is a plugin that generates a site for the current project.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt4_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_2jpp7
- new version

* Thu Apr 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.3jpp
- added obsoletes on maven2-plugin-site

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.2jpp
- added oro dependency to pom

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

