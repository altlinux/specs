BuildRequires: /proc
BuildRequires: jpackage-compat
%global git_commit 6e04bca
%global cluster    wmeissner

Name:    jnr-netdb
Version: 1.0.1
Release: alt1_6jpp7
Summary: Network services database access for java

Group:   System/Libraries
License: LGPLv3
URL:      http://github.com/%{cluster}/%{name}
Source0:  %{url}/tarball/%{version}/%{cluster}-%{name}-%{git_commit}.tar.gz
Patch0:  fix_jnr_netdb_jar_dependencies.patch
BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: jaffl
BuildRequires: ant-junit
BuildRequires: junit4
BuildRequires: jffi
Requires: jpackage-utils
Requires: jaffl
Source44: import.info

%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}
%patch0

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
build-jar-repository -s -p lib junit junit4 jaffl objectweb-asm jffi

ant jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -a dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# pom
%add_to_maven_depmap org.jruby.extras %{name} %{version} JPP %{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jnr-netdb.pom

%check
ant test

%files
%{_javadir}/*
%doc COPYING
%doc COPYING.LESSER
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_6jpp7
- new version

