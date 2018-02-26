# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-dependency-plugin
Version:        2.4
Release:        alt1_1jpp7
Summary:        Plugin to manipulate, copy and unpack local and remote artifacts

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         0001-Add-setThreshold-stub.patch
# Added apache-commons-io dep
Patch1:         %{name}-commons-io.patch
# Added maven-core dep
Patch2:         %{name}-core.patch
# Removed a test because it was using a legacy class
Patch3:         %{name}-removed-test.patch
# Removed exception catching as it has already been done
# (not upstreamable)
Patch4:         %{name}-removed-exception-catching.patch

BuildArch:      noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: asm2
BuildRequires: apache-commons-io
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-dependency-analyzer
BuildRequires: maven-shared-dependency-tree
BuildRequires: maven-shared-common-artifact-filters
BuildRequires: maven-shared-file-management
BuildRequires: maven-project
BuildRequires: maven-artifact-manager
BuildRequires: maven-plugin-testing-tools

Requires: maven
Requires: jpackage-utils
Requires: maven-shared-common-artifact-filters
Requires: maven-shared-dependency-analyzer
Requires: maven-shared-file-management
Requires: maven-project
Requires: maven-artifact-manager

Obsoletes: maven2-plugin-dependency <= 0:2.0.8
Provides: maven2-plugin-dependency = 1:%{version}-%{release}
Source44: import.info

%description

The dependency plugin provides the capability to manipulate
artifacts. It can copy and/or unpack artifacts from local or remote
repositories to a specified location.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

sed -i \
    's:org.codehaus.classworlds.ClassRealm:org.codehaus.plexus.classworlds.realm.ClassRealm:' \
    src/test/java/org/apache/maven/plugin/dependency/its/AbstractDependencyPluginITCase.java


%build
mvn-rpmbuild -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

