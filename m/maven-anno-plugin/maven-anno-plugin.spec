# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: maven-anno-plugin
Version: 1.4.1
Release: alt3_6jpp7
Summary: Maven Annotated Mojo
Group: Development/Java
License: ASL 2.0
Url: http://wiki.jfrog.org/confluence/display/OSS/Maven+Anno+Mojo

# git clone git://github.com/JFrogDev/maven-anno-mojo.git
# cd maven-anno-mojo
# git archive --prefix=maven-anno-plugin-1.4.1/ maven-plugin-anno-parent-1.4.1 | xz > maven-anno-plugin-1.4.1.tar.xz
Source0: %{name}-%{version}.tar.xz

Source1: http://www.apache.org/licenses/LICENSE-2.0.txt

# Fork tests, otherwise one of the tests of the tools module fails:
Patch0: %{name}-fork-tools-tests.patch

BuildRequires: jpackage-utils

BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-plugin-jxr
BuildRequires: maven-project-info-reports-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: maven-plugin-descriptor
BuildRequires: maven-local

Requires: jpackage-utils

BuildArch: noarch
Source44: import.info


%description
Maven maven-plugin-plugin extension that allows writing annotated Mojos using
JDK 1.5 annotations instead of doclet comments.


%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0 -p1
cp -p %{SOURCE1} .


%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 maven-plugin-anno/target/maven-plugin-anno-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 maven-plugin-tools-anno/target/maven-plugin-tools-anno-%{version}.jar %{buildroot}%{_javadir}/%{name}-tools.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 maven-plugin-anno/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 maven-plugin-tools-anno/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-tools.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-tools.pom %{name}-tools.jar

# Javadocs:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE-2.0.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README.rdoc


%files javadoc
%doc LICENSE-2.0.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt3_6jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_3jpp7
- new version

