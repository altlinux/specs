# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		jiprof
Version:	1.1.1
Release:	alt1_8jpp8
Summary:	Java Interactive Profiler
Group:		Development/Java
URL:		http://jiprof.sourceforge.net
Source:		http://downloads.sourceforge.net/project/jiprof/jip/%{version}/jip-src-%{version}.zip
License:	BSD
BuildRequires:	ant
BuildRequires:	objectweb-asm
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	xerces-j2
Requires:	jpackage-utils
Requires:	xerces-j2
BuildArch:	noarch
Source44: import.info

%description
JIP is a high performance, low overhead profiler that is written entirely in Java.
JIP gives the developer the ability to turn the profiler on and off while the
VM is running. You can also filter out classes and packages as well as control the
output.

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
BuildArch: noarch

%description	javadoc
The Java Interactive Profiler.

This package contains javadoc for %{name}.

%package	manual
Summary:	Manual for %{name}
Group:		Development/Java
BuildArch: noarch

%description	manual
The Java Interactive Profiler.

This package contains manual for %{name}.

%prep
%setup -q -c %{name}-%{version}

for j in $(find -name "*.jar"); do
   mv $j  $j.no
done

for file in src/com/mentorgen/tools/profile/instrument/PerfMethodAdapter.java \
	    src/org/objectweb/asm/jip/attrs/StackMapTableAttribute.java; do \
	    native2ascii -encoding UTF8 $file $file
done

%build
export CLASSPATH=$(build-classpath junit objectweb-asm/asm objectweb-asm/asm-commons xerces-j2):bin
%ant dist

%install
mkdir -p %{buildroot}%{_javadir}/%{name}

install -pm 644 client/client.jar %{buildroot}%{_javadir}/%{name}/client-%{version}.jar
install -pm 644 profile/profile.jar %{buildroot}%{_javadir}/%{name}/profile-%{version}.jar
install -pm 644 profile/jipViewer.jar %{buildroot}%{_javadir}/%{name}/jipViewer-%{version}.jar

(
  cd %{buildroot}%{_javadir}/%{name}
  for jar in *-%{version}*; do 
    ln -sf ${jar} ${jar/-%{version}/}
  done
)

mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s jiprof-%{version} %{buildroot}%{_javadocdir}/%{name}
rm -rf doc/javadoc

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/client-%{version}.jar
%{_javadir}/%{name}/client.jar
%{_javadir}/%{name}/profile-%{version}.jar
%{_javadir}/%{name}/profile.jar
%{_javadir}/%{name}/jipViewer-%{version}.jar
%{_javadir}/%{name}/jipViewer.jar
%doc doc/license.txt

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc doc/*


%changelog
* Fri Jan 03 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_8jpp8
- sisyphus build

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_8
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_7
- new version

