# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Use rpmbuild --without gcj to disable native bits
%global with_gcj %{!?_without_gcj:1}%{?_without_gcj:0}

Name: flute
Version: 1.3.0
Release: alt1_6.OOo31jpp6
Summary: Java CSS parser using SAC
# The entire source code is W3C except ParseException.java which is LGPLv2+
License: W3C and LGPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant jpackage-utils sac
Requires: jpackage-utils sac
%if %{with_gcj}
BuildRequires: java-gcj-compat-devel >= 1.0.31
Requires(post): java-gcj-compat >= 1.0.31
Requires(postun): java-gcj-compat >= 1.0.31
%else
BuildArch: noarch
%endif
Source44: import.info

%description
A Cascading Style Sheets parser using the Simple API for CSS, for Java.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
%if %{with_gcj}
BuildArch: noarch
%endif

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib sac

%build
ant jar javadoc

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%if %{with_gcj}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc COPYRIGHT.html
%{_javadir}/*.jar
%if %{with_gcj}
%{_libdir}/gcj/%{name}
%endif

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_6.OOo31jpp6
- new version

