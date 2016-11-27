# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           cambozola
Version:        0.936
Release:        alt1_2jpp8
Summary:        A viewer for multipart jpeg streams

Group:          Development/Other
License:        GPLv2+
URL:            http://www.charliemouse.com/code/cambozola/index.html
Source0:        http://www.andywilcock.com/code/cambozola/%{name}-latest.tar.gz


#patch to add javadoc generation in build.xml
Patch0:         %{name}-%{version}-add_javadoc.patch


BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
#BuildRequires:  ant-nodeps
Requires:       jpackage-utils
Requires:       java
Source44: import.info

%description
Cambozola is a very simple (cheesy!) viewer for multipart jpeg streams
that are often pumped out by a streaming webcam server,
sending over multiple images per second.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p0

# Remove pre-built JAR and class files
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

%build
ant javadoc
ant


%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar   \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p dist/%{name}-server.jar   \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-server.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-server.jar
%doc LICENSE README.html


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.936-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_6jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_5jpp7
- update to new release by jppimport

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_4jpp7
- new version

