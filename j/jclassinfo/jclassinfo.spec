Summary: Extracts information from java class files
Name: jclassinfo
Version: 0.19.1
Release: alt4
Packager: Igor Vlasenko <viy@altlinux.ru>
License: GPL2
URL: http://jclassinfo.sourceforge.net/
Group: Development/Java

BuildRequires: zlib-devel gcc-c++
BuildRequires: gtk-doc
Source0: jclassinfo-0.19.1.tar
Patch: jclassinfo-0.19.1-alt-Makefile.patch

%description -n jclassinfo
Reads java class files and provides information about what packages,
 classes and methods are used, as well as information about the class
 itself.

%package -n libjclass3
Summary: Library for reading java class files
Group: Development/C

%description -n libjclass3
Library which provides a high level interface for reading java class
 files. It is still in its early stages of development.

%package -n libjclass-devel
Summary: Development files for libjclass
Requires: libjclass3 = %version-%release zlib-devel pkg-config
Group: Development/C

%description -n libjclass-devel
libjclass is a library which provides a high level interface for 
 reading java class files. It is still in its early stages of development. 
 This package provides the necessary files for developing programs 
 that use libjclass.

%package -n libjclass-docs
Group: Documentation
Summary: Documentation and DevHelp book for libjclass
Requires: libjclass-devel

%description -n libjclass-docs
Documentation for libjclass. The documentation can either be viewed
 with you favourite browser or with DevHelp.

%prep
%setup -q
%patch -p1

%build
%autoreconf -fisv

%configure \
 --with-html-dir=%_datadir/doc/libjclass-docs-%version/html

# regenerete gtk-doc (no need)
# --enable-gtk-doc \

%make

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/doc/libjclass-docs-%version/html
%make_install install DESTDIR=$RPM_BUILD_ROOT

%files -n libjclass3
%doc TODO NEWS
%_libdir/libjclass.so.*

%files -n libjclass-devel
%doc ChangeLog
%_includedir/jclass
%_libdir/jclass
%_libdir/libjclass.so
%_pkgconfigdir/jclass.pc

%files -n libjclass-docs
%doc %_datadir/doc/libjclass-docs-%version/html
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/libjclass-docs-%version 

%files -n jclassinfo
%doc README
%doc NEWS
%_bindir/jclassinfo
%_man1dir/jclassinfo*
/usr/share/xml/jclassinfo

%changelog
* Mon Jan 04 2010 Igor Vlasenko <viy@altlinux.ru> 0.19.1-alt4
- fixed build

* Mon Apr 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.19.1-alt3
- fixed docdir ownership

* Tue Jul 29 2008 Igor Vlasenko <viy@altlinux.ru> 0.19.1-alt2
- libjclass-devel unmet fix

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.19.1-alt1
- first build for Sisyphus
