Name: forge-parent
Version: 38
Summary: Sonatype Forge Parent Pom
License: ASL 2.0
Url: https://docs.sonatype.org/display/FORGE/Index
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: forge-parent = 38-4.fc23
Provides: mvn(org.sonatype.forge:forge-parent:pom:) = 38
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-source-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: forge-parent-38-4.fc23.cpio

%description
Sonatype Forge is an open-source community dedicated to the creation of the
next-generation of development tools and technologies.

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 38-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 31-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 31-alt1_1jpp7
- new version

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt1_8jpp7
- fc update

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 5-alt1_7jpp6
- fixed repolib

