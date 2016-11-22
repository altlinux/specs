Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oversion 1.1.4c

Summary:        XML Pull Parser
Name:           xpp3
Version:        1.1.4
Release:        alt1_11.cjpp8
License:        ASL 1.1
URL:            http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/index.html
Source0:        http://www.extreme.indiana.edu/dist/java-repository/xpp3/distributions/xpp3-%{oversion}_src.tgz
Source1:        http://repo1.maven.org/maven2/xpp3/xpp3/%{oversion}/xpp3-%{oversion}.pom
Source2:        http://repo1.maven.org/maven2/xpp3/xpp3_xpath/%{oversion}/xpp3_xpath-%{oversion}.pom
Source3:        http://repo1.maven.org/maven2/xpp3/xpp3_min/%{oversion}/xpp3_min-%{oversion}.pom
Source4:        %{name}-%{oversion}-OSGI-MANIFEST.MF
Patch0:         %{name}-link-docs-locally.patch
BuildRequires:  javapackages-local
BuildRequires:  zip
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  xml-commons-apis
Requires:       xml-commons-apis

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

%build
export CLASSPATH=$(build-classpath xml-commons-apis junit)
ant xpp3 junit apidoc

# Add OSGi metadata
pushd build
mkdir META-INF
unzip -o %{name}-%{oversion}.jar META-INF/MANIFEST.MF
cat %{SOURCE4} >> META-INF/MANIFEST.MF
sed -i '/^\r$/d' META-INF/MANIFEST.MF
zip -u %{name}-%{oversion}.jar META-INF/MANIFEST.MF
popd

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# JARs
install -p -m 644 build/%{name}-%{oversion}.jar \
    %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 build/%{name}_xpath-%{oversion}.jar \
    %{buildroot}%{_javadir}/%{name}-xpath.jar
install -p -m 644 build/%{name}_min-%{oversion}.jar \
    %{buildroot}%{_javadir}/%{name}-minimal.jar

# POMs
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -p -m 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}-xpath.pom
install -p -m 644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP-%{name}-minimal.pom

# XMvn metadata
%add_maven_depmap
%add_maven_depmap JPP-%{name}-xpath.pom %{name}-xpath.jar
%add_maven_depmap JPP-%{name}-minimal.pom %{name}-minimal.jar -f minimal

# Javadocs
cp -pr doc/api/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc README.html doc/*
%doc LICENSE.txt

%files minimal -f .mfiles-minimal
%doc LICENSE.txt

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
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

