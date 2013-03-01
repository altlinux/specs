Name: macwidgets
Version: 0.9.5
Release: alt1_0jpp6
Summary: Collection of Mac style widgets written in Java

Group: Development/Java
License: LGPLv3
Url: http://code.google.com/p/macwidgets/

Source0: %name-%version.tar

BuildPreReq: rpm-build-java
BuildRequires: /proc ant jgoodies-forms
BuildRequires: jpackage-utils >= 0:5.0.0
#BuildRequires: junit4

Requires: jpackage-utils >= 0:5.0.0

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

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
* Fri Mar 01 2013 Paul Wolneykien <manowar@altlinux.ru> 0.9.5-alt1_0jpp6
- Initial build for ALT Linux.
