%define _unpackaged_files_terminate_build 1
%def_with check

%define cgitrc cgitrc
%define cgit_data %_datadir/%name
%define cgit_script_path %prefix/libexec
%define cgit_script_name %name
%define cgit_httpd_conf %apache2_sites_available/%name.conf
%define cgit_nginx_conf %_sysconfdir/nginx/sites-available.d/%name.conf
%define cgit_nginx_enabled_conf %_sysconfdir/nginx/sites-enabled.d/%name.conf
%define cgit_user cgit
%define cgit_group cgit
%define lua_version 5.4

Name: cgit
Version: 1.3.1
Release: alt1

Summary: A hyperfast web frontend for git repositories written in C
Url: https://git.zx2c4.com/cgit/
License: GPL-2
Group: Development/Tools

Source0: %name-%version.tar
Source1: submodules.tar
Source2: %cgitrc
Source3: generate-config.py
Source4: cgit.conf.in
Source5: httpd2.conf.in
Source6: nginx.conf.in

BuildRequires(pre): rpm-macros-apache2
BuildRequires: libzip-devel
BuildRequires: libssl-devel
BuildRequires: liblua%lua_version-devel
BuildRequires: zlib-devel
BuildRequires: rpm-build-python3

# BuildRequires for documentation
BuildRequires: asciidoc-a2x
BuildRequires: asciidoc-latex

# BuildRequires for check
%if_with check
BuildRequires: lzip
BuildRequires: unzip
BuildRequires: tidy
BuildRequires: strace
%endif

%description
This is an attempt to create a fast web interface for the Git SCM, using a
built-in cache to decrease server I/O pressure.

%package apache2
Summary: Cgit config file for Apache2
Group: Development/Tools
BuildArch: noarch
Requires(preun): apache2-base
Requires: %name = %EVR

%description apache2
%summary.

%package nginx
Summary: Cgit config file for Nginx
Group: Development/Tools
BuildArch: noarch
Requires: fcgiwrap
Requires: nginx
Requires: %name = %EVR

%description nginx
%summary.

%prep
%setup -a1

%SOURCE3 cgit-conf --in %SOURCE4 --out cgit.conf \
    --cgit-script-path %cgit_script_path \
    --cgit-script-name %cgit_script_name \
    --cgit-data %cgit_data \
    --prefix %prefix \
    --buildroot %buildroot \
    --docdir %_docdir/%name-%version

%SOURCE3 httpd2 --in %SOURCE5 --out httpd.conf \
    --apache2-moduledir %apache2_moduledir \
    --cgit-data %cgit_data \
    --cgit-script-path %cgit_script_path \
    --cgit-script-name %cgit_script_name

%SOURCE3 nginx --in %SOURCE6 --out nginx.conf \
    --cgit-data %cgit_data \
    --cgit-script-path %cgit_script_path \
    --cgit-script-name %cgit_script_name

%build
%make_build LUA_PKGCONFIG=lua%lua_version

%pre
%_sbindir/groupadd -r -f %cgit_group 2>/dev/null ||:
%_sbindir/useradd -r -M -g %cgit_group -s /dev/null -c "cgit" \
    -d /var/www/cgit %cgit_user 2>/dev/null ||:

%install
%makeinstall_std install-man install-doc

ln -fs %_licensedir/GPL-2.0 COPYING

# install example of cgitrc
install -pD %SOURCE2 %buildroot/%_sysconfdir/%cgitrc

# install httpd config file
install -Dp -m0644 httpd.conf %buildroot/%cgit_httpd_conf

# install nginx config file
install -Dp -m0644 nginx.conf %buildroot/%cgit_nginx_conf

mkdir -p %buildroot/var/www/cgit

%check
%make_build test

%post apache2
cat << EOF
----[ cgit-apache2 ]------------------------------------------------------------
  To enable cgit in Apache2:
    a2ensite cgit
    systemctl restart httpd2
--------------------------------------------------------------------------------
EOF

%preun apache2
[ $1 = 0 ] && a2dissite cgit ||:

%post nginx
cat << EOF
----[ cgit-nginx ]--------------------------------------------------------------
  To enable cgit in Nginx:
    ln -s %cgit_nginx_conf %cgit_nginx_enabled_conf
    systemctl start fcgiwrap@_nginx.socket
    systemctl restart nginx
--------------------------------------------------------------------------------
EOF

%preun nginx
[ $1 = 0 ] && rm -f %cgit_nginx_enabled_conf ||:

%files apache2
%config(noreplace) %cgit_httpd_conf

%files nginx
%config(noreplace) %cgit_nginx_conf

%files
%doc README
%doc --no-dereference COPYING
%cgit_script_path/%cgit_script_name
%cgit_data
%_target_libdir_noarch/%name
%_man5dir/%cgitrc.5*
%config(noreplace) %_sysconfdir/%cgitrc
%dir %attr(0755,%cgit_user,%cgit_group) /var/www/cgit

%changelog
* Sat Jun 13 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.
- Renamed cgitrc.example to cgitrc.
- Improved Apache2 config.
- Added cgit-nginx subpackage.

* Sat Apr 15 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.2.3-alt2
- cgitrc.example: add lines from man cgitrc example

* Sat Oct 01 2022 Alexandr Shashkin <dutyrok@altlinux.org> 1.2.3-alt1
- Initial build for sisyphus

