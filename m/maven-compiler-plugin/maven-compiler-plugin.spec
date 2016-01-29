Name: maven-compiler-plugin
Version: 3.3
Summary: Maven Compiler Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-compiler-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-compiler-plugin = 3.3-2.fc23
Provides: mvn(org.apache.maven.plugins:maven-compiler-plugin) = 3.3
Provides: mvn(org.apache.maven.plugins:maven-compiler-plugin:pom:) = 3.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.shared:maven-shared-incremental)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-toolchain)
Requires: mvn(org.codehaus.plexus:plexus-compiler-api)
Requires: mvn(org.codehaus.plexus:plexus-compiler-javac)
Requires: mvn(org.codehaus.plexus:plexus-compiler-manager)
Requires: mvn(org.codehaus.plexus:plexus-container-default)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-compiler-plugin-3.3-2.fc23.cpio

%description
The Compiler Plugin is used to compile the sources of your project.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2_2jpp7
- rebuild with maven.req

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt3_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_2jpp7
- new release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

