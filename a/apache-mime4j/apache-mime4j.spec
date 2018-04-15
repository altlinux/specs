Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-mime4j
Version:        0.7.2
Release:        alt3_17jpp8
Summary:        Apache JAMES Mime4j
License:        ASL 2.0
URL:            http://james.apache.org/mime4j
BuildArch:      noarch

Source0:        http://apache.online.bg//james/mime4j/apache-mime4j-project-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.james:james-project:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.rat:apache-rat-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
Source44: import.info

%description
Java stream based MIME message parser.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-project-%{version}
rm -fr stage
# prevents rat plugin from failing the build
rm -fr DEPENDENCIES

# Compat symlinks for jboss-as
for p in core dom storage; do
  %mvn_file :*$p %{name}/%{name}-$p %{name}/$p
done

# Don't use deprecated "attached" goal of Maven Assembly Plugin, which
# was removed in version 3.0.0.
%pom_xpath_set "pom:plugin[pom:artifactId='maven-assembly-plugin']/pom:executions/pom:execution/pom:goals/pom:goal[text()='attached']" single assemble

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE_NOTES.txt
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_16jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_3jpp7
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt2_3jpp7
- rebuild with new apache-resource-bundles

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt1_3jpp7
- new release

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt3_2jpp6
- dropped felix-maven2 dependency

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt2_2jpp6
- fixed build with maven3

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_2jpp6
- new version

