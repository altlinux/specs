Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global beta_number b3

Summary:        Collection of tasks for Ant
Name:           ant-contrib
Version:        1.0
Release:        alt5_0.20.b3jpp7
License:        ASL 2.0 and ASL 1.1
URL:            http://ant-contrib.sourceforge.net/
Group:          Development/Java
Source0:        https://downloads.sourceforge.net/project/ant-contrib/ant-contrib/1.0b3/ant-contrib-1.0b3-src.tar.bz2
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/1.0b3/%{name}-1.0b3.pom
# ASL 2.0 Licence text
# Upstream bug at https://sourceforge.net/tracker/?func=detail&aid=3590371&group_id=36177&atid=416920
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         local-ivy.patch
Patch2:         %{name}-antservertest.patch
Patch3:         %{name}-pom.patch
BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  junit >= 3.8.0
BuildRequires:  ant-junit >= 1.6.2
BuildRequires:  xerces-j2
BuildRequires:  bcel >= 5.0
BuildRequires:  apache-ivy
Requires:       junit >= 3.8.0
Requires:       ant >= 1.6.2
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
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
Api documentation for %%{name}.

%prep
%setup -q  -n %{name}
%patch0 -b .sav
%patch2

cp %{SOURCE1} %{name}-1.0b3.pom
%patch3 -p1

cp %{SOURCE2} LICENSE-2.0.txt

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

sed -i "s|xercesImpl|xerces-j2|g" ivy.xml
# needs porting to latest ivy
rm -fr src/java/net/sf/antcontrib/net/URLImportTask.java

%build
ant dist

%install
# jars
install -Dpm 644 target/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/ant/%{name}.jar

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "ant/ant-contrib" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/ant-contrib

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{name}-1.0b3.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.ant-%{name}.pom

%add_maven_depmap JPP.ant-%{name}.pom ant/%{name}.jar
# jpp compat symlink
ln -s ant/ant-contrib.jar %buildroot%_javadir/ant-contrib.jar

%files
%{_sysconfdir}/ant.d/ant-contrib
%{_javadir}/ant/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc target/docs/LICENSE.txt LICENSE-2.0.txt
%doc target/docs/manual/tasks/*
%_javadir/ant-contrib.jar

%files javadoc
%doc target/docs/LICENSE.txt LICENSE-2.0.txt
%doc %{_javadocdir}/%{name}

%changelog
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

