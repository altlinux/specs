%define libmajor 1
%define libname libwget
%define devname	libwget-devel

Name:		wget2
Summary:	The successor of GNU Wget, a file and recursive website downloader
Version:	2.0.0
Release:	alt2
License:	%gpl3plus
Group:		Networking/WWW
Url:		https://gitlab.com/gnuwget/wget2
Source0:	https://ftp.gnu.org/gnu/wget/wget2-%{version}.tar.gz

BuildRequires(pre):	rpm-build-licenses
BuildRequires: doxygen
BuildRequires: libgpgme-devel
BuildRequires: bzlib-devel
BuildRequires: libgnutls-devel
BuildRequires: libbrotli-devel
BuildRequires: libidn2-devel
BuildRequires: libnghttp2-devel
BuildRequires: libpcre2-devel
BuildRequires: libpsl-devel

%description
GNU Wget2 is the successor of GNU Wget, a file and recursive website downloader.

Designed and written from scratch it wraps around libwget, that provides the basic
functions needed by a web client.

Wget2 works multi-threaded and uses many features to allow fast operation.

In many cases Wget2 downloads much faster than Wget1.x due to HTTP2, HTTP compression,
parallel connections and use of If-Modified-Since HTTP header.

%package -n %{libname}
Summary:	Shared libraries for wget2
Group:		System/Libraries
License:	%lgpl3plus

%description -n %{libname}
Shared libraries for wget2 providing the basic functions needed by a web client.

%package -n %{devname}
Summary:	Development files for wget2
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libwget2-devel = %{version}-%{release}
Provides:	wget2-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development libraries and headers for wget2.

%prep

%setup

%build
%autoreconf
%configure \
    --disable-static 
#    --disable-rpath \
#    --with-openssl=no \
#    --with-ssl=gnutls \
#    --without-libhsts \
#    --without-libidn \
#    --without-pcre
%make_build

%install
%makeinstall_std

# man page
install -Dpm644 docs/man/man1/wget2.1 %buildroot%_mandir/man1/wget2.1

# we don't want these
find %buildroot -name "*.la" -delete

# not needed
rm -rf %buildroot%_bindir/wget2_noinstall

%find_lang %{name}

%check
%make_build check

%files -f %{name}.lang
%doc README* NEWS COPYING
%_bindir/wget2
%_mandir/man1/wget2.1*

%files -n %{libname}
%doc COPYING.LESSER
%_libdir/libwget*.so.%{libmajor}*

%files -n %{devname}
%_includedir/wget*.h
%_libdir/libwget*.so
%_libdir/pkgconfig/libwget.pc
%_mandir/man3/libwget-*.3*

%changelog
* Thu Oct 21 2021 Pavel Vasenkov <pav@altlinux.org> 2.0.0-alt2
- Build for Sisyphus (closes #41170)

* Thu Oct 14 2021 Anton Shevtsov <x09@altlinux.org> <shevtsov.anton@gmail.com> 2.0.0-alt1
- Init wget2 build
