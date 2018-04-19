Epoch: 0
Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: sac
Version: 1.3
Release: alt3_28jpp8
Summary: Java standard interface for CSS parser
License: W3C
#Original source: http://www.w3.org/2002/06/%{name}java-%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source0: %{name}java-%{version}-jarsdeleted.zip
Source1: %{name}-build.xml
Source2: %{name}-MANIFEST.MF
Source3: https://repo1.maven.org/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
URL: http://www.w3.org/Style/CSS/SAC/

BuildRequires: ant
BuildRequires: javapackages-local

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

# inject OSGi manifest
jar ufm build/lib/sac.jar %{SOURCE2}

%install
%mvn_artifact %{SOURCE3} build/lib/sac.jar
%mvn_file ":sac" sac
%mvn_install -J build/api

%files -f .mfiles
%doc --no-dereference COPYRIGHT.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYRIGHT.html

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_28jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_27jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_24jpp8
- new jpp release

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

