# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name: libfonts
Version: 1.1.3
Release: alt1_18jpp8
Summary: TrueType Font Layouting
License: LGPLv2 and UCD
Group: System/Libraries
#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant ant-contrib javapackages-tools rpm-build-java libloader >= 1.1.3
Requires: javapackages-tools rpm-build-java libloader >= 1.1.3
BuildArch: noarch
Patch0: libfonts-1.1.2.build.patch
Source44: import.info

%description
LibFonts is a library developed to support advanced layouting in JFreeReport.
This library allows to read TrueType-Font files to extract layouting specific
informations.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
Requires: %{name} = %{version}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
find . -name "*.jar" -exec rm -f {} \;
rm -r source/org/pentaho/reporting/libraries/fonts/itext
mkdir -p lib
build-jar-repository -s -p lib libbase commons-logging-api libloader
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_18jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_17jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_10jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_8jpp7
- new version

