%define sunvers 1_2_1

Name: jmx
Version: 1.2.1
Release: alt3_jvm4.2
Summary: Java Management Extensions
License: Sun Binary Code License
Url: http://java.sun.com/products/JavaManagement/
Group: Development/Java
Packager: Igor Vlasenko <viy@altlinux.ru>

Source0: %name-%sunvers-ri.zip
BuildArch: noarch
BuildPreReq: /proc rpm-build-java
BuildRequires: java-common unzip alternatives
Provides: jmx_impl
Requires: alternatives

%description
JavaTM Management Extensions (JMX) represent a universal,
open technology for management, and monitoring ready
to be deployed across all industries, wherever management
and/or monitoring is/are or will be needed.

%package javadoc
Summary: Javadoc for %name
Group: Development/Java
Requires: java-common

%description javadoc
Javadoc for %name.

%prep
%setup -c -q
# fix files perms
chmod -R go=u-w *

%build
%install
# jars
install -d -m 755 %buildroot%_javadir
install -m 644 %name-%sunvers-bin/lib/%{name}ri.jar %buildroot%_javadir
install -m 644 %name-%sunvers-bin/lib/%{name}tools.jar %buildroot%_javadir

# javadoc
install -d -m 755 %buildroot%_javadocdir/%name
cp -pr %name-%sunvers-bin/doc/api/* %buildroot%_javadocdir/%name

# alternatives
install -d -m 755 %buildroot%_altdir
cat <<EOF > %buildroot%_altdir/%name
%_javadir/jmx_impl.jar	%_javadir/%{name}ri.jar	5
EOF

%files
%_altdir/%name
%_javadir/*.jar

%files javadoc
%_javadocdir/%name

%changelog
* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3_jvm4.2
- resurrected; is still used for log4j build

* Thu Mar 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt2
- rpm-build-java macroces
- alternatives for jmx_impl

* Sun Sep 12 2004 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1
- 1.2.1
- spec cleanup

* Tue Mar 25 2003 Nicolas Mailhot <Nicolas.Mailhot (at) laPoste.net> 1.2-4jpp
- use jmxri alternative

* Fri Mar 21 2003 Nicolas Mailhot <Nicolas.Mailhot (at) laPoste.net> 1.2-1jpp
- for jpackage-utils 1.5
- bumped to 1.2

* Thu Jun 20 2002 Henri Gomez <hgomez@slib.fr> 1.1-1jpp
- Initial release
