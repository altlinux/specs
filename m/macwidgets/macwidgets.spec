Name: macwidgets
Version: 0.9.5
Release: alt2_0jpp6
Summary: Collection of Mac style widgets written in Java

Group: Development/Java
License: LGPLv3
Url: http://code.google.com/p/macwidgets/

Source0: %name-%version.tar

BuildPreReq: rpm-build-java
BuildRequires: /proc ant jgoodies-forms
BuildRequires: jpackage-utils
BuildRequires: java-devel-default
#BuildRequires: junit4

BuildArch: noarch

%description
Mac Widgets for Java are a collection of widgets seen in OS X
applications, offered in a Java API. These widgets help Java developers
create more Mac-like applications. Their usage is not restricted to Mac
though, as they will render across platforms.

%prep
%setup -n %name-%version

%build
ant
ant compress

%install
install -D -m0644 mac_widgets-%version.jar %buildroot%_javadir/mac_widgets-%version.jar
ln -s mac_widgets-%version.jar %buildroot%_javadir/mac_widgets.jar

%files
%_javadir/*.jar


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt2_0jpp6
- NMU: fixed build

* Fri Mar 01 2013 Paul Wolneykien <manowar@altlinux.ru> 0.9.5-alt1_0jpp6
- Initial build for ALT Linux.
