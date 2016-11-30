%define modname mod_auth_gssapi
%define module_name auth_gssapi

Name: apache2-%modname
Version: 1.4.1
Release: alt1

Summary: A GSSAPI Authentication module for Apache2
Group: System/Servers
License: %mit
Url: https://github.com/modauthgssapi/mod_auth_gssapi

Source: %modname-%version.tar
Source1: %module_name.load
Patch: %modname-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: apache2-devel
BuildRequires: libssl-devel libkrb5-devel gssntlmssp-devel libaprutil1-devel

Requires: apache2

Provides: %modname

%define _unpackaged_files_terminate_build 1

%description
The mod_auth_gssapi module is an authentication service that implements
the SPNEGO based HTTP Authentication protocol defined in RFC4559.

%prep
%setup -n %modname-%version
%patch -p1

%build
%autoreconf
%configure \
	--with-apxs=%apache2_apxs
%make_build

%install
%makeinstall_std
install -d -m 755 %buildroot%apache2_mods_available
install -p -m 644 -- %SOURCE1 %buildroot%apache2_mods_available/%module_name.load

%files
%doc COPYING README
%apache2_libexecdir/%modname.so
%config %apache2_mods_available/%module_name.load

%exclude %apache2_libexecdir/*.la

%changelog
* Wed Nov 30 2016 Mikhail Efremov <sem@altlinux.org> 1.4.1-alt1
- 1.4.1.

* Fri Jul 29 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Initial build.

