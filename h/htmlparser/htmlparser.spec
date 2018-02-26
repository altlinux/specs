Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
Name:		htmlparser
Version:	1.6
Release:	alt1_5.1jpp6
Summary:	HTML Parser, a Java library used to parse HTML
Group:		Development/Java
License:	LGPLv2+
URL:		http://htmlparser.sourceforge.net/
Source0:	http://downloads.sourceforge.net/htmlparser/htmlparser1_6_20060610.zip
BuildArch:	noarch

BuildRequires: jpackage-utils ant

Requires: jpackage-utils


%description
HTML Parser is a Java library used to parse HTML in either a linear or
nested fashion. Primarily used for transformation or extraction, it features
filters, visitors, custom tags and easy to use JavaBeans. It is a fast,
robust and well tested package.

%package	javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch
%description 	javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n htmlparser1_6

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;
%{__unzip} -qq src.zip


%build
export ANT_OPTS=" -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 "
ant jar
ant javadoc

%install

install -D lib/htmlparser.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -D lib/htmllexer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-lexer-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
	ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
	ln -s %{name}-lexer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/htmllexer.jar
popd


mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp docs/javadoc/ $RPM_BUILD_ROOT%{_javadocdir}/%{name}



%files
%doc license.txt readme.txt docs/articles docs/bug.html docs/changes.txt docs/contributors.html docs/faq.html docs/htmlparser.jpg docs/htmlparserlogo.jpg docs/index.html  docs/joinus.html docs/mailinglists.html docs/main.html docs/panel.html docs/pics docs/release.txt docs/samples.html docs/support.html docs/wiki
%{_javadir}/*



%files javadoc
%{_javadocdir}/*

%changelog
* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5.1jpp6
- new version

