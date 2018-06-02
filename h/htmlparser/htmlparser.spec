# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		htmlparser
Epoch:		1
Version:	1.5
Release:	alt1_8jpp8
Summary:	HTML Parser, a Java library used to parse HTML
Group:		Development/Java
License:	LGPLv2+
URL:		http://htmlparser.sourceforge.net/
Source0:	http://downloads.sourceforge.net/htmlparser/htmlparser1_5_20050614.zip
Patch1:         htmlparser-build.patch
BuildArch:	noarch

BuildRequires:	java-devel >= 1.6.0
BuildRequires:	jpackage-utils ant

Requires:	jpackage-utils
Source44: import.info

%description
HTML Parser is a Java library used to parse HTML in either a linear or
nested fashion. Primarily used for transformation or extraction, it features
filters, visitors, custom tags and easy to use JavaBeans. It is a fast,
robust and well tested package.

%package	javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch
%description 	javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n htmlparser1_5

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;
unzip -qq src.zip
%patch1 -p1


%build
export ANT_OPTS=" -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 "
ant jar
ant javadoc

%install
install -D lib/htmlparser.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D lib/htmllexer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-lexer.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp docs/javadoc/ $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc license.txt readme.txt docs/articles docs/bug.html docs/changes.txt docs/contributors.html docs/htmlparser.jpg docs/htmlparserlogo.jpg docs/index.html  docs/joinus.html docs/mailinglists.html docs/main.html docs/panel.html docs/pics docs/release.txt docs/samples.html docs/support.html docs/wiki
%{_javadir}/*


%files javadoc
%{_javadocdir}/*

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_8jpp8
- java fc28+ update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_7jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_5jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_3jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_11jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_10jpp7
- fc update

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5.1jpp6
- new version

