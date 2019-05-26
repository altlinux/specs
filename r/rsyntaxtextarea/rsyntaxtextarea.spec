Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global upname RSyntaxTextArea

Name:           rsyntaxtextarea
Version:        2.6.1
Release:        alt1_5jpp8
Summary:        A syntax highlighting, code folding text editor for Java Swing applications

License:        BSD
URL:            https://github.com/bobbylight/%{upname}
Source0:        https://github.com/bobbylight/%{upname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# This patch removes upstream's dependency on gradle coveralls plugin.
Patch0:         %{name}-no-coveralls.patch
# This patch enables proper Arduino Support
Patch1:         %{name}-arduino.patch

BuildArch:      noarch

BuildRequires:  gradle-local
Requires:       java
Source44: import.info

%description
%{upname} is a customizable, syntax highlighting text component for Java
Swing applications. Out of the box, it supports syntax highlighting for 40+
programming languages, code folding, search and replace, and has add-on
libraries for code completion and spell checking. Syntax highlighting for
additional languages can be added via tools such as JFlex.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{upname}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{upname}-%{version}
%patch0 -p1
%patch1 -p2
find . -name "*.jar" -delete
for file in src/main/dist/%{upname}.License.txt src/main/dist/readme.txt; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done


%build
# We skip unit tests because they require an X11 server.
%gradle_build --skip-tests


%install
%mvn_install -J build/docs/javadoc/


%files -f .mfiles
%doc --no-dereference src/main/dist/%{upname}.License.txt
%doc src/main/dist/readme.txt


%files javadoc -f .mfiles-javadoc
%doc --no-dereference src/main/dist/%{upname}.License.txt


%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_5jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_2jpp8
- new jpp release

