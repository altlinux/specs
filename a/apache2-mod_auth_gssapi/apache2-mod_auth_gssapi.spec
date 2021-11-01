%define _unpackaged_files_terminate_build 1

%define modname mod_auth_gssapi
%def_with check

Name: apache2-%modname
Version: 1.6.3
Release: alt2

Summary: A GSSAPI Authentication module for Apache2
Group: System/Servers
License: %mit
Url: https://github.com/modauthgssapi/mod_auth_gssapi

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): apache2-devel

BuildRequires: libssl-devel
BuildRequires: libkrb5-devel >= 1.15
BuildRequires: libaprutil1-devel
BuildRequires: gssntlmssp-devel
BuildRequires: flex

%if_with check
BuildRequires: words
BuildRequires: krb5-kdc
BuildRequires: socket_wrapper
BuildRequires: nss_wrapper
BuildRequires: openssl
BuildRequires: apache2-httpd-prefork
BuildRequires: apache2-mod_cache_disk
BuildRequires: apache2-suexec
BuildRequires: python3-module-requests-gssapi
%endif

Provides: %modname = %EVR

Requires: apache2 >= %apache2_version
Requires: libkrb5 >= 1.15

%description
The mod_auth_gssapi module is an authentication service that implements
the SPNEGO based HTTP Authentication protocol defined in RFC4559.

%prep
%setup
%patch -p1

%build
sed -si 's,^\(#!.* \)\(python\)$,\1python3,' tests/*.py
%autoreconf
%configure
%make_build

%install
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%apache2_libexecdir
install src/.libs/%modname.so %buildroot%apache2_libexecdir
echo "LoadModule auth_gssapi_module modules/mod_auth_gssapi.so" > %buildroot%apache2_mods_available/auth_gssapi.load

%check
%make test

%files
%doc COPYING README
%apache2_libexecdir/%modname.so
%config(noreplace) %apache2_mods_available/auth_gssapi.load

%changelog
* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 1.6.3-alt2
- Fixed FTBFS (requests-2.26).

* Thu Aug 06 2020 Stanislav Levin <slev@altlinux.org> 1.6.3-alt1
- 1.6.2 -> 1.6.3.

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 1.6.2-alt1
- 1.6.1 -> 1.6.2.

* Sun Oct 6 2019 Anton Farygin <rider@altlinux.org> 1.6.1-alt3
- build with python3

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 1.6.1-alt2
- Build with new openssl1.1.

* Fri May 04 2018 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.6.0 -> 1.6.1

* Tue Nov 14 2017 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.4.1 -> 1.6.0

* Wed Nov 30 2016 Mikhail Efremov <sem@altlinux.org> 1.4.1-alt1
- 1.4.1.

* Fri Jul 29 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Initial build.

