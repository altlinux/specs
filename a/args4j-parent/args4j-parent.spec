Name: args4j-parent
Version: 2.32
Summary: args4j parent POM
License: MIT
Url: http://args4j.kohsuke.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: args4j-parent = 2.32-1.fc23
Provides: mvn(args4j:args4j-site:pom:) = 2.32
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.felix:maven-bundle-plugin)
Requires: mvn(org.apache.maven.plugins:maven-site-plugin)
Requires: mvn(org.kohsuke:pom:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: args4j-parent-2.32-1.fc23.cpio

%description
This package contains parent POM for args4j project.

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.32-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.25-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt1_8jpp7
- new version

