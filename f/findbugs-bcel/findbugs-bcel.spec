# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# This is a snapshot of the BCEL trunk for FindBugs 3.0.

%global findbugsver 20140707svn1547656

Name:           findbugs-bcel
Version:        6.0
Release:        alt1_0.6.20140707svn1547656jpp8
Summary:        Byte Code Engineering Library for FindBugs

Group:          Development/Other
License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-bcel/

# This archive was created with:
#   $ svn export http://svn.apache.org/repos/asf/commons/proper/bcel/trunk -r 1547656 bcel-6.0
#   $ tar -zcf bcel-20140707svn1547656.tgz bcel-6.0
Source0:        bcel-%{findbugsver}.tgz
Source1:        http://central.maven.org/maven2/com/google/code/findbugs/bcel-findbugs/%{version}/bcel-findbugs-%{version}.pom

BuildRequires:  javapackages-tools rpm-build-java
Requires:       javapackages-tools rpm-build-java

BuildArch:      noarch
Source44: import.info

%description
This is a snapshot of Apache's Byte Code Engineering Library (BCEL) for use
with FindBugs 3.0.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
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

