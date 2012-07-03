# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: ant-antlr3
Version: 20110110
Release: alt1_4jpp7
Summary: Antlr3 task for Ant
Group: Development/Java
License: ASL 2.0
URL: http://antlr.org/
# Repackaged until rhbz#699529 RPM fix takes place in Fedora.
# RPM cannot read the upstream zip file.
# wget http://antlr.org/share/1169924912745/antlr3-task.zip
# unzip antlr3-task.zip
# rm antlr3-task.zip
# zip antlr3-task -r antlr3-task/
Source0: antlr3-task.zip
#Source0: http://antlr.org/share/1169924912745/antlr3-task.zip
BuildRequires: jpackage-utils
BuildRequires: ant
Requires: jpackage-utils
Requires: ant
BuildArch: noarch
Source44: import.info

%description
Antlr3 task for Ant.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
BuildArch: noarch
Requires: jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n antlr3-task
rm -f ant-antlr3.jar

%build
export CLASSPATH=`build-classpath ant`
javac -encoding utf-8 antlr3-src/src/org/apache/tools/ant/antlr/ANTLR3.java
jar cvf ant-antlr3.jar -C antlr3-src/src org/apache/tools/ant/antlr/antlib.xml -C antlr3-src/src org/apache/tools/ant/antlr/ANTLR3.class
javadoc -encoding utf-8 -d antlr3-src/javadoc -sourcepath antlr3-src/src -subpackages java:org.apache.tools.ant.antlr

# Sanitize line endings
find examples Readme.txt -type f -print0 | xargs -0 -e sed -i 's/\r//'
# Remove zero length Java properties files
find examples -size 0 -name \*.properties -print0 | xargs -0 -e rm -f

%install
install -m 644 ant-antlr3.jar -D $RPM_BUILD_ROOT%{_javadir}/ant/ant-antlr3.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/ant-antlr3
cp -rf antlr3-src/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/ant-antlr3

# /etc/ant.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/ant-antlr3 << EOF
ant/ant-antlr3 antlr3
EOF

%files
%doc Readme.txt examples
%{_javadir}/ant/ant-antlr3.jar
%config(noreplace) %{_sysconfdir}/ant.d/ant-antlr3

%files javadoc
%{_javadocdir}/ant-antlr3

%changelog
* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 20110110-alt1_4jpp7
- new version

