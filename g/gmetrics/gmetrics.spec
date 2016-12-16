Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname GMetrics

Name:          gmetrics
Version:       0.6
Release:       alt1_15jpp8
Summary:       Groovy library that provides reports and metrics for Groovy code
License:       ASL 2.0
Url:           http://gmetrics.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}/%{oname}-%{version}-bin.tar.gz
# use antrun-plugin instead of gmaven
# fix log4j groovy version
# rebase for groovy 2
Patch0:        gmetrics-0.6-antrunplugin.patch
Patch1:        gmetrics-0.6-groovy2.patch

BuildRequires: maven-local
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.groovy:groovy-all)
BuildRequires: mvn(org.fusesource:fusesource-pom:pom:)
# groovy-all embedded libs
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(org.ow2.asm:asm-all)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(org.slf4j:slf4j-nop)

BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
GMetrics provides calculation and reporting of size and
complexity metrics for Groovy source code, by scanning the
code with an Ant Task, applying a set of metrics, and
generating an HTML or XML report of the results.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

# clean up
find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/*
%patch0 -p0
%patch1 -p1

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :gmaven-plugin
%pom_remove_dep :CodeNarc

sed -i "s|pom.version|project.version|" pom.xml

chmod 644 README.txt

for d in CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt ; do
  sed -i 's/\r//' $d
done

%mvn_file :%{oname} %{name} %{oname}

%build

# test skipped require Codenarc, circular deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.txt README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_5jpp7
- new release

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2jpp7
- new version

