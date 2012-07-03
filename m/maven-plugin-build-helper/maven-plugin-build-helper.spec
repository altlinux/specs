BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-plugin-build-helper
Version:        1.5
Release:        alt1_5jpp7
Summary:        Build Helper Maven Plugin

Group:          Development/Java
License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/build-helper-maven-plugin/
# The source tarball has been generated from upstream VCS:
# svn export https://svn.codehaus.org/mojo/tags/build-helper-maven-plugin-%{version} 
#            %{name}-%{version}
# tar caf %{name}-%{version}.tar.xz %{name}-%{version}
Source0:        %{name}-%{version}.tar.xz
Patch0:         add-junit-dependency.patch
Patch1:         %{name}-core.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: plexus-utils
BuildRequires: maven
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-doxia-sitetools
BuildRequires: mojo-parent
BuildRequires: junit4
Requires: jpackage-utils
Requires: plexus-utils
Requires: mojo-parent
Source44: import.info

%description
This plugin contains various small independent goals to assist with
Maven build lifecycle.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%patch0
%patch1 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/build-helper-maven-plugin-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar


# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_5jpp7
- fc version

