Name: maven-remote-resources-plugin
Version: 1.4
Summary: Maven Remote Resources Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-remote-resources-plugin/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-remote-resources-plugin = 1.4-10.fc23
Provides: mvn(org.apache.maven.plugins:maven-remote-resources-plugin) = 1.4
Provides: mvn(org.apache.maven.plugins:maven-remote-resources-plugin:pom:) = 1.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.shared:maven-artifact-resolver)
Requires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
Requires: mvn(org.apache.maven.shared:maven-filtering)
Requires: mvn(org.apache.maven:maven-artifact:2.0.6)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model:2.0.6)
Requires: mvn(org.apache.maven:maven-monitor)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.maven:maven-settings:2.0.6)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-resources)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.codehaus.plexus:plexus-velocity)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: maven-remote-resources-plugin-1.4-10.fc23.cpio

%description
Process resources packaged in JARs that have been deployed to
a remote repository. The primary use case being satisfied is
the consistent inclusion of common resources in a large set of
projects. Maven projects at Apache use this plug-in to satisfy
licensing requirements at Apache where each project much include
license and notice files for each release.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2jpp7
- new release

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp7
- new version

