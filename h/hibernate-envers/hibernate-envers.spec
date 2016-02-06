Name: hibernate-envers
Version: 4.3.5
Summary: Hibernate Envers
License: LGPLv2+ and ASL 2.0
Url: http://www.hibernate.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hibernate-envers = 4.3.5-6.fc23
Provides: mvn(org.hibernate:hibernate-envers) = 4.3.5.Final
Provides: mvn(org.hibernate:hibernate-envers:pom:) = 4.3.5.Final
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.hibernate:hibernate-core)
Requires: mvn(org.hibernate:hibernate-entitymanager)
Requires: mvn(org.jboss.logging:jboss-logging)
Requires: mvn(org.jboss.logging:jboss-logging-annotations)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hibernate-envers-4.3.5-6.fc23.cpio

%description
Support for entity auditing.

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

