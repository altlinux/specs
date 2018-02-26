Name: gettext-doclet
Version: 1.0.3
Release: alt1

Summary: Standard doclet based doclet with localization support
License: GPLv3
Group: Development/Java
Url: http://altlinux.org/GettextDoclet
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source: %name-%version.tar.gz

# Common dependencies
BuildPreReq: /proc rpm-build-java jpackage-utils
BuildRequires: java-devel-default 

# Apache Ant is used for build
BuildRequires: ant junit

BuildArch: noarch

%description
Standard doclet based doclet with localization support.
Produce Javadoc documentation in different languages
using GNU Gettext localization tools.

# Doesn't exist yet :)
#%package javadoc
#Summary: Documentation for %name
#Group: Development/Documentation
#Requires: java-common

#%description javadoc
#Provides Javadoc documentation for %name.

%prep
%setup -n %name-%version

%build
%ant dist

%install
# jars
install -d -m 755 %buildroot%_javadir
install -m 644 dist/%name.jar %buildroot%_javadir/%name-%version.jar
ln -s %name-%version.jar %buildroot%_javadir/%name.jar

## javadoc
#install -d -m 755 %buildroot%_javadocdir/%name
#cp -pr dist/docs/api/* %buildroot%_javadocdir/%name

%files
%doc README COPYING
%_javadir/%name-%version.jar
%_javadir/%name.jar

#%files javadoc
#%doc %_javadocdir/%name

%changelog
* Fri Aug 27 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt1
- Do not remove some usual spacing when tight the text.
- Properly comment multiline values.

* Fri Aug 27 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.2-alt1
- Fix/improve output of the preformatted (code fragments, etc) comments.
- Do not link to the Standard doclet class.
- Add -base-doclet option to specify the name of the base doclet class.

* Thu Aug 26 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.1-alt2
- Build proper 1.0.1 version (fix the build tags).

* Thu Aug 26 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.1-alt1
- Multiline template entry output.
- Better split of HTML comments.

* Fri Aug 20 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux.
