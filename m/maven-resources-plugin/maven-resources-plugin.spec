Name: maven-resources-plugin
Version: 2.7
Summary: Maven Resources Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-resources-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-resources-plugin = 2.7-3.fc23
Provides: mvn(org.apache.maven.plugins:maven-resources-plugin) = 2.7
Provides: mvn(org.apache.maven.plugins:maven-resources-plugin:pom:) = 2.7
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.shared:maven-filtering)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model:2.2.1)
Requires: mvn(org.apache.maven:maven-monitor)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.maven:maven-settings:2.2.1)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-resources-plugin-2.7-3.fc23.cpio

%description
The Resources Plugin handles the copying of project resources
to the output directory.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_6jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_3jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt2_6jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_6jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

