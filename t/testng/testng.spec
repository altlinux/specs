Epoch: 0
BuildRequires: oss-parent
Requires: oss-parent
BuildRequires: /proc
BuildRequires: jpackage-compat

%global group_id  org.testng

Name:             testng
Version:          6.0.1
Release:          alt2_1jpp7
Summary:          Java-based testing framework
License:          ASL 2.0
Group:            Development/Java
URL:              http://testng.org/
# git clone git://github.com/cbeust/testng.git
# cd testng
# git archive --prefix="testng-6.0.1/" --format=tar testng-6.0.1 | xz > testng-6.0.1.tar.xz
Source0:          %{name}-%{version}.tar.xz
Source1:          %{name}.depmap

Patch0:           %{name}-test-fails-workaround.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    beust-jcommander
BuildRequires:    snakeyaml

Requires:         beust-jcommander
Requires:         snakeyaml
Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
TestNG is a testing framework inspired from JUnit and NUnit but introducing
some new functionality, including flexible test configuration, and
distributed test running.  It is designed to cover unit tests as well as
functional, end-to-end, integration, etc.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%patch0 -p1

# remove bundled stuff
rm -rf spring
rm -rf 3rdparty
rm -rf doc
rm -rf lib-supplied
rm -rf gigaspaces
rm -rf sandbox
rm -rf examples
rm -f *.jar


# fix the ant group_id ... ant -> org.apache.ant
sed -i 's/<groupId>ant/<groupId>org.apache.ant/g' pom.xml

# replace CR+LF with LF
sed -i 's/\r//g' README

# convert to UTF8

#$ enca CHANGES.txt
#Unrecognized encoding
#$ enca ANNOUNCEMENT.txt
#Unrecognized encoding

#$ chardet-file ANNOUNCEMENT.txt
#{'confidence': 0.8484260688832136, 'encoding': 'ISO-8859-2'}
#$ chardet-file CHANGES.txt
#{'confidence': 0.7833420201466339, 'encoding': 'ISO-8859-2'}

iconv --from-code=ISO-8859-2 --to-code=UTF-8 ANNOUNCEMENT.txt > ANNOUNCEMENT.txt.utf8
mv -f ANNOUNCEMENT.txt.utf8 ANNOUNCEMENT.txt
iconv --from-code=ISO-8859-2 --to-code=UTF-8 CHANGES.txt > CHANGES.txt.utf8
mv -f CHANGES.txt.utf8 CHANGES.txt

%build
# gdata-java has no maven support -> depmap file needed
# http://code.google.com/p/gdata-java-client/issues/detail?id=328
mvn-rpmbuild -Dmaven.local.depmap.file="%{SOURCE1}" -Dgpg.skip=true install javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap %{group_id} %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt ANNOUNCEMENT.txt CHANGES.txt README
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt2_1jpp7
- added oss-parent pom dependency

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt1_1jpp7
- new version

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt2_2jpp6
- fixed build

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt1_2jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt4_1jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt1_1jpp5
- converted from JPackage by jppimport script

