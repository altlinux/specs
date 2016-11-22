# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define origname libxml

Name: pentaho-libxml
Version: 1.1.3
Release: alt1_14jpp8
Summary: Namespace aware SAX-Parser utility library
License: LGPLv2
Group: System/Libraries
#Original source: http://downloads.sourceforge.net/jfreereport/%%{origname}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{origname}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant ant-contrib javapackages-tools rpm-build-java libbase libloader
Requires: javapackages-tools rpm-build-java libbase >= 1.1.2 libloader >= 1.1.2
BuildArch: noarch
Patch0: libxml-1.1.2-build.patch
Source44: import.info

%description
Pentaho LibXML is a namespace aware SAX-Parser utility library. It eases the
pain of implementing non-trivial SAX input handlers.

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
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase libloader
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
cp -p ./dist/%{origname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{origname}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{origname}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{origname}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{origname}.jar

%files javadoc
%{_javadocdir}/%{origname}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_5jpp7
- new version

