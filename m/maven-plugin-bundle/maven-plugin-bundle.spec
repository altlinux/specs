BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-plugin-bundle
Version:        2.0.0
Release:        alt1_12jpp6
Summary:        Maven Bundle Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/felix/maven-bundle-plugin-2.0.0-project.tar.gz
# Apply the following patch for newer bndlibs
Patch0:         %{name}-BundlePlugin.patch
Patch1:         %{name}-ManifestPlugin.patch
Patch2:         %{name}-pom.patch
BuildRequires:  aqute-bndlib >= 0:0.0.311
BuildRequires:  plexus-utils >= 0:1.4.7
BuildRequires:  felix-osgi-core >= 0:1.0.0
BuildRequires:  felix-osgi-obr >= 0:1.0.1
BuildRequires:  kxml2 >= 0:2.2.2
BuildRequires:  maven-shared-dependency-tree >= 1.1
BuildRequires:  maven-wagon >= 1.0-0.2.b2
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin >= 2.3
BuildRequires:  maven-surefire-provider-junit4 >= 2.3
BuildRequires:  maven-doxia-sitetools
BuildRequires:  felix-parent
# XXX: 1.0-alpha-7
BuildRequires: plexus-archiver >= 0:1.0
# XXX: 1.0-alpha-9-stable-1
BuildRequires: plexus-containers-container-default >= 0:1.0
Requires: aqute-bndlib >= 0:0.0.311
Requires: plexus-utils >= 0:1.4.5
Requires: felix-osgi-core >= 0:1.0.0
Requires: felix-osgi-obr >= 0:1.0.1
Requires: kxml2 >= 0:2.2.2
Requires: maven2
Requires: maven-shared-archiver
Requires: maven-shared-dependency-tree
Requires: maven-shared-osgi
Requires: maven-wagon
# XXX: 1.0-alpha-7
Requires: plexus-archiver >= 0:1.0
# XXX: 1.0-alpha-9-stable-1
Requires: plexus-containers-container-default >= 0:1.0
Requires: felix-parent

BuildArch: noarch
Source44: import.info


%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n maven-bundle-plugin-%{version}
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%{_bindir}/mvn-jpp -e -Dmaven.repo.local=${MAVEN_REPO_LOCAL} package javadoc:aggregate

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 644 target/maven-bundle-plugin-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.felix maven-bundle-plugin %{version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_12jpp6
- fixed buildrequires

* Fri Oct 15 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_4jpp6
- new version

