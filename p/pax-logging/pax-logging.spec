# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          pax-logging
Version:       1.6.9
Release:       alt1_5jpp7
Summary:       OSGi Logging framework implementation
Group:         Development/Java
License:       ASL 2.0 and BSD and MIT
URL:           http://team.ops4j.org/wiki//display/paxlogging/Pax+Logging
# git clone git://github.com/ops4j/org.ops4j.pax.logging.git pax-logging-1.6.9
# cd pax-logging-1.6.9 && git archive --format=tar --prefix=pax-logging-1.6.9/ logging-1.6.9  | xz > pax-logging-1.6.9-src-git.tar.xz
Source0:       %{name}-%{version}-src-git.tar.xz

BuildRequires: jpackage-utils

BuildRequires: avalon-framework
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: log4j

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

Requires:      avalon-framework
Requires:      felix-osgi-compendium
Requires:      felix-osgi-core
Requires:      log4j

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The OSGi Logging framework implementation. Supports SLF4J,
LOG4J,Jakarta Commons Logging etc.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_remove_parent
%pom_disable_module pax-logging-it
%pom_disable_module pax-logging-samples
# test deps*
%pom_remove_dep junit:junit
%pom_remove_dep org.easymock:easymock
# unavailable
%pom_remove_dep jmock:jmock
%pom_remove_dep org.ops4j.pax.exam:pax-exam
%pom_remove_dep org.ops4j.pax.exam:pax-exam-container-default
%pom_remove_dep org.ops4j.pax.exam:pax-exam-junit
%pom_remove_dep org.ops4j.pax.runner:pax-runner-no-jcl
# sample deps
%pom_remove_dep org.mortbay.jetty:jetty

%pom_remove_plugin org.ops4j:maven-pax-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin

sed -i "s|<source>1.4</source>|<source>1.5</source>|" pom.xml
sed -i "s|<target>1.4</target>|<target>1.5</target>|" pom.xml
# prevent log4j re-bundle 
sed -i "s|<_include>-osgi.bnd</_include>|<!--_include>-osgi.bnd</_include-->|" pom.xml

%pom_remove_dep jmock:jmock pax-logging-api
%pom_remove_dep junit:junit pax-logging-api
%pom_remove_plugin org.ops4j:maven-pax-plugin pax-logging-api
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin pax-logging-api

%pom_remove_dep jmock:jmock pax-logging-service
%pom_remove_plugin org.ops4j:maven-pax-plugin pax-logging-service
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin pax-logging-service
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin pax-logging-service

%build

# test skip unavailable test deps*
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.skip=true install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml  %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

mkdir -p %{buildroot}%{_javadir}
for m in %{name}-api \
         %{name}-service; do
    install -m 644 ${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/${m}.jar
    install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-${m}.pom
%add_maven_depmap JPP-${m}.pom ${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

cp -rp pax-logging-api/NOTICE.txt .

%files
%{_javadir}/%{name}-*.jar
%{_mavenpomdir}/JPP-%{name}*.pom
%{_mavendepmapfragdir}/%{name}
%doc CONTRIBUTORS.txt LICENSE.txt NOTICE.txt RELEASE-NOTES.html

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_5jpp7
- new release

* Sat Mar 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_3jpp7
- fc update

