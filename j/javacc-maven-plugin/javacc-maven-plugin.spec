Name: javacc-maven-plugin
Version: 2.6
Summary: JavaCC Maven Plugin
License: ASL 2.0
Url: http://mojo.codehaus.org/javacc-maven-plugin/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: javacc-maven-plugin = 2.6-20.fc23
Provides: mvn(org.codehaus.mojo:javacc-maven-plugin) = 2.6
Provides: mvn(org.codehaus.mojo:javacc-maven-plugin:pom:) = 2.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(net.java.dev.javacc:javacc)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.reporting:maven-reporting-impl)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: javacc-maven-plugin-2.6-20.fc23.cpio

%description
Maven Plugin for processing JavaCC grammar files.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_15jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_14jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_10jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt2_10jpp7
- fixed build

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_10jpp7
- fc update

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp6
- new version

