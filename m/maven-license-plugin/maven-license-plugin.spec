Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-license-plugin
Version:        1.8.0
Release:        alt6_20jpp8
Summary:        Maven plugin to update header licenses of source files

Group:          Development/Other
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

BuildRequires:  java-devel
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
Summary:        Javadocs for %{name}
Group:          Development/Java
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

%build
%mvn_build -f

%install
%mvn_install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt
%doc NOTICE.txt

%files javadoc  -f .mfiles-javadoc

%changelog
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

