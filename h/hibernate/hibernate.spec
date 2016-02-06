Name: hibernate
Version: 4.3.5
Summary: Relational persistence and query service
License: LGPLv2+ and ASL 2.0
Url: http://www.hibernate.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hibernate = 4.3.5-6.fc23
Provides: mvn(org.hibernate:hibernate-parent:pom:) = 4.3.5.Final
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hibernate-4.3.5-6.fc23.cpio

%description
Hibernate is a powerful, ultra-high performance
object/relational persistence and query service
for Java. Hibernate lets you develop persistent
objects following common Java idiom - including
association, inheritance, polymorphism, composition
and the Java collections framework. Extremely
fine-grained, richly typed object models are
possible. The Hibernate Query Language, designed
as a "minimal" object-oriented extension to SQL,
provides an elegant bridge between the object and
relational worlds. Hibernate is now the most
popular ORM solution for Java.

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

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.7-alt1_6jpp7
- new version

