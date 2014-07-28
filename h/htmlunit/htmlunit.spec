Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           htmlunit
Version:        2.9
Release:        alt3_5jpp7
Summary:        A headless web browser for automated testing

Group:          Development/Java
License:        ASL 2.0 
URL:            http://htmlunit.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-2.9-src.zip
Patch0:         %{name}-%{version}-dep-fixes.patch
Patch1:         %{name}-%{version}-no-jfreechart.patch
Patch2:         %{name}-%{version}-old-nekohtml.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-fileupload
BuildRequires:  cssparser
BuildRequires:  nekohtml
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  htmlunit-core-js
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  xalan-j2
BuildRequires:  xalan-j2-xsltc

Requires:       jpackage-utils
Requires:       xalan-j2
Requires:       xalan-j2-xsltc
Requires:       apache-commons-codec
Requires:       apache-commons-collections
Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-logging
Requires:       apache-commons-io
Requires:       apache-commons-fileupload
Requires:       cssparser
Requires:       nekohtml
Requires:       jakarta-commons-httpclient
Requires:       htmlunit-core-js
Source44: import.info

%description
HtmlUnit is a "GUI-Less browser for Java programs". It models HTML 
documents and provides an API for automated testing of
web applications. 

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p 0
%patch1 -p 0
%patch2 -p 0

%build
# enabling tests would require packaging some selenium plugins
mvn-rpmbuild -Dmaven.test.skip=true package javadoc:aggregate

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc LICENSE.txt
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
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

