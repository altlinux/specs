Name: lucene3-contrib
Version: 3.6.2
Summary: Lucene contributed extensions
License: ASL 2.0 and BSD
Url: http://lucene.apache.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: lucene3-contrib = 0:3.6.2-7.fc23
Requires: lucene3

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: lucene3-contrib-3.6.2-7.fc23.cpio

%description
Lucene contributed extensions.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

