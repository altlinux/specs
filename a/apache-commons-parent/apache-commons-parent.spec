Name: apache-commons-parent
Version: 38
Summary: Apache Commons Parent Pom
License: ASL 2.0
Url: http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-38/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-parent = 38-1.fc23
Provides: mvn(org.apache.commons:commons-parent:pom:) = 38
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.felix:maven-bundle-plugin)
Requires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
Requires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
Requires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Requires: mvn(org.apache.maven.plugins:maven-jar-plugin)
Requires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
Requires: mvn(org.apache.rat:apache-rat-plugin)
Requires: mvn(org.apache:apache:pom:)
Requires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-commons-parent-38-1.fc23.cpio

%description
The Project Object Model files for the apache-commons packages.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:38-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:32-alt1_2jpp7
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:26-alt1_5jpp7
- fc update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:22-alt2_4jpp7
- rebuild with maven-local

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:22-alt1_4jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:12-alt6_2jpp6
- build with maven-jxr

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:12-alt5_2jpp6
- dropped commons-build-plugin dependency

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt4_2jpp6
- added maven-plugin-bundle as replacement for felix-maven

* Wed Sep 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt3_2jpp6
- removed felix-maven from requires

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt2_2jpp6
- removed mojo-maven2-plugin-* from requires

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_2jpp6
- new jpp release

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_1jpp6
- fixed init script

