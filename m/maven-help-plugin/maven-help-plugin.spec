# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-help-plugin
Version:        2.1.1
Release:        alt4_8jpp7
Summary:        Plugin to to get relative information about a project or the system

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-help-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         add-compat.patch
Patch1:         reduce-exception.patch
Patch2:         %{name}-migration-to-component-metadata.patch
BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-exec
BuildRequires: xstream
BuildRequires: jpackage-utils
BuildRequires: plexus-containers-component-metadata
BuildRequires: maven-plugin-tools-generators
Requires: ant
Requires: maven
Requires: jpackage-utils
Requires: xstream
Requires: maven-plugin-tools-generators

Obsoletes: maven2-plugin-help < 0:%{version}-%{release}
Provides: maven2-plugin-help = 0:%{version}-%{release}
Source44: import.info

%description
The Maven Help Plugin is used to get relative information about a project
 or the system. It can be used to get a description of a particular plugin,
including the plugin's mojos with their parameters and component requirements,
the effective POM and effective settings of the current build,
and the profiles applied to the current project being built.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0
%patch1
%patch2 -p1

# In newer versions of maven-plugin-tools the PluginUtils.toText()
# static method was moved to GeneratorUtils class.
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-tools-generators
sed -i "s|PluginUtils.toText|org.apache.maven.tools.plugin.generator.GeneratorUtils.toText|" \
    src/main/java/org/apache/maven/plugins/help/DescribeMojo.java

# Generated HelpMojo.java is missing package declaration.  Use exec
# plugin to inject package declaration during process-sources phase.
%pom_add_plugin org.codehaus.mojo:exec-maven-plugin . "
  <executions>
    <execution>
      <phase>process-sources</phase>
      <goals>
        <goal>exec</goal>
      </goals>
    </execution>
  </executions>
  <configuration>
    <executable>sed</executable>
    <arguments>
      <argument>-i</argument>
      <argument>1ipackage org.apache.maven.plugins.help;</argument>
      <argument>target/generated-sources/plugin/org/apache/maven/plugins/help/HelpMojo.java</argument>
    </arguments>
  </configuration>"

%build
# no junit-addons, skip test
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt4_8jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt4_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt3_7jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_7jpp7
-  new release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_4jpp7
- fixed build with xpp3

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_4jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

