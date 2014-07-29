# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jazzy
Version:        0.5.2
Release:        alt1_6jpp7
Summary:        Java-based spell checker

Group:          Text tools
License:        LGPLv2+
URL:            http://sourceforge.net/projects/jazzy
Source0:        http://downloads.sourceforge.net/project/jazzy/Jazzy/Jazzy-%{version}/jazzy-%{version}.src.zip
Patch0:         0001-No-hardcoded-class-paths.patch

BuildRequires:  ant
BuildRequires:  unzip
BuildRequires:  jpackage-utils
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Jazzy is a pure Java library implementing a spell checking algorithm
similar to aspell. It may be used to spell check a variety of sources.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
Java API Documentation for %{name}.


%prep
%setup -q -c
%patch0 -p1 -b .classpath
find -name '*.jar' -delete


%build
ant binary-release javadoc

# Get rid of CP/M line enxoding
for F in *.txt
do
        sed 's/\r//' <$F >temp
        touch -r $F temp
        mv temp $F
done


%install

# Code
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
find dist -name '*.jar' |while read F
do
        BASE=$(basename $F)
        VER=$(echo $BASE |sed 's/\.jar$/-%{version}.jar/')
        install -p -m644 $F $RPM_BUILD_ROOT%{_javadir}/%{name}/$VER
        ln -s $VER $RPM_BUILD_ROOT%{_javadir}/%{name}/$BASE
done

# Documentation
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}


%files
%{_javadir}/%{name}
%doc CONTRIBUTORS.txt example2.txt LICENSE.txt README.txt


%files javadoc
%{_javadocdir}/%{name}-%{version}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_6jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_5jpp7
- new version

