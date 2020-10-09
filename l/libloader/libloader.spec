Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: libloader
Version: 1.1.3
Release: alt1_21jpp8
Summary: Resource Loading Framework
License: LGPLv2
#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant ant-contrib jpackage-utils
BuildRequires: libbase >= 1.1.3
Requires: jpackage-utils libbase >= 1.1.3
BuildArch: noarch
Patch0: libloader-1.1.2.build.patch
Source44: import.info

%description
LibLoader is a general purpose resource loading framework. It has been
designed to allow to load resources from any physical location and to
allow the processing of that content data in a generic way, totally
transparent to the user of that library.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
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
build-jar-repository -s -p lib libbase commons-logging-api
cd lib
ln -s /usr/share/java/ant ant-contrib

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
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_21jpp8
- update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_19jpp8
- fc update & java 8 build

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_16jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_5jpp7
- new version

