BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name shrinkwrap-descriptors
%define version 2.0.0
%global namedreltag -alpha-2
%global namedversion %{version}%{?namedreltag}


Name:          shrinkwrap-descriptors
Version:       2.0.0
Release:       alt3_0.2.alpha2jpp7
Summary:       ShrinkWrap subproject for creating Archive Descriptors
Group:         Development/Java
License:       ASL 2.0
Url:           http://www.jboss.org/shrinkwrap/

# git clone https://github.com/shrinkwrap/descriptors.git shrinkwrap-descriptors-2.0.0-alpha-2
# cd shrinkwrap-descriptors-2.0.0-alpha-2 && git archive --format=tar --prefix=shrinkwrap-descriptors-2.0.0-alpha-2/ 2.0.0-alpha-2 | xz > ../shrinkwrap-descriptors-2.0.0-alpha-2.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

# saxon-dom is built in saxon in Fedora
Patch0:        %{name}-saxon-dom.patch

BuildRequires: jboss-parent
BuildRequires: jpackage-utils

BuildRequires: apiviz
BuildRequires: junit4

BuildRequires: maven
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

BuildRequires: apache-commons-lang3
BuildRequires: saxon
BuildRequires: codemodel
BuildRequires: glassfish-dtd-parser
BuildRequires: xmlunit

Requires:      junit4
Requires:      apache-commons-lang3
Requires:      saxon
Requires:      codemodel
Requires:      glassfish-dtd-parser
Requires:      xmlunit

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
ShrinkWrap subproject for creating Archive Descriptors

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

# Do not build test module, which is only for tests
sed -i "s|<module>test</module>|<!--module>test</module-->|" pom.xml

%build

export JAVA5_HOME=%{_jvmdir}/java
mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}

for m in api-base \
         api-javaee \
         api-jboss \
         gen \
         impl-base \
         impl-javaee \
         impl-jboss \
         impl-misc \
         metadata-parser \
         metadata-parser-test \
         spi \
         test-util \
       ; do

   # JAR
   install -pm 644 ${m}/target/%{name}-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
   # POM
   install -pm 644 ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
   # DEPMAP
   %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar

done

# POMs and DEPMAP
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom
install -pm 644 bom/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-bom.pom
%add_maven_depmap JPP.%{name}-%{name}-bom.pom
install -pm 644 depchain/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-depchain.pom
%add_maven_depmap JPP.%{name}-%{name}-depchain.pom

# APIDOCS
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.2.alpha2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_0.2.alpha2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.2.alpha2jpp7
- new version

