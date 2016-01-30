Name: apache-commons-digester
Version: 2.1
Summary: XML to Java object mapping module
License: ASL 2.0
Url: http://commons.apache.org/digester/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-digester = 2.1-5.fc23
Provides: mvn(commons-digester:commons-digester) = 2.1
Provides: mvn(commons-digester:commons-digester:pom:) = 2.1
Provides: mvn(org.apache.commons:commons-digester) = 2.1
Provides: mvn(org.apache.commons:commons-digester:pom:) = 2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-beanutils:commons-beanutils)
Requires: mvn(commons-logging:commons-logging)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: apache-commons-digester-2.1-5.fc23.cpio

%description
Many projects read XML configuration files to provide initialization of
various Java objects within the system. There are several ways of doing this,
and the Digester component was designed to provide a common implementation
that can be used in many different projects

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_14jpp7
- new release

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_11jpp7
- fc update

* Tue Mar 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_11jpp6
- bumped release to fix obsoletes

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt2_11jpp6
- fixed repolib version

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt1_11jpp6
- new version

