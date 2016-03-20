# SPEC file for aerospike-server
#

Name:     aerospike-server
Version:  3.7.4.1
Release:  alt1

Summary: Aerospike Database Server

Group:    Databases
License:  %gagpl3only
URL:      https://github.com/aerospike/aerospike-server
Packager: Nikolay Fetisov <naf@altlinux.ru>

# Aerospike can't be used on 32bit systems
ExclusiveArch: x86_64
#BuildArch: x86_64

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

# Submodules:
## URL:  https://github.com/aerospike/aerospike-common
Source1: aerospike-common.tar
## URL:  https://github.com/aerospike/asmalloc
Source2: asmalloc.tar
## URL:  https://github.com/aerospike/jansson
Source3: jansson.tar
## URL:  https://github.com/aerospike/jemalloc
Source4: jemalloc.tar
## URL:  https://github.com/aerospike/aerospike-lua-core
Source5: aerospike-lua-core.tar
## URL:  https://github.com/aerospike/luajit
Source6: luajit.tar
## URL:  https://github.com/aerospike/aerospike-mod-lua
Source7: aerospike-mod-lua.tar
## URL:  https://github.com/aerospike/s2-geometry-library
Source8: s2-geometry-library.tar

######
SOURCE101: %name.sysconfig
SOURCE102: %name.init
SOURCE103: %name.logrotate
SOURCE104: %name.conf

Patch1:  aerospike-server-3.6.3-alt-build_version.patch


BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Sun Mar 20 2016
# optimized out: gnu-config python-base python-modules python3 python3-base
BuildRequires: gcc-c++ glibc-devel-static libssl-devel libstdc++-devel python-module-distribute python-module-google xsltproc zlib-devel


# Skip optional configuration script /etc/aerospike/initfns from Requires:
%add_findreq_skiplist */asd-systemd-helper

%description
Aerospike is a distributed, scalable NoSQL database. It is architected
with three key objectives:
- To create a high-performance, scalable platform that would meet
  the needs of today's web-scale applications
- To provide the robustness and reliability (ie, ACID) expected from
  traditional databases.
- To provide operational efficiency (minimal manual involvement)

%define as_name  aerospike
%define as_dir   %_localstatedir/%as_name
%define as_user  _aerospike
%define as_group _aerospike


%prep
%setup  -n %name-%version
%patch0 -p1

# Submodules:
pushd modules/common;   tar xf %SOURCE1; popd
pushd modules/asmalloc; tar xf %SOURCE2; popd
pushd modules/jansson;  tar xf %SOURCE3; popd
pushd modules/jemalloc; tar xf %SOURCE4; popd
pushd modules/lua-core; tar xf %SOURCE5; popd
pushd modules/luajit;   tar xf %SOURCE6; popd
pushd modules/mod-lua;  tar xf %SOURCE7; popd
pushd modules/s2-geometry-library;  tar xf %SOURCE8; popd

### Well, time to fix things....
# Fix os and version detection scripts
%patch1 -p0
sed -e 's/@@VERSION@@/%version/g' -i build/gen_version

# ... and pkg/rpm/Makefile
sed -e 's/el7/alt/g' -i pkg/rpm/Makefile

# Fix Makefile for mod-lua submodule
# See https://github.com/aerospike/aerospike-mod-lua/pull/1 for details
# Note about double %% - RPM shall eats one of it
sed -e 's#(TARGET_INCL)/aerospike/\*.h#(HEADERS)#' -i modules/mod-lua/Makefile
sed -e '/mod_lua_val.o/ a\\nAEROSPIKE-HEADERS = $(patsubst $(SOURCE_INCL)/aerospike/%%.h,%%.h,$(wildcard $(SOURCE_INCL)/aerospike/*.h))\n\nHEADERS =\nHEADERS += $(AEROSPIKE-HEADERS:%%=$(TARGET_INCL)/aerospike/%%)\n' -i modules/mod-lua/Makefile


###
# Default location in /opt/aerospike. Move thing out of it...

# Work directory:
sed -e '/work_directory/ s#/opt/aerospike#%{as_dir}#' -i as/src/base/cfg.c
sed -e 's#file /opt/aerospike#file %{as_dir}#'        -i as/etc/*.conf
sed -e '/work-directory/ s#/opt/aerospike#%{as_dir}#' -i tools/fixownership/fixownership.py

# Lua system and user path:
sed -e '/mod_lua\.system_path/ s#/opt/aerospike/sys#%_datadir/%{as_name}#' -i as/src/base/cfg.c
sed -e 's#/opt/aerospike/sys#%_datadir/%{as_name}#'                        -i modules/mod-lua/src/main/mod_lua.c

sed -e '/mod_lua\.user_path/ s#/opt/aerospike/usr#%{as_dir}#'           -i as/src/base/cfg.c
sed -e 's#/opt/aerospike/usr#%{as_dir}#'                                -i modules/mod-lua/src/main/mod_lua.c
sed -e 's#/opt/aerospike/usr#%{as_dir}#'                                -i tools/fixownership/fixownership.py

# User and group:
sed -e '/^User/ s/root/$AS_USER/' -e '/^Group/ s/root/$AS_GROUP/' -i as/etc/aerospike-server.service
sed -e '/user/ s/root/%as_user/'  -e '/group/ s/root/%as_group/'  -i as/etc/*.conf


%build
# All build options in the make_in/Makefile.vars file
%make LD_CRYPTO=dynamic

%install
# Prepare layout for RPM packaging
%make -C pkg/rpm/ EDITION=community BUILD_ROOT=%buildroot VER=%version OPT_AS=%buildroot%as_dir dist

# There are no AGPL license in %%_licensedir - replacing only ASL one
mv -f -- LICENSE-APACHE LICENSE.orig
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE-APACHE) LICENSE-APACHE

## License file placed in the %%doc dir
rm -rf -- %buildroot%as_dir/doc

## System and user Lua scripts
mkdir -p -- %buildroot%_datadir/%as_name
mv --  %buildroot%as_dir/sys/* %buildroot%_datadir/%as_name
mv --  %buildroot%as_dir/usr/* %buildroot%as_dir/
rmdir -- %buildroot%as_dir/usr

## sysconfig file
rm -f -- %buildroot%_sysconfdir/sysconfig/%as_name
install -m 0640 -- %SOURCE101 %buildroot%_sysconfdir/sysconfig/%name
sed -e 's/@@USER@@/%as_user/' -e 's/@@GROUP@@/%as_group/' -i %buildroot%_sysconfdir/sysconfig/%name

## systemd files
mkdir -p -- %buildroot%_unitdir
mv -f -- %buildroot/usr/lib/systemd/system/%as_name.service %buildroot%_unitdir/%name.service

## init script
mkdir -p --  %buildroot%_initdir/
install -m 0755 -- %SOURCE102  %buildroot%_initdir/%name

# Pid file directory
rm -f -- %buildroot%_sysconfdir/tmpfiles.d/%as_name.conf
echo "d /var/run/%as_name 0775 root %as_user - " > %buildroot%_sysconfdir/tmpfiles.d/%name.conf
mkdir -p -- %buildroot/var/run/%name

# logrotate file
rm -f -- %buildroot%_sysconfdir/logrotate.d/%as_name
install -m 664 -- %SOURCE103 %buildroot%_sysconfdir/logrotate.d/%name


# Default configuration files
for f in %buildroot%_sysconfdir/%as_name/*.conf; do
  mv -- ${f} ${f}.dist
done
install -m 664 -- %SOURCE104 %buildroot%_sysconfdir/%as_name/aerospike.conf
sed -e 's/@@AS_USER@@/%as_user/'  -e 's/@@AS_GROUP@@/%as_group/' \
    -i  %buildroot%_sysconfdir/%as_name/aerospike.conf

# Log directory
mkdir -p -- %buildroot/var/log/%as_name


%pre
# Add the "_aerospike" user
%_sbindir/groupadd -r -f %as_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %as_group -c 'Aerospike Database Server daemon' \
        -s /dev/null -d /dev/null %as_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name


%files
%doc README.md LICENSE LICENSE-AGPL
%doc --no-dereference LICENSE-APACHE

%_bindir/*
%_datadir/%{as_name}*

%attr(0750,root,%as_group) %dir %_sysconfdir/%as_name
%config(noreplace)  %_sysconfdir/%as_name/*.conf
%config             %_sysconfdir/%as_name/*.conf.dist
%config(noreplace)  %_sysconfdir/sysconfig/%name

%config(noreplace)  %_sysconfdir/logrotate.d/%name

%config             %_sysconfdir/tmpfiles.d/%name.conf

%config   %_initdir/%name
%_unitdir/%name.service
%dir  %_sysconfdir/systemd/system/aerospike.service.d
%config(noreplace) %_sysconfdir/systemd/system/aerospike.service.d/*

%ghost %attr(0775,root,%as_group) %dir /var/run/%name
       %attr(0775,root,%as_group) %dir /var/log/%as_name

%attr(0750,root,%as_group) %dir %as_dir
%attr(3770,root,%as_group) %dir %as_dir/data
%attr(3770,root,%as_group) %dir %as_dir/smd
%attr(0750,root,%as_group) %dir %as_dir/udf
%attr(0750,root,%as_group) %dir %as_dir/udf/lua


%changelog
* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.7.4.1-alt1
- Initial build for ALT Linux Sisyphus

