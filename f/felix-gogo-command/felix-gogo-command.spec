Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           felix-gogo-command
Version:        0.16.0
Release:        alt1_3jpp8
Summary:        Apache Felix Gogo Command

License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/felix/org.apache.felix.gogo.command-%{version}-project.tar.gz

Patch0:         felix-gogo-command-pom.xml.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:gogo-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.bundlerepository)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.osgi:org.osgi.compendium)
BuildRequires:  mvn(org.mockito:mockito-all)
Source44: import.info

%description
Provides basic shell commands for Gogo.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n org.apache.felix.gogo.command-%{version}
%patch0 -p1

# These deps are provided at runtime by the osgi framework in which are running
# Adding "provided" scope here avoids unnecessary deps on the felix stack if we
# are running in a different osgi container like equinox, for example
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId[text()='org.apache.felix.framework']]" "<scope>provided</scope>"
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId[text()='org.osgi.compendium']]" "<scope>provided</scope>"
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId[text()='org.apache.felix.bundlerepository']]" "<scope>provided</scope>"

# Upstream distribution does not have this requirement, we don't need it here either
sed -i -e 's|\*</Import-Package>|!org.apache.felix.bundlerepository,*</Import-Package>|' pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_5jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_4jpp7
- new release

