BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cortado
Version:        0.6.0
Release:        alt1_5jpp7
Summary:        Java media framework
URL:            http://www.theora.org/cortado/
# The codecs are all LGPLv2+, the jst framework is mixed, the player applet GPL
License:        LGPLv2+ and GPLv2+
Group:          System/Libraries
Source0:        http://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  jpackage-utils jorbis
Requires:       jpackage-utils jorbis
Source44: import.info

%description
Cortado is a Java media framework based on GStreamer's design.


%package javadoc
Summary:        Java docs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
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
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_5jpp7
- new version

