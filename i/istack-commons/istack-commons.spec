BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           istack-commons
Version:        2.6.1
Release:        alt3_5jpp7
Summary:        Common code for some Glassfish projects
Group:          Development/Java
License:        CDDL and GPLv2
URL:            http://istack-commons.java.net

# svn export https://svn.java.net/svn/istack-commons~svn/tags/istack-commons-2.6.1/ istack-commons-2.6.1
# find istack-commons-2.6.1/ -name '*.class' -delete
# find istack-commons-2.6.1/ -name '*.jar' -delete
# tar -zcvf istack-commons-2.6.1.tar.gz istack-commons-2.6.1
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-activation.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  bea-stax-api
BuildRequires:  codemodel >= 2.6-4
BuildRequires:  dom4j
BuildRequires:  jpackage-utils
BuildRequires:  jvnet-parent
BuildRequires:  junit
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-shared-file-management
BuildRequires:  maven-surefire-plugin
BuildRequires:  plexus-archiver
BuildRequires:  plexus-io

Requires:       jpackage-utils
Requires:       jvnet-parent
Source44: import.info


%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.


%package -n maven-istack-commons-plugin
Summary:        istack-commons Maven Mojo
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       codemodel >= 2.6-4
Requires:       maven-shared-file-management
Requires:       plexus-archiver
Requires:       plexus-io


%description -n maven-istack-commons-plugin
This package contains the istack-commons Maven Mojo.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
rm -rf test/lib/*.zip


%build

# The "-Pdefault-tools.jar" option is needed in order to make sure that the
# "tools.jar" file is added to the dependencies, otherwise it will not be added
# if the "java.vendor" property is "Oracle Corporation", which happens to be
# the value in JDK7:
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  -Pdefault-tools.jar \
  install \
  javadoc:aggregate


%install

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# JAR
cp -p runtime/target/istack-commons-runtime-%{version}.jar %{buildroot}%{_javadir}/%{name}-runtime.jar
cp -p tools/target/istack-commons-tools-%{version}.jar %{buildroot}%{_javadir}/%{name}-tools.jar
cp -p test/target/istack-commons-test-%{version}.jar %{buildroot}%{_javadir}/%{name}-test.jar
cp -p buildtools/target/%{name}-buildtools-%{version}.jar %{buildroot}%{_javadir}/%{name}-buildtools.jar
cp -p maven-plugin/target/maven-%{name}-plugin-%{version}.jar %{buildroot}%{_javadir}/maven-%{name}-plugin.jar

# JAVADOC
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# POM
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
cp -p runtime/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-runtime.pom
cp -p tools/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-tools.pom
cp -p test/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-test.pom
cp -p buildtools/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-buildtools.pom
cp -p maven-plugin/pom.xml %{buildroot}%{_mavenpomdir}/JPP-maven-%{name}-plugin.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap JPP-%{name}-runtime.pom %{name}-runtime.jar
%add_maven_depmap JPP-%{name}-tools.pom %{name}-tools.jar
%add_maven_depmap JPP-%{name}-test.pom %{name}-test.jar
%add_maven_depmap JPP-%{name}-buildtools.pom %{name}-buildtools.jar
%add_maven_depmap JPP-maven-%{name}-plugin.pom maven-%{name}-plugin.jar -f maven-plugin

%files
%{_mavenpomdir}/JPP-%{name}-runtime.pom
%{_mavenpomdir}/JPP-%{name}-test.pom
%{_mavenpomdir}/JPP-%{name}-tools.pom
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-buildtools.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}-buildtools.jar
%{_javadir}/%{name}-runtime.jar
%{_javadir}/%{name}-test.jar
%{_javadir}/%{name}-tools.jar
%doc Licence.txt

%files -n maven-istack-commons-plugin
%{_javadir}/maven-%{name}-plugin.jar
%{_mavenpomdir}/JPP-maven-%{name}-plugin.pom
%{_mavendepmapfragdir}/%{name}-maven-plugin
%doc Licence.txt

%files javadoc
%{_javadocdir}/%{name}
%doc Licence.txt


%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt3_5jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_5jpp7
- new version

