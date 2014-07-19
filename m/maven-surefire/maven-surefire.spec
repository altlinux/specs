# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bootstrap 0

Name:           maven-surefire
Version:        2.12.4
Release:        alt1_2jpp7
Epoch:          0
Summary:        Test framework project
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/surefire/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/surefire/surefire/%{version}/surefire-%{version}-source-release.zip
Source1:        %{name}-jpp-depmap.xml

# provide compatibility for maven3
Patch0:         0003-Fix-maven3-compatibility.patch
Patch1:         0004-Surefire-2.12-bootstrap.patch

BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  apache-commons-lang3
BuildRequires:  classworlds
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  junit >= 3.8.2
BuildRequires:  plexus-utils
BuildRequires:  junit4
BuildRequires:  testng

BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-help-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-shared-verifier
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire-plugin >= 0:2.12-1
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-toolchain
BuildRequires:  maven-project
BuildRequires:  maven-shared-common-artifact-filters
BuildRequires:  modello
BuildRequires:  plexus-containers-component-api >= 1.0-0.a34
BuildRequires:  tomcat6-servlet-2.5-api
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  bsf
BuildRequires:  javacc-maven-plugin

Requires:       apache-commons-lang3
Requires:       classworlds
Requires:       maven
Requires:       maven-toolchain
Requires:       maven-project
Requires:       maven-shared-common-artifact-filters
Requires:       junit
Requires:       plexus-utils

Obsoletes:      maven-surefire-booter <= 0:1.5.3
Provides:       maven-surefire-booter = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Surefire is a test framework project.

%package plugin
Summary:                Surefire plugin for maven
Group:                  Development/Java
Requires:               %{name} = %{epoch}:%{version}-%{release}
Requires:               %{name}-provider-junit = %{epoch}:%{version}-%{release}
Obsoletes:              maven2-plugin-surefire <= 0:2.0.4
Provides:               maven2-plugin-surefire = %{epoch}:%{version}-%{release}
Obsoletes:              maven-surefire-maven-plugin < 0:2.6
Provides:               maven-surefire-maven-plugin = %{epoch}:%{version}-%{release}

%description plugin
Maven surefire plugin for running tests via the surefire framework.

%package report-plugin
Summary:                Surefire reports plugin for maven
Group:                  Development/Java
Requires:               %{name} = %{epoch}:%{version}-%{release}
Obsoletes:              maven2-plugin-surefire-report <= 0:2.0.4
Provides:               maven2-plugin-surefire-report = %{epoch}:%{version}-%{release}
Obsoletes:              maven-surefire-report-maven-plugin < 0:2.6
Provides:               maven-surefire-report-maven-plugin = %{epoch}:%{version}-%{release}

%description report-plugin
Plugin for generating reports from surefire test runs.

%package provider-junit
Summary:                JUnit3 provider for Maven Surefire
Group:                  Development/Java
Requires:               junit
Requires:               %{name} = %{epoch}:%{version}-%{release}
Obsoletes:              maven2-plugin-surefire-report <= 0:2.0.4O
#Obsoletes:              maven-surefire-junit = 2.3.1
Provides:               maven2-plugin-surefire-report = %{epoch}:%{version}-%{release}
#Provides:              maven-surefire-junit = 2.3.1

%description provider-junit
JUnit3 provider for Maven Surefire.

%package provider-junit4
Summary:                JUnit4 provider for Maven Surefire
Group:                  Development/Java
Requires:               %{name} = %{epoch}:%{version}-%{release}
Requires:               %{name}-provider-junit = %{epoch}:%{version}-%{release}
Requires:               junit4

%description provider-junit4
JUnit4 provider for Maven Surefire.

%package provider-testng
Summary:                TestNG provider for Maven Surefire
Group:                  Development/Java
Requires:               %{name} = %{epoch}:%{version}-%{release}
Requires:               testng

%description provider-testng
TestNG provider for Maven Surefire.

%package -n maven-failsafe-plugin
Summary:                Maven plugin for running integration tests
Group:                  Development/Java
Requires:               %{name} = %{epoch}:%{version}-%{release}

%description -n maven-failsafe-plugin
The Failsafe Plugin is designed to run integration tests while the
Surefire Plugins is designed to run unit. The name (failsafe) was
chosen both because it is a synonym of surefire and because it implies
that when it fails, it does so in a safe way.

If you use the Surefire Plugin for running tests, then when you have a
test failure, the build will stop at the integration-test phase and
your integration test environment will not have been torn down
correctly.

The Failsafe Plugin is used during the integration-test and verify
phases of the build lifecycle to execute the integration tests of an
application. The Failsafe Plugin will not fail the build during the
integration-test phase thus enabling the post-integration-test phase
to execute.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n surefire-%{version}

%patch0 -p1 -b .sav

%if %{bootstrap}
%patch1 -p1 -b .sav
%endif

sed -i 's:${shadedVersion}:%{version}:' surefire-integration-tests/pom.xml


%build
# tests turned off because they need jmock
mvn-rpmbuild -e \
        -Dmaven.test.skip=true \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven-surefire
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}


install -pm 644 maven-surefire-plugin/target/maven-surefire-plugin-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/maven-plugin.jar
install -pm 644 maven-surefire-plugin/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-maven-plugin.pom
%add_maven_depmap JPP.maven-surefire-maven-plugin.pom maven-surefire/maven-plugin.jar -f maven-plugin


%if %{bootstrap}
  install -pm 644 maven-surefire-common/target/maven-surefire-common-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/common.jar
%else
  install -pm 644 maven-surefire-common/target/original-maven-surefire-common-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/common.jar
%endif
install -pm 644 maven-surefire-common/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-common.pom
%add_maven_depmap JPP.maven-surefire-common.pom maven-surefire/common.jar


install -pm 644 maven-surefire-report-plugin/target/maven-surefire-report-plugin-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/report-maven-plugin.jar
install -pm 644 maven-surefire-report-plugin/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-report-maven-plugin.pom
%add_maven_depmap JPP.maven-surefire-report-maven-plugin.pom maven-surefire/report-maven-plugin.jar -f report-plugin


%if %{bootstrap}
  install -pm 644 surefire-api/target/surefire-api-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/api.jar
%else
  install -pm 644 surefire-api/target/original-surefire-api-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/api.jar
%endif
install -pm 644 surefire-api/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-api.pom
%add_maven_depmap JPP.maven-surefire-api.pom maven-surefire/api.jar


%if %{bootstrap}
install -pm 644 surefire-booter/target/surefire-booter-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/booter.jar
%else
install -pm 644 surefire-booter/target/original-surefire-booter-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/booter.jar
%endif
install -pm 644 surefire-booter/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-booter.pom
%add_maven_depmap JPP.maven-surefire-booter.pom maven-surefire/booter.jar

install -pm 644 surefire-providers/common-junit3/target/common-junit3-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/common-junit.jar
install -pm 644 surefire-providers/common-junit3/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-common-junit.pom
%add_maven_depmap JPP.maven-surefire-common-junit.pom maven-surefire/common-junit.jar -f junit


%if %{bootstrap}
  install -pm 644 surefire-providers/surefire-junit3/target/surefire-junit3-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/junit.jar
%else
  install -pm 644 surefire-providers/surefire-junit3/target/original-surefire-junit3-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/junit.jar
%endif
install -pm 644 surefire-providers/surefire-junit3/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-junit.pom
%add_maven_depmap JPP.maven-surefire-junit.pom maven-surefire/junit.jar -a "org.apache.maven.surefire:surefire-junit" -f junit


install -pm 644 surefire-providers/common-junit4/target/common-junit4-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/common-junit4.jar
install -pm 644 surefire-providers/common-junit4/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-common-junit4.pom
%add_maven_depmap JPP.maven-surefire-common-junit4.pom maven-surefire/common-junit4.jar -f junit4


%if %{bootstrap}
  install -pm 644 surefire-providers/surefire-junit4/target/surefire-junit4-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/junit4.jar
%else
  install -pm 644 surefire-providers/surefire-junit4/target/original-surefire-junit4-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/junit4.jar
%endif
install -pm 644 surefire-providers/surefire-junit4/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-junit4.pom
%add_maven_depmap JPP.maven-surefire-junit4.pom maven-surefire/junit4.jar -f junit4


%if %{bootstrap}
  install -pm 644 surefire-providers/surefire-junit47/target/surefire-junit47-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/junit47.jar
%else
  install -pm 644 surefire-providers/surefire-junit47/target/original-surefire-junit47-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/junit47.jar
%endif
install -pm 644 surefire-providers/surefire-junit47/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-junit47.pom
%add_maven_depmap JPP.maven-surefire-junit47.pom maven-surefire/junit47.jar -f junit4


%if %{bootstrap}
  install -pm 644 surefire-providers/common-junit48/target/common-junit48-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/common-junit48.jar
%else
  install -pm 644 surefire-providers/common-junit48/target/original-common-junit48-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/common-junit48.jar
%endif
install -pm 644 surefire-providers/common-junit48/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-common-junit48.pom
%add_maven_depmap JPP.maven-surefire-common-junit48.pom maven-surefire/common-junit48.jar -f junit4


install -pm 644 surefire-providers/surefire-testng/target/surefire-testng-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/testng.jar
install -pm 644 surefire-providers/surefire-testng/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-testng.pom
%add_maven_depmap JPP.maven-surefire-testng.pom maven-surefire/testng.jar -f testng


%if %{bootstrap}
  install -pm 644 surefire-providers/surefire-testng-utils/target/surefire-testng-utils-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/testng-utils.jar
%else
  install -pm 644 surefire-providers/surefire-testng-utils/target/original-surefire-testng-utils-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/testng-utils.jar
%endif
install -pm 644 surefire-providers/surefire-testng-utils/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-testng-utils.pom
%add_maven_depmap JPP.maven-surefire-testng-utils.pom maven-surefire/testng-utils.jar -f testng


install -pm 644 surefire-providers/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-providers.pom
%add_maven_depmap JPP.maven-surefire-providers.pom


install -pm 644 maven-failsafe-plugin/target/maven-failsafe-plugin*.jar $RPM_BUILD_ROOT%{_javadir}/maven-failsafe-plugin.jar
install -pm 644 maven-failsafe-plugin/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-maven-failsafe-plugin.pom
%add_maven_depmap JPP-maven-failsafe-plugin.pom maven-failsafe-plugin.jar -f failsafe-plugin


install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-main.pom
%add_maven_depmap JPP.maven-surefire-main.pom


install -pm 644 surefire-grouper/target/surefire-grouper-*.jar $RPM_BUILD_ROOT%{_javadir}/maven-surefire/grouper.jar
install -pm 644 surefire-grouper/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-surefire-grouper.pom
%add_maven_depmap JPP.maven-surefire-grouper.pom maven-surefire/grouper.jar


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Create compatibility links
ln -s %{_javadir}/maven-surefire/api.jar \
      $RPM_BUILD_ROOT%{_javadir}/maven-surefire/surefire.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/plugins
ln -s %{_javadir}/maven-surefire/maven-plugin.jar \
      $RPM_BUILD_ROOT%{_datadir}/maven2/plugins/surefire-plugin.jar

ln -s %{_javadir}/maven-surefire/report-maven-plugin.jar \
      $RPM_BUILD_ROOT%{_datadir}/maven2/plugins/surefire-report-plugin.jar


%files
%doc LICENSE NOTICE
%dir %{_javadir}/maven-surefire
%{_javadir}/maven-surefire/api.jar
%{_javadir}/maven-surefire/booter.jar
%{_javadir}/maven-surefire/surefire.jar
%{_javadir}/maven-surefire/common.jar
%{_javadir}/maven-surefire/grouper.jar
%{_mavenpomdir}/JPP.%{name}-api.pom
%{_mavenpomdir}/JPP.%{name}-booter.pom
%{_mavenpomdir}/JPP.%{name}-common.pom
%{_mavenpomdir}/JPP.%{name}-main.pom
%{_mavenpomdir}/JPP.%{name}-providers.pom
%{_mavenpomdir}/JPP.%{name}-grouper.pom
%{_mavendepmapfragdir}/%{name}

%files plugin
%{_javadir}/maven-surefire/maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-maven-plugin.pom
%{_mavendepmapfragdir}/%{name}-maven-plugin
%dir %{_datadir}/maven2/plugins
%{_datadir}/maven2/plugins/surefire-plugin.jar

%files report-plugin
%{_javadir}/maven-surefire/report-maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-report-maven-plugin.pom
%{_mavendepmapfragdir}/%{name}-report-plugin
%dir %{_datadir}/maven2/plugins
%{_datadir}/maven2/plugins/surefire-report-plugin.jar

%files provider-junit
%{_mavendepmapfragdir}/%{name}-junit
%{_mavenpomdir}/JPP.%{name}-junit.pom
%{_mavenpomdir}/JPP.%{name}-common-junit.pom
%{_javadir}/maven-surefire/junit.jar
%{_javadir}/maven-surefire/common-junit.jar

%files provider-junit4
%{_mavendepmapfragdir}/%{name}-junit4
%{_mavenpomdir}/JPP.%{name}-junit4.pom
%{_mavenpomdir}/JPP.%{name}-junit47.pom
%{_mavenpomdir}/JPP.%{name}-common-junit4.pom
%{_mavenpomdir}/JPP.%{name}-common-junit48.pom
%{_javadir}/maven-surefire/junit4.jar
%{_javadir}/maven-surefire/junit47.jar
%{_javadir}/maven-surefire/common-junit4.jar
%{_javadir}/maven-surefire/common-junit48.jar

%files provider-testng
%{_mavendepmapfragdir}/%{name}-testng
%{_mavenpomdir}/JPP.%{name}-testng.pom
%{_mavenpomdir}/JPP.%{name}-testng-utils.pom
%{_javadir}/maven-surefire/testng.jar
%{_javadir}/maven-surefire/testng-utils.jar

%files -n maven-failsafe-plugin
%{_mavendepmapfragdir}/%{name}-failsafe-plugin
%{_mavenpomdir}/JPP-maven-failsafe-plugin.pom
%{_javadir}/maven-failsafe-plugin.jar

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/*

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt1_2jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt2_5jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt1_5jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

