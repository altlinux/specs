BuildRequires: javapackages-local
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           not-yet-commons-ssl
Version:        0.3.17
Release:        alt2_4jpp8
Summary:        Library to make SSL and Java Easier

Group:          Development/Other
License:        ASL 2.0
URL:            http://juliusdavies.ca/commons-ssl
Source0:        http://juliusdavies.ca/commons-ssl/not-yet-commons-ssl-%{version}.zip
Source1:        %{name}-MANIFEST.MF
Source2:        %{name}-%{version}.pom
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  log4j
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  bouncycastle
BuildRequires:  ant-junit
BuildRequires:  mockito
BuildRequires:  zip
Requires:       log4j
Requires:       jakarta-commons-httpclient
Source44: import.info

%description
Commons-SSL lets you control the SSL options you need in an 
natural way for each SSLSocketFactory, and those options won't 
bleed into the rest of your system.

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
rm -fr javadocs/
sed -i -e 's|optimize="false"|optimize="false" encoding="UTF-8"|g' build.xml
sed -i -e 's|linksource="yes"|linksource="yes" encoding="UTF-8"|g' build.xml

%build
export CLASSPATH=$(build-classpath log4j commons-httpclient bcprov mockito)
ant -Dbuild.sysclasspath=first jar test javadoc

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/not-yet-commons-ssl.jar META-INF/MANIFEST.MF

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/not-yet-commons-ssl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/javadocs/*  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -dm 755 %{buildroot}/%{_mavenpomdir}
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.3.17-alt2_4jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.3.17-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.3.17-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.3.17-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.3.11-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.3.11-alt2_9jpp7
- new release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.3.11-alt2_8jpp7
- added compat depmap

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.3.11-alt1_8jpp7
- fc update

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.11-alt1_2jpp6
- new version

