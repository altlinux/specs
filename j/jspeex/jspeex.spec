# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jspeex
Version:        0.9.7
Release:        alt1_8jpp8
Summary:        Java Implementation of Speex

Group:          Development/Other
License:        BSD with advertising
URL:            http://jspeex.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.zip
BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  proguard
BuildRequires:  junit
  
Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
JSpeex is a Java port of the Speex speech Codec (Open Source/Free Software
patent-free audio compression format designed for speech). It provides both
the decoder and the encoder in pure Java, as well as a JavaSound SPI.

%package javadoc
Summary:        Java docs for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
# Make sure to remove any prebuilt jars and classes
find . \( -name '*.class' -o -name '*.jar' \) -exec rm -f '{}' \;
# Remove doc dir if it is already there
[ -d doc ] && rm -rf doc
# Fix wrong end of file encoding
sed -i 's|\r||g' License.txt README

%build
export CLASSPATH=$(build-classpath proguard junit)
%ant package javadoc


%install
install -Dpm 644 dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc License.txt README
%{_javadir}/%{name}.jar

%files javadoc
%doc License.txt
%doc %{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_4jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_3jpp7
- new version

