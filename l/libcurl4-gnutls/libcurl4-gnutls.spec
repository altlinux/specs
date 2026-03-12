%define libname3 libcurl-gnutls.so.3
%define libname4 libcurl-gnutls.so.4

%if "%_libsuff" == "64"
%define libsuffix (64bit)
%else
%define libsuffix %nil
%endif

Name: libcurl4-gnutls
Version: 8.0
Release: alt1

Summary: Libcurl-gnutls compatibility symlinks for 3rdparty applications

License: GPL-3.0+
Group: System/Libraries

ExcludeArch: %ix86

BuildRequires: libcurl
Requires: libcurl >= 8.0
Obsoletes: libcurl-gnutls-compat

Provides: %libname3%libsuffix
Provides: %libname3(CURL_GNUTLS_3)%libsuffix
Provides: libcurl3-gnutls = %EVR

Provides: %libname4%libsuffix
Provides: %libname4(CURL_GNUTLS_3)%libsuffix
# some deb packages depend on libcurl-gnutls.so.4() without arch suffix
Provides: %libname4()
Provides: libcurl-gnutls-compat = %EVR

%description
Provides libcurl-gnutls.so.3 and libcurl-gnutls.so.4 compatibility symlinks
pointing to libcurl.so.4 for 3rdparty applications (Spotify, SBIS plugin, etc.)
that depend on Debian/Ubuntu-specific libcurl-gnutls library.

In ALT Linux libcurl is already built with GnuTLS backend, so the symlink
is sufficient for ABI compatibility.

%install
mkdir -p %buildroot%_libdir/
ln -s %_libdir/libcurl.so.4 %buildroot%_libdir/%libname3
ln -s %_libdir/libcurl.so.4 %buildroot%_libdir/%libname4

%files
%_libdir/%libname3
%_libdir/%libname4


%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 8.0-alt1
- initial build for ALT Sisyphus
