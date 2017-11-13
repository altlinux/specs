%define _unpackaged_files_terminate_build 1

Name: apache2-mod_lookup_identity
Version: 1.0.0
Release: alt1%ubt
License: ASL 2.0 
Group: System/Servers
Summary: Apache module to retrieve additional information about the authenticated user
Url: http://www.adelton.com/apache/mod_lookup_identity/
Source0: %name-%version.tar
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): apache2-devel
BuildRequires: libdbus-devel
BuildRequires: pkgconfig
BuildRequires: libapr1-devel
Provides: mod_lookup_identity = %EVR

Requires: apache2 >= %apache2_version

%description
mod_lookup_identity can retrieve additional pieces of information
about user authenticated in Apache httpd server and store these values
in notes/environment variables to be consumed by web applications.
Use of REMOTE_USER_* environment variables is recommended.

%prep
%setup

%build

%apache2_apxs -c $(pkg-config --cflags dbus-1) $(pkg-config --libs dbus-1) \
	-Wc,"-Wall -pedantic -std=c99" mod_lookup_identity.c

%install
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%apache2_moduledir
echo "LoadModule lookup_identity_module modules/mod_lookup_identity.so" > %buildroot%apache2_mods_available/lookup_identity.load
install -m 644 lookup_identity.conf %buildroot%apache2_mods_available/lookup_identity.conf
install -m 644 .libs/mod_lookup_identity.so %buildroot%apache2_moduledir/mod_lookup_identity.so

%files
%doc README LICENSE
%config(noreplace) %apache2_mods_available/lookup_identity.conf
%config(noreplace) %apache2_mods_available/lookup_identity.load
%apache2_moduledir/mod_lookup_identity.so

%changelog
* Mon Nov 13 2017 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1%ubt
- Initial build
