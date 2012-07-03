BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-one-plugin
Version:        1.2
Release:        alt1_8jpp7
Summary:        Plugin provides some integration tasks with Maven 1.x

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-one-plugin/
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-one-plugin-1.2/
# tar jcf maven-one-plugin-1.2.tar.bz2 maven-one-plugin-1.2/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-jpp-depmap.xml

Patch0:         %{name}-compat.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-model-converter
BuildRequires: jpackage-utils
Requires: ant
Requires: maven
Requires: maven-shared-model-converter
Requires: jpackage-utils

Obsoletes: maven2-plugin-one <= 0:2.0.8
Provides: maven2-plugin-one = 1:%{version}-%{release}
Source44: import.info

%description
This plugin provides some integration tasks with Maven 1.x:
* Helps you to switch your project from Maven 1 to Maven 2 by
converting your project.xml to a pom.xml
* Provides a packaging mechanism for Maven 1.x plugins,
building them using Maven 2.0
* Provides a hook for installation that will copy built artifacts
into a local or remote Maven 1.x repository, for concurrent development with
Maven 1.x projects

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

%build
mvn-rpmbuild \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar


# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8jpp7
- complete build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

