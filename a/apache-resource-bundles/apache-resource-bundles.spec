Name: apache-resource-bundles
Version: 2
Summary: Apache Resource Bundles
License: ASL 2.0
Url: http://repo1.maven.org/maven2/org/apache/apache-resource-bundles/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-resource-bundles = 2-16.fc23
Provides: mvn(org.apache:apache-incubator-disclaimer-resource-bundle) = 1.1
Provides: mvn(org.apache:apache-incubator-disclaimer-resource-bundle:pom:) = 1.1
Provides: mvn(org.apache:apache-jar-resource-bundle) = 1.4
Provides: mvn(org.apache:apache-jar-resource-bundle:pom:) = 1.4
Provides: mvn(org.apache:apache-license-header-resource-bundle) = 1.1
Provides: mvn(org.apache:apache-license-header-resource-bundle:pom:) = 1.1
Provides: mvn(org.apache:apache-resource-bundles:pom:) = 2
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: apache-resource-bundles-2-16.fc23.cpio

%description
An archive which contains templates for generating the necessary license files
and notices for all Apache releases.

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
* Wed Jan 27 2016 Igor Vlasenko <viy@altlinux.ru> 1:2-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt2_11jpp7
- fixed build

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt2_9jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt2_8jpp7
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt1_8jpp7
- update

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:3-alt3_2jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt2_2jpp6
- fixed build

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_2jpp6
- new jpp relase

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2-alt2_1jpp6
- apache-jar-resource-bundle is made compat package.

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:2-alt1_1jpp6
- new version
