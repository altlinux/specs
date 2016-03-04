Name: uniset-configurator
Version: 1.0
Release: alt6
Summary: UniSet configurator
Group: Development/Python
License: GPL
Url: http://wiki.office.etersoft.ru/asu/Jauza?v=1fw

Packager: Pavel Vainerman <pv@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch

# Automatically added by buildreq on Sat Sep 25 2010 (-bi)
BuildRequires: python-devel
BuildRequires(pre): rpm-build-python

%add_findreq_skiplist %_datadir/%name/*.sh
%global _target_python_libdir %_target_libdir_noarch
%define python_sitelibdir_noarch %python_sitelibdir
%define python_sitelibdir_arch %_libdir/python%__python_version/site-packages

%description
%summary

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

if [ %python_sitelibdir_arch != %python_sitelibdir_noarch -a -d %buildroot%python_sitelibdir_arch/%name ]; then
    mkdir -p %buildroot%python_sitelibdir_noarch
    mv %buildroot%python_sitelibdir_arch/%name %buildroot%python_sitelibdir_noarch/
    mv %buildroot%python_sitelibdir_arch/*.py %buildroot%python_sitelibdir_noarch/
fi
mkdir -p %buildroot%python_sitelibdir_noarch/%name
mv -f %buildroot%python_sitelibdir_noarch/*.py %buildroot%python_sitelibdir_noarch/%name/

mkdir -p %buildroot/%_bindir/
ln -s %python_sitelibdir_noarch/%name/%name.py %buildroot/%_bindir/%name
ln -s %python_sitelibdir_noarch/%name/%name.py %buildroot/%_bindir/uniset-linkeditor
ln -s %python_sitelibdir_noarch/%name/%name.py %buildroot/%_bindir/uniset-apeditor
ln -s %python_sitelibdir_noarch/%name/uniset_io_conf.py %buildroot/%_bindir/uniset-ioconf
ln -s %python_sitelibdir_noarch/%name/lcaps_conf.py %buildroot/%_bindir/uniset-lcaps-conf
ln -s %python_sitelibdir_noarch/%name/apspanel_conf.py %buildroot/%_bindir/uniset-apspanel-conf
ln -s %python_sitelibdir_noarch/%name/can_conf.py %buildroot/%_bindir/uniset-can-conf

%files
%dir %python_sitelibdir/%name
%python_sitelibdir/*
%dir %_datadir/%name/
%_datadir/%name/
%_datadir/%name/templates
%_datadir/%name/images
%_bindir/*

%changelog
* Tue Mar 24 2015 Pavel Vainerman <pv@altlinux.ru> 1.0-alt6
- Use 'xml.dom.minidom' replaced by the use 'lxml'

* Mon Feb 17 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt5
- fixed minor bug in LinkEditor

* Tue Oct 15 2013 Pavel Vainerman <pv@altlinux.ru> 1.0-alt4
- added "comment" for io-card 

* Mon Mar 18 2013 Pavel Vainerman <pv@altlinux.ru> 1.0-alt3
- added check the channel type in the editor 

* Wed Mar 13 2013 Pavel Vainerman <pv@altlinux.ru> 1.0-alt2
- rename uniset --> uniset-comm (fix conflict with new python-modules-uniset)
- rename uniset_io --> uniset-io
- minor fixes

* Tue Sep 04 2012 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1
- remove unused modules 'ses' and 'geu' (use LinkEditor)
- LinkEditor: added support for the selection ID or name

* Tue Sep 04 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt19
- add ID column for uniset-linkeditor

* Sat Aug 18 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt18
- add uniset-apeditor (apspanel editor)

* Thu Aug 02 2012 Pavel Vaynerman <pv@server> 0.9-alt17
- remove display jack-number for AIxx5a

* Sun Jul 01 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt15
- added to the display of channel number and subdev (eterbug #8573)

* Fri Jun 01 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt14.1
- update changelog

* Tue May 29 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt14
- added 'default' field to LinkEditor::variables

* Thu Mar 15 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt13
- added support 'unet_respond_invert' for UNET

* Fri Feb 10 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt12
- Added support for setting boards such as 'Grayhill'

* Fri Jan 13 2012 Pavel Vainerman <pv@altlinux.ru> 0.9-alt11
- fixed bug (incorrect channel list for UNIO96/48)

* Fri Dec 30 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-alt10
- add "link status"(image) for LinkEditor

* Fri Nov 11 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-alt9
- add new card (Advantech PCI-1750) 

* Fri Nov 11 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-alt8
- add configure DAC0,1 for aixx5a


* Sat Oct 22 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-alt6
- LinkEditor: rename <params> --> <variables> (changed in uniset-codegen)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt14.1
- Rebuild with Python-2.7

* Fri Oct 21 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-alt5
- add UNIO96-1 card editor

* Thu Oct 20 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-alt4
- add ses and geu editor
- add LinkEditor

* Tue Oct 04 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-alt3
- add "unet" configurator

* Sun Jul 24 2011 Pavel Vainerman <pv@altlinux.ru> 0.8-alt8
- fixed bug in io-modules (processing threshold_aid)

* Tue Jun 21 2011 Pavel Vainerman <pv@altlinux.ru> 0.8-alt7
- fixed minor bug in io-module

* Fri May 20 2011 Pavel Vainerman <pv@altlinux.ru> 0.8-alt6
- (can-editor): fixed bug in can200mp config dialog

* Tue May 17 2011 Pavel Vainerman <pv@altlinux.ru> 0.8-alt5
- minor fixes in can.glade

* Tue May 17 2011 Pavel Vainerman <pv@altlinux.ru> 0.8-alt4
- minor fixed in glade-files (spinbutton problem)

* Sat Apr 23 2011 Pavel Vainerman <pv@altlinux.ru> 0.8-alt2
- remove the packing of unnecessary glade-files

* Fri Apr 22 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.8-alt1
- Strip common glade-file on separate glade-files for every module

* Fri Apr 22 2011 Pavel Vainerman <pv@altlinux.ru> 0.7-alt5
- minor fixes in lcaps editor

* Thu Apr 21 2011 Pavel Vainerman <pv@altlinux.ru> 0.7-alt4
- fixed minor bug in apspanel editor

* Mon Apr 18 2011 Pavel Vainerman <pv@altlinux.ru> 0.7-alt3
- (ioconf): change io="nodeID" to io="nodeName"

* Mon Apr 11 2011 Pavel Vainerman <pv@altlinux.ru> 0.7-alt2
- decrease dependence on python

* Sun Mar 27 2011 Pavel Vainerman <pv@altlinux.ru> 0.7-alt1
- add new card type (AIxxx/8 and AIxx/16)

* Sat Mar 26 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-alt23
- fixed bug in subdev number for ai16, ao16 cards

* Wed Mar 23 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-alt22
- add popupmenu for io channel
- minor fixes

* Sat Mar 19 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-alt21
- add pictures for can-editor

* Fri Mar 18 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-alt20
- add pictures for node-editor and  io-editor

* Fri Mar 18 2011 Pavel Vainerman <pv@server> 0.6-alt19
- add 'hack' for run with new python

* Tue Feb 01 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-alt18
- fixed bug in apspanel module

* Mon Jan 31 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-alt17
- fixed bug in apspanel module (don`t save comment)

* Fri Jan 28 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-alt16
- add generic 'dev' for ioconf 


* Mon Jan 17 2011 Ilya Shpigor <elly@altlinux.org> 0.6-alt14
- fix build for x86_64 arch

* Mon Jan 17 2011 Ilya Shpigor <elly@altlinux.org> 0.6-alt13
- initial build for ALT Linux Sisyphus

* Fri Jan 14 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-eter12
- fixed bug in io-conf (change card number for sensors)

* Wed Jan 12 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-eter11
- fixed bug in io-conf (number of channels for DO32 and DI32)

* Tue Jan 11 2011 Pavel Vainerman <pv@altlinux.ru> 0.6-eter10
- fixed bug (add new sensor)

* Wed Dec 08 2010 Pavel Vainerman <pv@altlinux.ru> 0.6-eter9
- fixed bug in i/o (thank's yv@ again)

* Wed Dec 08 2010 Pavel Vainerman <pv@altlinux.ru> 0.6-eter8
- fixed bug (thank`s yv@)

* Thu Nov 18 2010 Ilya Shpigor <elly@altlinux.org> 0.6-eter7
- fix python version requires in configure.ac

* Tue Nov 09 2010 Pavel Vainerman <pv@altlinux.ru> 0.6-eter3
- minor fixes in io_conf and can_conf

* Tue Nov 09 2010 Pavel Vainerman <pv@altlinux.ru> 0.6-eter2
- add to CANEditor: card parameters editor

* Sun Nov 07 2010 Pavel Vainerman <pv@altlinux.ru> 0.6-eter1
- add apspanel editor

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.5-eter6
- rebuild new verion

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.5-eter5
- set executable bit for lcaps-conf and uniset-ioconf

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.5-eter4
- add 'ALL' for lcaps-conf --gen-test-skel

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter3
- new release (master merge aps)

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter2
- add link for uniset-lcaps-conf

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter1
- add LCAPS test generator 

* Wed Oct 20 2010 Pavel Vainerman <pv@altlinux.ru> 0.3-eter2
- fixed bug in previous build

* Wed Oct 20 2010 Pavel Vainerman <pv@altlinux.ru> 0.3-eter1
- add uniset-ioconf utilities
- new version (add new functions)

* Sun Sep 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.2-eter4
- minor fixes

* Sun Sep 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.2-eter3
- minor fixes in card setup dialog

* Sun Sep 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.2-eter2
- add subdev and device file param for card

* Sat Sep 25 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter2
- second build

* Sat Sep 25 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter1
- initial build
