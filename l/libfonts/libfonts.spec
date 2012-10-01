# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: libfonts
Version: 1.1.3
Release: alt1_8jpp7
Summary: TrueType Font Layouting
License: LGPLv2+
Group: System/Libraries
Source: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant ant-contrib ant-nodeps jpackage-utils libloader >= 1.1.3 itext-core
Requires: jpackage-utils libloader >= 1.1.3 itext-core
BuildArch: noarch
Patch0: libfonts-1.1.2.build.patch
Source44: import.info

%description
LibFonts is a library developed to support advanced layouting in JFreeReport.
This library allows to read TrueType-Font files to extract layouting specific
informations.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase commons-logging-api libloader itext
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
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_8jpp7
- new version

