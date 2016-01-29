Name: weld-parent
Version: 31
Summary: Parent POM for Weld
License: ASL 2.0
Url: http://seamframework.org/Weld
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.jboss.weld:weld-parent:pom:) = 31
Provides: weld-parent = 31-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Requires: mvn(org.apache.maven.plugins:maven-source-plugin)
Requires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: weld-parent-31-2.fc23.cpio

%description
Parent POM for Weld

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 31-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 26-alt1_1jpp7
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 17-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 17-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 17-alt1_4jpp7
- new version

