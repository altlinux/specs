BuildRequires: rpm-build-java-osgi
AutoReq: yes,noosgi

Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name       lang
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        2.6
Release:        alt2_7jpp7
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         0001-Make-source-version-1.3.patch
Patch1:         0002-Fix-FastDateFormat-for-Java-7-behaviour.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven-site-plugin
BuildRequires:  maven
BuildRequires:  apache-commons-parent
BuildRequires:  maven-surefire-provider-junit

Requires:       jpackage-utils >= 0:1.6


# This should go away with F-17
Provides:       jakarta-commons-lang = 0:%{version}-%{release}
Obsoletes:      jakarta-commons-lang <= 0:2.4
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Source44: import.info

Source3:        %{name}-component-info.xml
%def_with repolib
%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif


%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils

Obsoletes:      jakarta-%{short_name}-javadoc <= 0:2.4
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' *.txt

%build
mvn-rpmbuild install javadoc:javadoc

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name},%{base_name}:%{base_name}"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc PROPOSAL.html LICENSE.txt RELEASE-NOTES.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_javadir}/jakarta-%{short_name}.jar
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp7
- new version

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt3_7jpp6
- restored javadoc

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt2_7jpp6
- fixed build

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_7jpp6
- renamed

