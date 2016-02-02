Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           apache-mime4j
Version:        0.7.2
Release:        alt3_11jpp8
Summary:        Apache JAMES Mime4j
Group:          Development/Java
License:        ASL 2.0
URL:            http://james.apache.org/mime4j
Source0:        http://apache.online.bg//james/mime4j/apache-mime4j-project-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-logging
BuildRequires:  log4j
BuildRequires:  junit
BuildRequires:  apache-commons-io
BuildRequires:  apache-james-project
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  apache-rat-plugin
BuildRequires:  apache-resource-bundles
BuildRequires:  maven-surefire-provider-junit
Source44: import.info

%description
Java stream based MIME message parser.

%package javadoc
Group:          Development/Java
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

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE RELEASE_NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

