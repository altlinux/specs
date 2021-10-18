Name: libsieve
Version: 2.2.5
Release: alt3

Summary: Standalone library providing an interpreter for RFC 3028 Sieve and various extensions
License: CMU and LGPL
Group: Development/Other
Packager: Eugene Prokopiev <enp@altlinux.ru>

URL: http://libsieve.sf.net/
Source: %name-%version.tar.gz

%package -n %name-devel
Summary: Standalone library providing an interpreter for RFC 3028 Sieve and various extensions
License: CMU and LGPL
Group: Development/Other
Requires: %name = %version-%release

%description
This is a standalone library providing an interpreter for RFC 3028 Sieve
and various extensions. It is based upon code distributed with the Cyrus Mail
Server prior to CMU's switch to a more restrictive license. The libSieve API
attempts to be easy to use and extensible, and replaces the more rigid API in
the Cyrus Sieve implementation.

%description -n %name-devel
This is a standalone library providing an interpreter for RFC 3028 Sieve
and various extensions. It is based upon code distributed with the Cyrus Mail
Server prior to CMU's switch to a more restrictive license. The libSieve API
attempts to be easy to use and extensible, and replaces the more rigid API in
the Cyrus Sieve implementation.

%prep
%setup

%build
cd libsieve2/src
./bootstrap
%add_optflags -fcommon
%configure
%make_build

%install

# adjust $RPM_BUILD for install
mkdir -p %buildroot/%_includedir
mkdir -p %buildroot/%_libdir
mkdir -p %buildroot/%_docdir/%name-%version

# package docs
cd libsieve2
install -m 0644 AUTHORS %buildroot/%_docdir/%name-%version
install -m 0644 COPYING %buildroot/%_docdir/%name-%version
install -m 0644 NEWS %buildroot/%_docdir/%name-%version
install -m 0644 README %buildroot/%_docdir/%name-%version

# make install
cd src
%makeinstall

rm -rf %buildroot%_libdir/*.a

%files
%_libdir/%name.so.?*
%doc %_docdir/%name-%version/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way.
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/libsieve-%version

%files -n %name-devel
%_includedir/*.h
%_libdir/%name.so

%changelog
* Mon Oct 18 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.5-alt3
- Fixed FTBFS.

* Wed Apr 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.5-alt2
- Fixed FTBFS with -fcommon.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.5-alt1.qa2
- NMU: rebuilt for debuginfo.

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libsieve
  * postun_ldconfig for libsieve
  * docdir-is-not-owned for libsieve
  * postclean-05-filetriggers for spec file

* Fri Apr 13 2007 Eugene Prokopiev <enp@altlinux.ru> 2.2.5-alt1
- new version

* Fri Dec 15 2006 Eugene Prokopiev <enp@altlinux.ru> 2.2.4-alt1
- Initial build
