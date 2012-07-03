# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define _without_gcj 1
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           swing-layout
Version:        1.0.4
Release:        alt1_4jpp7
Summary:        Natural layout for Swing panels

Group:          Development/Java
License:        LGPLv2
URL:            https://swing-layout.dev.java.net/
# Need to register to download, from url above
Source0:        %{name}-%{version}-src.zip

BuildRequires:  jpackage-utils >= 1.6
BuildRequires:  ant
BuildRequires:  dos2unix

BuildArch:      noarch
Source44: import.info

%description
Extensions to Swing to create professional cross platform layout.

%package javadoc
Summary:        Javadoc documentation for Swing Layout
Group:          Development/Java
BuildArch: noarch

%description javadoc
Documentation for Swing Layout code.


%prep
%setup -q
dos2unix releaseNotes.txt


%build
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc dist


%install
install -d $RPM_BUILD_ROOT%{_javadir} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%files
%{_javadir}/%{name}*.jar
%doc releaseNotes.txt


%files javadoc
%{_javadocdir}/%{name}-%{version}


%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_4jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp6
- update to new release by jppimport

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp6
- new build for netbeans

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp5
- converted from JPackage by jppimport script

