Name: libexttextcat
Version: 3.4.5
Release: alt1

Summary: Text categorisation library
License: BSD
Group: Development/Other
Url: https://wiki.documentfoundation.org/Libexttextcat

# git-vcs git://gerrit.libreoffice.org/libexttextcat
Source: %name-%version.tar
Obsoletes: libtextcat < %version
Provides: libtextcat = %version

%description
%name is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libtextcat-devel < %version
Provides: libtextcat-devel = %version

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Tool for creating custom document fingerprints
Group: Publishing
Requires: %name = %version-%release
Conflicts: libtextcat-devel < %version

%description tools
The %name-tools package contains the createfp program that allows
you to easily create your own document fingerprints.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/*.so.*
%_datadir/*

%files devel
%doc LICENSE README*
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%files tools
%_bindir/*

%changelog
* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 3.4.5-alt1
- 3.4.5

* Thu Aug 07 2014 Alexey Shabalin <shaba@altlinux.ru> 3.4.4-alt1
- 3.4.4

* Wed Aug 14 2013 Alexey Shabalin <shaba@altlinux.ru> 3.4.3-alt1
- 3.4.3
- rename package from libtextcat to libexttextcat
- move createfp program to libexttextcat-tools package

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2-alt4.qa1
- NMU: rebuilt for debuginfo.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 2.2-alt4
- Rebuilt for soname set-versions.

* Wed Nov 18 2009 Victor Forsyuk <force@altlinux.org> 2.2-alt3
- Fix testtextcat to find installed conf.txt.
- Package testtextcat as textcat.
- Sample texts does not needed to be installed, drop it.
- Remove excessive path element from language data location. Fixes ALT #20722.

* Wed Jul 08 2009 Victor Forsyuk <force@altlinux.org> 2.2-alt2
- Split devel subpackage.

* Tue Apr 05 2005 Victor Forsyuk <force@altlinux.ru> 2.2-alt1
- In fact license is BSD.
- Package shared libraries instead of static.

* Sun Jul 13 2003 Ott Alex <ott@altlinux.ru> 2.1-alt1
- Initial build for ALTLinux
