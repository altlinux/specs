

%define skip_python2 1
%define t_version %(rpm -q --qf '%%{VERSION}' trytond)
%define majorver 4.0

Name: gnuhealth

Version: %majorver.3
Release: alt0.1.1
Url: https://health.gnu.org
Summary: A Health and Hospital Information System
License: GPLv3+
Group: Sciences/Medicine
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: https://ftp.gnu.org/gnu/health/%name-%version.tar.gz
Source1: GNUHealth.README.openSUSE
Source2: gnuhealth-control
Source3: gnuhealth.service
Source4: gnuhealth-webdav@.service
Source5: openSUSE-gnuhealth-setup
Source6: gnuhealth
Source7: gnuhealth-rpmlintrc
Source8: https://ftp.gnu.org/gnu/health/%name-%version.tar.gz.sig
Source9: https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=health&download=1#/%name.keyring


BuildRequires: fdupes
BuildRequires: python3-module-setuptools rpm-build-python3
BuildRequires: python3-module-pytest python3-module-ly python3-module-Reportlab

# For the tests:
BuildRequires: python3-module-trytond
BuildRequires: python3-module-trytond_company
BuildRequires: python3-module-trytond_currency
BuildRequires: python3-module-trytond_party

# new fonts for the forms:
Requires: fonts-ttf-gnu-freefont-common python3-module-proteus
Requires: bsdtar
Requires: python3-module-trytond
Requires: python3-module-trytond_company
Requires: python3-module-trytond_currency
Requires: python3-module-trytond_party
BuildArch: noarch

#TODO:
# gnuhealth-client
# mygnuhealth

%{?systemd_ordering}

%add_python3_self_prov_path %buildroot%python3_sitelibdir/trytond/modules/

%description
GNU Health is the Hospital Information System adopted by the United
Nations University, International Institute for Global Health, for
the implementations and trainings.

This is the server component of GNU Health.
You would need the GNU Health Client as well, on the same or a different machine.
You may use the Tryton Client either
See https://en.opensuse.org/GNUHealth_on_openSUSE for instructions

%package -n python3-module-%name-orthanc
Summary: Integration module for Orthanc
Group: Sciences/Medicine
Requires: gnuhealth

%description -n python3-module-%name-orthanc
This package provides the interface to Orthanc

%prep
%setup -n %name-%version
cp %{S:1} .
cp %{S:2} .

%build
for i in h*; do
  pushd $i
  %python3_build
  popd
done

%install
for i in h*; do
  pushd $i
  %python3_install --prefix=%prefix --root=%buildroot
  popd
done

mkdir -p -m 755 %buildroot%_bindir
install -p -m 755 gnuhealth-control %buildroot%_bindir/gnuhealth-control
install -p -m 755 %{S:5} %buildroot%_bindir/openSUSE-gnuhealth-setup
install -p -m 755 %{S:6} %buildroot%_bindir/gnuhealth
install -p -m 755 scripts/demo/install_demo_database.sh %buildroot%_bindir/install_demo_database.sh

#delete empty demo directory
rm -rf scripts/demo

mkdir -p %buildroot%_unitdir
install -p -m 644 %SOURCE3 %buildroot%_unitdir/%name.service
install -p -m 644 %SOURCE4 %buildroot%_unitdir/%name-webdav@.service

mkdir -p %buildroot%_sysconfdir/tryton

#remove double license file:
rm backend/fhir/client/COPYING

#Move FHIR server to examples directory
mkdir -p -m 755 %buildroot%_docdir/%name/examples/
mv backend/fhir* %buildroot%_docdir/%name/examples/.
rmdir backend


%if %{with tests}
%check
cd %buildroot%python3_sitelibdir/trytond/modules
for i in h*; do
  pushd $i
    %pytest -rs tests
  popd
done
%endif

%pre

#Write GH Variable /etc/tryton/gnuhealthrc
#cat > %buildroot/etc/tryton/gnuhealthrc << "EOF"
#GNUHEALTH_VERSION=%version
#TRYTON_VERSION=%t_version
#EOF

%post
%post_service gnuhealth
%post_service gnuhealth-webdav@

%preun
%preun_service gnuhealth
%preun_service gnuhealth-webdav@


%files -n python3-module-%name-orthanc
%python3_sitelibdir/%{name}_orthanc*
%python3_sitelibdir/trytond/modules/health_orthanc*

%files
%_bindir/gnuhealth
%_bindir/gnuhealth-control
%_bindir/gnuhealth-webdav-server
%_bindir/openSUSE-gnuhealth-setup
%_bindir/install_demo_database.sh
%_unitdir/%name.service
%_unitdir/%name-webdav@.service
%doc Changelog gnuhealth-setup version gnuhealthrc GNUHealth.README.openSUSE scripts/* config/* doc/*
%_docdir/%name/examples*
%dir %_sysconfdir/tryton
#/etc/tryton/gnuhealthrc
%exclude %python3_sitelibdir/%{name}_orthanc*
%exclude %python3_sitelibdir/trytond/modules/health_orthanc*
%python3_sitelibdir/*

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 4.0.3-alt0.1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sat May 28 2022 Ilya Mashkin <oddity@altlinux.ru> 4.0.3-alt0.1
- Build for Sisyphus based on suse spec

* Sat Apr  2 2022 Axel Braun <axel.braun@gmx.de>
- version 4.0.3
  * Remove pinning from vobject library version (Vanilla installation)
  * fix bug #62235: Traceback on default health professional
* Wed Mar 23 2022 Axel Braun <axel.braun@gmx.de>
- version 4.0.2
  * Use ODT binary format for pediatric growth charts reports
  * Force Beren library to 0.7.0 to make it compatible with Python 3.6
  * Allow Python minor versions > 10 (ej Python 3.10.2)
  * fix webdav import error, bug #62165
* Sun Mar  6 2022 Axel Braun <axel.braun@gmx.de>
- version 4.0.0
  * based on Tryton 6.0
  * Improved ergonomics on the GTK client
  * New HELP command that allows offline and contextualized documentation
  * WebDAV and CalDAV packages are fully integrated in GH (no links)
  * Weblate now holds 34 language teams!
  * Removed obsoleted binary ODT (except for some charts)
  * Improved integration with OpenStreetMap (OSM)
  * Improved surgery and patient evaluation flows
  * New health service Dx imaging package
  * Update person gender list
  * Add medical evaluations to health services
  * Include (optional) expiration date on the person ID
  * Add context field for Dx Imaging and Lab tests
* Fri Apr 16 2021 Axel Braun <axel.braun@gmx.de>
- update to gnuhealth-control
* Wed Mar 24 2021 Axel Braun <axel.braun@gmx.de>
- Variable for EDITOR set
* Sat Feb 27 2021 Andreas Stieger <andreas.stieger@gmx.de>
- add upstream signing key and verify source signature
* Tue Feb 16 2021 Axel Braun <axel.braun@gmx.de>
- python_dependency_generator removed
* Mon Feb 15 2021 Axel Braun <axel.braun@gmx.de>
- version 3.8.0
  dentistry package added
* Tue Dec 22 2020 Axel Braun <axel.braun@gmx.de>
- Documentation added to package description
* Fri Aug 21 2020 Axel Braun <axel.braun@gmx.de>
- version 3.6.5
  HMIS: Update to 3.6.5 including ICD10 codes 2020
* Tue Jul 21 2020 Axel Braun <axel.braun@gmx.de>
- Readme renamed (SUSE -> openSUSE)
  gnuhealth: Link to oS wiki added
* Thu Jun 25 2020 Axel Braun <axel.braun@gmx.de>
- gnuhealth-control updated to 3.6.5-openSUSE
  * change of translation server for language packs
* Thu May 21 2020 Axel Braun <axel.braun@gmx.de>
- fixed different behviour of bsdtar in script and shell (gnuhealth-control)
* Tue May 19 2020 Axel Braun <axel.braun@gmx.de>
- version 3.6.4 of gnuhealth-control
* Mon May 18 2020 Axel Braun <axel.braun@gmx.de>
- python3-matplotlib got lost.....added
* Sat May 16 2020 Axel Braun <axel.braun@gmx.de>
- Version 3.6.4
  additional functionality for COVID-19 and epidemiology tracing
  new epidemiology evaluations
  lab1.diff and lab2.diff removed, included in new version
* Wed Apr 22 2020 Axel Braun <axel.braun@gmx.de>
- pre-release of 3.6.4 covering improved diagnostics on COVID-19
  lab1.diff and lab2.diff added
* Sun Apr  5 2020 Axel Braun <axel.braun@gmx.de>
- correction for service file
* Tue Mar 31 2020 Axel Braun <axel.braun@gmx.de>
- update for boo#1167126, 1167128
* Tue Mar 17 2020 Axel Braun <axel.braun@gmx.de>
- clean up of spec file to get rid of warnings
  added gnuhealth-rpmlintrc
* Sat Mar 14 2020 Axel Braun <axel.braun@gmx.de>
- gnuhealth-control 3.6.3 - added chmod after getlang command
* Mon Mar  2 2020 Axel Braun <axel.braun@gmx.de>
- modified getlang to exclude 2 directories (otherwise initialization fails after language installation)
* Fri Feb 28 2020 Axel Braun <axel.braun@gmx.de>
- version 3.6.3
  * GH HMIS server. task #15562: Include coronavirus COVID-19 in ICD10 codes
  * GH HMIS server. bug #57695: Traceback when creating a page of life associated to an empty evaluation
  * GH HMIS server. task #15561: Werkzeug 1.0 is not compatible with Trytond 5.0
  * shebang.diff to fix /usr/bin/env
* Thu Nov 21 2019 Axel Braun <axel.braun@gmx.de>
- version 3.6.1
  demo.diff removed (included in 3.6.1)
* Mon Nov 11 2019 Axel Braun <axel.braun@gmx.de>
- demo.diff to update installation script for demo-db added
* Tue Jun 11 2019 Axel Braun <axel.braun@gmx.de>
- gnuhealth-control changed to version 3.4.1
  * use bsdtar (can handle zip files, tar can't)
* Sun Mar 10 2019 Axel Braun <axel.braun@gmx.de>
- version 3.4.1 various bugfixes, e.g.
  bug #55594: Traceback when creating a person without a system institution
  bug #55595: Remove unimplemented functionality fields from Federation Country
* Thu Feb 28 2019 Axel Braun <axel.braun@gmx.de>
- add dependency for bsdtar (gnuhealth-control changed)
* Sat Dec 29 2018 Axel Braun <axel.braun@gmx.de>
- gnuhealth-webdav service adapted to new GH webdav server
* Fri Dec  7 2018 Axel Braun <axel.braun@gmx.de>
- New version 3.4.0
  * The GNU Health Federation model
  * Thalamus message server
  * New Health Information System (on MongoDB)
  * Person Master Index
  * MongoDB support (on the HIS)
  * Updated UniprotKB database with over 30K protein natural variants
  * Contextualized information on genetics and social determinants
  * Genetic and family history and environmental factors integrated to
    the Page of Life and Federation The GNU Health Book of Life
  * Tryton 4.6 integration on the HMIS node
* Thu Nov 15 2018 Axel Braun <axel.braun@gmx.de>
- correction for gnuhealth-control (v 3.2.4)
* Mon Aug 27 2018 axel.braun@gmx.de
- Adding a dummy executable called 'gnuhealth' with some help text
  (boo#1107771)
* Tue Jul 17 2018 axel.braun@gmx.de
- openSUSE-gnuhealth-setup: User tryton set to SUPERUSER
  Documentation updated
* Wed Jun 20 2018 axel.braun@gmx.de
- gnuhealth-control: added info about backup file
  openSUSE-gnuhealth-setup added
* Tue Jun  5 2018 axel.braun@gmx.de
- Version 3.2.10
  bug #54055: Caldav event does not update after changing the appointment
* Fri Jan 19 2018 axel.braun@gmx.de
- added gnuhealth-client to documentation
* Fri Dec 29 2017 axel.braun@gmx.de
- typo in documentation corrected
* Sat Dec  9 2017 axel.braun@gmx.de
- documentation updated
* Wed Dec  6 2017 axel.braun@gmx.de
- Version 3.2.9
  Fix bug #52580: Removing the patient field before saving the record generates an error
  Fix bug #52579: some on_change numeric method operations generate traceback
  Fix bug #52578: WHR should be on the same line as hip and waist fields
* Wed Nov 15 2017 axel.braun@gmx.de
- removed pypi dependencies
* Wed Nov 15 2017 axel.braun@gmx.de
- health_crypto. Fix bug #52366: Error when signing the death certificate
  task #14626: Renaming Package names prefix trytond_ from Pypi. Update descriptions
  task #14626: Renaming Package names prefix trytond_ from Pypi. Remove tryton from keywords
  remove lingering egg-info dirs from webdav3
* Sun Oct 29 2017 axel.braun@gmx.de
- Version 3.2.6
  dependency on python3-pymongo removed
  fix bug #52298: Traceback generating an invoice from service with an insurance policy plan
  Fix bug #52275: Traceback when creating a free slot in appointments or work schedule
* Wed Oct 18 2017 axel.braun@gmx.de
- Correction for gnuhealth-control (file not found in backup)
* Sun Oct  8 2017 axel.braun@gmx.de
- version 3.2.5
  health, health_qrcodes : Fix bug #52179: Traceback due to obsolete unicode method in reports
* Wed Oct  4 2017 axel.braun@gmx.de
- Version 3.2.4
  health_services: Fix bug #52160: Issues related to invoice type and domain when creating the service invoice
  health_disability : Rename anf fix  Amputation model description from Amputation to Prothesis
  health : Prescription report . Include duration frequency selections strings for translation. Update conditional op. to Python3 (!=)
* Wed Sep 27 2017 axel.braun@gmx.de
- gnuhealth-control corrected (message command)
* Sat Sep 16 2017 axel.braun@gmx.de
- version 3.2.3 Fix bug #52038: Field history is repeated in the tree
  view of the prescription line
* Thu Sep 14 2017 axel.braun@gmx.de
- Documentation adapted
* Mon Aug 28 2017 axel.braun@gmx.de
- version 3.2.2
  health_imaging : Update health professional retrieval to the current standard method
* Tue Aug  8 2017 axel.braun@gmx.de
- added gnuhealth-webdav@.service
- updated documentation on gnuhealth-webdav@.service
- added alias cdutil for compatibility reasons (not really needed,
  as binaries are in /usr/bin anyway)
- fixed path for cdexe
* Sat Jul 22 2017 axel.braun@gmx.de
- version 3.2.1
  Fix view error on lab order
* Tue Jul 11 2017 axel.braun@gmx.de
- update of documentation for upgrade from Leap 42.2
* Sun Jul  2 2017 axel.braun@gmx.de
- Version 3.2.0
* Sat Jun 24 2017 axel.braun@gmx.de
- Requirement on python3-PyWebDAV3-GNUHealth added
* Tue Jun 20 2017 axel.braun@gmx.de
- GNU Health version 3.1.0b3
* Sun Mar 26 2017 axel.braun@gmx.de
- release 3.0.8
  [bug #50635] Missing declaration of view directory on setup.py on health_disability module
* Tue Mar 14 2017 axel.braun@gmx.de
- Release 3.0.7 (bnc1026365)
* Sat Feb 25 2017 axel.braun@gmx.de
- added DB-role to gnuhealh-control
  updated documentation
* Mon Feb 20 2017 axel.braun@gmx.de
- renamed gnuhealth_control to gnuhealth-control
  fixed documentation
* Tue Feb 14 2017 axel.braun@gmx.de
- version 3.06
  * Fix bug #50269: Traceback when assigning a new meal order
  * Fix bug #50281: Traceback when displaying patient critical info
    in non-english languages
  * fix bug #50288: Wrong widget for mealtime field. // Fix
    validation for meal order warning
  * Remove readonly from patient meal order warning, to correctly
    save state of the field
* Mon Dec 12 2016 axel.braun@gmx.de
- Release 3.0.5
  * Update to ICD10 version 2016
  * fix bug #49414: Error when printing prescription using review dates
  * bug #49405: Error on summary report when no date of birh is assigned to the person
* Sat Oct 22 2016 axel.braun@gmx.de
- temporary fix for prescription_orders report until 3.0.5 is released
* Sat Oct 22 2016 axel.braun@gmx.de
- Release 3.0.4
* Tue Oct 18 2016 axel.braun@gmx.de
- README updated
* Wed Sep 28 2016 axel.braun@gmx.de
- update of README.SUSE
* Wed Aug 31 2016 axel.braun@gmx.de
- file permissions corrected
* Sun Aug 21 2016 jengelh@inai.de
- Trim summary/description from redundant words
* Mon Jan 11 2016 axel.braun@gmx.de
- version 3.0.0
* Mon Jan  4 2016 axel.braun@gmx.de
- Version 3.0RC2
* Thu Jan 22 2015 axel.braun@gmx.de
- version 2.8
* Thu Jul 10 2014 axel.braun@gmx.de
- Release 2.6.0
* Wed Jan 22 2014 axel.braun@gmx.de
- GnuHealth 2.4RC1 on Tryton 3.0
* Fri Oct 18 2013 axel.braun@gmx.de
- Initial package build on OBS ( version 2.2.1 )
