BuildRequires: /proc
BuildRequires: jpackage-compat
%global cluster wmeissner
%global git_commit 78eebb2
%global commit_dl g78eebb2
%global commit_rev 0

Name:           jnr-x86asm
Version:        0.1
Release:        alt1_4jpp7
Summary:        Pure-java port of asmjit

Group:          Development/Java
License:        LGPLv3
URL:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{version}-%{commit_rev}-%{commit_dl}.tar.gz
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  jpackage-utils
Requires:       jpackage-utils
Source44: import.info

%description
Pure-java port of asmjit (http://code.google.com/p/asmjit/)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant

%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

%files
%doc LICENSE COPYING*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_4jpp7
- new version

