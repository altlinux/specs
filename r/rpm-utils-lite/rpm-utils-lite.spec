Name: rpm-utils-lite
Version: 0.9.12
Release: alt2
BuildArch: noarch

Summary: Portions from full blown rpm-utils
License: GPL
Group: Development/Other

Requires: getopt, time
Requires: mktemp >= 1:1.3.1
# strace version that works properly without -F/-k options
Requires: strace >= 4.5.18-alt5

BuildRequires: rpm-utils

%description
This package contains following utilities:
+ stamp_spec.lite - generates timestamp for rpm specfile changelog entry;
+ add_changelog.lite - generates and adds changelog entry to rpm specfile;

Instead of rpm-utils, it does not require rpm-build

%prep

%build

%install
mkdir -p %buildroot/%_bindir/

cp %_bindir/stamp_spec %buildroot/%_bindir/stamp_spec.lite
cp %_bindir/add_changelog %buildroot/%_bindir/add_changelog.lite

sed -i 's,stamp_spec,stamp_spec.lite,' %buildroot/%_bindir/add_changelog.lite

%files
%_bindir/*

%changelog
* Thu Mar 10 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.12-alt2
- noarch

* Thu Mar 10 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.12-alt1
- initial build for Sisyphus, based on rpm-utils 0.9.12-alt1
