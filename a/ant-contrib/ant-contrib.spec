Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global beta_number b3

Summary:        Collection of tasks for Ant
Name:           ant-contrib
Version:        1.0
Release:        alt5_0.29.b3jpp8
License:        ASL 2.0 and ASL 1.1
URL:            http://ant-contrib.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/ant-contrib/ant-contrib/1.0b3/ant-contrib-1.0b3-src.tar.bz2
# ASL 2.0 Licence text
# Upstream bug at https://sourceforge.net/tracker/?func=detail&aid=3590371&group_id=36177&atid=416920
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch2:         %{name}-antservertest.patch
BuildRequires:  ivy-local
BuildRequires:  junit
BuildRequires:  ant-junit
BuildRequires:  xerces-j2
BuildRequires:  bcel
BuildRequires:  apache-ivy
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-parent
Requires:       junit
Requires:       ant
Requires:       xerces-j2
BuildArch:      noarch
Source44: import.info

%description
The Ant-Contrib project is a collection of tasks
(and at one point maybe types and other tools)
for Apache Ant.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description    javadoc
Api documentation for %{name}.

%prep
%setup -q  -n %{name}
%patch2

cp %{SOURCE2} LICENSE-2.0.txt

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

sed -i "s|xercesImpl|xerces-j2|g" ivy.xml
# needs porting to latest ivy
rm -fr src/java/net/sf/antcontrib/net/URLImportTask.java

sed -i '/<ivy:configure /d' build.xml
rm -f ivy-conf.xml

sed -i '/<info /s//&revision="1.0b3" /' ivy.xml
%mvn_alias : ant-contrib:

%build
%ant -Divy.mode=local dist

%install
%mvn_artifact ivy.xml target/%{name}.jar
%mvn_install -J target/docs/api

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "ant-contrib/ant-contrib" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/ant-contrib

%files -f .mfiles
%{_sysconfdir}/ant.d/ant-contrib
%doc target/docs/LICENSE.txt LICENSE-2.0.txt
%doc target/docs/manual/tasks/*

%files javadoc -f .mfiles-javadoc
%doc target/docs/LICENSE.txt LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.29.b3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.28.b3jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.22.b3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.21.b3jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.20.b3jpp7
- fc update

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.17.b3jpp7
- fc release

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_1.b3.2jpp6
- new jpp release

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_1.b3.1jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.b3.1jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b3.1jpp5
- converted from JPackage by jppimport script

* Wed Aug 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b2.2jpp1.7
- converted from JPackage by jppimport script

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b2.1jpp1.7
- converted from JPackage by jppimport script

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b2.1jpp1.7
- converted from JPackage by jppimport script

* Thu Jul 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b2.1jpp1.7
- converted from JPackage by jppimport script

