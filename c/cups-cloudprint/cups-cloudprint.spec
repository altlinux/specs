Name: cups-cloudprint
Version: 20131017
Release: alt1
Summary: Google Cloud Print driver for CUPS, allows printing to printers hosted on Google Cloud Print

License: GPLv3+
Url: http://ccp.niftiestsoftware.com
Group: System/Servers
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libcups-devel python-module-httplib2 python-module-oauth2client
Requires: cups ghostscript-cups system-config-printer ImageMagick-tools

BuildArch: noarch

%description
Google Cloud Print driver for CUPS, allows printing to printers hosted on Google Cloud Print.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std NOPERMS=1
mkdir -p %buildroot{%_bindir,%_sysconfdir}
install -Dpm 640 cloudprint.conf.example %buildroot%_sysconfdir/cups/cloudprint.conf
ln -r -s %buildroot%_prefix/lib/cloudprint-cups/setupcloudprint.py %buildroot%_bindir/setupcloudprint

%post
if [ $1 -gt 2 ] ; then
%_prefix/lib/cloudprint-cups/upgrade.py
fi

%files
%_bindir/setupcloudprint
%config(noreplace) %attr(0640,root,lp) %_sysconfdir/cups/cloudprint.conf
%_prefix/lib/cloudprint-cups
%_prefix/lib/cups/backend/cloudprint
%_prefix/lib/cups/driver/cupscloudprint
%ghost %attr(0660,root,lp) %_var/log/cups/cloudprint_log

%changelog
* Mon Oct 21 2013 Alexey Shabalin <shaba@altlinux.ru> 20131017-alt1
- inital build
