Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-license-plugin
Version:        1.8.0
Release:        alt6_31jpp11
Summary:        Maven plugin to update header licenses of source files

License:        ASL 2.0
URL:            http://code.google.com/p/maven-license-plugin
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://maven-license-plugin.googlecode.com/svn/tags/maven-license-plugin-1.8.0 maven-license-plugin
# tar cfJ maven-license-plugin-1.8.0.tar.xz maven-license-plugin
Source0:        %{name}-%{version}.tar.xz
# remove testng dep (tests are skipped) and maven-license-plugin call
Patch0:         001-mavenlicenseplugin-fixbuild.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  apache-resource-bundles
BuildRequires:  maven-local
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-shared
BuildRequires:  plexus-utils
BuildRequires:  plexus-classworlds
BuildRequires:  xml-commons-apis
BuildRequires:  xmltool
BuildRequires:  maven-source-plugin
BuildRequires:  mvn(org.apache.maven:maven-project)

Requires:       jpackage-utils
Requires:       maven
Requires:       maven-shared
Requires:       xmltool
Source44: import.info

%description
maven-license-plugin is a Maven plugin that help you managing license
headers in source files. Basically, when you are developing a project
either in open source or in a company, you often need to add at the top
of your source files a license to protect your work.
This plugin lets you maintain the headers, including checking if the
header is present, generating a report and of course having the
possibility to update / reformat missing license headers.


%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
%patch0 -p1
# fix EOL
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' NOTICE.txt

# Remove wagon-webdav extension which is not available
%pom_xpath_remove pom:build/pom:extensions

# Set sources/resources encoding
%pom_xpath_inject "pom:properties" "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc --no-dereference LICENSE.txt
%doc NOTICE.txt

%files javadoc  -f .mfiles-javadoc

%changelog
* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 0:1.8.0-alt6_31jpp11
- fixed build

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.8.0-alt6_30jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt6_27jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt6_25jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt6_23jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt6_22jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt6_21jpp8
- new jpp release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt6_20jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt4_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt4_14jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt4_9jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt3_9jpp7
- rebuild with new apache-resource-bundles

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt2_9jpp7
- fc update

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt2_5jpp7
- applied repocop patches

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0-alt1_5jpp7
- dropped obsoletes on mojo-maven2-plugin-cobertura

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt1_1jpp6
- new jpp release

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

