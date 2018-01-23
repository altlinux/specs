Name:		apache2-mod_http2
Version:	1.10.14
Release:	alt1%ubt
Summary:	module implementing HTTP/2 for Apache 2
Group:		System/Servers
License:	ASL 2.0
URL:		https://icing.github.io/mod_h2/
Source0:	%name-%version.tar
Source1:	%name.watch
Patch0:		%name-%version-alt.patch
BuildRequires(pre): apache2-devel > 2.4.27-alt1, rpm-build-ubt
BuildRequires:	pkgconfig, libnghttp2-devel >= 1.7.0, libssl-devel >= 1.0.2, libaprutil1-devel
Provides: mod_h2 = %EVR
Provides: mod_http2 = %EVR

%description
The mod_h2 Apache httpd module implements the HTTP2 protocol (h2+h2c) on
top of libnghttp2 for httpd 2.4 servers.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf -fisv
%configure
%make

%install
make DESTDIR=%{buildroot} install
rm -rf %buildroot/etc/httpd/share/doc/

# remove links and rename SO files
rm -r %buildroot%apache2_moduledir/mod_http2.so
rm -r %buildroot%apache2_moduledir//mod_proxy_http2.so
mv %buildroot%apache2_moduledir/mod_http2.so.0.0.0 %buildroot%apache2_moduledir/mod_http2.so
mv %buildroot%apache2_moduledir/mod_proxy_http2.so.0.0.0 %buildroot%apache2_moduledir/mod_proxy_http2.so

# create configuration
mkdir -p %buildroot%apache2_mods_available
echo "LoadModule http2_module modules/mod_http2.so" > %buildroot%apache2_mods_available/%name.load
echo "LoadModule proxy_http2_module modules/mod_proxy_http2.so" > %buildroot%apache2_mods_available/mod_proxy_http2.load

%files
%doc README README.md ChangeLog AUTHORS LICENSE
%apache2_mods_available/*.load 
%apache2_moduledir/mod_http2.so
%apache2_moduledir/mod_proxy_http2.so

%changelog
* Wed Jan 10 2018 Anton Farygin <rider@altlinux.ru> 1.10.14-alt1%ubt
- new version

* Wed Nov 01 2017 Anton Farygin <rider@altlinux.ru> 1.10.13-alt1%ubt
- new version

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 1.10.12-alt1%ubt
- new version

* Wed Jul 19 2017 Anton Farygin <rider@altlinux.ru> 1.10.7-alt1%ubt
- first build for ALT
