Name: cups-cloudprint
Version: 20140308
Release: alt1
Summary: Print via Google Cloud print using CUPS

License: GPLv3+
Url: http://ccp.niftiestsoftware.com
Group: System/Servers
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libcups-devel python-module-httplib2 python-module-oauth2client
Requires: cups ghostscript-cups system-config-printer ImageMagick-tools

BuildArch: noarch

%description
Google Cloud Print driver for UNIX-like operating systems.
It allows any application which prints via CUPS to print to Google Cloud 
Print directly.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std NOPERMS=1
mkdir -p %buildroot{%_bindir,%_var/log/cups}
ln -r -s %buildroot%_datadir/cloudprint-cups/setupcloudprint.py %buildroot%_bindir/setupcloudprint
touch %buildroot%_var/log/cups/cloudprint_log

%post
if [ $1 -gt 2 ] ; then
%_datadir/cloudprint-cups/upgrade.py
fi

%files
%_bindir/setupcloudprint
%_datadir/cloudprint-cups
%_prefix/lib/cups/backend/cloudprint
%_prefix/lib/cups/driver/cupscloudprint
%ghost %attr(0660,root,lp) %_var/log/cups/cloudprint_log
%exclude %_datadir/cloudprint-cups/test_*
%exclude %_datadir/cloudprint-cups/full-test.sh
%exclude %_datadir/cloudprint-cups/testfiles

%changelog
* Mon Mar 17 2014 Alexey Shabalin <shaba@altlinux.ru> 20140308-alt1
- 20140308

* Mon Oct 21 2013 Alexey Shabalin <shaba@altlinux.ru> 20131017-alt1
- inital build
