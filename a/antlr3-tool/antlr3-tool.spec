Name: antlr3-tool
Version: 3.4
Summary: ANother Tool for Language Recognition
License: BSD
Url: http://www.antlr.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: antlr3
Requires: /bin/sh
Requires: antlr3-java
Requires: java
Requires: jpackage-utils
Requires: stringtemplate4

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: antlr3-tool-3.4-11.fc19.cpio

%description
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical
descriptions containing actions in a variety of target languages.

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

