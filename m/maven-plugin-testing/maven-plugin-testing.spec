Name: maven-plugin-testing
Version: 3.3.0
Summary: Maven Plugin Testing
License: ASL 2.0
Url: http://maven.apache.org/plugin-testing/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-testing = 3.3.0-3.fc23
Provides: mvn(org.apache.maven.plugin-testing:maven-plugin-testing:pom:) = 3.3.0
Provides: mvn(org.apache.maven.shared:maven-plugin-testing:pom:) = 3.3.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-site-plugin)
Requires: mvn(org.apache.maven:maven-parent:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-testing-3.3.0-3.fc23.cpio

%description
The Maven Plugin Testing contains the necessary modules
to be able to test Maven Plugins.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_7jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_4.alpha1jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4.alpha1jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_4.alpha1jpp7
- new fc release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_3.alpha1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

