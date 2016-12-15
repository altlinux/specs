Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             jline
Version:          2.13
Release:          alt1_2jpp8
Summary:          JLine is a Java library for handling console input
License:          BSD and ASL 2.0
URL:              https://github.com/jline/jline2

# git clone git://github.com/jline/jline2.git
# cd jline2/ && git archive --format=tar --prefix=jline-2.13/ jline-2.13 | xz > jline-2.13.tar.xz
Source0:          jline-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven-local
BuildRequires:    maven-site-plugin
BuildRequires:    jansi
BuildRequires:    fusesource-pom
BuildRequires:    mvn(org.powermock:powermock-module-junit4)
BuildRequires:    mvn(org.powermock:powermock-api-easymock)
BuildRequires:    mvn(org.easymock:easymock)

Obsoletes: jline2 < %{version}-%{release}
Provides: jline2 = %{version}-%{release}
Source44: import.info

%description
JLine is a Java library for handling console input. It is similar
in functionality to BSD editline and GNU readline. People familiar
with the readline/editline capabilities for modern shells (such as
bash and tcsh) will find most of the command editing features of
JLine to be familiar. 

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
Obsoletes: jline2-javadoc < %{version}-%{release}
Provides: jline2-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jline-%{version}

# Remove maven-shade-plugin usage
%pom_remove_plugin "org.apache.maven.plugins:maven-shade-plugin"
# Remove animal sniffer plugin in order to reduce deps
%pom_remove_plugin "org.codehaus.mojo:animal-sniffer-maven-plugin"

# Remove unavailable and unneeded deps
%pom_xpath_remove "pom:build/pom:extensions"
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-site-plugin']"

# Do not import non-existing internal package
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Import-Package"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions" "<Import-Package>javax.swing;resolution:=optional,org.fusesource.jansi,!org.fusesource.jansi.internal</Import-Package>"

# Let maven bundle plugin figure out the exports.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Export-Package"

# For some reason these directories do not exist, failing compilation due to -Werror
mkdir -p target/generated-sources/annotations
mkdir -p target/generated-test-sources/test-annotations

%build
%mvn_build -- -Dmaven.test.skip.exec=true

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/jline
%dir %{_mavenpomdir}/jline

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.13-alt1_2jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.12.1-alt1_2jpp8
- unbootstrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.12.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp7
- applied repocop patches

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.94-alt1_1jpp5
- new version

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt2_1jpp5
- fixed build w/java5

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt2_1jpp1.7
- build with maven

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_1jpp1.7
- updated to new jpackage release

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9-alt2_2jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2
- fixed build using elinks-utf8-hack

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 0.9.1-alt1
- Rebuild for ALTLinux Sisyphus
- spec cleanup

* Mon Apr 25 2005 Fernando Nasser <fnasser@redhat.com> - 0:0.9.1-1jpp
- Upgrade to 0.9.1
- Disable attempt to include external jars

* Mon Apr 25 2005 Fernando Nasser <fnasser@redhat.com> - 0:0.8.1-3jpp
- Changes to use locally installed DTDs
- Do not try and access sun site for linking javadoc

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:0.8.1-2jpp
- Rebuild with ant-1.6.2

* Mon Jan 26 2004 David Walluck <david@anti-microsoft.org> 0:0.8.1-1jpp
- release
