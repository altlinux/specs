# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bootstrap 0

Name:           maven-javadoc-plugin
Version:        2.8.1
Release:        alt1_1jpp7
Summary:        Maven Javadoc Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-javadoc-plugin
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         remove-test-deps.patch
Patch1:         pom.patch
Patch2:         reduce-exceptions.patch
Patch3:         %{name}-compat.patch

BuildRequires:  maven
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  maven-shade-plugin
BuildRequires:  plexus-interactivity
BuildRequires:  maven-shared-invoker
BuildRequires:  maven-enforcer-plugin
BuildRequires:  modello
%if ! %{bootstrap}
BuildRequires:  maven-javadoc-plugin
%endif        

Requires:       jpackage-utils
Requires:       maven
Requires:       maven-shared-invoker

BuildArch: noarch

Obsoletes: maven2-plugin-javadoc <= 2.0.8
Provides:  maven2-plugin-javadoc = %{version}-%{release}
Source44: import.info

%description
The Maven Javadoc Plugin is a plugin that uses the javadoc tool for
generating javadocs for the specified project.
 
%if ! %{bootstrap}
%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.
%endif

%prep
%setup -q 
%patch0 -b .sav
# Update source for use with newer doxia
%patch1
%patch2
%patch3 -p1

sed -i -e "s|org.apache.maven.doxia.module.xhtml.decoration.render|org.apache.maven.doxia.sink.render|g" src/main/java/org/apache/maven/plugin/javadoc/JavadocReport.java

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install
%if ! %{bootstrap}
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        -Dproject.build.sourceEncoding=UTF-8 \
       javadoc:javadoc
%endif        

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%if ! %{bootstrap}
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*
%endif

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%if ! %{bootstrap}
%files javadoc
%{_javadocdir}/%{name}
%endif

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

