Name: sonar-plugin-api
Version: 3.2
Summary: Plugin-api module for sonar
License: LGPLv3+
Url: http://www.sonarqube.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.sonar:sonar-plugin-api) = 3.2
Provides: mvn(org.codehaus.sonar:sonar-plugin-api:pom:) = 3.2
Provides: sonar-plugin-api = 3.2-5.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml.staxmate:staxmate)
Requires: mvn(com.google.code.findbugs:jsr305)
Requires: mvn(com.google.guava:guava)
Requires: mvn(com.thoughtworks.xstream:xstream)
Requires: mvn(commons-codec:commons-codec)
Requires: mvn(commons-configuration:commons-configuration)
Requires: mvn(javax.persistence:persistence-api)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.codehaus.sonar:sonar-check-api)
Requires: mvn(org.codehaus.sonar:sonar-colorizer)
Requires: mvn(org.codehaus.sonar:sonar-duplications)
Requires: mvn(org.codehaus.sonar:sonar-graph)
Requires: mvn(org.codehaus.sonar:sonar-squid)
Requires: mvn(org.codehaus.woodstox:stax2-api)
Requires: mvn(org.codehaus.woodstox:woodstox-core-lgpl)
Requires: mvn(org.hibernate:hibernate-core:3)
Requires: mvn(org.jfree:jfreechart)
Requires: mvn(org.slf4j:jcl-over-slf4j)
Requires: mvn(org.slf4j:log4j-over-slf4j)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(xalan:xalan)
Requires: mvn(xerces:xercesImpl)
Requires: mvn(xpp3:xpp3)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sonar-plugin-api-3.2-5.fc23.cpio

%description
Plugin-api module for sonar.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

