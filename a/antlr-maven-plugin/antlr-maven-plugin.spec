# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:			antlr-maven-plugin
Version:		2.2
Release:		alt1_5jpp7
Summary:		Maven plugin that generates files based on grammar file(s)
License:		ASL 2.0
URL:			http://mojo.codehaus.org/antlr-maven-plugin/
Group:			Development/Java

Source0:		http://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Modern modello expects to see <models></models>, even if there is only one.
Patch0:			maven-antlr-plugin-2.2-modello-issue.patch
# siteRenderer.createSink doesn't exist anymore
Patch2:			maven-antlr-plugin-2.1-sinkfix.patch

BuildArch:		noarch

BuildRequires:		jpackage-utils
BuildRequires:		antlr
BuildRequires:		maven
BuildRequires:		maven-enforcer-plugin
BuildRequires:		maven-compiler-plugin
BuildRequires:		maven-install-plugin
BuildRequires:		maven-jar-plugin
BuildRequires:		maven-javadoc-plugin
BuildRequires:		maven-resources-plugin
BuildRequires:		maven-surefire-plugin
BuildRequires:		maven-antrun-plugin
BuildRequires:		maven-clean-plugin
BuildRequires:		maven-invoker-plugin
BuildRequires:		maven-plugin-plugin
BuildRequires:		maven-release-plugin
BuildRequires:		maven-site-plugin
BuildRequires:		maven-source-plugin
BuildRequires:		maven-plugin-bundle
BuildRequires:		maven-plugin-cobertura
BuildRequires:		apache-commons-exec
BuildRequires:		maven2-common-poms
BuildRequires:		modello

Requires:		antlr
Requires:       maven
Requires:		jpackage-utils
Requires:		apache-commons-exec

Provides:		maven2-plugin-antlr = %{version}-%{release}
Obsoletes:		maven2-plugin-antlr <= 2.0.8
Source44: import.info

%description
The Antlr Plugin has two goals:
- antlr:generate Generates file(s) to a target directory based on grammar
  file(s).
- antlr:html Generates Antlr report for grammar file(s).

%package javadoc
Summary:		Javadocs for %{name}
Group:			Development/Java
Requires:		jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .modello
%patch2 -p1 -b .sink

# remove all binary bits
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
mvn-rpmbuild -Dmaven.test.skip=true \
install javadoc:aggregate

%install
mkdir -p %{buildroot}%{_javadir}

cp -p target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/ %{buildroot}%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5jpp7
- new version

