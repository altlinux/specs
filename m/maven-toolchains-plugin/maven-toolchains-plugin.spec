Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		maven-toolchains-plugin
Version:	1.0
Release:	alt4_7jpp7
Summary:	Maven plugin for sharing configuration across projects
License:	ASL 2.0
URL:		http://maven.apache.org/plugins/maven-toolchains-plugin/
Source0:	http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:	noarch
BuildRequires:	maven-local
Source44: import.info

%description
The Toolchains Plugins allows to share configuration across plugins. For
example to make sure the plugins like compiler, surefire, javadoc, webstart
etc. all use the same JDK for execution. Similarly to maven-enforcer-plugin, it
allows to control environmental constraints in the build.

%package javadoc
Group: Development/Java
Summary:	API documentation for %{name}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
The API documentation of %{name}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_4jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4jpp7
- new version

