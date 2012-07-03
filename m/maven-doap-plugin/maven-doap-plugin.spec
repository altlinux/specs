BuildRequires: modello icu4j
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-doap-plugin
Version:        1.1
Release:        alt1_2jpp7
Summary:        Plugins which generate a DOAP file from information in a POM

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-doap-plugin/
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-doap-plugin-1.1/
# tar caf maven-doap-plugin-1.1.tar.xz maven-doap-plugin-1.1/
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-fixed-dependencies.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-artifact-manager
BuildRequires: jpackage-utils
BuildRequires: jena
Requires: maven
Requires: jpackage-utils
Requires: jena

Obsoletes: maven2-plugin-doap <= 0:2.0.8
Provides: maven2-plugin-doap = 1:%{version}-%{release}
Source44: import.info

%description
Maven 2 DOAP Plugin is used to generate compliant Description 
of a Project (DOAP) file from a POM. The main goal is to 
be able to provide DOAP files for Semantic Web systems that 
use them as primary input but that would also alleviate 
the burden of maintaining two sets of metadata.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -b .sav -p1

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:aggregate -X

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
# rpmlint complains about a missing shebang in the javascript.sh file
rm target/site/apidocs/javadoc.sh
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- fc version

