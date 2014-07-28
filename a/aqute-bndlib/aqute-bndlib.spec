Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:           aqute-bndlib
Version:        1.50.0
Release:        alt2_5jpp7
Summary:        BND Library
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.aQute.biz/Code/Bnd

Source0:        http://repo1.maven.org/maven2/biz/aQute/bndlib/1.50.0/bndlib-1.50.0.jar
Source1:        http://repo1.maven.org/maven2/biz/aQute/bndlib/1.50.0/bndlib-1.50.0.pom

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit4

Requires:       jpackage-utils
Source44: import.info

%description
The bnd tool helps you create and diagnose OSGi R4 bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package javadoc
BuildRequires:  jpackage-utils
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -c

# fixing incomplete source directory structure
mkdir -p src/main/java target/classes
mv -f OSGI-OPT/src/* src/main/java/

# removing bundled classess & junk
rm -rf OSGI-OPT
rm -rf META-INF
rm -rf src/main/java/aQute/bnd/test
find . -iname '*.class' -delete
find . -iname 'packageinfo' -delete

# recycling all data files
mv -f aQute target/classes
mv -f org target/classes

# for building with maven
cp %{SOURCE1} pom.xml

# CR+LF -> LF
sed -i "s|\r||g" LICENSE

%build
export LC_ALL=en_US.UTF-8
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -Dpm 644 target/bndlib-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -Dpm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.50.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.50.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.50.0-alt1_3jpp7
- new version

* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.363-alt2_1jpp6
- fixed build

* Mon Oct 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0.363-alt1_1jpp6
- new version

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt4_2jpp5
- fixed build

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt3_2jpp5
- rebuild with eclipse 3.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt2_2jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt1_2jpp5
- converted from JPackage by jppimport script

