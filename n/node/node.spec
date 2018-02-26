%define node_name      node
%define node_version  0.6.19
%define node_release   alt4
%define npmver 1.1.24

Name: %node_name
Version: %node_version
Release: %node_release
Summary: Evented I/O for V8 Javascript
Group: Development/Tools
License: MIT License
Url: http://nodejs.org/
Source: node-source.tar
Source1: node.macros

BuildRequires: python-devel gcc-c++ openssl-devel zlib-devel
Provides: nodejs = %version-%release
Provides: node.js = %version-%release
Obsoletes: nodejs < %version-%release
Obsoletes: node.js < %version-%release

%add_python_req_skip TestCommon

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

%package -n rpm-build-%node_name
Summary:        RPM helper macros to rebuild Node.js packages
Group:          Development/Other
License:        GPL
BuildArch:      noarch
Requires: %node_name-devel = %node_version

%description -n rpm-build-%node_name
These helper macros provide possibility to rebuild
Node.js packages by some Alt Linux Team Policy compatible way.

%package devel
Summary:        Devel package for Node.js
Group:          Development/Other
License:        GPL
BuildArch:      noarch
Requires:	%node_name = %node_version gcc-c++

%description devel
Node.js header and build tools

%package -n npm
Version: %npmver
Group: Development/Tools
Summary: A package manager for node
License: MIT License
Requires: node
BuildArch: noarch
Requires: %node_name-devel = %node_version

%description -n npm
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

%prep
%setup -q -n node-source

%build
./configure --no-ssl2 \
    --prefix=/usr \
    --libdir=%_libexecdir
#    --shared-cares \
#    --shared-zlib
#    --shared-v8 \
#    --without-snapshot

%make_build
%make doc

%install
%makeinstall_std
install -d %buildroot%_sysconfdir/profile.d
echo 'export NODE_PATH="%{_libexecdir}/node_modules"' >%buildroot%_sysconfdir/profile.d/node.sh
echo 'setenv NODE_PATH %{_libexecdir}/node_modules' >%buildroot%_sysconfdir/profile.d/node.csh
chmod 0755 %buildroot%_sysconfdir/profile.d/*

mkdir -p %buildroot/%_rpmmacrosdir
cp %SOURCE1 %buildroot%_rpmmacrosdir/%node_name

subst 's,@node_name@,%node_name,'           %buildroot%_rpmmacrosdir/%node_name
subst 's,@node_version@,%node_version,'     %buildroot%_rpmmacrosdir/%node_name
subst 's,@node_release@,%node_release,'     %buildroot%_rpmmacrosdir/%node_name



%files
%doc AUTHORS ChangeLog LICENSE README.md out/doc
%_bindir/node
%dir %_libexecdir/node_modules/
%_man1dir/*.1.gz
%_sysconfdir/profile.d/*

%files devel
%_bindir/node-waf
%_includedir/node/
%_libexecdir/node/


%files -n npm
%_bindir/npm
%_libexecdir/node_modules/npm

%files -n rpm-build-%node_name
%_rpmmacrosdir/%node_name

%changelog
* Thu Jun 21 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt4
- Fix BuildRequires
- Added rpm-build-node subpackage
- Provides nodejs node.js
- Separate package devel

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt3.1
- Conflicts with node.js

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt3
- Declare NODE_PATH

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt2
- npm is noarch package

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt1
- v0.6.19
- Separate npm package

* Sat May 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.17-alt1
- v0.6.17

* Tue Apr 10 2012 Mikhail Pokidko <pma@altlinux.org> 0.6.15-alt1
- v0.6.15

* Mon Feb 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.10-alt1
- v0.6.10

* Sun Jan 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.9-alt1
- v0.6.9

* Fri Dec 02 2011 Mikhail Pokidko <pma@altlinux.org> 0.6.4-alt1
- v0.6.4

* Mon Nov 28 2011 Mikhail Pokidko <pma@altlinux.org> 0.6.3-alt1
- v0.6.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.11-alt1.1
- Rebuild with Python-2.7

* Mon Aug 22 2011 Mikhail Pokidko <pma@altlinux.org> 0.4.11-alt1
- v0.4.11

* Tue Jun 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.8-alt1
- initial

