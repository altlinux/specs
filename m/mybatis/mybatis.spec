Name: mybatis
Version: 3.2.8
Summary: SQL Mapping Framework for Java
License: ASL 2.0
Url: http://www.mybatis.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.mybatis:mybatis) = 3.2.8
Provides: mvn(org.mybatis:mybatis:pom:) = 3.2.8
Provides: mybatis = 3.2.8-3.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: mybatis-3.2.8-3.fc23.cpio

%description
The MyBatis data mapper framework makes it easier
to use a relational database with object-oriented
applications. MyBatis couples objects with stored
procedures or SQL statements using a XML descriptor
or annotations. Simplicity is the biggest advantage
of the MyBatis data mapper over object relational
mapping tools.

To use the MyBatis data mapper, you rely on your
own objects, XML, and SQL. There is little to
learn that you don't already know. With the
MyBatis data mapper, you have the full power of
both SQL and stored procedures at your fingertips.

The MyBatis project is developed and maintained by
a team that includes the original creators of the
"iBATIS" data mapper. The Apache project was retired
and continued here.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

