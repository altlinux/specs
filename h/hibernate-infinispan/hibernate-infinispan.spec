Name: hibernate-infinispan
Version: 4.3.5
Summary: Hibernate Infinispan Integration
License: LGPLv2+ and ASL 2.0
Url: http://www.hibernate.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hibernate-infinispan = 4.3.5-6.fc23
Provides: mvn(org.hibernate:hibernate-infinispan) = 4.3.5.Final
Provides: mvn(org.hibernate:hibernate-infinispan:pom:) = 4.3.5.Final
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.hibernate:hibernate-core)
Requires: mvn(org.infinispan:infinispan-core)
Requires: mvn(org.jboss.logging:jboss-logging)
Requires: mvn(org.jboss.logging:jboss-logging-annotations)
Requires: mvn(org.rhq.helpers:rhq-pluginAnnotations)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hibernate-infinispan-4.3.5-6.fc23.cpio

%description
Integration of Hibernate with Infinispan.

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

