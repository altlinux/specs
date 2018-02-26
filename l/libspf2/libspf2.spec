Name: libspf2
Version: 1.2.9
Release: alt4

Summary: Implementation of the SPF specification
License: LGPLv2.1+
Group: System/Libraries

URL: http://www.libspf2.org/
Source0: http://libspf2.org/spf/libspf2-%version.tar.gz

# Automatically added by buildreq on Mon Nov 03 2008
BuildRequires: gcc-c++

%description
Libspf2 is an implementation of the SPF specification as found at
http://www.ietf.org/internet-drafts/draft-mengwong-spf-01.txt

%package tools
Summary: Tools distributed with libspf2
Group: Networking/Other
Requires: %name = %version-%release

%description tools
Tools distributed with libspf2; at the time of writing: spf_example,
spf_example_2mx, spfd, spfquery and spftest.

%package devel
Summary: Development files for libspf2 library
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for libspf2 library.

%prep
%setup

%build
# The configure script checks for the existence of __ns_get16 and uses the
# system-supplied version if found, otherwise one from src/libreplace.
# However, this function is marked GLIBC_PRIVATE in recent versions of glibc
# and shouldn't be called even if the configure script finds it. So we make
# sure that the configure script always uses the version in src/libreplace.
# This prevents us getting an unresolvable dependency in the built RPM.
cat > config.cache << EOF
ac_cv_func___ns_get16=no
EOF

%configure --cache-file=config.cache
# fix rpath libtool issues
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std

%files
%_libdir/lib*.so.*

%files tools
%_bindir/*
%exclude %_bindir/*_static

%files devel
%doc LICENSES
%_includedir/*
%_libdir/*.so
%exclude %_libdir/*.a

%changelog
* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.2.9-alt4
- Fix RPATH issue.

* Tue May 10 2011 Victor Forsiuk <force@altlinux.org> 1.2.9-alt3
- Rebuilt for debuginfo.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.2.9-alt2
- Rebuilt for soname set-versions.

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 1.2.9-alt1
- 1.2.9

* Mon Nov 03 2008 Victor Forsyuk <force@altlinux.org> 1.2.8-alt1
- 1.2.8
- Security fix for CVE-2008-2469.

* Tue Jul 12 2005 Victor Forsyuk <force@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Tue Jan 18 2005 Victor Forsyuk <force@altlinux.ru> 1.0.4-alt1
- Initial build for Sysiphus.
- Fix for case-sensitivity bug and "config.cache trick" from Mandrake spec.
