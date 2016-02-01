Name: args4j-tools
Version: 2.32
Summary: Development-time tool for generating additional artifacits
License: MIT
Url: http://args4j.kohsuke.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: args4j-tools = 2.32-1.fc23
Provides: mvn(args4j:args4j-tools) = 2.32
Provides: mvn(args4j:args4j-tools:pom:) = 2.32
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(args4j:args4j)
Requires: mvn(com.sun:tools)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: args4j-tools-2.32-1.fc23.cpio

%description
This package contains args4j development-time tool for generating
additional artifacits.

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

