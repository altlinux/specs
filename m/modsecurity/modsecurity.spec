# SPEC file for ModSecurity package

%def_enable static

Name:    modsecurity
Version: 3.0.8
Release: alt1

Summary: web application firewall (WAF) engine
Group: Security/Networking
License: %asl
Url: https://github.com/SpiderLabs/ModSecurity
#Url: https://www.modsecurity.org

Source0: %name-%version.tar
Source1: submodules-%version.tar
Patch0:  %name-%version-%release.patch

Source2: %name.conf
Source3: %name.logrotate

BuildRequires(pre): rpm-build-licenses rpm-macros-webserver-common


# Automatically added by buildreq on Fri Jul 16 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libsasl2-3 libstdc++-devel perl pkg-config python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: doxygen gcc-c++ libGeoIP-devel libcurl-devel libpcre-devel libxml2-devel lua-devel
%{?_enabled_static:BuildRequires: glibc-devel-static}

%description
ModSecurity is an open source, cross platform web application
firewall (WAF) engine for Apache, IIS and Nginx that is developed
by Trustwave's SpiderLabs. It has a robust event-based programming
language which provides protection from a range of attacks against
web applications and allows for HTTP traffic monitoring, logging
and real-time analysys.

%package -n lib%{name}
Summary: libmodsecurity web application firewall framework library
Group: System/Libraries

Requires(pre): webserver-common

%description -n lib%{name}
ModSecurity is an open source, cross platform web application
firewall (WAF) engine for Apache, IIS and Nginx that is developed
by Trustwave's SpiderLabs.

This package contains libmodsecurity web application firewall
framework shared library.


%package -n lib%{name}-devel
Summary: libmodsecurity web application firewall framework development package
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%{name}-devel
This package contains development library and header files needed for
developing applications that use ModSecurity web application firewall
framework libmodsecurity library.


%if_enabled static
%package -n lib%{name}-devel-static
Summary: libmodsecurity web application firewall framework static library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%{name}-devel-static
This package contains static version of libmodsecurity library.
%endif


%prep
%setup
%patch0 -p1

tar -x  -f %SOURCE1

mv -f -- LICENSE LICENSE.Apache-2.0
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE) LICENSE

%build
# LTO support for static libraries
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%autoreconf
%configure %{?_disabled_static:--disable-static}

%make_build

%install
%makeinstall_std

# Default configuration
install -pD -m644 %SOURCE2         %buildroot%_sysconfdir/%name/%name.conf
install -pD -m644 unicode.mapping  %buildroot%_sysconfdir/%name/unicode.mapping

# Temporary files, logs, etc...
mkdir -p -- %buildroot%_spooldir/%name/{tmp,data,upload}
mkdir -p -- %buildroot%_logdir/%name/audit

# Logrotate configuration
install -d %buildroot%_logrotatedir
install -m 640 %SOURCE3 %buildroot%_logrotatedir/%name


%files
%doc  README.md AUTHORS CHANGES
%doc  --no-dereference LICENSE
%_bindir/modsec-rules-check

%files -n lib%{name}
%doc  README.md AUTHORS CHANGES
%doc  --no-dereference LICENSE
%_libdir/*.so.*

%attr(0750,root,%webserver_group) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%config            %_sysconfdir/%name/unicode.mapping

%attr(0750,root,%webserver_group) %dir %_spooldir/%name
%attr(2770,root,%webserver_group) %dir %_spooldir/%name/tmp
%attr(2770,root,%webserver_group) %dir %_spooldir/%name/data
%attr(2770,root,%webserver_group) %dir %_spooldir/%name/upload

%attr(2770,root,%webserver_group) %dir %_logdir/%name
%attr(2770,root,%webserver_group) %dir %_logdir/%name/audit

%config %_logrotatedir/%name

%files -n lib%{name}-devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc


%if_enabled static
%files -n lib%{name}-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Dec 06 2022 Nikolay A. Fetisov <naf@altlinux.org> 3.0.8-alt1
- New version

* Sun Nov 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.0.6-alt1
- New version

* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.0.5-alt2
- Fix build with LTO flags
- Update project URL

* Fri Jul 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.0.5-alt1
- Initial build for ALT Linux Sisyphus
