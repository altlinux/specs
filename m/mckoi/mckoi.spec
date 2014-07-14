Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          mckoi
Version:       1.0.4
Release:       alt2_2jpp7
Summary:       Open Source Java SQL Database
Group:         Development/Java
License:       GPLv2
URL:           http://mckoi.com/database/
Source0:       http://mckoi.com/database/ver/%{name}%{version}.zip

Patch0:        %{name}-%{version}-jdk7.patch

Patch1:        %{name}-%{version}-fix_fsf-address.patch

BuildRequires: jpackage-utils

BuildRequires: javacc
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: zip

BuildRequires: gnu-regexp

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Mckoi SQL Database is an Open Source SQL Database System written in Java.
The Mckoi SQL Database project was started in 1998, and the goal was to
build a database management system in a traditional shared disk/shared memory
style architecture. Mckoi SQL Database includes some nice features such as
write-ahead-logging. Many of the design ideas implemented in this project
were carried through into MckoiDDB, the evolution of this project.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package demos
Group:         Development/Java
Summary:       Demonstrations and samples for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:      gnu-regexp

%description demos
This package contains sources archive demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}%{version}
find . -name '*.jar' -delete
find . -name '*.class' -delete
find . -name '*.bat' -delete
unzip -qq src.zip
%patch0 -p0
%patch1 -p1

# contrib require org.jboss.system
# fix generics support for java 7
sed -i "s|<source>1.3</source>|<source>1.5</source>|" pom.xml
sed -i "s|<target>1.3</target>|<target>1.5</target>|" pom.xml

sed -i "s|../mckoidb.jar:../gnu-regexp-1.0.8.jar|../target/MckoiSQLDB-%{version}.jar:%{_javadir}/gnu-regexp.jar|" test/*.sh
chmod 755 test/*.sh

sed -i 's/\r//' README.txt LICENSE.txt docs/LICENSE.txt

cd src/main/java/com/mckoi/database/sql
rm -rf TokenMgrError.java ParseException.java Token.java SimpleCharStream.java
javacc.sh SQL.jj

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/MckoiSQLDB-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
( cd %{buildroot}%{_javadir} && ln -s %{name}.jar MckoiSQLDB.jar )

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "mckoi:mckoi"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}
(
  cd src/main/java
  zip ../../../%{name}-src -r com
)
cp -pr %{name}-src.zip %{buildroot}%{_datadir}/%{name}
cp -pr contrib %{buildroot}%{_datadir}/%{name}
cp -pr demo %{buildroot}%{_datadir}/%{name}
cp -pr test %{buildroot}%{_datadir}/%{name}

%check
cd test
sh ./runLocalTest.sh

%files
%{_javadir}/%{name}.jar
%{_javadir}/MckoiSQLDB.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%files demos
%{_datadir}/%{name}
%doc docs/*

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_2jpp7
- new version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt2_1jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_1jpp5
- new version

