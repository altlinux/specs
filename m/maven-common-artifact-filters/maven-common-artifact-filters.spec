Name: maven-common-artifact-filters
Version: 1.4
Summary: Maven Common Artifact Filters
License: ASL 2.0
Url: http://maven.apache.org/shared/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-common-artifact-filters = 1.4-16.fc23
Provides: maven-shared-common-artifact-filters = 1.4-16.fc23
Provides: mvn(org.apache.maven.shared:maven-common-artifact-filters) = 1.4
Provides: mvn(org.apache.maven.shared:maven-common-artifact-filters:pom:) = 1.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: maven-common-artifact-filters-1.4-16.fc23.cpio

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_11jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_3jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

