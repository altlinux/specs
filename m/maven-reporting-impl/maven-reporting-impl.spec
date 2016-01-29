Name: maven-reporting-impl
Version: 2.3
Summary: Abstract classes to manage report generation
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-reporting-impl
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-reporting-impl = 2.3-2.fc23
Provides: maven-shared-reporting-impl = 2.3-2.fc23
Provides: mvn(org.apache.maven.reporting:maven-reporting-impl) = 2.3
Provides: mvn(org.apache.maven.reporting:maven-reporting-impl:pom:) = 2.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-validator:commons-validator)
Requires: mvn(org.apache.maven.doxia:doxia-core)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-reporting-impl-2.3-2.fc23.cpio

%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

This is a replacement package for maven-shared-reporting-impl

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0jpp7
- new version

