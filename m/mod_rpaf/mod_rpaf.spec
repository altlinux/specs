# This spec is backported to ALTLinux 5.1 automatically by rpmbph script. Do not edit it.
#
%define modname rpaf
Name: mod_rpaf
Version: 0.6
Release: alt4
Summary: Apache module for reverse proxy add forward
License: GPL
Url: http://stderr.net/apache/rpaf/
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.gz
Source1: apache2-%name-load.conf.in
Source2: apache2-%name.conf

Patch0: mod_rpaf-%version-register.patch
# Debian patches
Patch40: 040_multiple_hostnames.patch
Patch100: 100_apache-2.2.patch


# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires(pre): apache-devel apache2-devel

BuildRequires: rpm-build-compat >= 0.95

%description
rpaf changes the remote address of the client visible to other Apache modules
when two conditions are satisfied. First condition is that the remote client is
actually a proxy that is defined in httpd.conf. Secondly if there is an
incoming X-Forwarded-For header and the proxy is in it's list of known proxies
it takes the last IP from the incoming X-Forwarded-For header and changes the
remote address of the client in the request structure. It also takes the
incoming X-Host header and updates the virtualhost settings accordingly. For
Apache2 mod_proxy it takes the X-Forwared-Host header and updates the
virtualhosts

%package -n apache-%name
Summary: Apache module for reverse proxy add forward
Group: System/Servers
PreReq: apache >= %apache_version-%apache_release

%package -n apache2-%name
Summary: Apache module for reverse proxy add forward
Group: System/Servers
PreReq: apache2 >= %apache2_version-%apache2_release

%description -n apache-%name
rpaf changes the remote address of the client visible to other Apache modules
when two conditions are satisfied. First condition is that the remote client is
actually a proxy that is defined in httpd.conf. Secondly if there is an
incoming X-Forwarded-For header and the proxy is in it's list of known proxies
it takes the last IP from the incoming X-Forwarded-For header and changes the
remote address of the client in the request structure. It also takes the
incoming X-Host header and updates the virtualhost settings accordingly.

%description -n apache2-%name
rpaf changes the remote address of the client visible to other Apache modules
when two conditions are satisfied. First condition is that the remote client is
actually a proxy that is defined in httpd.conf. Secondly if there is an
incoming X-Forwarded-For header and the proxy is in it's list of known proxies
it takes the last IP from the incoming X-Forwarded-For header and changes the
remote address of the client in the request structure. It also takes the
incoming X-Host header and updates the virtualhost settings accordingly. For
Apache2 mod_proxy it takes the X-Forwared-Host header and updates the
virtualhosts.
Build for apache2.

%prep
%setup -q -n %name-%version
%patch0 -p0

%patch40 -p1
%patch100 -p1

%build
%undefine __libtoolize
%apache_apxs -c -o mod_rpaf.so mod_rpaf.c
%apache2_apxs -c -o mod_rpaf.so mod_rpaf-2.0.c

%install
install -D -p -m 0644 %SOURCE1 %buildroot%apache2_mods_available/%modname.load
sed -i 's,@libdir@,%_libdir,' %buildroot%apache2_mods_available/%modname.load
install -D -p -m 0644 %SOURCE2 %buildroot%apache2_mods_available/%modname.conf
install -D -p -m 0755 .libs/%name.so %buildroot%apache2_moduledir/%name.so
install -D -p -m 0755 %name.so %buildroot%apache_moduledir/%name.so

%files -n apache-%name
%doc CHANGES README
%apache_moduledir/%name.so

%files -n apache2-%name
%doc CHANGES README
%config(noreplace) %apache2_mods_available/%modname.conf
%apache2_mods_available/%modname.load
%apache2_moduledir/%name.so

%changelog
* Wed Dec 30 2009 Boris Savelev <boris@altlinux.org> 0.6-alt4
- fix package summary (closes: #21836)

* Wed Dec 30 2009 Boris Savelev <boris@altlinux.org> 0.6-alt2.M51.3
- backport to ALTLinux 5.1 (by rpmbph script)

* Sat Dec 26 2009 Boris Savelev <boris@altlinux.org> 0.6-alt3
- drop unneeded patches

* Mon Jan 12 2009 Boris Savelev <boris@altlinux.org> 0.6-alt2
- mod_rpaf.conf is now rpaf.conf for Apache2 (fix #14614)
- add modified patches from Debian that fix (I hope) altbug #14052

* Tue Dec 02 2008 Boris Savelev <boris@altlinux.org> 0.6-alt1
- new version
- pickup from orphaned
- add build for apache

* Mon May 14 2007 L.A. Kostis <lakostis@altlinux.ru> 0.5-alt3
- fix build for new apache2.
- rename register patch to 0.5.

* Mon Mar 19 2007 L.A. Kostis <lakostis@altlinux.ru> 0.5-alt2
- x86_64 fix (closes #11145).

* Thu Mar 08 2007 L.A. Kostis <lakostis@altlinux.ru> 0.5-alt1
- Add X-Real-IP header detection.
- Initial build for ALTLinux.
