BuildRequires: /proc
BuildRequires: jpackage-compat
%global git_commit 3035acd
%global cluster jnr

Name:           jnr-posix
Version:        1.1.8
Release:        alt1_2jpp7
Summary:        Java Posix layer
Group:          Development/Java
License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/%{cluster}/%{name}/
Source0:        https://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz
Patch0:         jnr_posix_fix_jar_dependencies.patch
Patch1:         jnr_posix_remove_windows_specific_bits.patch

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  jpackage-utils
BuildRequires:  jnr-constants
BuildRequires:  jaffl
BuildRequires:  jffi
BuildRequires:  objectweb-asm

Requires:       jpackage-utils
Requires:       jnr-constants
Requires:       jaffl
Requires:       jffi
Requires:       objectweb-asm

BuildArch:      noarch
Source44: import.info

%description
jnr-posix is a lightweight cross-platform POSIX emulation layer for Java, 
written in Java and is part of the JNR project 

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
%patch1
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

mkdir build_lib
build-jar-repository -s -p build_lib jaffl jffi constantine objectweb-asm/asm \
                                     objectweb-asm/analysis objectweb-asm/commons \
                                     objectweb-asm/tree objectweb-asm/util objectweb-asm/xml

%build
ant jar
ant javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -a dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# pom
%add_to_maven_depmap org.jruby.ext.posix %{name} %{version} JPP %{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jnr-posix.pom

%files
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_2jpp7
- new version

