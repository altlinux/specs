Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		jcharts
Version:	0.7.5
Release:	alt2_7jpp7
Summary:	A java based charts library

Group:		Publishing
License:	BSD
URL:		http://jcharts.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/jCharts-%{version}.zip
Patch1:		jcharts_remove_legacy.patch
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	batik
BuildRequires:	servlet25
Requires:	batik
Requires:	jpackage-utils
Requires:	servlet25
Source44: import.info


%description
jCharts is a 100%% Java based charting utility that outputs a variety 
of charts. This package has been designed from the ground up by 
volunteers for displaying charts via Servlets, JSP's, and Swing apps.

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description	javadoc
Javadoc for %{name}.

%prep
%setup -q -n jCharts-%{version}
%patch1
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
sed -i 's/\r//' docs/jCharts_license.txt

%build
export CLASSPATH=$(build-classpath batik/batik-svggen batik/batik-dom batik/batik-awt-util tomcat6-servlet-2.5-api)

cd build
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 jar javadocs -Dant.build.javac.source=1.4
cd ..

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/jCharts-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/
ln -sf %{_javadir}/jCharts-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

#javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc docs/README.html docs/jCharts_license.txt
%{_javadir}/%{name}.jar
%{_javadir}/jCharts-%{version}.jar

%files	javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.5-alt2_7jpp7
- fc version

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7.5-alt2_4jpp6
- add documentation

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.7.5-alt2_2jpp5
- fixed build with java 5

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.7.5-alt1_2jpp1.7
- converted from JPackage by jppimport script

