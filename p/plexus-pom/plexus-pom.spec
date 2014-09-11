BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          plexus-pom
Version:       3.3.1
Release:       alt1_5jpp7
Summary:       Root Plexus Projects POM
Group:         Development/Java
License:       ASL 2.0
URL:           https://github.com/sonatype/%{name}/
Source0:       https://github.com/sonatype/plexus-pom/archive/plexus-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: spice-parent
Source44: import.info

%description
The Plexus project provides a full software stack for creating and
executing software projects.  This package provides parent POM for
Plexus packages.

%prep
%setup -q -n plexus-pom-plexus-%{version}
# require: maven-site-plugin *
%pom_xpath_remove "pom:profile[pom:id='maven-3']"
# * require: org.codehaus.plexus plexus-stylus-skin 1.0
# org.apache.maven.wagon wagon-webdav-jackrabbit 1.0
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_4jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt3_3jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp7
- new version

