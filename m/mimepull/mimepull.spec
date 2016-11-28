Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             mimepull
Version:          1.9.6
Release:          alt1_2jpp8
Summary:          Streaming API to access attachments from a MIME message
License:          CDDL and GPLv2 with exceptions
URL:              http://mimepull.java.net

# svn export https://svn.java.net/svn/mimepull~svn/tags/mimepull-1.9.6/ mimepull-1.9.6
# tar cafJ mimepull-1.9.6.tar.xz mimepull-1.9.6
Source0:          mimepull-%{version}.tar.xz

BuildArch:        noarch
BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(net.java:jvnet-parent:pom:)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:    mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Source44: import.info
#BuildRequires:    mvn(org.tmatesoft.svnkit:svnkit)

%description
Provides a streaming API to access attachments parts in a MIME message

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# Unavailable plugins
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
# Unneeded plugins
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
# Disable svnkit support for buildnumber-maven-plugin
%pom_remove_dep org.tmatesoft.svnkit:svnkit
%pom_xpath_remove pom:providerImplementations


iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE
sed -i 's/\r//' LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.6-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.5-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_5jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_3jpp7
- fixed maven1 dependency

* Tue Jan 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_3jpp7
- initial build

