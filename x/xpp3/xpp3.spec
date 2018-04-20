Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oversion 1.1.4c

Summary:        XML Pull Parser
Name:           xpp3
Version:        1.1.4
Release:        alt1_18.cjpp8
License:        ASL 1.1
URL:            http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/index.html
Source0:        http://www.extreme.indiana.edu/dist/java-repository/xpp3/distributions/xpp3-%{oversion}_src.tgz
Source1:        http://repo1.maven.org/maven2/xpp3/xpp3/%{oversion}/xpp3-%{oversion}.pom
Source2:        http://repo1.maven.org/maven2/xpp3/xpp3_xpath/%{oversion}/xpp3_xpath-%{oversion}.pom
Source3:        http://repo1.maven.org/maven2/xpp3/xpp3_min/%{oversion}/xpp3_min-%{oversion}.pom
Source4:        %{name}-%{oversion}-OSGI-MANIFEST.MF
Patch0:         %{name}-link-docs-locally.patch

BuildRequires:  javapackages-local
BuildRequires:  java-javadoc
BuildRequires:  ant
BuildRequires:  junit

BuildArch:      noarch
Source44: import.info

%description
XML Pull Parser 3rd Edition (XPP3) MXP1 is an XmlPull
parsing engine that is based on ideas from XPP and in
particular XPP2 but completely revised and rewritten to
take best advantage of latest JIT JVMs such as Hotspot in JDK 1.4.

%package minimal
Group: Development/Java
Summary:        Minimal XML Pull Parser

%description minimal
Minimal XML pull parser implementation.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Requires:       java-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{oversion}
# remove all binary libs
find -name \*.jar -delete
# Remove class bundled from Axis (now it's bundled in JRE)
rm -rf src/java/builder/javax

%patch0

# "src/java/addons_tests" does not exist
sed -i 's|depends="junit_main,junit_addons"|depends="junit_main"|' build.xml

# relax javadoc linting
sed -i '/<javadoc/aadditionalparam="-Xdoclint:none"' build.xml

%build
export CLASSPATH=$(build-classpath junit)
ant xpp3 junit apidoc

# Add OSGi metadata
jar ufm build/%{name}-%{oversion}.jar %{SOURCE4}

%install
%mvn_file ':{*}' @1
%mvn_package :xpp3_min minimal

%mvn_artifact %{SOURCE1} build/%{name}-%{oversion}.jar
%mvn_artifact %{SOURCE2} build/%{name}_xpath-%{oversion}.jar
%mvn_artifact %{SOURCE3} build/%{name}_min-%{oversion}.jar

# Javadocs
%mvn_install -J doc/api

ln -s xpp3_min.jar %buildroot%_javadir/xpp3-minimal.jar

%files -f .mfiles
%doc README.html doc/*.txt doc/*.html
%doc --no-dereference LICENSE.txt

%files minimal -f .mfiles-minimal
%doc --no-dereference LICENSE.txt
%_javadir/xpp3-minimal.jar

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.1.4-alt1_18.cjpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.1.4-alt1_17.cjpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1.4-alt1_11.cjpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1.4-alt1_7.cjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1.3.8-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1.3.8-alt1_8jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.1.3.8-alt1_7jpp7
- fc update

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt2_2jpp6
- split maven-fragments for minimal subpackage

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_2jpp6
- added pom

* Wed Feb 25 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3.8-alt3_1jpp5
- added xpp3_min pom

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3.8-alt2_1jpp5
- jpackage 5.0

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3.8-alt1_1jpp1.7
- updated to new jpackage release

* Thu Mar 23 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1.3.4-alt2m
- Fix build with j2se-1.5

* Sun Apr 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1.3.4-alt1m
- Initial build for ALT Linux Sisyphus

