Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           swing-layout
Version:        1.0.4
Release:        alt2_21jpp11
Summary:        Natural layout for Swing panels
License:        LGPLv2
URL:            https://swing-layout.dev.java.net/
# https://svn.java.net/svn/swing-layout~svn/trunk/
# the above urls are dead, since the upstream project doesn't exist anymore
Source0:        %{name}-%{version}-src.zip
# from http://java.net/jira/secure/attachment/27303/pom.xml
Source1:        %{name}-pom.xml
# use javac target/source 1.5
Patch0:         %{name}-%{version}-project_properties.patch
Patch1:         %{name}-%{version}-fix-incorrect-fsf-address.patch

BuildRequires:  junit >= 3.8.2
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  dos2unix

BuildArch:      noarch
Source44: import.info

%description
Extensions to Swing to create professional cross platform layout.

%prep
%setup -q
dos2unix releaseNotes.txt
%patch0 -p0
%patch1 -p0
sed -i 's/\r//' COPYING

cat %{SOURCE1} | sed "s|<version>1.0.3</version>|<version>%{version}</version>|"  >  %{name}.pom

%build

%{ant} jar 
%mvn_artifact %{name}.pom dist/%{name}.jar

%install

%mvn_install -J dist/javadoc


%check
%{ant} test

%files -f .mfiles
%doc releaseNotes.txt
%doc --no-dereference COPYING

%changelog
* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt2_21jpp11
- new version

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_13jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_7jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_4jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp6
- update to new release by jppimport

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp6
- new build for netbeans

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp5
- converted from JPackage by jppimport script

