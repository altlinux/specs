Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# If you do not want wengsoft-SNMP support, give rpmbuild option '--without nonfree'
%define with_nonfree 0
%define without_nonfree 1
%define name		snmptrapappender
%define version		1.2.9

Summary:	SNMP Trap Appender extension for log4j
URL:		http://www.m2technologies.net/asp/snmpTrapAppender.asp
Source0:	http://www.m2technologies.net/bin/snmptrapappender-1.2.9.tar.bz2
Source1:	snmpTrapAppender_build.xml
#Patch0:		snmpTrapAppender_1_2_8.patch

Name:		%{name}
Version:	%{version}
Release:	alt2_0jpp5
Epoch:		0
License:	Open Source
Group:		Development/Java
BuildArch:	noarch
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant >= 0:1.6.1
BuildRequires: joesnmp >= 0:0.3.2
BuildRequires: log4j >= 0:1.2.8
%if %{with_nonfree}
BuildRequires: wengsoftsnmp
%endif
Requires: jpackage-utils >= 0:1.5
Requires: joesnmp >= 0:0.3.2
Requires: log4j >= 0:1.2.8
%if %{with_nonfree}
Requires: wengsoftsnmp
%endif

%description
An appender to send formatted logging event strings to a 
specified managment host (typically, a MLM of some sort, 
but could also be an SNMP management console) in the form 
of an SNMP trap. 
This appender does not attempt to provide full access to the 
SNMP API. In particular, use of this appender does not make 
an SNMP agent out of the calling application. You cannot use 
this appender as an interface to do SNMP GET or SET calls -- 
all it does is pass on your logging event as a TRAP.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} build.xml
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;
%if %{without_nonfree}
  rm -f src/org/apache/log4j/ext/WengsoftSNMPTrapSender.java
%endif

# Fix package name
#%patch0

%build
%if %{without_nonfree}
export CLASSPATH=$(build-classpath \
joesnmp \
log4j \
)
%else
export CLASSPATH=$(build-classpath \
joesnmp \
log4j \
wengsoftsnmp \
)
%endif
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 dist javadoc

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 dist/lib/snmpTrapAppender-%{version}.jar \
                   $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt2_0jpp5
- fixes for java 5

* Thu Jul 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt1_0jpp5
- based on jpackage 1.6 spec

* Thu May 05 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.9-alt1
- Initial build for ALT Linux Sisyphus

