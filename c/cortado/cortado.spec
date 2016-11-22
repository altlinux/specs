# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           cortado
Version:        0.6.0
Release:        alt1_12jpp8
Summary:        Java media framework
URL:            http://www.theora.org/cortado/
# The codecs are all LGPLv2+, the jst framework is mixed, the player applet GPL
License:        LGPLv2+ and GPLv2+
Group:          System/Libraries
Source0:        http://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         cortado-0.6.0-javadoc-fix.patch
BuildArch:      noarch
BuildRequires: javapackages-tools rpm-build-java jorbis
Requires:       javapackages-tools rpm-build-java jorbis
Source44: import.info

%description
Cortado is a Java media framework based on GStreamer's design.


%package javadoc
Summary:        Java docs for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
# Remove included jorbis copy
rm -fr src/com/jcraft
# We don't want to include the examples in the jar we build
mv src/com/fluendo/examples .
# javac does not like the UTF-8 x, ∗, − and ’ symbols used in the comments
sed -i "s/×/x/g" src/com/fluendo/jheora/Quant.java
sed -i "s/∗/*/g" src/com/fluendo/jheora/Quant.java
sed -i "s/−/-/g" src/com/fluendo/jheora/Quant.java
sed -i "s/’/'/g" src/com/fluendo/jheora/Quant.java


%build
javac `find stubs -name "*.java"`
export CLASSPATH=stubs:%{_javadir}/jogg.jar:%{_javadir}/jorbis.jar:.
javac `find src -name "*.java"`
pushd src
jar cf %{name}.jar `find -name "*.class"`
popd
javadoc -d doc -public `find src -name "*.java"`


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a src/%{name}.jar $RPM_BUILD_ROOT%{_javadir}
cp -a doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc ChangeLog HACKING LICENSE.* NEWS README RELEASE TODO examples
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE.*
%doc %{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_7jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_6jpp7
- update to new release by jppimport

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_5jpp7
- new version

