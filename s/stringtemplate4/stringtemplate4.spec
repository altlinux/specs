Name: stringtemplate4
Version: 4.0.4
Summary: A Java template engine
License: BSD
Url: http://www.stringtemplate.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: java
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: stringtemplate4-4.0.4-4.fc18.cpio

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

