Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%def_with repolib
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: jcommon
Version: 1.0.18
Release: alt1_1jpp7
Summary: JFree Java utility classes
License: LGPLv2+
Group: System/Libraries
Source: http://downloads.sourceforge.net/jfreechart/%%{name}-%%{version}.tar.gz
Source2: bnd.properties
URL: http://www.jfree.org/jcommon
BuildRequires: ant jpackage-utils
# Required for converting jars to OSGi bundles
BuildRequires:  aqute-bnd
Requires: jpackage-utils
BuildArch: noarch
Source44: import.info

%description
JCommon is a collection of useful classes used by 
JFreeChart, JFreeReport and other projects.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %%{name}.


%description javadoc -l fr
Javadoc pour %{name}.

%package xml
Summary: JFree XML utility classes
Group: System/Libraries
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: jpackage-utils

%description xml
Optional XML utility classes.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;

%build
pushd ant
ant compile compile-xml javadoc
popd
# Convert to OSGi bundle
java -Djcommon.bundle.version="%{version}" \
     -jar $(build-classpath aqute-bnd) wrap -output %{name}-%{version}.bar -properties %{SOURCE2} %{name}-%{version}.jar

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}-%{version}.bar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p %{name}-xml-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-xml.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc licence-LGPL.txt README.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}.jar

%files xml
%{_javadir}/%{name}-xml.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.18-alt1_1jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.17-alt1_4jpp7
- new version

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.16-alt2_2jpp6
- enabled repolib

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.16-alt1_2jpp6
- added pom

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt2_3jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt1_2jpp5
- converted from JPackage by jppimport script

* Fri Jun 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.0-alt0.1pre2
- First build for ALTLinux
