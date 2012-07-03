Epoch: 0
BuildRequires: maven2-plugin-site
BuildRequires: /proc
BuildRequires: jpackage-compat

%global with_maven 1

%global parent plexus
%global subname containers

# this needs to be exact version of maven-javadoc-plugin for
# integration tests
%global javadoc_plugin_version 2.8.1

Name:           %{parent}-%{subname}
Version:        1.5.5
Release:        alt1_5jpp7
Summary:        Containers for Plexus
License:        ASL 2.0 and Plexus
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export \
#  http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.5.5
# tar caf plexus-containers-1.5.5.tar.xz plexus-containers-1.5.5
Source0:        %{name}-%{version}.tar.xz
Source1:        plexus-container-default-build.xml
Source2:        plexus-component-annotations-build.xml
Source3:        plexus-containers-settings.xml

Patch0:         0001-Fix-test-oom.patch
Patch1:         0002-Fix-maven3-compatibility.patch
Patch2:         0003-Fix-OpenJDK7-compatibility.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin = %{javadoc_plugin_version}
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shared-invoker
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven2-common-poms >= 1.0
BuildRequires:  maven-release
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-utils
BuildRequires:  plexus-cli
BuildRequires:  xbean
BuildRequires:  guava

Requires:       plexus-classworlds >= 2.2.3
Requires:       plexus-utils
Requires:       xbean
Requires:       guava
Source44: import.info


%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package component-metadata
Summary:        Component metadata from %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       plexus-cli

%description component-metadata
%{summary}.

%package component-javadoc
Summary:        Javadoc component from %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description component-javadoc
%{summary}.


%package component-annotations
Summary:        Component API from %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description component-annotations
%{summary}.

%package container-default
Summary:        Default Container from %{name}
Group:          Development/Java
Requires:       %{name}-component-annotations = %{version}-%{release}
Provides:       plexus-containers-component-api = %{version}-%{release}

%description container-default
%{summary}.

%package javadoc
Summary:        API documentation for all plexus-containers packages
Group:          Development/Java
Requires:       jpackage-utils
Provides:       %{name}-component-annotations-javadoc = %{version}-%{release}
Obsoletes:      %{name}-component-annotations-javadoc < %{version}-%{release}
Provides:       %{name}-component-javadoc-javadoc = %{version}-%{release}
Obsoletes:      %{name}-component-javadoc-javadoc < %{version}-%{release}
Provides:       %{name}-component-metadata-javadoc = %{version}-%{release}
Obsoletes:      %{name}-component-metadata-javadoc < %{version}-%{release}
Provides:       %{name}-container-default-javadoc = %{version}-%{release}
Obsoletes:      %{name}-container-default-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n plexus-containers-%{version}

cp %{SOURCE1} plexus-container-default/build.xml
cp %{SOURCE2} plexus-component-annotations/build.xml

%patch0 -p1
%patch1 -p1
%patch2 -p1

# to prevent ant from failing
mkdir -p plexus-component-annotations/src/test/java

# integration tests fix
sed -i "s|<version>2.3</version>|<version> %{javadoc_plugin_version}</version>|" plexus-component-javadoc/src/it/basic/pom.xml

%build

mvn-rpmbuild -Dmaven.test.skip=true install

# for integration tests ran during javadoc:javadoc
for file in $MAVEN_REPO_LOCAL/org/apache/maven/plugins/maven-javadoc-plugin/%{javadoc_plugin_version}/*;do
    sha1sum $file | awk '{print $1}' > $ile.sha1
done

mvn-rpmbuild javadoc:aggregate

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
install -pm 644 plexus-component-annotations/target/*.jar \
 $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}-component-annotations.jar
install -pm 644 plexus-container-default/target/*.jar \
 $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}-container-default.jar
install -pm 644 plexus-component-metadata/target/*.jar \
 $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}-component-metadata.jar
install -pm 644 plexus-component-annotations/target/*.jar \
 $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}-component-javadoc.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom

install -pm 644 plexus-component-annotations/pom.xml \
         $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}-component-annotations.pom
install -pm 644 plexus-container-default/pom.xml \
         $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}-container-default.pom
install -pm 644 plexus-component-metadata/pom.xml \
         $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}-component-metadata.pom
install -pm 644 plexus-component-javadoc/pom.xml \
         $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}-component-javadoc.pom

%add_maven_depmap JPP.%{parent}-%{subname}.pom
%add_maven_depmap JPP.%{parent}-%{subname}-component-annotations.pom %{parent}/%{subname}-component-annotations.jar -f component-annotations
# component-api is now folded into container-default
%add_maven_depmap JPP.%{parent}-%{subname}-container-default.pom %{parent}/%{subname}-container-default.jar -a "org.codehaus.plexus:containers-component-api" -f container-default
%add_maven_depmap JPP.%{parent}-%{subname}-component-metadata.pom %{parent}/%{subname}-component-metadata.jar -f component-metadata
%add_maven_depmap JPP.%{parent}-%{subname}-component-javadoc.pom %{parent}/%{subname}-component-javadoc.jar -f component-javadoc

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom
%{_mavendepmapfragdir}/%{name}

%files component-annotations
%{_mavendepmapfragdir}/%{name}-component-annotations
%{_mavenpomdir}/JPP.%{parent}-%{subname}-component-annotations.pom
%{_javadir}/%{parent}/containers-component-annotations.jar

%files container-default
%{_mavendepmapfragdir}/%{name}-container-default
%{_mavenpomdir}/JPP.%{parent}-%{subname}-container-default.pom
%{_javadir}/%{parent}/containers-container-default.jar

%files component-metadata
%{_mavendepmapfragdir}/%{name}-component-metadata
%{_mavenpomdir}/JPP.%{parent}-%{subname}-component-metadata.pom
%{_javadir}/%{parent}/containers-component-metadata.jar

%files component-javadoc
%{_mavendepmapfragdir}/%{name}-component-javadoc
%{_mavenpomdir}/JPP.%{parent}-%{subname}-component-javadoc.pom
%{_javadir}/%{parent}/containers-component-javadoc.jar

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_5jpp7
- fc build

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_1jpp6
- new version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.1.a34.5jpp6
- fixed build

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.1.a34.5jpp6
- fixed build

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.1.a34.5jpp6
- fixed build

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.1.a34.5jpp6
- new release a34

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a32.3jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a30.1jpp5
- converted from JPackage by jppimport script

