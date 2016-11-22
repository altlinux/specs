# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name sblim-cim-client2
%define version 2.2.5

%global project_folder %{name}-%{version}-src
%global archive_folder build

Name:           sblim-cim-client2
Version:        2.2.5
Release:        alt1_5jpp8
Summary:        Java CIM Client library

Group:          Development/Other
License:        EPL
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}-src.zip

BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant >= 0:1.6

Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
The purpose of this package is to provide a CIM Client Class Library for Java
applications. It complies to the DMTF standard CIM Operations over HTTP and
intends to be compatible with JCP JSR48 once it becomes available. To learn
more about DMTF visit http://www.dmtf.org.
More infos about the Java Community Process and JSR48 can be found at
http://www.jcp.org and http://www.jcp.org/en/jsr/detail?id=48.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       sblim-cim-client2 = %{version}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual and sample code for %{name}
Group:          Development/Java
Requires:       sblim-cim-client2 = %{version}
BuildArch: noarch

%description manual
Manual and sample code for %{name}.


%prep
%setup -q -n %{project_folder}

dos2unixConversion() {
        fileName=$1
        %{__sed} -i 's/\r//g' "$fileName"
}

dosFiles2unix() {
        fileList=$1
        for fileName in $fileList; do
                dos2unixConversion $fileName
        done
}

dosFiles2unix 'ChangeLog NEWS README COPYING sblim-cim-client2.properties sblim-slp-client2.properties'
dosFiles2unix 'smpl/org/sblim/slp/example/*'
dosFiles2unix 'smpl/org/sblim/cimclient/samples/*'

%build
export ANT_OPTS="-Xmx256m"
ant \
        -Dbuild.compiler=modern \
        -DManifest.version=%{version}\
        package java-doc


%install
# --- documentation ---
dstDocDir=$RPM_BUILD_ROOT%{_docdir}/%{name}
install -d $dstDocDir
install --mode=644 ChangeLog COPYING README NEWS $dstDocDir
# --- samples (also into _docdir) ---
cp -pr  smpl/org $dstDocDir
# --- config files ---
confDir=$RPM_BUILD_ROOT%{_sysconfdir}/java
install -d $confDir
install --mode=664 sblim-cim-client2.properties sblim-slp-client2.properties $confDir
# --- jar ---
install -d $RPM_BUILD_ROOT%{_javadir}
install %{archive_folder}/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
# --- javadoc ---
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr %{archive_folder}/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%dir %{_docdir}/%{name}
%config(noreplace) %{_sysconfdir}/java/sblim-cim-client2.properties
%config(noreplace) %{_sysconfdir}/java/sblim-slp-client2.properties
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/ChangeLog
%doc %{_docdir}/%{name}/NEWS
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/org


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_4jpp8
- new version

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2jpp7
- new version

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.12-alt1_2jpp7
- new version

