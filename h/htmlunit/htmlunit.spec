Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           htmlunit
Version:        2.19
Release:        alt1_2jpp8
Summary:        A headless web browser for automated testing
License:        ASL 2.0 
URL:            http://htmlunit.sourceforge.net/
Source0:        http://downloads.sourceforge.net/htmlunit/%{name}-%{version}-src.zip

BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(net.sourceforge.cssparser:cssparser)
BuildRequires:  mvn(net.sourceforge.htmlunit:htmlunit-core-js)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpmime)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.eclipse.jetty.websocket:websocket-client)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xalan:xsltc)
BuildRequires:  mvn(xerces:xercesImpl)

BuildArch:      noarch
Source44: import.info

%description
HtmlUnit is a "GUI-Less browser for Java programs". It models HTML 
documents and provides an API for automated testing of
web applications. 

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
find -name '*.jar' -print -delete 
find -name '*.class' -print -delete

%pom_xpath_remove "pom:build/pom:extensions"

%pom_xpath_set "pom:packaging" bundle
%pom_xpath_remove "pom:Embed-Dependency"

# unwanted plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-scm-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

# Unavailable test deps
%pom_remove_dep :gsbase
%pom_remove_dep org.seleniumhq.selenium:
%pom_xpath_remove "pom:dependency[pom:type = 'test-jar']"
# org.apache.httpcomponents:httpclient:4.1.2:test-jar
%pom_xpath_remove "pom:project/pom:dependencies/pom:dependency[pom:scope = 'test']"

%pom_add_dep xalan:xsltc:2.7.1

%mvn_file : %{name}

%build

# enabling tests would require packaging some selenium plugins
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.19-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.17-alt1_1jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt3_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt3_3jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt2_3jpp7
- fixed build

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt1_3jpp7
- new release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt6_4jpp6
- fixed build w/new commons-parent

* Thu May 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt5_4jpp6
- fixed build

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt4_4jpp6
- build with velocity15

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt3_4jpp6
- build with new jakarta-commons-lang

* Wed Nov 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt2_4jpp6
- added BR: jetty6-servlet-2.5-api

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_4jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_3jpp5
- full build

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt0.1jpp
maven 2.0.7 bootstrap

