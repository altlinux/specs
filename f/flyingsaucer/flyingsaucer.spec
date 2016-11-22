Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          flyingsaucer
Version:       8
Release:       alt1_13jpp8
Summary:       XML/XHTML and CSS 2.1 renderer in pure Java
# licensed under CC-BY-SA: demos/svg/xhtml/dat/*.svg
License:       LGPLv2+ and CC-BY-SA
URL:           https://github.com/flyingsaucerproject/flyingsaucer
Source0:       http://flying-saucer.googlecode.com/files/%{name}-R%{version}-src.zip
Source1:       http://repo1.maven.org/maven2/org/xhtmlrenderer/core-renderer/R%{version}/core-renderer-R%{version}.pom
# remove Pack200Task.jar references
# add system itext svgsalamander xml-commons-apis
Patch0:        %{name}-R%{version}-build.patch
# fix xml-apis groupId version
# remove org.jvnet.wagon-svn wagon-svn 1.8
Patch1:        %{name}-R%{version}-pom.patch

BuildRequires: javapackages-local

BuildRequires: ant
# main
BuildRequires: itext-core
BuildRequires: xml-commons-apis
# optional for svg demo
BuildRequires: svgsalamander

Provides:      xhtmlrenderer = %{version}-%{release}
BuildArch:     noarch
Source44: import.info

%description
An XML/XHTML CSS 2.1 Renderer library in pure Java
for rendering to PDF, images, and Swing panels.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package demos
Group: Development/Java
Summary:       Demostrations and samples for %{name}
Requires:      %{name} = %{version}

%description demos
This package contains demostrations and samples for %{name}.

%prep
%setup -q -c

find -name '*.class' -delete
find -name '*.dll' -delete
find -name '*.exe' -delete
find -name '*.jar' -delete

# file non free licensed
# under CC-2.5
rm -rf demos/browser/xhtml/recipebook-xml.css
# under CC-BY-NC-SA
rm -rf demos/svg/xhtml/dat/face-crying.svg
rm -rf demos/svg/xhtml/dat/face-sad.svg
# unclear license, unimportant file anyway
rm -rf demos/docbook/xml/plugin-implement.xml

%patch0 -p1
cp -p %{SOURCE1} pom.xml
%patch1 -p0

iconv -f iso8859-1 -t utf-8 LICENSE-W3C-TEST > LICENSE-W3C-TEST.conv && mv -f LICENSE-W3C-TEST.conv LICENSE-W3C-TEST
sed -i 's/\r//' LICENSE-W3C-TEST

sed -i '/Class-Path/d' src/packaging/manifest

# requires
# lib/xml-apis-xerces-2.9.1.jar x
# lib/iText-2.0.8.jar x
# optionals
# lib/dev/antlrall.jar x
# lib/dev/bsh-core-2.0b4.jar x
# lib/dev/jsch-20060408.jar x
# lib/dev/jsyntaxpane-0.9.4.jar x
# lib/dev/junit.jar x
# lib/dev/looks-2.1.4.jar x
# lib/dev/PDFRenderer.jar x
# lib/dev/Piccolo.jar x
# lib/dev/svgSalamander.jar x
# lib/dev/tagsoup-1.1.3.jar x
# lib/dev/Tidy.jar x
# lib/dev/xilize-engine.jar x

# lib/dev/java2html.jar !
# lib/dev/javasrc.jar !?
# lib/dev/Pack200Task.jar !
# lib/dev/jdic_win_30092005/jdic_30092005.jar !

sed -i 's|<property name="compiler.source" value="1.4"/>|<property name="compiler.source" value="1.6"/>|' \
  etc/build/properties.xml
sed -i 's|<property name="compiler.target" value="1.4"/>|<property name="compiler.target" value="1.6"/>|' \
  etc/build/properties.xml
  
%build

# test skipped requires X11 DISPLAY variable set
%ant jar docs
# test

%install
%mvn_artifact pom.xml build/core-renderer.jar
%mvn_install -J doc/full/api


install -pm 644 build/core-renderer-minimal.jar %{buildroot}%{_javadir}/%{name}/

(
  cd %{buildroot}%{_javadir}/%{name}
  ln -sf core-renderer.jar xhtmlrenderer.jar
)

# demo
install -pm 644 build/aboutbox.jar %{buildroot}%{_javadir}/%{name}/
install -pm 644 build/browser.jar %{buildroot}%{_javadir}/%{name}/
install -pm 644 build/docbook.jar %{buildroot}%{_javadir}/%{name}/
install -pm 644 build/svg.jar %{buildroot}%{_javadir}/%{name}/

%files -f .mfiles
%{_javadir}/%{name}/core-renderer-minimal.jar
%{_javadir}/%{name}/xhtmlrenderer.jar
%doc README
%doc LICENSE*

%files demos
%{_javadir}/%{name}/aboutbox.jar
%{_javadir}/%{name}/browser.jar
%{_javadir}/%{name}/docbook.jar
%{_javadir}/%{name}/svg.jar
%doc LICENSE*

%files javadoc -f .mfiles-javadoc
%doc LICENSE*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt1_13jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt1_11jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 8-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 8-alt1_5jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 8-alt1_4jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_3jpp7
- new version

