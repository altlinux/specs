Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 3.0.1
%define name jbossws-framework
%define _with_repolib 1

%define version_maj 3
%define version_min 0
%define version_rev 1
%define version_tag GA
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir_root repository.jboss.com
%define repodir_release jboss/%{name}/%{version_full}
%define repodir %{_javadir}/%{repodir_root}/jboss/jbossws-framework/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

 
Name:           jbossws-framework
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:        alt1_2jpp5
Epoch:          0
Summary:        JBoss Web Services (framework)
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/jbossws/
# svn export http://anonsvn.jboss.org/repos/jbossws/framework/tags/jbossws-framework-3.0.1.GA/
# tar cjf jbossws-framework-3.0.1.GA.tar.bz2 jbossws-framework-3.0.1.GA
Source0:        %{name}-%{version_full}.tar.bz2
Source1:        %{name}-component-info.xml
Patch0:         %{name}-ant-hack.patch
Patch1:         %{name}-no-classpath-in-manifest.patch
Requires: annotation_1_0_api
Requires: dom4j
# FIXME: (dwalluck): For servlet-api.jar
Requires: geronimo-j2ee-1.4-apis
Requires: jaxws_2_1_api
Requires: jboss-common
Requires: jbossws-common >= 0:1.0.4
Requires: jbossws-spi >= 0:1.0.2
Requires: jbossxb >= 0:1.0.0
BuildRequires: annotation_1_0_api
BuildRequires: ant
BuildRequires: dom4j
# FIXME: (dwalluck): For servlet-api.jar
BuildRequires: geronimo-j2ee-1.4-apis
BuildRequires: jaxws_2_1_api
BuildRequires: jboss-common
BuildRequires: jbossws-common >= 0:1.0.4
BuildRequires: jbossws-spi >= 0:1.0.2
BuildRequires: jbossxb >= 0:1.0.0
BuildArch:      noarch

%description
JBossWS Framework.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}-%{version_full}
%patch0 -p1
%patch1 -p1
%{__cp} -a ant.properties.example ant.properties

%{__mkdir_p} thirdparty
pushd thirdparty
%{__ln_s} $(build-classpath dom4j) dom4j.jar
%{__ln_s} $(build-classpath jboss-common/jboss-common) jboss-common-core.jar
%{__ln_s} $(build-classpath jbossws-common) jbossws-common.jar
%{__ln_s} $(build-classpath jbossws-spi) jbossws-spi.jar
%{__ln_s} $(build-classpath jboss/jbossxb) jboss-xml-binding.jar
%{__ln_s} $(build-classpath geronimo-j2ee-1.4-apis) servlet-api.jar
popd

%build
export CLASSPATH=$(build-classpath annotation_1_0_api geronimo-j2ee-1.4-apis jaxws_2_1_api)
export OPT_JAR_LIST=:
%{ant}

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -a output/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version_full}.jar
%{__cp} -a output/lib/jbossws-framework-src.zip %{buildroot}%{_javadir}/%{name}-sources-%{version_full}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version_full}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version_full}||g"`; done)

%{__mkdir} %{buildroot}%{_bindir}
%{__cp} -a src/main/etc/wsconsume.sh %{buildroot}%{_bindir}/%{name}-wsconsume
%{__cp} -a src/main/etc/wsprovide.sh %{buildroot}%{_bindir}/%{name}-wsprovide

%if %{with_repolib}
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodir}/bin
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{buildroot}%{_javadir}/%{name}-%{version_full}.jar %{buildroot}%{repodirlib}/jbossws-framework.jar
%{__install} -p -m 0644 %{buildroot}%{_javadir}/%{name}-sources-%{version_full}.jar %{buildroot}%{repodirlib}/jbossws-framework-src.zip
%{__install} -p -m 0755 src/main/etc/wsconsume.bat %{buildroot}%{repodir}/bin/wsconsume.bat
%{__install} -p -m 0755 src/main/etc/wsconsume.sh %{buildroot}%{repodir}/bin/wsconsume.sh
%{__install} -p -m 0755 src/main/etc/wsprovide.bat %{buildroot}%{repodir}/bin/wsprovide.bat
%{__install} -p -m 0755 src/main/etc/wsprovide.sh %{buildroot}%{repodir}/bin/wsprovide.sh
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/@VERSION@/%{version_full}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i 's/@TAG@/$tag/g' %{buildroot}%{repodir}/component-info.xml
%endif

%files
%{_javadir}/%{name}-%{version_full}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-sources-%{version_full}.jar
%{_javadir}/%{name}-sources.jar
%attr(0755,root,root) %{_bindir}/%{name}-wsconsume
%attr(0755,root,root) %{_bindir}/%{name}-wsprovide

%if %{with_repolib}
%files repolib
%{_javadir}/%{repodir_root}
%endif

%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_2jpp5
- full version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt0.1jpp
- bootstrap for jbossas

