%def_enable static

Name: libipathverbs
Version: 1.2
Release: alt1
Summary: PathScale InfiniPath HCA Userspace Driver
Group: System/Libraries
License: %gpl2only
Url: http://openib.org
Source: %name-%version.tar
Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Requires: libibverbs >= 1.0

BuildRequires(pre): rpm-build-licenses
BuildRequires: libibverbs-devel >= 1.0

%description
%name provides a device-specific userspace driver for QLogic
HCAs for use with the libibverbs library.


%if_enabled static
%package devel-static
Summary: Static %name library
Group: Development/C

%description devel-static
Static the %name library.
%endif


%prep
%setup
touch ChangeLog NEWS


%build
%autoreconf
%configure %{subst_enable static}
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS COPYING README
%_libdir/*.so
%_sysconfdir/libibverbs.d/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Thu Aug 19 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2-alt1
- New version (OFED 1.5.1)

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libipathverbs
  * postun_ldconfig for libipathverbs

* Tue Oct 28 2008 Led <led@altlinux.ru> 1.1-alt1
- initial build
