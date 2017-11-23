Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           felix-parent
Version:        4
Release:        alt1_4jpp8
Summary:        Parent POM file for Apache Felix Specs
License:        ASL 2.0
URL:            http://felix.apache.org/
Source0:        http://repo1.maven.org/maven2/org/apache/felix/felix-parent/%{version}/%{name}-%{version}-source-release.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.mockito:mockito-all)

# FIXME auto-requires are not generated
Requires:  mvn(org.easymock:easymock)
Requires:  mvn(org.mockito:mockito-all)
Source44: import.info

%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q -n felix-parent-%{version}
%mvn_alias : :felix
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

# wagon ssh dependency unneeded
%pom_xpath_remove pom:extensions

# Remove workaround for MANTRUN-51/MNG-6205 issue
# (should only be needed with old versions of Maven)
# See: http://svn.apache.org/viewvc/maven/plugins/trunk/maven-antrun-plugin/src/site/fml/faq.fml?r1=790402&r2=790401
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-antrun-plugin']/pom:dependencies"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_4jpp8
- new fc release

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_3jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_13jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_10jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_9jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_8jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_8jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_8jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_5jpp6
- use maven-plugin-build-helper

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt3_5jpp6
- fixed build with maven3

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_5jpp6
- new jpp release

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_3jpp6
- dropped mojo-maven2-* dependency

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_3jpp6
- fixed repolib

