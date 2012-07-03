Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define _with_repolib 1

%define version_maj 3
%define version_min 2
%define version_rev 0
%define version_tag GA
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jbpm/jpdl/3.2.GA
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
 
Name:           jboss-jbpm-jpdl
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:        alt1_1jpp5
Epoch:          0
Summary:        BPM and workflow engine in Java
License:        LGPLv2+
Group:          Development/Java
URL:            http://jbpm.org

BuildArch:      noarch
Source0:        %{name}-%{version_full}-tp.tar.gz
Source1:        %{name}-%{version_full}-component-info.xml

%description
BPM and workflow engine in Java.

%if %{with_repolib}
%package repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -c %{name} 

%if %{with_repolib}
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}
%endif

%build
#Do Nothing here

# FIXME: (dwalluck) jars are not build from source

%install

# FIXME: E: no-jar-manifest /usr/share/java/jboss-jbpm-jpdl/jbpm-jpdl-examplesdb.jar

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 jbpm-console.war $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-enterprise.ear $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-identity.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-jmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-jpdl-config.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-jpdl-db.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-jpdl-examples.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-jpdl-examplesdb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 0644 jbpm-jpdl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p * $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%{_javadir}/%{name}

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_1jpp5
- new version

