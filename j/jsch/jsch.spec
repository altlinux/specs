Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jsch
Version:        0.1.55
Release:        alt1_7jpp11
Summary:        Pure Java implementation of SSH2
License:        BSD
URL:            http://www.jcraft.com/jsch/
BuildArch:      noarch

Source0:        http://download.sourceforge.net/sourceforge/jsch/jsch-%{version}.zip
# stripped manifest based on 
# https://download.eclipse.org/tools/orbit/downloads/drops2/R20201130205003/repository/plugins/com.jcraft.jsch_0.1.55.v20190404-1902.jar
Source1:        MANIFEST.MF
Source2:        plugin.properties

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  zip

Requires:       jzlib >= 0:1.0.5
Source44: import.info

%description
JSch allows you to connect to an sshd server and use port forwarding, 
X11 forwarding, file transfer, etc., and you can integrate its 
functionality into your own Java programs.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q
%mvn_file : jsch

%pom_remove_parent

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-compiler-plugin

%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_set pom:project/pom:version %{version}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7

# inject the OSGi Manifest
mkdir META-INF
cp %{SOURCE1} META-INF
cp %{SOURCE2} plugin.properties
touch META-INF/MANIFEST.MF
touch plugin.properties
zip target/%{name}-%{version}.jar META-INF/MANIFEST.MF
zip target/%{name}-%{version}.jar plugin.properties

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:0.1.55-alt1_7jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:0.1.55-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:0.1.55-alt1_2jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:0.1.54-alt1_11jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:0.1.54-alt1_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:0.1.54-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.1.54-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.1.54-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.1.54-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.1.53-alt1_4jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.1.53-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.1.50-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.1.50-alt1_1jpp7
- new version

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.48-alt1_2jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.48-alt1_1jpp7
- update to new release by jppimport

* Sat Nov 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.45-alt1_1jpp6
- update to new release by jppimport

* Sat Oct 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt2_4jpp6
- fixed target

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt1_4jpp6
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt1_3jpp6
- update to new release by jppimport

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1.44-alt1_2jpp6
- new version

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.41-alt1_2jpp5
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.39-alt1_1.1jpp5
- new version

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.31-alt1.3_2jpp5
- rebuild with osgi provides

* Mon Nov 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1.31-alt1_1.2jpp1.7
- build for ALTLinux

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1.28-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.25-alt1
- 0.1.25
- Patch0: add source and target attributes to javac

* Wed Oct 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.22-alt1
- 0.1.22

* Wed Aug 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.21-alt1
- Updated to 0.1.21

* Tue Jan 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.18-alt1
- New upstream release
- Use macros provided by rpm-build-java
- Examples packaged

* Mon Sep 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.17-alt1
- New upstream release

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.15-alt1
- New upstream release

* Sun Mar 28 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.14-alt1
- Package created
