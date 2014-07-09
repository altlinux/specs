Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             paranamer
Version:          2.4.1
Release:          alt1_5jpp7
Summary:          Library for accessing non-private method parameter names at run-time
Group:            Development/Java
License:          BSD
URL:              http://paranamer.codehaus.org

# git clone git://git.codehaus.org/paranamer-git.git paranamer-2.4.1
# cd paranamer-2.4.1 && git checkout paranamer-2.4.1
# find . -name '*.jar' -delete
# rm -rf .git
# cd .. && tar cafJ paranamer-2.4.1-CLEAN.tar.xz paranamer-2.4.1
Source0:          paranamer-%{version}-CLEAN.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jmock

Requires:         jpackage-utils
Source44: import.info

%description
It is a library that allows the parameter names of non-private methods
and constructors to be accessed at runtime.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

chmod -x LICENSE.txt

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"
# Disable distribution module
%pom_disable_module paranamer-distribution
# Specify version in the plugin
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'paranamer-maven-plugin']" "<version>%{version}</version>" paranamer/pom.xml

%build
# Test failures
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 paranamer-generator/target/paranamer-generator-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-generator.jar
install -pm 644 paranamer-maven-plugin/target/paranamer-maven-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-maven-plugin.jar
install -pm 644 paranamer-integration-tests/it-011/target/paranamer-it-011-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-it-011.jar
install -pm 644 paranamer-ant/target/paranamer-ant-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-ant.jar
install -pm 644 paranamer/target/paranamer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar

# POM
install -pm 644 paranamer-generator/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-generator.pom
install -pm 644 paranamer-maven-plugin/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-maven-plugin.pom
install -pm 644 paranamer-integration-tests/it-011/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-it-011.pom
install -pm 644 paranamer-integration-tests/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-it.pom
install -pm 644 paranamer-ant/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-ant.pom
install -pm 644 paranamer/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}-generator.pom %{name}/%{name}-generator.jar
%add_maven_depmap JPP.%{name}-%{name}-maven-plugin.pom %{name}/%{name}-maven-plugin.jar
%add_maven_depmap JPP.%{name}-%{name}-it-011.pom %{name}/%{name}-it-011.jar
%add_maven_depmap JPP.%{name}-%{name}-ant.pom %{name}/%{name}-ant.jar
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

%add_maven_depmap JPP.%{name}-%{name}-it.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_5jpp7
- converted from JPackage by jppimport script

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_1jpp6
- use jmock1 (TODO: try jmock2)

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_1jpp6
- fixed build

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_1jpp6
- fixed build (added BR: sun-annotation-1.0-api)

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp6
- new version

