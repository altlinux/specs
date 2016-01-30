Name: spock-core
Version: 0.7
Summary: Spock Framework - Core Module
License: ASL 2.0
Url: https://github.com/spockframework/spock
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.spockframework:spock-core) = 0.7.groovy.2.0
Provides: mvn(org.spockframework:spock-core:pom:) = 0.7.groovy.2.0
Provides: spock-core = 0.7-0.9.groovy.2.0.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(junit:junit)
Requires: mvn(org.codehaus.groovy:groovy-all)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: spock-core-0.7-0.9.groovy.2.0.fc23.cpio

%description
Spock Framework - Core Module.

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
* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_0.2.groovy.1.8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_0.5.groovy.1.8jpp7
- new release

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_0.3.groovy.1.8jpp7
- merged junit-junit4

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_0.3%(echo -groovy-1.8 | tr - . )jpp7
- fixed build with new junit

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_0.3%(echo -groovy-1.8 | tr - . )jpp7
- new version

