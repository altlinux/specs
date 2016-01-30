Name: apache-commons-beanutils
Version: 1.9.2
Summary: Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License: ASL 2.0
Url: http://commons.apache.org/beanutils
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-beanutils = 1.9.2-4.fc23
Provides: mvn(commons-beanutils:commons-beanutils) = 1.9.2
Provides: mvn(commons-beanutils:commons-beanutils-bean-collections) = 1.9.2
Provides: mvn(commons-beanutils:commons-beanutils-bean-collections:pom:) = 1.9.2
Provides: mvn(commons-beanutils:commons-beanutils-core) = 1.9.2
Provides: mvn(commons-beanutils:commons-beanutils-core:pom:) = 1.9.2
Provides: mvn(commons-beanutils:commons-beanutils:pom:) = 1.9.2
Provides: mvn(org.apache.commons:commons-beanutils) = 1.9.2
Provides: mvn(org.apache.commons:commons-beanutils-bean-collections) = 1.9.2
Provides: mvn(org.apache.commons:commons-beanutils-bean-collections:pom:) = 1.9.2
Provides: mvn(org.apache.commons:commons-beanutils-core) = 1.9.2
Provides: mvn(org.apache.commons:commons-beanutils-core:pom:) = 1.9.2
Provides: mvn(org.apache.commons:commons-beanutils:pom:) = 1.9.2
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-logging:commons-logging)

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: apache-commons-beanutils-1.9.2-4.fc23.cpio

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_9jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_7jpp7
- fc update

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_4jpp6
- fixed build

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt2_4jpp6
- fixed repolib

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_4jpp6
- new version

