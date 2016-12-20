Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          gmavenplus-plugin
Version:       1.5
Release:       alt1_1jpp8
Summary:       Integrates Groovy into Maven projects
License:       ASL 2.0
URL:           http://groovy.github.io/GMavenPlus/
Source0:       https://github.com/groovy/GMavenPlus/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(jline:jline)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-antlr)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.ant:ant-launcher)
BuildRequires: mvn(org.apache.ivy:ivy)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-plugin-registry)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.shared:file-management)
BuildRequires: mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires: mvn(org.codehaus.groovy:groovy-all)
BuildRequires: mvn(org.codehaus.groovy:groovy-ant)
BuildRequires: mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires: mvn(org.codehaus.plexus:plexus-cli)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires: mvn(org.fusesource.jansi:jansi)
BuildRequires: mvn(org.mockito:mockito-all)
# IT tests deps
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch:     noarch
Source44: import.info

%description
GMavenPlus is a rewrite of GMaven, a Maven plugin
that allows you to integrate Groovy into your
Maven projects.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n GMavenPlus-%{version}

%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-help-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-site-plugin

%pom_xpath_remove "pom:build/pom:extensions"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

# Mockito cannot mock this class: class org.codehaus.gmavenplus.mojo.AbstractGroovyMojoTest$TestGroovyMojo
rm -r src/test/java/org/codehaus/gmavenplus/mojo/AbstractGroovyMojoTest.java

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' README.markdown
touch -r README.markdown.orig README.markdown
rm README.markdown.orig

%mvn_file : %{name}

%build

%mvn_build -- -Pnonindy

%install
%mvn_install

%files -f .mfiles
%doc README.markdown
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1jpp8
- new version

