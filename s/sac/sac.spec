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
Name: sac
Version: 1.3
Release: alt3_23jpp8
Summary: Java standard interface for CSS parser
License: W3C
Group: System/Libraries
#Original source: http://www.w3.org/2002/06/%{name}java-%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source0: %{name}java-%{version}-jarsdeleted.zip
Source1: %{name}-build.xml
Source2: %{name}-MANIFEST.MF
Source3: https://repo1.maven.org/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant javapackages-tools rpm-build-java zip
Requires: javapackages-tools rpm-build-java
BuildArch: noarch
Source44: import.info

%description
SAC is a standard interface for CSS parsers, intended to work with CSS1, CSS2,
CSS3 and other CSS derived languages.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
install -m 644 %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant jar javadoc

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/sac.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./build/lib/sac.jar $RPM_BUILD_ROOT%{_javadir}/sac.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE3} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc COPYRIGHT.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/*

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_23jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_21jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_17jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_15jpp7
- new release

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_13jpp7
- added osgi provides

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_13jpp7
- new release

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_7jpp6
- updated OSGi manifest

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_7jpp6
- added osgi manifest

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp5
- first build

