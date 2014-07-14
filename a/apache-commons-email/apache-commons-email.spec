Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       email
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.2
Release:          alt2_3jpp7
Summary:          Apache Commons Email Package
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

# Depmap needed to remove test deps and fix javax:activation (part of JDK 5+)
Source1:          %{short_name}.depmap
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    apache-commons-parent
BuildRequires:    javamail
Requires:         javamail
Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
Commons-Email aims to provide an API for sending email. It is built on top of 
the JavaMail API, which it aims to simplify.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

%build
#Skip tests due to missing deps: net.sf.retrotranslator:retrotranslator-runtime
#                                org.subethamail:subethasmtp-smtp
#                                org.subethamail:subethasmtp-wiser
mvn-rpmbuild \
             -Dmaven.test.skip=true \
             -Dmaven.local.depmap.file="%{SOURCE1}" \
              install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt RELEASE-NOTES.txt NOTICE.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp7
- new version

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_4jpp6
- fixed build (added jansi BR:)

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed symlinks

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- added osgi manifest

