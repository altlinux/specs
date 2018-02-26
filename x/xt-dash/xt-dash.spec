Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define base_name	xt

Name:		%{base_name}-dash
Version:	19991105
Release:	alt2_2jpp5
Epoch:		1
Summary:	Fast, free implementation of XSLT in Java
License:	BSD
Group:		Development/Java
URL:		http://www.blnz.com/xt/index.html
Source0:	http://www.blnz.com/xt/xt.zip
Source1:	xt-dash.build.script
Patch0:		xt-dash-java5-enum.patch
Patch1:         xt-dash.source.patch
Requires: servlet_2_3_api
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: servlet_2_3_api
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildArch:	noarch

%description
XT is an implementation in Java of XSL Transformations.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:	Demo for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Group:		Development/Java

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p0
rm com/jclark/xsl/dom/SunXMLProcessorImpl.java
find . -name "*.jar" | xargs -t rm
cp -a %{SOURCE1} build.xml

%build
export CLASSPATH=$(build-classpath servlet_2_3_api xerces-j2 xml-commons-jaxp-1.3-apis)
export OPT_JAR_LIST=:
ant jar
ant javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# data
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr demo $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc copying.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:19991105-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:19991105-alt1_2jpp5
- converted from JPackage by jppimport script

