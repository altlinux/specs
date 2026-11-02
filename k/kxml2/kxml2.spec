%define _unpackaged_files_terminate_build 1

Name: kxml2
Version: 2.3.0
Release: alt1

Summary: Small XML pull parser with namespace and WBXML support
License: MIT
Group: Development/Java
Url: https://kxml.sourceforge.net/
VCS: :pserver:anonymous@kxml.cvs.sourceforge.net:/cvsroot/kxml

Source: %name-src-%version.zip
Source1: %name-%version.pom
Source2: build.gradle
Source3: settings.gradle
Source4: ParserCheck.java

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xpp3
BuildRequires: unzip

%description
kXML is a small XML pull parser with namespace and WBXML support. It uses
the system XML pull API supplied by xpp3.

%package javadoc
Summary: API documentation for kXML
Group: Development/Documentation

%description javadoc
API documentation for kXML.

%prep
%setup -q -c
cp %SOURCE1 pom.xml
cp %SOURCE2 build.gradle
cp %SOURCE3 settings.gradle

%build
%gradle_publish

%install
%gradle_register --artifacts=%name-%version
%gradle_register_javadoc --artifacts=%name-%version
%gradle_install

%check
%gradle_check
mkdir -p build/consumer
kxml_classpath=build/libs/%name-%version.jar:$(build-classpath xpp3)
javac -encoding UTF-8 -cp "$kxml_classpath" \
    -d build/consumer %SOURCE4
java -cp "build/consumer:$kxml_classpath" ParserCheck

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 2.3.0-alt1
- Initial build for ALT.
