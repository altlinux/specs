Epoch: 0
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name codec
%global short_name commons-%{base_name}

Name:          apache-%{short_name}
Version:       1.6
Release:       alt1_4jpp7
Summary:       Implementations of common encoders and decoders
Group:         Development/Java
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/

Source0:       http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz


BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: maven-antrun-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
Requires:      jpackage-utils

Provides:      jakarta-%{short_name} = %{version}-%{release}
Obsoletes:     jakarta-%{short_name} < %{version}-%{release}
# It looks like there are packages in F-13 that BR/R the short name
Provides:      %{short_name} = %{version}-%{release}
Obsoletes:     %{short_name} < %{version}-%{release}
Source44: import.info

%def_with repolib
%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%if_with repolib
Source3:        %{name}-component-info.xml

%package	 repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}

%description	 repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif


%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%package javadoc
Summary:       API documentation for %{name}
Group:         Development/Java
Requires:      jpackage-utils
Obsoletes:     jakarta-%{short_name}-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{short_name}.jar

# javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar -a "%{short_name}:%{short_name}"
# jakarta compat
ln -s %{short_name}.jar %buildroot%_javadir/jakarta-%{short_name}.jar
ln -s %{short_name}.jar %buildroot%_javadir/apache-%{short_name}.jar

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{short_name}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES*
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%{_javadir}/*
%if %with repolib
%exclude %{repodir}
%files repolib
%{repodir}
%endif

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp6
- fixed repolib

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_5jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp6
- new version

