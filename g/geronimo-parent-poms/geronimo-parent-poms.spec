Name: geronimo-parent-poms
Version: 1.6
Summary: Parent POM files for geronimo-specs
License: ASL 2.0
Url: http://geronimo.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: geronimo-parent-poms = 1.6-20.fc23
Provides: geronimo-specs = 1.6-20.fc23
Provides: mvn(org.apache.geronimo.specs:specs-parent:pom:) = 1.6
Provides: mvn(org.apache.geronimo.specs:specs:pom:) = 1.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.felix:maven-bundle-plugin)
Requires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires: mvn(org.apache.maven.plugins:maven-jar-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: geronimo-parent-poms-1.6-20.fc23.cpio

%description
The Project Object Model files for the geronimo-specs modules.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_16jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_14jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_10jpp7
- new fc release

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

