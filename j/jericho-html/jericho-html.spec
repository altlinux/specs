# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jericho-html
Version:        3.2
Release:        alt1_6jpp7
Summary:        Java library allowing analysis and manipulation of parts of an HTML document

Group:          Development/Java
License:        EPL or LGPLv2+
URL:            http://jericho.htmlparser.net/
Source0:        http://downloads.sf.net/jerichohtml/%{name}-%{version}.zip
BuildArch:      noarch
ExcludeArch:    ppc64

BuildRequires:  jpackage-utils
BuildRequires:  jakarta-commons-logging
BuildRequires:  log4j
BuildRequires:  slf4j
#For tests
BuildRequires:  junit4
Requires:       jpackage-utils
Source44: import.info


%description
Jericho HTML Parser is a java library allowing analysis and manipulation of
parts of an HTML document, including server-side tags, while reproducing
verbatim any unrecognized or invalid HTML. It also provides high-level HTML
form manipulation functions.

It is an open source library released under both the Eclipse Public License
(EPL) and GNU Lesser General Public License (LGPL). You are therefore free to
use it in commercial applications subject to the terms detailed in either one
of these license documents. 


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
find \( -name '*.class' -o -name '*.[jw]ar' \) -exec rm -f '{}' +
find \( -name '*.java' -o -name '*.bat' -o -name '*.txt' -o -name '*.jsp' -o -name '*.css' -o -name '*.xml' \) -exec sed -i 's/\r//' '{}' +


%build
export CLASSPATH=$(build-classpath slf4j/api commons-logging log4j)

javac -Xlint -g:none -d classes -encoding Windows-1252 src/java/net/htmlparser/jericho/*.java src/java/net/htmlparser/jericho/nodoc/*.java
jar -cf dist/%{name}-%{version}.jar -C classes .

javadoc -encoding Windows-1252 -quiet -windowtitle "Jericho HTML Parser %version" -use -d docs/javadoc -subpackages net.htmlparser.jericho -exclude net.htmlparser.jericho.nodoc -noqualifier net.htmlparser.jericho -group "Core Package" src/java/net/htmlparser/jericho/*.java src/java/net/htmlparser/jericho/nodoc/*.java
cat docs/src/append/stylesheet.css >> docs/javadoc/stylesheet.css
cp docs/src/replace/*.* docs/javadoc

javac -Xlint -g -deprecation -classpath dist/%{name}-%{version}.jar -d samples/console/classes samples/console/src/*.java


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp docs/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# Install link for web app
#ln -s %{_javadir}/%{name}-%{version}.jar samples/webapps/JerichoHTML/WEB-INF/lib


%check
rm -rf test/classes
mkdir -p test/classes
export CLASSPATH=classes:samples/console/classes:$(build-classpath junit4.jar)
javac -Xlint -g -d test/classes test/src/*.java test/src/samples/*.java test/src/net/htmlparser/jericho/*.java
java -classpath $CLASSPATH:test/classes -Djava.util.logging.config.file=test/logging.properties org.junit.runner.JUnitCore TestSuite


%files
%doc licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt
%doc project-description.txt release.txt
%doc --no-dereference samples
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%doc licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt
%{_javadocdir}/%{name}


%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_6jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_4jpp7
- new version

