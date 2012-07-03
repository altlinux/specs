Name: pERP
Version: 0.4
Release: alt2
Summary: project ERP is a group of third-party applications for the eGroupWare project

Group: Networking/WWW
License: GPL/LGPL
Url: http://www.projecterp.org/
Source: %name.tar

Requires: eGroupWare-core
Requires: eGroupWare-tracker eGroupWare-infolog eGroupWare-timesheet pear-Image_Barcode

BuildArch: noarch
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

%description
project ERP is a group of third-party applications for the eGroupWare project, providing accounting, inventory, and manufacturing support.
It aims to be as seamless as possible in its look and feel, and with its integration with other eGroupWare applications.

%prep
%setup -n pERP

%build
%install
find -name .svn | xargs rm -rf
find \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete
find \( -name '*.swp' -o -name '#*#' \) -print -delete
mkdir -p %buildroot%_datadir/egroupware/
%__mv perp_ap %buildroot%_datadir/egroupware/
%__mv perp_api %buildroot%_datadir/egroupware/
%__mv perp_ar %buildroot%_datadir/egroupware/
%__mv perp_human_resources %buildroot%_datadir/egroupware/
%__mv perp_inventory %buildroot%_datadir/egroupware/
%__mv perp_ledger %buildroot%_datadir/egroupware/
%__mv perp_manufacturing %buildroot%_datadir/egroupware/
%__mv perp_orders %buildroot%_datadir/egroupware/
%__mv perp_payroll %buildroot%_datadir/egroupware/
%__mv perp_setup_wizard %buildroot%_datadir/egroupware/
%__mv perp_timeclock %buildroot%_datadir/egroupware/
%__mv egroupware-addons/wizard %buildroot%_datadir/egroupware/
%__mv perp_warranty %buildroot%_datadir/egroupware/

%files
%doc ChangeLog dbdump.php gpl.txt install.sh README sample_manufacturing_company.bz2
%_datadir/egroupware/*

%changelog
* Tue May 12 2009 gray_graff <gray_graff@altlinux.org> 0.4-alt2
- Fix critical bug (symlink to egroupware not working)
- Fix Requires
- Updated to revision 3464
- Add Requires - pear-Image_Barcode
- Fix repocop warnings

* Fri Apr 10 2009 gray_graff <gray_graff@altlinux.org> 0.4-alt1
- Initial build
