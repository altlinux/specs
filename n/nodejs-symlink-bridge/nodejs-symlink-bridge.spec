Name: nodejs-symlink-bridge
Version: 0.0.2
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
   %buildroot%_datadir/%name/
#   /usr/lib/node_modules/nodeunit \

%files
%_datadir/%name

%changelog
* Sat Aug 27 2022 Igor Vlasenko <viy@altlinux.org> 0.0.2-alt1
- removed nodeunit

* Sat Jul 24 2021 Igor Vlasenko <viy@altlinux.org> 0.0.1-alt1
- initial build

