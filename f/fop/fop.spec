Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:	XSL-driven print formatter
Name:		fop
Version:	1.1
Release:	alt1_1jpp7
License:	ASL 2.0
Group:		Text tools
URL:		http://xmlgraphics.apache.org/fop
# wget http://www.apache.org/dist/xmlgraphics/fop/source/%{name}-%{version}-src.tar.gz
# tar xzvf fop-%{version}-src.tar.gz
# find ./fop-%{version}/src/java/org/apache/fop/pdf/ -name "*.icm*" -delete
# find ./fop-%{version}/ -name "*.jar" -delete
# find ./fop-%{version}/ -name "*.pdf" -delete
# we don't run tests, we don't need test data
# find ./fop-%{version}/ -name "*.ser" -delete
# tar czvf fop-%{version}-src.tar.gz fop-%{version}
Source0:	%{name}-%{version}-src.tar.gz
Source1:	%{name}.script
Source2:	batik-pdf-MANIFEST.MF
Source3:	http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/xmlgraphics/%{name}/%{version}/%{name}-%{version}.pom
Patch0:		%{name}-main.patch
Patch1:		%{name}-Use-sRGB.icc-color-profile-from-icc-profiles-openicc.patch
BuildArch:  noarch
Requires:	xmlgraphics-commons >= 1.5
Requires:	avalon-framework >= 4.1.4
Requires:	batik >= 1.7
Requires:	xalan-j2 >= 2.7.0
Requires:	xml-commons-apis >= 1.3.04
Requires:	jakarta-commons-httpclient
Requires:	apache-commons-io >= 1.2
Requires:	apache-commons-logging >= 1.0.4
Requires:	icc-profiles-openicc
Requires:   jpackage-utils

Requires(post): jpackage-utils
Requires(postun): jpackage-utils

BuildRequires:	ant
BuildRequires:	java-javadoc >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	apache-commons-logging
BuildRequires:	apache-commons-io
BuildRequires:	avalon-framework
BuildRequires:	xmlgraphics-commons >= 1.5
BuildRequires:	batik
BuildRequires:	servlet
BuildRequires:	qdox
BuildRequires:	xmlunit
BuildRequires:	zip
BuildRequires:	junit
Source44: import.info

Provides: xmlgraphics-fop = %{epoch}:%version-%release
Obsoletes: xmlgraphics-fop <= 0:1.0-alt3_4jpp6
Conflicts: xmlgraphics-fop <= 0:1.0-alt3_4jpp6

%description
FOP is the world's first print formatter driven by XSL formatting
objects. It is a Java application that reads a formatting object tree
and then turns it into a PDF document. The formatting object tree, can
be in the form of an XML document (output by an XSLT engine like XT or
Xalan) or can be passed in memory as a DOM Document or (in the case of
XT) SAX events.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

sed -i -e "s|1.4|1.5|g" build.xml

#upstream workaround -- many thanks to spepping@apache.org -- see https://issues.apache.org/bugzilla/show_bug.cgi?id=50575
ln -s %{_javadir}/qdox.jar lib/build/qdox.jar

%build
#qdox intentionally left off classpath -- see https://issues.apache.org/bugzilla/show_bug.cgi?id=50575
export CLASSPATH=$(build-classpath apache-commons-logging apache-commons-io xmlgraphics-commons batik-all avalon-framework-api avalon-framework-impl servlet batik/batik-svg-dom xml-commons-apis xml-commons-apis-ext objectweb-asm/asm-all xmlunit)
ant jar-main transcoder-pkg javadocs

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/%{name}.jar META-INF/MANIFEST.MF

# jars
mkdir -p %{buildroot}%{_javadir}
cp -a build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
cp -a build/%{name}-transcoder.jar %{buildroot}%{_javadir}/pdf-transcoder.jar

# script
mkdir -p %{buildroot}%{_bindir}
cp -a %{SOURCE1} %{buildroot}%{_bindir}/fop

# data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a conf %{buildroot}%{_datadir}/%{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a build/javadocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.apache.xmlgraphics %{name} %{version} JPP %{name} %{version}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/fop.conf`
touch $RPM_BUILD_ROOT/etc/fop.conf

# xmlgraphics-fop compat symlinks
ln -s fop.jar %buildroot%_javadir/xmlgraphics-fop.jar
ln -s fop %buildroot%_bindir/xmlgraphics-fop

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE README NOTICE
%{_javadir}/%{name}.jar
%{_datadir}/%{name}
%{_javadir}/pdf-transcoder.jar
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*pom
%attr(0755,root,root) %{_bindir}/fop
%config(noreplace,missingok) /etc/fop.conf
# compat symlinks
%_javadir/xmlgraphics-fop.jar
%_bindir/xmlgraphics-fop

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE


%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp7
- new version

* Sun Mar 31 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_20jpp7
- fc update

* Sat Oct 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp6
- fixed classpath for new batik

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp6
- fixed build w/new batik

* Sun Jan 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp6
- new jpp relase

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt5_6jpp6
- added commons-logging to the classpath

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt4_6jpp6
- add xmlgraphics-commons to classpath

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_6jpp6
- added OSGi provides

* Thu May 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_6jpp5
- new jpp release

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_5jpp5
- obsoletes fop 0.20.5

* Tue Oct 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt2_5jpp5
- fixed #17536

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt1_5jpp5
- added config

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt1_4jpp5
- converted from JPackage by jppimport script

