Name: hibernate-core
Version: 4.3.5
Summary: Hibernate Core
License: LGPLv2+ and ASL 2.0
Url: http://www.hibernate.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hibernate-core = 4.3.5-6.fc23
Provides: mvn(org.hibernate:hibernate-core) = 4.3.5.Final
Provides: mvn(org.hibernate:hibernate-core:pom:) = 4.3.5.Final
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(antlr:antlr)
Requires: mvn(com.fasterxml:classmate)
Requires: mvn(dom4j:dom4j)
Requires: mvn(javax.validation:validation-api)
Requires: mvn(org.hibernate.common:hibernate-commons-annotations)
Requires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
Requires: mvn(org.javassist:javassist)
Requires: mvn(org.jboss.logging:jboss-logging)
Requires: mvn(org.jboss.logging:jboss-logging-annotations)
Requires: mvn(org.jboss.spec.javax.security.jacc:jboss-jacc-api_1.4_spec)
Requires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
Requires: mvn(org.jboss:jandex)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hibernate-core-4.3.5-6.fc23.cpio

%description
Core Hibernate O/RM functionality

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

