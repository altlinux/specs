BuildRequires: maven-plugin-plugin
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-changes-plugin
Version:        2.7.1
Release:        alt3_2jpp7
Summary:        Plugin to support reporting of changes between releases

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}.depmap

Patch0:         0001-Fix-Maven-3-compatibility.patch
Patch1:         0002-Remove-geronimo-dependency-supplied-by-JVM.patch

BuildArch:      noarch

BuildRequires: apache-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: maven
BuildRequires: maven-project
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-reporting-api
BuildRequires: maven-shared-reporting-impl
BuildRequires: modello
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-containers-component-metadata
BuildRequires: plexus-mail-sender
BuildRequires: plexus-i18n
BuildRequires: plexus-interpolation
BuildRequires: plexus-utils
BuildRequires: plexus-velocity
BuildRequires: xmlrpc-client
BuildRequires: xmlrpc-common
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: velocity

Requires: jpackage-utils
Requires: apache-commons-collections
Requires: jakarta-commons-httpclient
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: maven
Requires: maven-project
Requires: maven-doxia-sitetools
Requires: maven-shared-filtering
Requires: maven-shared-reporting-api
Requires: maven-shared-reporting-impl
Requires: plexus-containers-container-default
Requires: plexus-i18n
Requires: plexus-interpolation
Requires: plexus-mail-sender
Requires: plexus-utils
Requires: plexus-velocity
Requires: xmlrpc-client
Requires: xmlrpc-common
Requires: xerces-j2
Requires: xml-commons-apis
Requires: velocity

Obsoletes: maven2-plugin-changes <= 0:2.0.8
Provides: maven2-plugin-changes = 1:%{version}-%{release}
Source44: import.info

%description
This plugin is used to inform your users of the changes that have
occurred between different releases of your project. The plugin can
extract these changes, either from a changes.xml file or from the JIRA
issue management system, and present them as a report. You also have
the option of creating a release announcement and even sending this
via email to your users.


%package javadoc
Group:    Development/Java
Summary:  Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild -e \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install

# jars
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt3_2jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt2_2jpp7
- fixed deps

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_2jpp7
- new version

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_2jpp7
- new version

