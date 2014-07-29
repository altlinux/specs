# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global         over 0_9
%global         svn  74

Summary:        Diagrams Through ASCII Art
Name:           ditaa
Version:        0.9
Release:        alt1_9.r74jpp7
Group:          File tools
License:        GPLv2+
URL:            http://ditaa.sourceforge.net/
#Source0:       http://downloads.sourceforge.net/ditaa/ditaa%{over}-src.zip
# Sources pulled from svn:
# rm -rf ditaa-0.9
# svn co -r%{svn} https://ditaa.svn.sourceforge.net/svnroot/ditaa/trunk ditaa-0.9
# tar cJvf ditaa-0.9.r%{svn}.tar.xz ditaa-0.9
Source0:        ditaa-0.9.r%{svn}.tar.xz
Source1:        ditaa.wrapper
Patch0:         ditaa-0.9-batik-png.patch
BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  jpackage-utils
BuildRequires:  batik
BuildRequires:  jericho-html
BuildRequires:  xml-commons-apis
BuildRequires:  apache-commons-cli
Requires:       apache-commons-cli
Requires:       xml-commons-apis
Requires:       jericho-html
Requires:       batik
Requires:       jpackage-utils
Source44: import.info

%description
ditaa is a small command-line utility written in Java, that can
convert diagrams drawn using ASCII art ('drawings' that contain
characters that resemble lines like | / - ), into proper bitmap
graphics.

%prep 
%setup -q
%patch0 -p1
find -name '*.class' -delete
find -name '*.jar' -delete

%build
%{__install} -d bin
build-jar-repository -s -p lib commons-cli batik-all xml-commons-apis-ext jericho-html
ant -f build/release.xml

%install
%{__install} -D -p -m 0644 releases/%{name}%{over}.jar \
    %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s}  %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
%{__install} -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING HISTORY
%{_bindir}/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_9.r74jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_8.r74jpp7
- new version

