Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# This is a snapshot of the BCEL trunk for FindBugs 3.0.

%global findbugsver 20140707svn1547656

Name:           findbugs-bcel
Version:        6.0
Release:        alt1_0.11.20140707svn1547656jpp8
Summary:        Byte Code Engineering Library for FindBugs

License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-bcel/

# This archive was created with:
#   $ svn export http://svn.apache.org/repos/asf/commons/proper/bcel/trunk -r 1547656 bcel-6.0
#   $ tar -zcf bcel-20140707svn1547656.tgz bcel-6.0
Source0:        bcel-%{findbugsver}.tgz
Source1:        http://central.maven.org/maven2/com/google/code/findbugs/bcel-findbugs/%{version}/bcel-findbugs-%{version}.pom

# Add temporary dependency on javapackages-local, for %%add_maven_depmap macro
# See https://lists.fedoraproject.org/archives/list/java-devel@lists.fedoraproject.org/thread/R3KZ7VI5DPCMCELFIVJQ4AXB2WQED35C/
BuildRequires:  javapackages-local

BuildRequires:  java-devel jpackage-utils
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
This is a snapshot of Apache's Byte Code Engineering Library (BCEL) for use
with FindBugs 3.0.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n bcel-%{version}

%build
mkdir classes
find src/main/java -type f -name '*.java' | \
xargs javac -g -d classes -source 1.5 -encoding ISO8859-1
cd classes
jar cf findbugs-bcel.jar org
cd ..

mkdir javadoc
find src/main/java -type f -name '*.java' | xargs javadoc -sourcepath src/main/java \
  -classpath classes -source 1.5 -encoding ISO8859-1 -d javadoc -Xdoclint:none

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p classes/findbugs-bcel.jar $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "com.google.code.findbugs:bcel"

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a javadoc $RPM_BUILD_ROOT%{_javadocdir}/findbugs-bcel

# set_javadoc_namelink_check
%pre javadoc
path = "%{_javadocdir}/%{name}"
if [ -L $path ]; then
  rm -f $path
fi ||:



%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/findbugs-bcel*

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 6.0-alt1_0.11.20140707svn1547656jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 6.0-alt1_0.10.20140707svn1547656jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 6.0-alt1_0.7.20140707svn1547656jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 6.0-alt1_0.6.20140707svn1547656jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 6.0-alt1_0.5.20140707svn1547656jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 5.2-alt3_1.3.8.8jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt3_1.3.8.7jpp7
- new fc release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_1.3.8.7jpp7
- new fc release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_1.3.8.7jpp7
- new version

