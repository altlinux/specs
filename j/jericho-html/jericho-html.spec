Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jericho-html
Version:        3.3
Release:        alt1_9jpp8
Summary:        Java library allowing analysis and manipulation of parts of an HTML document
License:        EPL or LGPLv2+
URL:            http://jericho.htmlparser.net/
Source0:        http://downloads.sf.net/jerichohtml/%{name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
BuildRequires:  apache-commons-logging
BuildRequires:  log4j
BuildRequires:  slf4j
#For tests
BuildRequires:  junit
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
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
find \( -name '*.class' -o -name '*.[jw]ar' \) -exec rm -f '{}' +
find \( -name '*.java' -o -name '*.bat' -o -name '*.txt' -o -name '*.jsp' -o -name '*.css' -o -name '*.xml' \) -exec sed -i 's/\r//' '{}' +

# fix non ASCII chars
for s in src/java/net/htmlparser/jericho/Renderer.java \
 src/java/net/htmlparser/jericho/StreamEncodingDetector.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build
export CLASSPATH=$(build-classpath slf4j/api commons-logging log4j)

%javac -Xlint -g:none -d classes -encoding UTF-8 src/java/net/htmlparser/jericho/*.java src/java/net/htmlparser/jericho/nodoc/*.java
%jar -cf dist/%{name}.jar -C classes .

%javadoc -encoding UTF-8 -classpath classes:$CLASSPATH -quiet -Xdoclint:none -windowtitle "Jericho HTML Parser %version" -use -d docs/javadoc -subpackages net.htmlparser.jericho -exclude net.htmlparser.jericho.nodoc -noqualifier net.htmlparser.jericho -group "Core Package" src/java/net/htmlparser/jericho/*.java src/java/net/htmlparser/jericho/nodoc/*.java
cp -p docs/src/*.* docs/javadoc

%javac -Xlint -g -deprecation -classpath dist/%{name}.jar -d samples/console/classes samples/console/src/*.java


%install
%mvn_file net.htmlparser.jericho:%{name}:%{version} %{name}
%mvn_artifact net.htmlparser.jericho:%{name}:%{version} dist/%{name}.jar
%mvn_install -J docs/javadoc

# Install link for web app
ln -s %{_javadir}/%{name}.jar samples/webapps/JerichoHTML/WEB-INF/lib


%check
mkdir -p test/classes
export CLASSPATH=classes:samples/console/classes:$(build-classpath junit hamcrest)
%javac -Xlint -g -d test/classes test/src/*.java test/src/samples/*.java test/src/net/htmlparser/jericho/*.java
%java -classpath $CLASSPATH:test/classes -Djava.util.logging.config.file=test/logging.properties org.junit.runner.JUnitCore TestSuite


%files -f .mfiles
%doc licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt
%doc project-description.txt release.txt
#doc samples

%files javadoc -f .mfiles-javadoc
%doc licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_9jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_7jpp8
- java8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_6jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_4jpp7
- new version

