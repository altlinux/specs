# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           beansbinding
Version:        1.2.1
Release:        alt1_15jpp8
Summary:        Beans Binding (JSR 295) reference implementation

Group:          Development/Other
License:        LGPLv2+
URL:            https://beansbinding.dev.java.net/
Source0:        https://beansbinding.dev.java.net/files/documents/6779/73673/beansbinding-1.2.1-src.zip
Patch0:         disable-doclint.patch

BuildRequires:  ant
BuildRequires:  ant-junit


BuildArch:      noarch
Source44: import.info

%description
In essence, Beans Binding (JSR 295) is about keeping two properties 
(typically of two objects) in sync. An additional emphasis is placed 
on the ability to bind to Swing components, and easy integration with 
IDEs such as NetBeans. This project provides the reference implementation.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p1
# remove all binary libs
find . -type f \( -iname "*.jar" -o -iname "*.zip" \) -print0 | xargs -t -0 %{__rm} -f

%build
%{ant} dist

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc license.txt releaseNotes.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_9jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_8jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_7jpp7
- update to new release by jppimport

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_5jpp6
- new build for netbeans

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3jpp6
- converted from JPackage by jppimport script

