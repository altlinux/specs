Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jsch
Version:        0.1.54
Release:        alt1_2jpp8
Summary:        Pure Java implementation of SSH2
Group:          Development/Other
License:        BSD
URL:            http://www.jcraft.com/jsch/
BuildArch:      noarch

Source0:        http://download.sourceforge.net/sourceforge/jsch/jsch-%{version}.zip
# wget \
# http://download.eclipse.org/tools/orbit/downloads/drops/R20090825191606/bundles/com.jcraft.jsch_0.1.41.v200903070017.jar
# unzip com.jcraft.jsch_*.jar META-INF/MANIFEST.MF
# mv META-INF/MANIFEST.MF .
# sed -i "/^Name/d" MANIFEST.MF
# sed -i "/^SHA1/d" MANIFEST.MF
# dos2unix MANIFEST.MF
# sed -i "/^$/d" MANIFEST.MF
# unix2dos MANIFEST.MF
Source1:        MANIFEST.MF
Source2:        plugin.properties

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  zip

Requires:       jzlib >= 0:1.0.5
Obsoletes: %{name}-demo < %{version}
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

%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_set pom:project/pom:version %{version}

%build
%mvn_build

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
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
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
