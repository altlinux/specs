Name: hibernate-jpamodelgen
Version: 1.3.0
Summary: Hibernate JPA 2 Metamodel Generator
License: ASL 2.0
Url: http://www.hibernate.org/subprojects/jpamodelgen.html
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hibernate-jpamodelgen = 1.3.0-1.fc23
Provides: mvn(org.hibernate:hibernate-jpamodelgen) = 1.3.0.Final
Provides: mvn(org.hibernate:hibernate-jpamodelgen:pom:) = 1.3.0.Final
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hibernate-jpamodelgen-1.3.0-1.fc23.cpio

%description
Annotation Processor to generate JPA 2 static meta-model classes.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2jpp7
- new version

