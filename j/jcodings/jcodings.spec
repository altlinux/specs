# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit_hash d50ee0e
%global tag_hash d50ee0e

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jcodings
Version:        1.0.9
Release:        alt1_1jpp7
Summary:        Java-based codings helper classes for Joni and JRuby

Group:          Development/Java
License:        MIT
URL:            http://github.com/jruby/%{name}
Source0:        https://github.com/jruby/jcodings/tarball/%{version}/jruby-%{name}-%{version}-0-g%{commit_hash}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils

BuildRequires:  maven
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       jpackage-utils
Source44: import.info

%description
Java-based codings helper classes for Joni and JRuby.


%prep
%setup -q -n jruby-%{name}-%{tag_hash}

find -name '*.class' -delete
find -name '*.jar' -delete

%build
echo "See %{url} for more info about the %{name} project." > README.txt

mvn-rpmbuild install javadoc:aggregate

%install
mkdir -p %{buildroot}%{_javadir}

cp -p target/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README.txt

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_1jpp7
- new version

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp7
- new release

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp5
- new version

