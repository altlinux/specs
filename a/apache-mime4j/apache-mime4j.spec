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
Version:        0.8.1
Release:        alt1_2jpp8
Summary:        Apache JAMES Mime4j
License:        ASL 2.0
URL:            http://james.apache.org/mime4j
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/james/mime4j/%{version}/james-mime4j-sources-%{version}.zip

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava:18.0)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
Source44: import.info

%description
Java stream based MIME message parser.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n james-mime4j

# Disable plugins not needed for RPM builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-jar-plugin

# Don't need to build dist assembly
%pom_disable_module assemble

# Compat symlinks for jboss-as
for p in core dom storage; do
  %mvn_file :*$p %{name}/%{name}-$p %{name}/$p
done

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
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt1_2jpp8
- fc29 update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt1_1jpp8
- new version

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

