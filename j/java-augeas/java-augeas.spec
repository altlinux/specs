# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:    Java bindings for the augeas library
Name:       java-augeas
Version:    0.0.2
Release:    alt1_5jpp7
License:    LGPLv2+
BuildArch:  noarch
Group:      Development/Java
Source:     http://augeas.net/download/java/%{name}-%{version}.tar.gz
URL:        http://augeas.net/

Requires:   jna
Requires:   augeas >= 0.7.2
Requires:   jpackage-utils
BuildRequires:  ant
BuildRequires:  jna
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  ant-junit
Source44: import.info

#
# the jpackage-utils should provide a %{java_home} macro
# to select a different Java JVM from the default one use the following
# rpmbuild --define 'java_home /usr/lib/jvm/your_jvm_of_choice'
#

%description
java-augeas is a java bindings onto the augeas configuration API.
It requires augeas >= 0.7.2


%package    javadoc
Summary:    Java documentation for %{name}
Group:      Development/Documentation
Requires:   %{name} = %{version}-%{release}
Requires:   jpackage-utils
BuildArch: noarch

%description    javadoc
API documentation for %{name}.
%prep
%setup -q

%build
ant build docs

%install
rm -fr %{buildroot}
install -d -m0755 %{buildroot}%{_javadir}
install -d -m0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -p target/augeas-%{version}.jar %{buildroot}%{_javadir}
%{__ln_s} %{_javadir}/augeas-%{version}.jar %{buildroot}%{_javadir}/augeas.jar 
cp -r -p target/javadoc %{buildroot}%{_javadocdir}/%{name}



%files
%doc AUTHORS COPYING NEWS README INSTALL
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_5jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_4jpp7
- new version

