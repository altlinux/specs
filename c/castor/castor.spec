# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:        An open source data binding framework for Java
Name:           castor
Version:        1.3.2
Release:        alt1_6jpp7
Epoch:          0
Group:          Development/Java
License:        BSD and MPLv1.1 and W3C
URL:            http://castor.codehaus.org
Source0:        http://dist.codehaus.org/castor/1.3.2/castor-1.3.2-src.tgz
Patch0:         disable-modules.patch
BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  codehaus-parent
BuildRequires:  maven-enforcer-plugin
Requires:       apache-commons-logging
Requires:       apache-commons-lang
Obsoletes:      castor-demo < 0:1.3.2
Obsoletes:      castor-test < 0:1.3.2
Obsoletes:      castor-xml < 0:1.3.2
Obsoletes:      castor-doc < 0:1.3.2
Source44: import.info

%description
Castor is an open source data binding framework for Java. It's basically
the shortest path between Java objects, XML documents and SQL tables.
Castor provides Java to XML binding, Java to SQL persistence, and more.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;
%patch0 -b .sav

%pom_xpath_remove "pom:build/pom:extensions"

sed -i 's/Class-Path: xerces.jar jdbc-se2.0.jar jndi.jar jta1.0.1.jar//' src/etc/MANIFEST.MF

%build
mvn-rpmbuild -Dgpg.skip=true -Dmaven.test.skip=true install javadoc:aggregate

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 core/target/%{name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_6jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_3jpp7
- new version

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt3_4jpp5
- fixed build

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt2_4jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt1_4jpp5
- new version

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

