%define apache 2.0
%define oname mod_limitipconn
Summary: Limit simultaneous connections by an IP address
Name: apache2-%oname
Version: 0.24
Release: alt1
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://dominia.org/djao/limitipconn2.html
Source: http://dominia.org/djao/limit/mod_limitipconn-0.24.tar.bz2
Source1: limitipconn.load
Source2: limitipconn.conf

# Automatically added by buildreq on Tue Jan 20 2009
BuildRequires: apache2-devel

%description
The mod_limitipconn module lets you enforce limits on the number of
simultaneous downloads allowed from a single IP address. You can also
control which MIME types are affected by the limits.

%prep
%setup -n %oname-%version
subst 's|APXS=apxs|#APXS=apxs|g' Makefile

%build
export APXS=%apache2_apxs
%make_build

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
install -m 644 .libs/%oname.so %buildroot%apache2_moduledir/%oname.so
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %buildroot%apache2_mods_available

%files
%doc ChangeLog README
%apache2_mods_available/*.load
%apache2_mods_available/*.conf
%apache2_moduledir/*.so

%changelog
* Wed Apr 27 2016 Sergey Alembekov <rt@altlinux.ru> 0.24-alt1
- new version 0.24
- rebuild with apache-2.4

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.23-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jan 20 2009 Boris Savelev <boris@altlinux.org> 0.23-alt1
- initial build for Sisyphus
