Name: nodejs-symlink-bridge
Version: 0.0.1
Summary: force node packages to provide node_modules symlinks
License: ALT-MIT
Packager: Igor Vlasenko <viy@altlinux.org>
Group: Development/Other
Release: alt1
BuildArch: noarch

BuildRequires: node-yargs node-nodeunit

%description
Temporary package to keep symlink provides alive.

%prep
%build
%install
mkdir -p %buildroot%_datadir/%name/
ln -s \
   /usr/lib/node_modules/yargs \
   /usr/lib/node_modules/nodeunit \
   %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Sat Jul 24 2021 Igor Vlasenko <viy@altlinux.org> 0.0.1-alt1
- initial build

