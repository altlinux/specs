Name: maven-license-plugin
Version: 1.8.0
Summary: Maven plugin to update header licenses of source files
License: ASL 2.0
Url: http://code.google.com/p/maven-license-plugin
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-license-plugin = 1.8.0-18.fc23
Provides: mvn(com.mycila.maven-license-plugin:maven-license-plugin) = 1.8.0
Provides: mvn(com.mycila.maven-license-plugin:maven-license-plugin:pom:) = 1.8.0
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils
Requires: maven
Requires: maven-shared
Requires: mvn(com.mycila.xmltool:xmltool)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: xmltool

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: maven-license-plugin-1.8.0-18.fc23.cpio

%description
maven-license-plugin is a Maven plugin that help you managing license
headers in source files. Basically, when you are developing a project
either in open source or in a company, you often need to add at the top
of your source files a license to protect your work.
This plugin lets you maintain the headers, including checking if the
header is present, generating a report and of course having the
possibility to update / reformat missing license headers.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
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

