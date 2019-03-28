%define node_modules %_libexecdir/node_modules

Name: azure-sdk-for-node
Version: 2.2.1
Release: alt1.preview2017

Summary: Windows Azure Client Library for node

Group: Development/Other
License: Apache-2.0
Url: https://github.com/Azure/azure-sdk-for-node

# Source0-url: https://github.com/Azure/azure-sdk-for-node/archive/2.2.1-preview-October2017.tar.gz
Source0: %name-%version.tar

Source1: %name-predownloaded-%version.tar

BuildArch: noarch

BuildRequires: npm node

Provides: node-azure = %version-%release

AutoReq:yes,nonodejs
AutoProv:yes,nonodejs

%description
Windows Azure SDK for Node.js and Linux client toold.

%prep
%setup -a1
# /usr/lib/rpm/nodejs.req supports only numerical versions there
subst "s|file:../../ms-rest|*|" runtime/ms-rest-azure/test/package.json

%install
#mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%node_modules/azure/
cp -a examples lib runtime node_modules test package.json README.md %buildroot/%node_modules/azure/
rm -f %buildroot/%node_modules/azure/node_modules/sax/examples/switch-bench.js
rm -f %buildroot/%node_modules/azure/node_modules/sinon/build
rm -f %buildroot/%node_modules/azure/node_modules/sinon/step-tests
rm -f %buildroot/%node_modules/azure/node_modules/streamline/examples/misc/shebang.sh
rm -rf %buildroot/%node_modules/azure/node_modules/adal-node/test/

#ln -s "../lib/node_modules/azure/bin/azure" %buildroot/%_bindir/azure

%files
#_bindir/azure
%node_modules/azure/

%changelog
* Thu Mar 28 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1.preview2017
- new version (2.2.1) with rpmgs script

* Wed Apr 03 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt3
- Fix build with new node version

* Fri Jul 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2
- merge upstream 6f210e9

* Wed Jul 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Fri Jun 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1
- initial
