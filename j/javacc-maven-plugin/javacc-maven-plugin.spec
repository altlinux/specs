BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           javacc-maven-plugin
Version:        2.6
Release:        alt1_7jpp6
Epoch:          0
Summary:        JavaCC Maven Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/javacc-maven-plugin/
#svn export http://svn.codehaus.org/mojo/tags/javacc-maven-plugin-2.6
#tar cjf javacc-maven-plugin-2.6.tar.bz2 javacc-maven-plugin-2.6
Source0:        javacc-maven-plugin-2.6.tar.bz2
Source1:        javacc-maven-plugin-jpp-depmap.xml
Patch0:         javacc-maven-plugin-pom.patch

BuildArch: noarch

BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2
BuildRequires: javacc >= 0:5.0
BuildRequires: plexus-utils
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-invoker
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: mojo-maven2-plugin-cobertura
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: mojo-parent
BuildRequires: plexus-containers-component-javadoc
BuildRequires: junit
Requires: javacc >= 0:5.0
Requires: plexus-utils
Requires: jpackage-utils
Requires: mojo-parent
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
Maven 2 Plugin for processing JavaCC grammar files.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -b .sav

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        package javadoc:javadoc

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}-%{version}.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap org.codehaus.mojo javacc-maven-plugin %{version} JPP javacc-maven-plugin

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
rm -rf target/site/api*

%files
%{_javadir}/%{name}*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%doc src/main/resources/NOTICE

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp6
- new version

