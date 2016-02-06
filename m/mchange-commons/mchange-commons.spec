Name: mchange-commons
Version: 0.2.7
Summary: A collection of general purpose utilities for c3p0
License: LGPLv2 or EPL
Url: https://github.com/swaldman/mchange-commons-java
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mchange-commons = 0.2.7-1.fc21
Provides: mvn(com.mchange:mchange-commons-java) = 0.2.7
Provides: mvn(com.mchange:mchange-commons-java:pom:) = 0.2.7
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: mchange-commons-0.2.7-1.fc21.cpio

%description
Originally part of c3p0, mchange-commons is a set of general purpose
utilities.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3.4-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3.4-alt1_2jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_0.7.20110130hgjpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_0.5.20110130hgjpp7
- fc version

