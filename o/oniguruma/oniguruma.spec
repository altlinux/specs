%define soversion 5
Name: oniguruma
Version: 6.8.2
Release: alt1%ubt
Summary: Regular expressions library

Group: System/Libraries
License: BSD
Url: https://github.com/kkos/oniguruma/
Source0: %name-%version.tar
# FIXME
# Don't know exactly why, however without Patch0 onig_new returns
# NULL reg variable
Patch0: oniguruma-5.9.2-onig_new-returns-NULL-reg.patch
BuildRequires(pre):rpm-build-ubt


%description
Oniguruma is a regular expressions library.
The characteristics of this library is that different character encoding
for every regular expression object can be specified.
(supported APIs: GNU regex, POSIX and Oniguruma native)

%package -n lib%name%soversion
Summary: Regular expressions library
Group: System/Libraries

%description -n lib%name%soversion
Oniguruma is a regular expressions library.
The characteristics of this library is that different character encoding
for every regular expression object can be specified.
(supported APIs: GNU regex, POSIX and Oniguruma native)

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
Requires: lib%name%soversion = %EVR
Provides: libOniGuruma-devel = %EVR
Provides: %name-devel = %EVR
Obsoletes: %name-devel
Obsoletes: libOniGuruma-devel

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
( cd src
%patch0 -p1 -b .nullreg
)
%__sed -i.multilib -e 's|-L@libdir@||' onig-config.in

for f in \
	README.ja \
	doc/API.ja \
	doc/FAQ.ja \
	doc/RE.ja
	do
	iconv -f EUC-JP -t UTF-8 $f > $f.tmp && \
		( touch -r $f $f.tmp ; %__mv -f $f.tmp $f ) || \
		%__rm -f $f.tmp
done

%build
autoreconf -fisv
%configure \
    --disable-silent-rules \
	--disable-static \
	--with-rubydir=%_bindir
%__make

%install
%__make install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="%__install -c -p"
find $RPM_BUILD_ROOT -name '*.la' \
	-exec %__rm -f {} ';'

%check
%__make check

%files -n lib%name%soversion
%doc	AUTHORS COPYING HISTORY README index.html
%_libdir/libonig.so.%{soversion}*

%files -n lib%name-devel
%doc	doc/API doc/FAQ doc/RE
%_bindir/onig-config
%_libdir/libonig.so
%_includedir/onig*.h
%_libdir/pkgconfig/%name.pc

%changelog
* Fri May 04 2018 Anton Farygin <rider@altlinux.ru> 6.8.2-alt1%ubt
- new version

* Thu Apr 05 2018 Anton Farygin <rider@altlinux.ru> 6.8.1-alt1%ubt
- new version
- the library package was renamed for compatability with ALT Linux shared policy

* Mon Jan 29 2018 Anton Farygin <rider@altlinux.ru> 6.7.1-alt1%ubt
- new version

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 6.6.1-alt1%ubt
- new version

* Wed Jul 12 2017 Anton Farygin <rider@altlinux.ru> 6.4.0-alt1%ubt
- new version with security fixes (CVE-2017-9224, CVE-2017-9225, CVE-2017-9226, CVE-2017-9227, CVE-2017-9228, CVE-2017-9229)

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 6.2.0-alt2%ubt
- added obsolete for libOniGuruma-devel to devel package

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 6.2.0-alt1%ubt
- first build for ALT, based on RH spec
