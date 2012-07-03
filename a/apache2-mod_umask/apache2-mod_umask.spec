%define apache 2.0
%define oname mod_umask
Summary: Sets the Unix umask of the Apache2 webserver process after it has started.
Name: apache2-%oname
Version: 0.1.0
Release: alt2
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://www.outoforder.cc/projects/apache/mod_umask/
Source: http://www.outoforder.cc/downloads/mod_umask/mod_umask-0.1.0.tar.bz2
Source1: umask.load
Source2: umask.conf

# Automatically added by buildreq on Tue Jan 20 2009
BuildRequires: apache2-devel gcc-c++

%description
mod_umask sets the Unix umask of the Apache HTTPd process after it has started.

%prep
%setup -n %oname-%version

%build
%configure --with-apxs=%_sbindir/apxs2
%make_build
cd src
%make make_so

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
cp -L src/%oname.so %buildroot%apache2_moduledir/%oname.so
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %buildroot%apache2_mods_available

%files
%apache2_mods_available/*.load
%apache2_mods_available/*.conf
%apache2_moduledir/*.so

%changelog
* Wed Mar 02 2011 Boris Savelev <boris@altlinux.org> 0.1.0-alt2
- fix umask.conf (closes: #25183)

* Tue Jan 20 2009 Boris Savelev <boris@altlinux.org> 0.1.0-alt1
- initial build for Sisyphus
