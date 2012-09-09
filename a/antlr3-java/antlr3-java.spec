Name: antlr3-java
Version: 3.4
Summary: Java run-time support for ANTLR-generated parsers
License: BSD
Url: http://www.antlr.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: java
Requires: jpackage-utils
Requires: stringtemplate
Requires: stringtemplate4

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: antlr3-java-3.4-11.fc19.cpio

%description
Java run-time support for ANTLR-generated parsers

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
* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 3.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

