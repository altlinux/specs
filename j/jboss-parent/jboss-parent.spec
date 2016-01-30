Name: jboss-parent
Version: 11
Summary: JBoss Parent POM
License: Public Domain
Url: http://www.jboss.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-parent = 11-6.fc23
Provides: mvn(org.jboss:jboss-parent:pom:) = 11
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.sun:tools)
Requires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Requires: mvn(org.apache.maven.plugins:maven-source-plugin)
Requires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: jboss-parent-11-6.fc23.cpio

%description
The Project Object Model files for JBoss packages.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:11-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:11-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:6-alt2_10jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:6-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:6-alt1_8jpp7
- new version

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_0.CR1.1jpp6
- jpp 6.0 release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_4jpp5
- new version

