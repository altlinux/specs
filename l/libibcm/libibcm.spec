%def_enable shared
%def_enable static

Name: libibcm
Version: 1.0.5
Release: alt1
Summary: Userspace InfiniBand Communication Manager
Group: System/Libraries
License: %gpl2only
Url: http://www.openfabrics.org
Source: %name-%version.tar
Packager: Repocop Q. A. Robot <repocop@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libibverbs-devel

%description
%name provides a userspace InfiniBand Communication Managment
library.


%package devel
Summary: Development files for the %name library
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release
Requires: libibverbs-devel

%description devel
Development files for the %name library.


%if_enabled static
%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static the %name library.
%endif


%prep
%setup


%build
%configure %{subst_enable shared} %{subst_enable static}
%make_build


%install
%make_install DESTDIR=%buildroot install


%if_enabled shared
%files
%doc AUTHORS COPYING README
%_libdir/*.so.*
%endif

%files devel
%if_enabled shared
%_libdir/*.so
%else
%doc AUTHORS COPYING README
%endif
%_includedir/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Thu Aug 19 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt1
- New version (OFED 1.5.1)

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libibcm
  * postun_ldconfig for libibcm

* Tue Oct 28 2008 Led <led@altlinux.ru> 1.0.4-alt1
- initial build
