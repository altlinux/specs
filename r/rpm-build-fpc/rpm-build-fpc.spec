Name: rpm-build-fpc
Version: 2.5
Release: alt1

Summary: RPM helpers for Free Pascal packages
License: GPL
Group: Development/Other

Source: %name-%version-%release.tar

BuildArch: noarch

%description
RPM helpers for Free Pascal packages:
- fpc.req -- find-requires wrapper;
- fpc.prov -- find-provides wrapper;
- fpc.macros -- RPM macros.

%prep
%setup -q -n %name-%version-%release

%install
install -pD -m755 fpc.req %buildroot%_rpmlibdir/fpc.req
ln -s fpc.req %buildroot%_rpmlibdir/fpc.prov
install -pD -m755 fpc.req.files %buildroot%_rpmlibdir/fpc.req.files
ln -s fpc.req.files %buildroot%_rpmlibdir/fpc.prov.files
install -pD -m644 fpc.macros %buildroot/etc/rpm/macros.d/fpc

%files
%doc README.ALT
%_rpmlibdir/fpc.req*
%_rpmlibdir/fpc.prov*
%config /etc/rpm/macros.d/fpc

%changelog
* Sun May 02 2010 Alexey Tourbin <at@altlinux.ru> 2.5-alt1
- handle indirect checksum in ppudump output (#23362, Slava Dubrovskiy)
- updated scripts for rpm 4.0.4-alt78 find-requires/provides system

* Wed Jan 17 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt2
- changed dependency versioning to $ppu_file_format-$interface_checksum

* Tue Jan 16 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt1
- reworked and unifeid fpc.{req,prov} scripts
- added %%fpc_win32_* aliases for %%fpc_*_win32 macros
- added README.ALT

* Sat Sep 16 2006 Alexey Tourbin <at@altlinux.ru> 2.0-alt2
- imported sources into git repo
- removed Requires to make fpc bootstrap more transparent
- changed win32 dependency format: fpc-win32(ppu) instead of fpc(ppu)(win32)
- removed internal ppu versioning since it is subject to interface CRC

* Sun Sep 10 2006 Alexey Tourbin <at@altlinux.ru> 2.0-alt1
- initial revision, based on previous helerps from fpc package
- fpc.macros: new RPM macros
  + %%fpc_dir
  + %%fpc_build %%fpc_install
  + %%fpc_build_win32 %%fpc_install_win32
- fpc.req, fpc.prov:
  + adjust dependencies for win32 cross-compiled units
  + adjust unit versioning according to internal ppu version
