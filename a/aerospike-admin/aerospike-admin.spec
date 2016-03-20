# SPEC file for aerospike-admin
#

Name:     aerospike-admin
Version:  0.0.17
Release:  alt1

Summary: Aerospike Administration tool

Group:    Databases
License:  %asl 2.0
URL:      https://github.com/aerospike/aerospike-admin
Packager: Nikolay Fetisov <naf@altlinux.ru>

BuildArch: noarch

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch


BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Sun Nov 08 2015
# optimized out: python-base rsync
BuildRequires: git-core python-module-distribute python-module-google zip

%description
Aerospike Administration tool allows operations to view vital stats
of the Aerospike server from the command line.

%prep
%setup  -n %name-%version
%patch0 -p1

%build
%make

%install
#%make INSTALL_ROOT=%buildroot%_bindir/ \
#      INSTALL_USER=$(/usr/bin/id -nu)  \
#      INSTALL_GROUP=$(/usr/bin/id -ng) \
#      SYMLINK=%buildroot%_bindir/%name.tmp \
#      install
#rm -f -- %buildroot%_bindir/%name.tmp

mkdir -p -- %buildroot%_bindir %buildroot%python_sitelibdir
cp -a -- build/tmp/asadm %buildroot%python_sitelibdir/asadm
ln -s -- %python_sitelibdir/asadm/asadm.py %buildroot%_bindir/asadm

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE) LICENSE

%files
%doc README.md
%doc --no-dereference LICENSE

%_bindir/asadm
%python_sitelibdir/asadm*

%changelog
* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.17-alt1
- Initial build for ALT Linux Sisyphus

