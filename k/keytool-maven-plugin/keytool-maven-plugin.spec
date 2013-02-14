# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global group_id  org.codehaus.mojo

Name:             keytool-maven-plugin
Version:          1.0
Release:          alt2_7jpp7
Summary:          A plugin that wraps the keytool program and allows to manipulate keystores
License:          MIT and ASL 2.0
Group:            Development/Java
# http://mojo.codehaus.org/keytool-maven-plugin/
URL:              http://mojo.codehaus.org/%{name}/
# svn export http://svn.codehaus.org/mojo/tags/keytool-maven-plugin-1.0/ keytool-maven-plugin-1.0
# tar caf keytool-maven-plugin-1.0.tar.xz keytool-maven-plugin-1.0
Source0:          %{name}-%{version}.tar.xz
Source1:          LICENSE-ASL

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven

Requires:         jpackage-utils
Requires:         maven
Requires:         plexus-utils
Requires:         apache-commons-lang

Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
A plugin that wraps the keytool program bundled with Sun's Java SDK.
It provides the capability to manipulate keys and keystores
with the goals "keytool:genkey" and "keytool:clean".

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q

# fixing licenses
mv LICENSE.txt LICENSE-MIT
cp %{SOURCE1} LICENSE-ASL

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE-MIT LICENSE-ASL
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE-MIT LICENSE-ASL
%doc %{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- complete build

