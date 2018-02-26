Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0.4
%define name jbossws-common
%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir_root repository.jboss.com
%define repodir_release jboss/%{name}/%{version_full}
%define repodir %{_javadir}/%{repodir_root}/%{repodir_release}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define version_maj 1
%define version_min 0
%define version_rev 4
%define version_tag GA
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}
 
Name:           jbossws-common
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:        alt1_2jpp5
Epoch:          0
Summary:        JBoss Web Services (common)
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/jbossws/
# svn export http://anonsvn.jboss.org/repos/jbossws/common/tags/jbossws-common-1.0.4.GA/
# tar cjf jbossws-common-1.0.4.GA.tar.bz2 jbossws-common-1.0.4.GA
Source0:        %{name}-%{version_full}.tar.bz2
Source1:        %{name}-component-info.xml
Patch0:         %{name}-ant-hack.patch
Requires: jaf_1_1_api
Requires: jaxb_2_1_api
Requires: jaxws_2_1_api
Requires: jboss-common
Requires: jboss-microcontainer
Requires: jbossws-spi >= 0:1.0.2
BuildRequires: ant
BuildRequires: jaf_1_1_api
BuildRequires: jaxb_2_1_api
BuildRequires: jaxws_2_1_api
BuildRequires: jboss-common
BuildRequires: jboss-microcontainer
BuildRequires: jbossws-spi >= 0:1.0.2
BuildRequires: junit >= 0:3.8.1
BuildArch:      noarch

%description
JBossWS Common.

%if %{with_repolib}
%package repolib
Summary:     Artifacts to be uploaded to a repository library
Group:       Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}-%{version_full}
%patch0 -p1
%{__cp} -a ant.properties.example ant.properties

%{__mkdir_p} thirdparty
pushd thirdparty
%{__ln_s} $(build-classpath jboss-common/jboss-common) jboss-common-core.jar
%{__ln_s} $(build-classpath jboss-microcontainer/jboss-microcontainer) jboss-microcontainer.jar
%{__ln_s} $(build-classpath jbossws-spi) jbossws-spi.jar
%{__ln_s} $(build-classpath junit) junit.jar
popd

%build
export CLASSPATH=$(build-classpath jaf_1_1_api jaxb_2_1_api jaxws_2_1_api)
export OPT_JAR_LIST=:
%{ant}

%install

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 output/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version_full}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version_full}.jar %{name}.jar
popd

%if %{with_repolib}
%{__mkdir_p} %{buildroot}%{repodir}
%{__cp} -a %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
%{__sed} -i 's/@VERSION@/%{version_full}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version_full}.jar $RPM_BUILD_ROOT%{repodirlib}/jbossws-common.jar
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -a %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
%endif

%files
%{_javadir}/%{name}-%{version_full}.jar
%{_javadir}/%{name}.jar

%if %{with_repolib}
%files repolib
%{_javadir}/%{repodir_root}
%endif

%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_2jpp5
- full version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt0.1jpp
- bootstrap for jbossas

