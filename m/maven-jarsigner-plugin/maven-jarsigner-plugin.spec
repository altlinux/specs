# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global group_id  org.apache.maven.plugins

Name:             maven-jarsigner-plugin
Version:          1.2
Release:          alt1_3jpp7
Summary:          Signs or verifies a project artifact and attachments using jarsigner
License:          ASL 2.0
Group:            Development/Java
URL:              http://maven.apache.org/plugins/%{name}/
# http://search.maven.org/remotecontent?filepath=org/apache/maven/plugins/maven-jarsigner-plugin/1.2/maven-jarsigner-plugin-1.2-source-release.zip
Source0:          http://search.maven.org/remotecontent?filepath=org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven

Requires:         jpackage-utils
Requires:         maven
Requires:         plexus-utils

Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
This plugin provides the capability to sign or verify
a project artifact and attachments using jarsigner.

If you need to sign a project artifact and all attached artifacts,
just configure the sign goal appropriately in your pom.xml
for the signing to occur automatically during the package phase.

If you need to verify the signatures of a project artifact
and all attached artifacts, just configure the verify goal
appropriately in your pom.xml for the verification to occur
automatically during the verify phase.


%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap %{group_id} %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE NOTICE DEPENDENCIES
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%doc %{_javadocdir}/%{name}

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- complete build

