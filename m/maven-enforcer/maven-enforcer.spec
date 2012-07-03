Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-enforcer
Version:        1.0.1
Release:        alt3_4jpp7
Summary:        Maven Enforcer

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/enforcer
Source0:        http://repo1.maven.org/maven2/org/apache/maven/enforcer/enforcer/%{version}/enforcer-%{version}-source-release.zip

#748074 - maven-enforcer-plugin is not compatible with maven3
Patch0:         %{name}-requirePluginVersions-maven3-compatibility.patch
Patch1:         %{name}-migration-to-component-metadata.patch
Patch2:         %{name}-maven3-compat.patch

BuildArch: noarch


BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-doxia-tools
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: plexus-containers-component-javadoc
BuildRequires: plexus-containers-component-metadata
Requires:      maven
Requires:       jpackage-utils
Source44: import.info

%description
Enforcer is a build rule execution framework.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package api
Summary: Enforcer API
Group: Development/Java
Requires: maven-enforcer = %{version}-%{release}
Provides: maven-shared-enforcer-rule-api = %{version}-%{release}

%description api
This component provides the generic interfaces needed to
implement custom rules for the maven-enforcer-plugin.

%package rules
Summary: Enforcer Rules
Group: Development/Java
Requires: maven-enforcer = %{version}-%{release}
Requires: maven-enforcer-api

%description rules
This component contains the standard Enforcer Rules.

%package -n maven-enforcer-plugin
Summary: Enforcer Rules
Group: Development/Java
Requires: maven-enforcer = %{version}-%{release}
Requires: maven-enforcer-rules
Obsoletes: maven2-plugin-enforcer <= 0:2.0.8
Provides: maven2-plugin-enforcer = 1:%{version}-%{release}

%description -n maven-enforcer-plugin
This component contains the standard Enforcer Rules.


%prep
%setup -q -n enforcer-%{version}

%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
mvn-rpmbuild \
        -e \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 enforcer-api/target/enforcer-api-%{version}.jar \
               %{buildroot}%{_javadir}/%{name}/enforcer-api.jar
install -m 644 enforcer-rules/target/enforcer-rules-%{version}.jar \
               %{buildroot}%{_javadir}/%{name}/enforcer-rules.jar
install -m 644 maven-enforcer-plugin/target/maven-enforcer-plugin-%{version}.jar \
               %{buildroot}%{_javadir}/%{name}/plugin.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 enforcer-api/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-enforcer-api.pom
install -pm 644 enforcer-rules/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-enforcer-rules.pom
install -pm 644 maven-enforcer-plugin/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-plugin.pom

# fragments
%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap -f enforcer-api JPP.%{name}-enforcer-api.pom %{name}/enforcer-api.jar
%add_maven_depmap -f enforcer-rules JPP.%{name}-enforcer-rules.pom %{name}/enforcer-rules.jar
%add_maven_depmap -f plugin JPP.%{name}-plugin.pom %{name}/plugin.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%dir %{_javadir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files api
%{_javadir}/%{name}/enforcer-api.jar
%{_mavenpomdir}/JPP.%{name}-enforcer-api.pom
%{_mavendepmapfragdir}/%{name}-enforcer-api

%files rules
%{_javadir}/%{name}/enforcer-rules.jar
%{_mavenpomdir}/JPP.%{name}-enforcer-rules.pom
%{_mavendepmapfragdir}/%{name}-enforcer-rules

%files -n maven-enforcer-plugin
%{_javadir}/%{name}/plugin.jar
%{_mavenpomdir}/JPP.%{name}-plugin.pom
%{_mavendepmapfragdir}/%{name}-plugin

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_4jpp7
- added maven-shared-enforcer-rule-api provides

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_4jpp7
- fixed depmap fragment

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp7
- fc version

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_3jpp6
- new jpp relase

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.2.b1.1.2jpp6
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.2.b1.1.2jpp6
- new version

