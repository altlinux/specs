Name: alt-gpgkeys
Version: 0.8.92
Release: alt1

Summary: ALT GnuPG keys
License: GPL-2.0-or-later
Group: System/Configuration/Packaging
Packager: ALT Security Team <security@altlinux.com>
BuildArch: noarch

Source0: options
Source1: keys.tar
Source2: alt-gpgkey-check
Source3: alt-gpgkey-strip
Source4: alt-rpmkeys-checksig

Conflicts: gnupg < 0:1.2.0
BuildPreReq: gnupg, libshell

%description
This package contains ALT Linux Team GnuPG keyring.

%package utils
Summary: Utilities to manipulate %name
License: GPL-2.0-or-later
Group: System/Configuration/Packaging
Requires: %name = %version-%release

%description utils
This package contains utilities to manipulate %name.

%package -n alt-rpmkeys
Summary: ALT GnuPG keys imported into RPM database
License: GPL-2.0-or-later
Group: System/Configuration/Packaging
Requires: %name = %version-%release

%description -n alt-rpmkeys
This package contains ALT Linux Team GnuPG keys imported into RPM database.

%package -n alt-rpmkeys-utils
Summary: Utilities to manipulate alt-rpmkeys
License: GPL-2.0-or-later
Group: System/Configuration/Packaging
Requires: alt-rpmkeys = %version-%release

%description -n alt-rpmkeys-utils
This package contains utilities to manipulate alt-rpmkeys.

%prep
%setup -qcT -n %name -a 1
install -pm755 %_sourcedir/{alt-gpgkey-check,alt-gpgkey-strip,alt-rpmkeys-checksig} .
mkdir -m700 home
mkdir -m700 rpmdb

%build
gpg --homedir home </dev/null ||:
for f in keys/*; do
	./alt-gpgkey-check "$f"
	gpg --homedir home --import "$f"
done
install -pm600 %_sourcedir/options home/gpg.conf
gpg --homedir home --list-keys
gpg --homedir home --export --armor > all.gpg
rpmkeys --dbpath "$PWD/rpmdb" --import all.gpg

%install
%define gpgkeydir %_prefix/lib/%name
cd home
mkdir -p %buildroot%gpgkeydir
install -pm644 gpg.conf pubring.gpg secring.gpg \
	%buildroot%gpgkeydir/
cd ..

%define rpmkeydir %_prefix/lib/alt-rpmkeys
cd rpmdb
mkdir -p %buildroot%rpmkeydir
cp -p Packages Name %buildroot%rpmkeydir/
chmod -R a-w %buildroot%rpmkeydir/
cd ..

mkdir -p %buildroot%_bindir
install -pm755 alt-gpgkey-check alt-gpgkey-strip alt-rpmkeys-checksig \
	%buildroot%_bindir/

%define _unpackaged_files_terminate_build 1

%files
%gpgkeydir/

%files utils
%_bindir/alt-gpgkey*

%files -n alt-rpmkeys
%rpmkeydir/

%files -n alt-rpmkeys-utils
%_bindir/alt-rpmkey*

%changelog
* Tue Oct 15 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.92-alt1
- Added keys:
  + alexvk@ (CFE385AF; see #51539);
  + oleg@ (FCE55B91; see #51633);
  + hromovpi@ (F6EE2CCD; see #51010).

* Mon Oct 14 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.91-alt1
- Added keys:
  + k0tran@ (C0801118; see #51003).
  + sheriffkorov@ (620D0920; see #50733).

* Tue Sep 24 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.90-alt1
- Added keys:
  + zeff@ (50DEDC01; see #47842);
  + armatik@ (155FD922; see #49026);
  + enimalojd@ (3F088E86; see #49849).
- Updated expired keys:
  + gerben@ (485BFB56; closes: #51498);
  + dutyrok@ (A2F63EDF; closes: #51513).

* Wed Sep 04 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.89-alt1
- Added keys:
  + alxvmr@ (D2FFF0E4; see #48922);
  + arzdez@ (23FCD126; see #49575).

* Mon Sep 02 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.88-alt1
- Added key: guschin@ (4487FEF7; see #45886).
- Updated expired key: kotopesutility@ (F6417A60; closes: #51039).

* Wed Jul 17 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.87-alt1
- Added keys:
  + morgonf@ (1A0ED7D3; see #46409);
  + sobue@ (E0474782; see #49395);
  + shm@ (E712E9E2; see #49809);
  + keller@ (9FE9477E; see #49777).

* Tue Jun 18 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.86-alt1
- Added key: palar@ (5A300462; see #42968).
- Updated key: ancieg@ (16159AB3; closes: #46624).

* Tue May 28 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.85-alt1
- Added keys:
  + fiersik@ (DD8C5853; see #50400);
  + zander@ (85BA8C76; see #49806).

* Tue May 28 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.84-alt1
- Added key: boria138@ (3FD39C76; see #49644).

* Thu May 23 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.83-alt1
- Replaced expired key: imz@ (FDE45C46 -> 74BFDB00; closes: #35923).
- Added key: alt-p11@ (925E1FF4).

* Tue May 14 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.82-alt1
- Updated keys:
  + alt-sisyphus@ (DA2773BB).
  + alt-p9@ (7AED4D09).

* Mon Apr 29 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.81-alt1
- Replaced key: slazav@ (DF615AF7 -> 6CDB8DEE; closes: #50222).

* Sat Apr 27 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.80-alt1
- Updated expired key: manowar@ (B9F22864; closes: #38344).

* Mon Apr 08 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.79-alt1
- Removed key: alexeys@ (E1D172DD; see #45714).
- Added keys:
  + rirusha@ (8FA48966; see #49311);
  + ded@ (DE98BF79; see #47464);
  + danild@ (9AC67D1D; see #47163);
  + lola@ (385BB7C9; see #49146).

* Wed Mar 27 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.78-alt1
- Added key: krf10@ (7F4354E4; see #46983).

* Wed Mar 27 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.77-alt1
- Added keys:
  + gerben@ (485BFB56; see #47537);
  + fedor@ (973A95B7; see #49402).
- Replaced key: cronbuild@ (278EB305 -> A71B8F0A; closes: #49820).

* Mon Feb 26 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.76-alt1
- Added keys:
  + savoptik@ (32AEF5C7; see #47194);
  + zerospirit@ (B8393397; see #45771).
  + kuznetsovam@ (A3621797; see #48799).
  + toxblh@ (C655F315; see #48131).
  + vanomj@ (827D4E2D; see #49012).
- Replaced key: mike@ (B60C9B72 -> FF00C15D; closes: #49515).

* Sat Feb 17 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.75-alt1
- Added key: grenka@ (3C92CDBD; closes: #45492).
- alt-gpgkeys-utils: bail out on key files with secret keys.

* Sat Feb 17 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.74-alt1
- Removed compromised key: grenka@ (F502E3C5).

* Sun Feb 11 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.73-alt1
- Updated expired keys:
  + ildar@ (799AEF89; closes: #22294);
  + george@ (CE50396C; closes: #41920).
- Replaced key: ogion@ (538E7273 -> 9CA0A9AA; closes: #49304).

* Fri Feb 02 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.72-alt1
- Replaced key: lav@ (2ADBEAE5 -> CAF54019; closes: #49237).

* Wed Jan 31 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.71-alt1
- Updated expired key: bircoph@ (5372756C; closes: #49239).

* Mon Jan 29 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.70-alt1
- Added key: lenka@ (55E760DB; see #47221).
- Replaced keys:
  + pauli@ (6B05E9C2 -> 21149454; closes: #49187);
  + jinn@ (D779C9B8 -> D0471397; closes: #49207).

* Mon Jan 22 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.69-alt1
- Added key: aibure@ (6117F0F4; see #47864).

* Mon Dec 25 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.68-alt1
- Readded key: kaf@ (127CA906; see #39627).

* Tue Dec 19 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.67-alt1
- Added keys:
  + neff@ (02F34C35; see #47525);
  + ved@ (B4478E0A; see #47763).

* Wed Dec 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.66-alt1
- Added keys:
  + proskur@ (AC94608C; see #47805);
  + kulikovsa@ (B1B25684; see #47258).

* Fri Dec 08 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.65-alt1
- Added key: serjigva@ (EAF91A27; see #48351).
- Removed keys:
  + kaf (127CA906; see #39627);
  + x09 (0C16659B; see #34359).

* Thu Dec 07 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.64-alt1
- Added keys:
  + qualimock@ (5101A392; see #45539);
  + rauty@ (1DB97BC3; see #47432);
  + sova@ (C9163799; see #43997).

* Tue Dec 05 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.63-alt1
- Updated key: asy@ (54F8ABD4; closes: #48606).
- Added keys:
  + samael@ (EF7EFED2; see #44326);
  + oficerovas@ (6FD53D1E; see #46301).
- Removed keys:
  + paksa (1917EAAC; see #44492);
  + palar (5A300462; see #42968);
  + prohorp (96AA4A6B; see #43501);
  + tema (A4B649FF; see #33388);
  + valentina (46F5A98B; see #37006).

* Fri Nov 10 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.62-alt1
- Replaced expired key: nbr@ (95781CE0 -> BBCF62CD; closes: #48315).

* Fri Aug 04 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.61-alt1
- Added keys:
  + chernigin@ (1604A422; see #46044);
  + oskiller@ (1D078CE3; see #45966);
  + smasher@ (EBC2B57E; see #45548).

* Fri Jun 23 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.60-alt1
- Updated key: ancieg@ (16159AB3; closes: #46624).
- Added key: fidel@ (E71DF8D3; see #46053).

* Tue Jun 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.59-alt1
- Added key: srebrov@ (C62E79FC; see #46137).

* Fri May 26 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.58-alt1
- Added key: alexeys@ (E1D172DD; see #45714).

* Fri Apr 21 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.57-alt1
- Updated expired key: manowar@ (B9F22864; closes: #38344).
- Added keys:
  + pavel@ (59C2C559; see #43809);
  + saahriktu@ (B5D8574C; see #45253).

* Thu Apr 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.56-alt1
- Added key: fl0pp5@ (02C600D2; see #44509).

* Tue Apr 04 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.55-alt1
- Added key: nofex@ (93E72A2D; see #45607).

* Tue Mar 28 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.54-alt1
- Added key: markow@ (47E7E41B; see #44835).

* Tue Mar 21 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.53-alt1
- Updated key: arseny@ (62E619E5; closes: #45575).
- Added key: paksa@ (1917EAAC; see #44492).

* Mon Mar 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.52-alt1
- Updated key: grenka@ (F502E3C5; closes: #45492).

* Mon Feb 27 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.51-alt1
- Added key: alimektor@ (047FDCEE; see #43409).

* Mon Feb 20 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.50-alt1
- Added key: dutyrok@ (A2F63EDF; see #43096).

* Mon Feb 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.49-alt1
- Replaced key: shadrinov@ (18C54D44 -> 55B2B7E6; closes: #45206).

* Mon Feb 06 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.48-alt1
- Added keys:
  + ameno@ (0BAD6621; see #44520);
  + turbid@ (CE2118B5; see #44756).

* Tue Jan 24 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.47-alt1
- Updated expired key: naf@ (DD7132A6; closes: #44906).
- Added key: thatman@ (A5389E40; see #44281).

* Mon Jan 16 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.46-alt1
- Added keys:
  + sav@ (738AB513; see #40829);
  + vcong@ (8945C3A2; see #42533);
  + morozovaes@ (3A97326D; see #43827).
- Replaced key: nit@ (103E42A6 -> 64CC2ED0; see: #43523).

* Tue Jan 10 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.45-alt1
- Added key: snk@ (6813991B; see #43285).

* Mon Dec 19 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.44-alt1
- Replaced key: zah@ (A585426A -> 14E3D59B; closes: #44645).
- Added key: toni@ (E1A0CF69; see #44484).

* Thu Dec 15 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.43-alt1
- Added key:
  + geochip@ (B4461E94; see #44279);
  + golubevan@ (206DF509; see #43982);
  + sirius@ (826C3FB0; see #43990).

* Fri Dec 09 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.42-alt1
- Updated key: egori@ (6BDF202A; closes: #44525).
- Added keys:
  + kaa@ (E03A678D; see #43172);
  + nit@ (103E42A6; see #43523).

* Mon Nov 07 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.41-alt1
- Added key: prohorp@ (96AA4A6B; see #43501).

* Tue Nov 01 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.40-alt1
- Added key: yabro@ (EBE98EDC; see #44080).

* Mon Oct 10 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.39-alt1
- Added key: ximper@ (1826BB48; see #43869).

* Tue Sep 13 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.38-alt1
- Updated expired key: lakostis@ (C4C4A01E; closes: #43774).

* Mon Jul 11 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.37-alt1
- Added keys:
  + homura@ (38041830; see #41734);
  + palar@ (5A300462; see #42968).

* Tue Jun 28 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.36-alt1
- Updated key: ancieg@ (16159AB3; closes: #43035).
- Added keys:
  + kovalev@ (962740C3; see #42475);
  + iakuninaa@ (A7AAB918; see #42532).

* Mon May 30 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.35-alt1
- Replaced expired key: sbolshakov@ (2DA1DFA5 -> 007AEDE1; closes: #42891).

* Thu May 19 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.34-alt1
- Replaced key: hellkar@ (1480B16E -> 9D2B1C9F; see #39691).

* Wed May 18 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.33-alt1
- Added key: felixz@ (85692E72; see #41672).
- Replaced key: snowmix@ (E2F5E034 -> 9617E232; closes: #42523).

* Tue May 17 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.32-alt1
- Added key:
  + tema@ (A4B649FF; see #33388);
  + hellkar@ (1480B16E; see #39691).

* Thu Apr 21 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.31-alt1
- Updated expired key: manowar@ (B9F22864; closes: #38344).

* Tue Apr 19 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.30-alt1
- Added keys:
  + zagagyka@ (8CF1B778; see #37959);
  + ancieg@ (16159AB3; see #40593).

* Tue Mar 22 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.29-alt1
- Replaced key: sem@ (983E0FAE -> 2433EF4A; closes: #42176).

* Thu Mar 03 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.28-alt1
- Replaced key: kernelbot@ (860B389E -> 3BD31283).

* Mon Feb 14 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.27-alt1
- Replaced key: legion@ (68E31E54 -> C0F6FE19; closes: #41941).

* Thu Feb 10 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.26-alt1
- Replaced key:
  + zerg@ (1C2A3F08 -> 2F16F138; closes: #41917);
  + george@ (7C10D900 -> CE50396C; closes: #41920).

* Mon Jan 31 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.25-alt1
- Added key: kdy@ (B2AB0061; see #41159).

* Sat Jan 22 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.24-alt1
- Updated key: bircoph@ (5372756C; closes: #41776).

* Fri Jan 21 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.23-alt1
- Updated expired key: qwetwe@ (DD9E0353; closes: #41754).

* Mon Jan 17 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.22-alt1
- Added key: qwetwe@ (DD9E0353; see #38003).

* Mon Dec 06 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.21-alt1
- Added keys:
  + liannnix@ (408272C0; see #41044);
  + fruktime@ (16D721C0; see #40302).

* Mon Nov 29 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.20-alt1
- Added keys:
  + koi@ (AFDB52E0; see #40164);
  + balbes150@ (0AA1837F; see #40999);
  + respublica@ (69B2D435; see #41139).

* Mon Oct 18 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.19-alt1
- Replaced key: august@ (AF11D923 -> 63690A71; see: #39874).

* Tue Sep 14 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.18-alt1
- Added key: kotopesutility@ (F6417A60; see #40788).

* Sat Sep 04 2021 Dmitry V. Levin <ldv@altlinux.org> 0.8.17-alt1
- Updated expired key: asy@ (54F8ABD4; closes: #40662).

* Thu Sep 02 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.16-alt1
- Added key: august@ (AF11D923; see #39874).
- Regenerated self-signatures (ldv@):
  + alt-p9@ (7AED4D09);
  + alt-sisyphus@ (DA2773BB);
  + alt-p10@ (C7EB80F9).

* Tue Aug 17 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.15-alt1
- Updated expired key: aris@ (96C47AC2).
- Replaced key: nickf@ (FB7F7DCC -> 2948CF32; closes: #39986).

* Wed Jul 21 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.14-alt1
- Added key: alt-p10@ (C7EB80F9).

* Mon Jul 12 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.13-alt1
- Replaced key: kirill@ (378C3619 -> 68F9A43B; closes: #40469).

* Thu Jun 17 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.12-alt1
- Updated key: darktemplar@ (D4C6316F; closes: #35057).

* Tue May 18 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.11-alt1
- Added keys:
  + alenka@ (15077C6A; see #38652);
  + ilyakurdyukov@ (92D26B2E; see #39887).

* Mon May 10 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.10-alt1
- Replaced expired key: manowar@ (A321B068 -> B9F22864; closes: #38344).
- Updated expired key: arei@ (7F7B2C7F; closes: #39959).

* Sun Apr 04 2021 Dmitry V. Levin <ldv@altlinux.org> 0.8.9-alt1
- Added keys:
  + voropaevdmtr@ (61C45E58; see #39483);
  + kernelpony@ (E659B074; a pet of vt@).

* Tue Mar 30 2021 Dmitry V. Levin <ldv@altlinux.org> 0.8.8-alt1
- Replaced key: mcpain@ (CFE5AD4F -> 298E0EA4; see #39852).

* Thu Mar 25 2021 Dmitry V. Levin <ldv@altlinux.org> 0.8.7-alt1
- Renewed key: nir@ (0CAE7AAC; see #35053).

* Thu Mar 25 2021 Dmitry V. Levin <ldv@altlinux.org> 0.8.6-alt1
- Added key: bne@ (34D43160; see #39461).

* Fri Mar 05 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.5-alt1
- Added key: neurofreak@ (2CA6C6FD; see #39613).
- Added key: kaf@ (127CA906; see #39627).

* Wed Feb 17 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.4-alt1
- Added key: egori@ (6BDF202A; see #39659).

* Wed Feb 03 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.3-alt1
- Replaced key: arbars@ (6C3802AA -> EB364EC5; closes: #39333).

* Mon Nov 30 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.2-alt1
- Added key: dshein@ (56DDDB04; see #39180).

* Tue Nov 10 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.1-alt1
- Updated the uid of key: cas@ (A9EBF131; closes: #38971).
- Updated expired key: gremlin@ (3D879005; closes: #39088).
- Added keys:
  + zah@ (A585426A; see #37407);
  + svn17@ (968F43DD; see #37945);
  + keremet@ (5ABE916A; see #38138);
  + khab@ (02FE1611; see #38797).

* Fri Aug 14 2020 Dmitry V. Levin <ldv@altlinux.org> 0.8.0-alt1
- Added alt-rpmkeys and alt-rpmkeys-utils packages.

* Thu Aug 06 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.175-alt1
- Replaced key: gkot@ (21C4D4CB -> 6AD47E1A; closes: #38728).

* Fri Jul 17 2020 Dmitry V. Levin <ldv@altlinux.org> 0.7.174-alt1
- Replaced key: vseleznv@ (2AD3A84B -> F21EB107; closes: #38432).

* Thu Jun 04 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.173-alt1
- Updated key: darktemplar@ (D4C6316F; closes: #35057).

* Tue Jun 02 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.172-alt1
- Updated expired key: underwit@ (1FA66FA3; closes: #38571).

* Mon Apr 13 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.171-alt2
- Fixed previous changelog entry.

* Mon Apr 13 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.171-alt1
- Updated expired key: manowar@ (A321B068; closes: #38344).

* Mon Mar 30 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.170-alt1
- Updated key: arseny@ (62E619E5; closes: #38291).
- Added keys:
  + mattaku@ (E8FAAE39; see #38040);
  + kevl@ (7B247518; see #37940).

* Tue Mar 03 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.169-alt1
- Updated expired key: ildar@ (799AEF89; closes: #22294).
- Added keys:
  + pav@ (0C72E18D; see #38059);
  + rav263@ (119B912B; see #37984).

* Fri Jan 31 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.168-alt1
- Replaced key: snowmix@ (4DE2462A -> E2F5E034; closes: #37955).
- Updated key: bircoph@ (5372756C; closes: #37932).

* Mon Jan 20 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.167-alt1
- Updated expired keys:
  + x09@ (0C16659B; see: #34359);
  + naf@ (DD7132A6; closes: #37772).

* Wed Dec 25 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.166-alt1
- Added key: nickf@ (FB7F7DCC; see #36074).

* Mon Dec 09 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.165-alt1
- Added key: greh@ (880615FF; see #37333).
- Changed License tags to GPL-2.0-or-later.

* Tue Oct 29 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.164-alt1
- Added key: nir@ (0CAE7AAC; see #35053).
- Added key: zacat@ (ABF555DC; see #35204).

* Mon Sep 30 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.163-alt1
- Added key: arbars@ (6C3802AA; see #37105).

* Tue Aug 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.162-alt1
- Added keys:
  + valentina@ (46F5A98B; see #37006);
  + admsasha@ (C5858BFA; see #37066).
- Replaced key: asy@ (D06F61FB -> 54F8ABD4; closes: #37034).

* Tue Jul 30 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.161-alt1
- Added key: snowmix@ (4DE2462A; see #35818).

* Mon May 27 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.160-alt1
- Added keys:
  + alt-sisyphus-ports@ (CBE14E8F);
  + alt-p9-ports@ (A8F77FE6).

* Thu May 16 2019 Dmitry V. Levin <ldv@altlinux.org> 0.7.159-alt1
- Added key: alt-sisyphus@ (DA2773BB).

* Wed May 15 2019 Dmitry V. Levin <ldv@altlinux.org> 0.7.158-alt1
- Added keys:
  + andy@ (AADF47CB; see #36480);
  + alt-p9@ (7AED4D09).

* Thu Apr 18 2019 Dmitry V. Levin <ldv@altlinux.org> 0.7.157-alt1
- Replaced key: arei@ (A564E495 -> 7F7B2C7F; closes: #36625).

* Wed Apr 17 2019 Dmitry V. Levin <ldv@altlinux.org> 0.7.156-alt1
- Updated expired key:
  + manowar@ (A321B068; closes: #34789).
- Added keys:
  + ptrnine@ (2CDB119C; see #35619);
  + rbapin@ (A9CE4585; see #35639).

* Thu Jan 24 2019 Dmitry V. Levin <ldv@altlinux.org> 0.7.155-alt1
- Replaced key: imz@ (09F75778 -> FDE45C46; closes: #35923).

* Mon Dec 17 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.154-alt1
- Added keys:
  + kastet@ (775C76D4; see #34903);
  + egorz@ (88A0B1E6; see #34857);
  + vercha@ (3CB9A2B8; see #35563).

* Mon Nov 26 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.153-alt1
- Added keys:
  + amakeenk@ (D2BC7068; see #35485);
  + krash@ (517F91EB; see #33992).

* Thu Nov 15 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.152-alt1
- Replaced key: rider@ (6BE5C0AB -> 090F291E; see #35027).
- Added key: bip@ (0B47A5A8; see #34897).

* Mon Oct 29 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.151-alt1
- Added keys:
  + mikhailnov@ (55E84CE1; see #35315);
  + lvol@ (CFCCAE0D; see #35230).

* Thu Aug 16 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.150-alt1
- Added keys:
  + majioa@ (00F19E2D; see #35086);
  + mars@ (295B9BBF; #35230).

* Wed Aug 08 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.149-alt1
- Added keys:
  + anton@ (8A6FE6AB; see #30734);
  + pak@ (CC23C2B8; see #35030).

* Fri Aug 03 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.148-alt1
- Added key: underwit@ (1FA66FA3; see #35035).

* Wed Jul 25 2018 Dmitry V. Levin <ldv@altlinux.org> 0.7.147-alt1
- Added key: arei@ (A564E495; see #35093).
- Removed keys:
  + zoros@ (72D56A88; see #33331);
  + stark@ (A846BEC7; see #33635).

* Tue Jun 19 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.146-alt1
- Updated expired key: darktemplar@ (D4C6316F; closes: #35057).

* Thu Jun 07 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.145-alt1
- Replaced key: cow@ (230B7611 -> 97FDAF8D; closes: #31130).

* Fri Jun 01 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.144-alt1
- Added key: omg@ (21E5D85B; closes: #34563).
- Added key: asheplyakov@ (4EBCC542; closes: #34883).
- Added key: ac1d@ (7D2CE7FB; closes: #34694).

* Mon May 28 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.143-alt1
- Added key: olegeg@ (2973DF7F; closes: #34676).
- Added key: hepoh@ (11F3210C; closes: #34726).

* Thu May 03 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.142-alt1
- Added key: jqt4@ (7FED2BC1; closes: #34659).

* Wed Apr 18 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.141-alt1
- Replaced key: shaba@ (DD9F673B -> BFE05A59; closes: #21654).

* Tue Apr 10 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.140-alt1
- Replaced expired key: manowar@ (7CE4360C -> A321B068; closes: #34789).

* Wed Apr 04 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.139-alt1
- Added key: dzagrebin@ (7A0A93F2; closes: #34529).

* Fri Mar 30 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.138-alt1
- Replaced key: grenka@ (6262D719 -> F502E3C5; closes: #34733).

* Fri Mar 23 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.137-alt1
- Added key: nickel@ (91B59FCF; closes: #34532).

* Tue Mar 13 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.136-alt1
- Added key: mrdrew@ (318C46B0; closes: #34547).

* Mon Mar 05 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.135-alt1
- Added key: vt@ (D40589C4; closes: #34494).

* Mon Feb 19 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.134-alt1
- Added key: aminov@ (F7F5D184; closes: #34007).

* Thu Feb 15 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.133-alt1
- Updated key: bircoph@ (5372756C; closes: #34543).
- Added key: mik@ (CD713CA3; closes: #34283).

* Mon Feb 05 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.132-alt1
- Replaced expired key: ildar@ (B2052C03 -> 799AEF89; closes: #22294).
- Added key: aas@ (97B7B549; closes: #34329).

* Mon Jan 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.131-alt1
- Added keys:
  + mvoronov@ (87D45ADA; closes: #34438);
  + x09@ (0C16659B; closes: #34359);
  + gkot@ (21C4D4CB; closes: #34282).

* Fri Jan 12 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.130-alt1
- Added key: trubach@ (39CEFF80; closes: #34115).

* Tue Oct 24 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.129-alt1
- Added keys:
  paulelms@ (02A9FF96; closes: #34005);
  bircoph@ (5372756C; closes: #34009).

* Thu Sep 28 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.128-alt1
- Added key: alexey@ (5D97B057; closes: #33730).

* Tue Sep 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.127-alt1
- Added key: grenka@ (6262D719; closes: #33877).

* Fri Sep 01 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.126-alt1
- Added key: klark@ (9FF8259F; closes: #33780).

* Wed Aug 30 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.125-alt1
- Replaced expired key: lakostis@ (59D16867 -> C4C4A01E; closes: #33821).

* Wed Aug 09 2017 Dmitry V. Levin <ldv@altlinux.org> 0.7.124-alt1
- Replaced key: arseny@ (3E6DF190 -> 62E619E5; closes: #33679).
- Added key: slev@ (5D9A19E8; closes: #33625).

* Wed Aug 02 2017 Dmitry V. Levin <ldv@altlinux.org> 0.7.123-alt1
- Updated expired key: at@ (38E7BB46; closes: #33708).
- Added key: arseny@ (3E6DF190; closes: #33679).

* Fri Jul 21 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.122-alt1
- Added key: stark@ (A846BEC7; closes: #33635).

* Fri Jun 30 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.121-alt1
- Updated key: obirvalger@ (2840F0FE).
- Updated expired key: boyarsh@ (83724063).

* Mon Jun 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.120-alt1
- Added key: darktemplar@ (D4C6316F; closes: #33560).

* Fri Jun 23 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.119-alt1
- Added key: gremlin@ (3D879005; closes: #33578).
- Replaced expired key: kirill@ (C78106FB -> 378C3619; closes: #33582).

* Tue Jun 13 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.118-alt1
- Added key: kondratyuk@ (243C51FE; closes: #33504).

* Mon Jun 05 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.117-alt1
- Updated expired key: aris@ (96C47AC2; closes: #33523).

* Thu May 25 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.116-alt1
- Replaced expired key: sbolshakov@ (E70A1172 -> 2DA1DFA5).

* Thu Apr 13 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.115-alt1
- Added key: zoros@ (72D56A88; closes: #33331).

* Tue Apr 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.114-alt1
- Added key: jenya@ (DD4207C2; closes: #33336).

* Mon Apr 03 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.113-alt1
- Replaced expired key: manowar@ (CB160A7C -> 7CE4360C).

* Thu Mar 23 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.112-alt1
- Added key: kernelbot@ (860B389E; closes: #33269).

* Fri Mar 17 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.111-alt1
- Added key: obirvalger@ (2840F0FE; closes: #33237).

* Mon Feb 27 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.110-alt1
- Added key: mcpain@ (CFE5AD4F; closes: #33146).

* Thu Feb 16 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.109-alt1
- Added key: lepata@ (D69E77A6; closes: #33061).

* Tue Feb 07 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.108-alt1
- Replaced key: week@ (9B062B32 -> 1B9B0273; closes: #33082).

* Sat Jan 28 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.107-alt1
- Added key: lineprinter@ (C6E4FEA1; closes: #33017).

* Mon Jan 23 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.106-alt1
- Added key: grumbler@ (F979132F; closes: #30532).

* Thu Jan 12 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.105-alt1
- Replaced expired key: naf@ (4C8055EB -> DD7132A6; closes: #32989).

* Mon Dec 19 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.104-alt1
- Replaced key: taf@ (9B769DEF -> 1AB92436; closes: #32897).
- Added key: sotor@ (43502B3E; closes: #32551).

* Wed Dec 07 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.103-alt1
- Replaced key: alexvm@ (28E76F05 -> DAA60B03; closes: #31765).

* Tue Nov 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.102-alt1
- Added key: zorg@ (442C06D6; closes: #30311).

* Mon Oct 24 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.101-alt1
- Added key: cronsync@ (A8E6DA50; closes: #32636).

* Mon Oct 24 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.100-alt1
- Replaced key: esyr@ (2C9E8768 -> 298E79A7; closes: #32654).

* Thu Sep 15 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.99-alt1
- Added keys:
  ekorneechev@ (B291E25D; closes: #32418);
  madcracken@ (A9EB25D1; closes: #31328).

* Thu Sep 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.98-alt1
- Replaced key: shadrinov@ (11C5751B -> 18C54D44).

* Sat Apr 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.97-alt1
- Replaced key: crux@ (11F19995 -> 16EDA98B; closes: #31949).

* Wed Mar 16 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.96-alt1
- Replaced key: pma@ (7D7A6670 -> 220689DD; closes: #31866).

* Mon Jan 18 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.95-alt1
- Updated key: ildar@ (B2052C03; closes: #22294).

* Thu Dec 24 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.94-alt1
- Replaced key: glebfm@ (CF429DFB -> D098D624).

* Thu Dec 24 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.93-alt1
- Added key: vseleznv@ (2AD3A84B; closes: #31633).

* Thu Nov 12 2015 Dmitry V. Levin <ldv@altlinux.org> 0.7.92-alt1
- Replaced key: ldv@ (F7DDBB3A -> A340AEB7).

* Tue Nov 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.91-alt1
- Replaced expired key: nbr@ (966B352F -> 95781CE0; closes: #31458).

* Sat Oct 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.90-alt1
- Added key: qa_glebfm@ (AE998E7A).

* Thu Sep 24 2015 Dmitry V. Levin <ldv@altlinux.org> 0.7.89-alt1
- Replaced expired key: shaba@ (5A3D03BA -> DD9F673B).
- Updated key: solo@ (2BDCCA89; closes: #31177).

* Thu Jul 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.88-alt1
- Replaced expired key:
  ali@ (125A1A7E -> FEC65B11; closes: #30781).
- Replaced key:
  cow@ (64CFCE0B -> 230B7611; closes: #31130).
- Added key: antohami@ (289D2295; closes: #31125).

* Fri Jan 30 2015 Dmitry V. Levin <ldv@altlinux.org> 0.7.86-alt1
- Added key: shadrinov@ (11C5751B; closes: #30319).

* Thu Jan 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.85-alt1
- Added key: galizin@ (201950A9; closes: #30547).

* Tue Dec 23 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.84-alt1
- Added key: cheusov@ (B37709ED; closes: #30499).

* Wed Aug 06 2014 Dmitry V. Levin <ldv@altlinux.org> 0.7.83-alt1
- Added key: bassmaster@ (185DEF5B; closes: #30168).

* Fri Jul 18 2014 Dmitry V. Levin <ldv@altlinux.org> 0.7.82-alt1
- Replaced expired key:
  manowar@ (063E9E37 -> CB160A7C; closes: #30184).

* Wed May 21 2014 Dmitry V. Levin <ldv@altlinux.org> 0.7.81-alt1
- Added key: akv@ (DA718D1F; closes: #29955).
- Updated keys: aris@ (96C47AC2).

* Tue Mar 04 2014 Dmitry V. Levin <ldv@altlinux.org> 0.7.80-alt1
- Replaced key: zver@ (304B781A -> 6660A9A2; closes: #29841).
- Added key: danil@ (4FDAC044; closes: #29441).

* Fri Jan 17 2014 Dmitry V. Levin <ldv@altlinux.org> 0.7.79-alt1
- Updated key: naf@ (4C8055EB; closes: #25143).
- Added key: ikar@ (E9C46618; closes: #29605).

* Wed Jan 08 2014 Dmitry V. Levin <ldv@altlinux.org> 0.7.78-alt1
- Updated key: ildar@ (B2052C03; closes: #22294).

* Tue Jan 07 2014 Dmitry V. Levin <ldv@altlinux.org> 0.7.77-alt1
- Added key: imz@ (09F75778; closes: #29687).

* Tue Nov 12 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.76-alt1
- Replaced key: asdus@ (ABE04615 -> 05DA4602).
- Added key: barssc@ (62CFAFBE; closes: #29461).

* Fri Sep 20 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.75-alt1
- Added key: cronport@ (E2C322D8; closes: #29339).

* Mon Aug 26 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.74-alt1
- Replaced key:
  karpov@ (8456EC8E -> C3AB1F57; closes: #29293).

* Thu Jul 11 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.73-alt1
- Replaced expired key:
  manowar@ (6661C80B -> 063E9E37; closes: #29174).

* Mon Jun 10 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.72-alt1
- Added key: aoliakh@ (AF267EAC; closes: #29021).

* Fri Jun 07 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.71-alt1
- Updated keys: morozov@ (FD39D372).

* Tue Jun 04 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.70-alt1
- Updated keys: aris@ (96C47AC2).

* Wed May 22 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.69-alt1
- Added key: qwest@ (9BE30705; closes: #28764).

* Mon Apr 22 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.68-alt1
- Added key: kotbegemot@ (37005EC8; closes: #28832).

* Sat Apr 13 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.67-alt1
- Added key: qa_ldv@ (1FE22419).

* Sun Mar 24 2013 Dmitry V. Levin <ldv@altlinux.org> 0.7.66-alt1
- Added key:
  valintinr@ (F8B56953; closes: #28479).

* Thu Nov 15 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.65-alt1
- Added key:
  cow@ (64CFCE0B; closes: #27969).

* Thu Oct 18 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.64-alt1
- Added key:
  tonik@ (17CAE505; closes: #27772).
- Replaced key:
  radik@ (8F78840A -> 82C6FAA9; closes: #27857).

* Thu Oct 04 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.63-alt1
- Replaced expired key:
  peet@ (539EAF87 -> 81140BF3).

* Tue Aug 07 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.62-alt1
- Updated keys:
  solo@ (2BDCCA89; closes: #27617).

* Tue Jul 31 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.61-alt1
- Added key:
  asdus@ (ABE04615; closes: #27524).

* Mon Jul 23 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.60-alt1
- Replaced keys:
  lakostis@ (172BC0F5 -> 59D16867; closes: #27562).

* Thu Jul 05 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.59-alt1
- Updated keys:
  manowar@ (6661C80B);

* Tue Jun 19 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.58-alt1
- Updated keys:
  boyarsh@ (83724063);
- Replaced key:
  kirill@ (9BC907B4 -> C78106FB; closes: #27465).

* Thu May 31 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.57-alt1
- Updated keys:
  rider@ (6BE5C0AB; closes: #27380);

* Wed May 23 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.56-alt1
- Replaced key:
  sbolshakov@ (C7527023 -> E70A1172).

* Thu May 03 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.55-alt1
- Added key:
  ali@ (125A1A7E; closes: #27006).

* Sun Apr 22 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.54-alt1
- Updated key:
  updates@ (231114B3).

* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.53-alt1
- Added key:
  esyr@ (2C9E8768).

* Mon Apr 09 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.52-alt1
- Replaced key:
  icesik@ (50274733 -> CFE26B8C; closes: #27182).

* Mon Mar 26 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.51-alt1
- Replaced key:
  taf@ (ECC29296 -> 9B769DEF; closes: #27127).

* Wed Mar 21 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.50-alt1
- Added key:
  lbutorina@ (2A60EFCE; closes: #26822).

* Fri Mar 16 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.49-alt1
- Remove keys of resigned people:
  raorn@ (AF3ABA49).

* Mon Mar 12 2012 Dmitry V. Levin <ldv@altlinux.org> 0.7.48-alt1
- Updated keys:
  baraka@ (480DEE67; closes: #23920);
  zerg@ (1C2A3F08; closes: #26994).

* Fri Nov 18 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.47-alt1
- Updated keys:
  ildar@ (B2052C03; closes: #22294).

* Fri Nov 11 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.46-alt1
- Replaced key:
  mex3@ (082B706A -> B5EDCB43).

* Thu Oct 13 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.45-alt1
- Added key:
  cetus@ (21081521; closes: #25870).

* Thu Sep 08 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.44-alt1
- Added key:
  ogion@ (538E7273; closes: #26204).

* Mon Sep 05 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.43-alt1
- Added key:
  yuk@ (8EBD651C; closes: #26024).
- Replaced expired key:
  dk@ (6B9ED85C -> 9AF81E60; closes: #26167).

* Fri Aug 05 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.42-alt1
- Added keys:
  dja@ (0A49969E; closes: #25233).

* Mon Jul 04 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.41-alt1
- Replaced expired key:
  manowar@ (96AC4B17 -> 6661C80B; closes: #25823).

* Sat May 21 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.40-alt1
- Replaced key:
  peet@ (3156C8D3 -> 539EAF87; closes: #25614).

* Tue Apr 19 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.39-alt1
- Added keys:
  torabora@ (6B078460; closes: #25397);
  mithraenbot@ (C283201A; closes: #24970).

* Wed Apr 13 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.38-alt1
- Added keys:
  mvk@ (6D63969F; closes: #24612);
  malo@ (9B0AED05; closes: #24727).

* Wed Mar 30 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.37-alt1
- Added keys:
  diana@ (38F7E41E; closes: #24767).

* Sat Feb 26 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.36-alt1
- Updated keys:
  naf@ (4C8055EB; closes: #25143).

* Thu Jan 13 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.35-alt1
- Added keys:
  etersoft-security@ (6F0D5886), etersoft-internal@ (72E83043)
  (closes: #24840).

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.34-alt1
- Replaced keys:
  gab@ (57AA7489 -> 45432555; closes: #24583).
- Added keys:
  alex@ (2B899CC8; closes: #24762).

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.33-alt1
- Updated keys:
  ldv@ (F7DDBB3A).
- Removed expired keys:
  atl@ (8E5A40B8; expired 2010-06-22);
  barabashka@ (19F61B3C; expired 2010-05-26);
  kharpost@ (8EC58E3D; expired 2010-08-14);
  robin@ (E3AB63F3; expired 2010-04-26).

* Fri Nov 12 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.32-alt1
- Added keys:
  pauli@ (6B05E9C2; closes: #24083).

* Tue Nov 02 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.31-alt1
- Replaced key:
  raorn@ (F913F30A -> AF3ABA49; closes: #24480).

* Mon Oct 18 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.30-alt1
- Added keys:
  timonbl4@ (59FE2CE6; closes: #24184);
  ach@ (ABBB7E40; closes: #24216).

* Fri Aug 27 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.29-alt1
- Added keys:
  baraka@ (98E5D873; closes: #23920);
  baywind@ (53BD0B4A; closes: #23977);
  cronbuild@ (278EB305; closes: #23922).

* Wed Aug 11 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.28-alt1
- Replaced key:
  radik@ (611552A9 -> 8F78840A; closes: #23862).

* Fri Jul 30 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.27-alt1
- Added keys:
  dd@ (3F596576; closes: #23561).

* Fri Jul 23 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.26-alt1
- Replaced expired key:
  manowar@ (7F7B7BC7 -> 96AC4B17).

* Thu Jul 15 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.25-alt1
- Added keys:
  glebfm@ (CF429DFB; closes: #23714).

* Mon May 31 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.24-alt1
- Added keys:
  kaman@ (E3A722F0; closes: #23538).

* Tue May 25 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.23-alt1
- Removed ghost keys:
  alexd@ (A00B441F);
  altruist@ (77EEE930);
  andreyka@ (BE63B4B7);
  avatar@ (56D99BDE);
  avd@ (5AB60307);
  avl@ (1DB4F366);
  az@ (637B61FD);
  banzaj@ (52B4447A);
  canis@ (CF39B9D3);
  chumpa@ (61E38C74);
  const@ (A02ACF73);
  darkstar@ (C56C8F21);
  dav@ (1D6DC85D);
  device@ (BCA066BF);
  dfo@ (785C5D0C);
  dh@ (FE4226E5);
  dizatorr@ (60B1A651);
  dketov@ (82A040A8);
  ed@ (450C39A7);
  eupenik@ (81790F8A);
  fc@ (7E70F2A3);
  fomichev@ (DA567B89);
  ghost@ (ACC6A340);
  go@ (2CDB48CD);
  gritzko@ (DC149698);
  hmepas@ (FA2527F1);
  ilar@ (7532D2F2);
  imz@ (45F0B3A0);
  jmura@ (F811B81E);
  koka@ (21F067FA);
  kt@ (85F4AD9A);
  kutovoy@ (9478C3B1);
  llk@ (EA323324);
  luch@ (A633D7C5);
  maldim@ (CFADA95C);
  markelov@ (6B858CF7);
  matveev@ (9686CB9E);
  maverik@ (C322A0C2);
  mb@ (FEA58EA9);
  meaty@ (65E7F7F2);
  mv@ (81153278);
  naumen@ (605AF46D);
  nikon@ (4B3567CE);
  oes@ (C98CF3D2);
  ott@ (26A9E254);
  past@ (DD89E169);
  phoenix@ (1239D355);
  pitch@ (E499447B);
  pvolkov@ (85505A9E);
  rad@ (05171A88);
  riiki@ (FA4D2E9B);
  sacha@ (8B1AE734);
  sadist@ (0EB72CE8);
  saint@ (ED6CE75C);
  scampler@ (07CE0B64);
  seirge@ (6704D662);
  smi@ (A090B5C8);
  someone@ (F60AB998);
  spider@ (77E800F5);
  ssg@ (B7AF5448);
  ssv@ (5F874695);
  sycore@ (8F022DAA);
  tma@ (C9DB6FF2);
  umka@ (155BAB0C);
  userad@ (CD7C4DA7);
  v_p@ (0F71D515);
  vakhov@ (B316FB51);
  vasy@ (B7DBFAED);
  voldar@ (CF22BF31);
  vserge@ (0A210834);
  vsl@ (98C968F9);
  xstranger@ (32AA4F2B);
  yurix@ (FDF0ECB8).
- Removed expired keys:
  jeninho@ (2B12EEC6, expired 2009-11-17);
  sadeness@ (E048098B, expired 2010-02-04).
  bezruk@ (884158D4, expired 2010-02-25);
  dek@ (EA4DC1D7, expired 2010-03-04);
  brun@ (59ADF9BD, expired 2010-03-21).
- Added keys:
  rad@ (0FCE73BB; closes: #23284);
  boresexpress@ (A64F0221; closes: #23296);
  mzhukov@ (46309F89; closes: #23404).

* Tue Apr 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.22-alt1
- Added keys:
  lamp@ (0AB24E63; closes #23124)

* Tue Apr 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.21-alt1
- Added keys:
  rolland@ (280BEAC3; closes #23046)

* Wed Apr 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.20-alt1
- Added keys:
  nenderus@ (20BFE6FD; closes #23324)
  letanton@ (DF7C83B7; closes #23326)

* Mon Feb 22 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.19-alt1
- Added keys:
  radik@ (611552A9; closes: #22565).

* Thu Jan 28 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.18-alt1
- Replaced key:
  arc@ (D9AD55AD -> FAF2CACE; closes: #22618).

* Wed Dec 23 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.17-alt1
- Replaced key:
  lnkvisistor@ (4E6333D7 -> FECF3E29; closes: #22408).

* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.7.16-alt1
- Updated keys:
  inger@ (EF2A6826)

* Mon Nov 16 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.15-alt1
- Updated keys:
  ildar@ (B2052C03; closes: #22294).

* Tue Nov 10 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.14-alt1
- Replaced key:
  anyr@ (6F57286E -> F3B462C2).

* Wed Nov 04 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.13-alt1
- Added keys:
  repocop@ (E029A65B; closes: #22132).
- Changed packaging to noarch.

* Sun Nov 01 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.12-alt1
- Replaced key:
  dkr@ (1BD0636C -> 9B22C967; closes: #21926).
- Added keys:
  elly@ (2B42763F; closes: #21691).
  michael@ (607A0B33; closes: #22030).

* Thu Oct 22 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.11-alt1
- Updated keys:
  updates@ (231114B3).
- Replaced key:
  nbr@ (9D54ED87 -> 966B352F; closes: #21969).

* Mon Sep 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.10-alt1
- Updated keys:
  shaba@ (5A3D03BA; closes: #21654).

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.9-alt1
- Replaced keys:
  dottedmag@ (A26F54C8 -> 3E338888; closes: #20009).

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.8-alt1
- Replaced keys:
  stalker@ (71F22C05 -> 4CBDFEAD; closes: #21100).
- Added keys:
  platform5@ (556DF34A).

* Mon Aug 17 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.7-alt1
- Replaced keys:
  kharpost@ (B6D80A43 -> 8EC58E3D; closes: #21079).
- Added keys:
  alecs@ (4222D8AA; closes: #20870).

* Sun Aug 09 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt1
- Replaced keys:
  evyscr@ (7688321E -> E3F3C431; closes: #20953).
- Added keys:
  vostok@ (ADFFBCC0; closes: #20853).
- Removed keys:
  avp@ (CD94DF33, expired 2008-08-03);
  blake@ (2DEF51AD, expired 2009-03-07);
  gilving@ (874FA95A, expired 2009-04-19);
  migor@ (CBEF2737, expired 2009-02-01).

* Mon Jul 27 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt1
- Updated keys:
  solo (2BDCCA89; closes: #20881).

* Sun Jun 28 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- Replaced keys:
  manowar (A53F070A -> 7F7B7BC7).
- Updated keys:
  avm (E3069EBD; closes: #20621).

* Mon Jun 22 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt1
- Updated key: p_solntsev -> psolntsev (33DDE4EB).

* Mon Jun 08 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.2-alt1
- Replaced keys:
  wrar (1166B795 -> 2866F3C1; closes: #20373).

* Fri Jun 05 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.1-alt1
- Replaced keys:
  thresh (FAAB9084 -> A0AF822A),
  becase (0DCFB5A8 -> DC0F7520),
  m31 (48852C02 -> 4C78E18B).

* Wed Apr 29 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- update keys: bertis (closes: #19816)

* Mon Apr 20 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- improve subkey check and strip
- fix keys: anarresti (closes: #19654)

* Fri Apr 17 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- add keys: vitus

* Wed Apr 08 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- fix keys: raorn
- improve alt-gpgkey-check and alt-gpgkey-strip utilities

* Wed Apr 08 2009 Stanislav Ievlev <inger@altlinux.org> 0.5.1-alt5
- update keys: raorn

* Thu Apr 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.5.1-alt4
- add keys: andyc, yushi

* Mon Mar 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.5.1-alt3
- add keys: anarresti

* Mon Feb 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.5.1-alt2
- add keys: lizzard, remaks

* Sun Feb 08 2009 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- Replaced keys:
  abr (885B6677 -> 6A9325EA).

* Mon Jan 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt16
- add: zidex
- update: morozov, kga

* Wed Jan 14 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt15
- add: conoc
- update: fmartini

* Mon Dec 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt14
- add: real, kga, droid

* Thu Dec 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt13
- update: lunetta

* Thu Dec 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt12
- update: zver
- add: zlos

* Thu Nov 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt11
- add keys: litvinovg, alunix, jeninho
- replace keys: alexvm

* Mon Nov 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt10
- add keys: alexvm, alsroot, vaa

* Thu Nov 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt9
- replace keys: piastry, greg

* Fri Oct 31 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt8
- replace keys: lnkvisistor

* Fri Oct 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt7
- add keys: kharpost, lnkvisistor, piastry

* Tue Oct 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt6
- add keys: dkoryavov, dplakhov, hsv, lbeasty
- replace key: vvpi

* Fri Sep 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- add keys: rom_as lunetta
- replace key: zhum

* Fri Sep 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- add keys: pbb vvpi
- alt-gpgkey-check: Cleanup (ldv@)

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- move utilities to separate subpackage
- update key: genix
- remove orphaned keys

* Mon Sep 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- add utility to strip gpg key

* Wed Sep 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add utility to test gpg key

* Fri Aug 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt10
- add keys: ender, rainbow

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt9
- add key: arc

* Tue Aug 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt8
- replace key: karpov

* Fri Jul 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt7
- add keys: vip, erthad

* Wed Jun 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt6
- add keys: manowar

* Wed Jun 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt5
- add keys: yurifil, p_solntsev, becase

* Wed May 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt4
- replace keys: barabashka

* Wed May 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt3
- add keys: kipruss

* Tue May 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt2
- add keys: iv, aris
- replace keys: vladimir

* Wed May 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.11-alt1
- add keys: wart, gray_graff, genix, wart

* Wed May 07 2008 Dmitry V. Levin <ldv@altlinux.org> 0.4.10-alt1
- Added key: qa-school (5ADE79BC).

* Sat Apr 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.9-alt4
- merge with ldv@ (Remove all remained subkeys)
- add keys: ildar

* Mon Apr 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.9-alt3
- add keys: amike

* Sun Apr 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.9-alt2
- add keys: shev, loki

* Mon Mar 31 2008 Dmitry V. Levin <ldv@altlinux.org> 0.4.9-alt1
- Replaced keys:
    dlebkov (D24EBCA4 -> 4A81DE8B)
- Removed keys:
    amike (E4A4648A, expired 2007-05-19)
    aris (C1ED20AE, expired 2008-02-25)
    avn (23C409AB, expired 2007-11-19)
    combr (A18DCDDE, expired 2008-03-08)
    cornet (111453ED, expired 2007-05-12)
    cray (A891000F, expired 2006-12-15)
    fattie (881ED0FA, expired 2007-12-17)
    genix (E618D733, expired 2008-03-30)
    greyp (9FDBEDFF, expired 2007-05-31)
    horror (C668B665, expired 2007-12-03)
    ildar (B2052C03, expired 2006-11-11)
    ldv (C1E23429, expired 2006-03-05)
    mouse (5DC64658, expired 2006-09-20)
    sa (2C54D264, expired 2006-06-13)

* Sun Mar 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.8-alt5
- add keys: prividen boris
- update keys: blake anyr

* Thu Mar 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.8-alt4
- add keys: sem

* Thu Feb 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.8-alt3
- update key: avm
- add keys: slazav vkni rlz

* Wed Feb 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.8-alt2
- add key: mtbest

* Tue Feb 19 2008 Dmitry V. Levin <ldv@altlinux.org> 0.4.8-alt1
- Added key: aspsk

* Sun Feb 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.7-alt5
- update keys: naf

* Mon Feb 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.7-alt4
- add keys: kana balbeko

* Thu Jan 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.7-alt3
- add keys: vladimir slavutich

* Fri Jan 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.4.7-alt2
- add key: ravil

* Thu Dec 20 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.7-alt1
- Updated keys: at.

* Mon Dec 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt11
- replace key: xmm
- add key: misha

* Fri Nov 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt10
- Add keys:
    bertis

* Tue Oct 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt9
- Add keys:
    snejok

* Fri Oct 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt8
- Add keys:
    aquarius
    redbaron
    zhum

* Thu Oct 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt7
- Add keys:
    lodin

* Mon Oct 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt6
- Add keys:
    greg

* Mon Sep 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt5
- Add keys:
    gab

* Fri Aug 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt4
- Add keys:
    worklez

* Fri Jul 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt3
- Added keys:
    demion

* Fri Jun 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.6-alt2
- Added keys:
    open

* Tue Jun 26 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.6-alt1
- Updated keys:
    nidd
- Replaced keys:
    svyt

* Mon Jun 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt10
- Replaced keys:
    svyt

* Fri Jun 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt9
- Added keys:
    svyt

* Fri Jun 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt8
- Added keys:
    dez
    huffman
    sadeness

* Tue Jun 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt7
- Updated keys:
    boyarsh

* Fri Jun 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt6
- Replaced keys:
    icesik
- Added keys:
    kurakin

* Thu May 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt5
- Updated keys:
    sbolshakov
    svd
- Added keys:
    morozov

* Mon May 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt4
- Replaced keys for ashen (Alexey Shentzev)

* Fri May 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt3
- Replaced keys for barabashka (Sergey Lebedev)

* Sat Apr 28 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.5-alt2
- Added keys:
    874FA95A (Andrey Shelvin aka Gil Ving)

* Wed Apr 25 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.5-alt1
- Added keys:
    07E9C65D (ALT Linux 4.0 backports)

* Tue Apr 24 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt1
- Added keys:
    231114B3 (ALT Linux 4.0 updates)

* Wed Apr 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.3-alt5
- Added keys:
    3156C8D3 (Peter V. Saveliev)
    DCE06648 (Denis Klimov)

* Mon Apr 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.3-alt4
- Added keys:
    C11B44DB (Andrey Konnov)
    135F2336 (Yuriy Kashirin)
    25AF14A3 (Vitaly Kuznetsov)

* Thu Mar 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.3-alt3
- Added keys:
    A9EBF131 (Andrey Cherepanov)
    EA4DC1D7 (Denis Kuznetsov)
    082B706A (Alexandra Panyukova)

* Mon Mar 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.3-alt2
- Added keys:
    DE3A1D1D (Yurkovsky Andrey)

* Fri Mar 02 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.3-alt1
- Updated keys:
    5A3D03BA (Alexey Shabalin)

* Thu Mar 01 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt1
- Changed source keys layout from id-based to uid-based.
- Updated keys:
    2BDCCA89 (Aleksey Avdeev)

* Mon Feb 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt26
- Replaced keys:
    B063A4B3 with 289196AA (Andriy Stepanov)

* Tue Feb 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt25
- Added keys:
    A26F54C8 (Mikhail Gusarov)

* Wed Feb 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt24
- Added keys:
    172BC0F5 (Konstantin A. Lepikhov)
- Updated keys:
    C18ED673 (Konstantin A. Lepikhov)

* Tue Jan 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt22
- Added keys:
    1BD0636C (Dmitriy L. Kruglikov)
    BD821656 (Alex Bogomolov)

* Tue Jan 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt21
- Added keys:
    D4889701 (Alexey Sidorov)

* Fri Dec 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt20
- Replaced keys:
	2460FA4E with 0ED8FC24 (Vitaly A. Ostanin)

* Wed Dec 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt19
- Added keys:
    7688321E (Egor Vyscrebentsov)
    C322A0C2  (Eugine V. Kosenko)

* Mon Dec 04 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt18
- Added keys:
    F811B81E(Yurii Diduh)
    D7C7C2E8(Alexey Morsov)

* Wed Nov 22 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt17
- Added keys:
    3ADDB8A7 (Sergey rt@)

* Fri Oct 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt16
- Added keys:
    9478C3B1 (Kutovoy Nickolay)

* Fri Oct 20 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt15
- Added keys:
    9B062B32 (Grigory Milev)

* Tue Oct 17 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt14
- Added keys:
    11992D8D (Wad Mashckoff)

* Mon Oct 09 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt13
- Added keys:
    9D54ED87 (Denis Medvedev)
- Removed keys:
    EAC91CA0 (ALT Security Team) [expired: 2006-03-05]
    E62B43B4 (Artem K. Jouravsky) [expired: 2006-10-04]
    AC278398 (S. Budnevitch) [expired: 2006-06-18]
    AE59C160 (Grigory Milev) [expired: 2006-09-02]

* Fri Sep 22 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt12
- Added keys:
    05F572FD (Alex Karpov)

* Fri Sep 15 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt11
- Added keys:
    A633D7C5 (Nickolay Petrov)

* Thu Sep 07 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt10
- Added keys:
    6B9ED85C (Denis Kirienko)
    083F18F8 (Hihin Ruslan)
- Replaced keys:
    667F7B2C with AE474A9B (Eugene Ostapets)

* Tue Aug 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt9
- Replaced keys:
    D9CFD89E with 1354F7DC (Yury A. Romanov)

* Fri Aug 25 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt8
- Added keys:
    D69874DC (Denis Pynkin)
    ADD0C444 (Gennadi Motsyo)

* Wed Jul 19 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt7
- Replaced keys:
    84147704 with 2BDCCA89 (Aleksey Avdeev)

* Tue Jul 11 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt6
- Added keys:
    7D7A6670 (Pokidko Mikhail)

* Tue Jun 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt5
- Added keys:
    3E6141C8 (Evgenii Terechkov)
    48852C02 (Dima Spodarets)

* Wed Jun 21 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt4
- Updated keys:
    9C0CCD48 (Aleksandr Blokhin)
    826EFA39 (Alexey Voinov)

* Thu Jun 15 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt3
- Replaced key:
    B83C1BBD with 32AA4F2B (xstranger)

* Tue Jun 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.4.1-alt2
- Updated keys:
    6AFD52A3 (Yury A. Zotov)
- Added keys:
    AC564253 (Sergey A. Sukiyazov)

* Mon Jun 12 2006 Dmitry V. Levin <ldv@altlinux.org> 0.4.1-alt1
- Updated keys:
    D3C994B8 (Mikhail Zabaluev)
- Removed keys:
    050FD52C (Peter V. Saveliev) [expired: 2006-04-20]
    09ABDEB6 (Alexey Novodvorsky) [expired: 2006-03-13]
    1475AF92 (Konstantin Volckov) [expired: 2006-03-14]
    5D11AE85 (Grigory Fateyev) [expired: 2006-05-05]
    7D442FC3 (Stanislav Ievlev) [expired: 2006-03-12]
    FD39D372 (Alexey Morozov) [expired: 2006-05-19]

* Sat Jun 03 2006 Dmitry V. Levin <ldv@altlinux.org> 0.4.0-alt1
- Split source keyblock on per-key basis.
- Removed all subkeys.
- Updated keys:
    AC93C324 (Igor Zubkov)

* Fri Jun 02 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt9
- Added keys:
    BA0CCCA2 (Alexey Shentzev)
    D9CFD89E (Yury A. Romanov)

* Tue May 02 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt8
- Added keys:
    03FB7443 (Artem Zolochevskiy)

* Mon Apr 10 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt7
- Added keys:
    88E114A2 (Denis Smirnov)

* Thu Apr 06 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt6
- Added keys:
    B2052C03 (Ildar Mulyukov)

* Thu Mar 23 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt5
- Updated keys:
    84147704 (Aleksey Avdeev)

* Mon Mar 20 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt4
- Added keys:
    B063A4B3 (Andriy Stepanov)

* Fri Mar 17 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt3
- Added keys:
    D047C102 (Grigory Mozhaev)

* Tue Mar 14 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.10-alt2
- Added keys:
    A18DCDDE (Mike Lykov)
    860A5745 (Sergey Mikerin)

* Mon Feb 27 2006 Dmitry V. Levin <ldv@altlinux.org> 0.3.10-alt1
- Added keys:
    6CFE9493 (leader)
    C1ED20AE (Yuri N. Sedunov)
    BA2E6DD8 (Michail Yakushin)
- Removed keys:
    4458F01F (Alexander Belov) [invalid format]
    ED1B7E12 (Yarik) [invalid format]
    64BB2D9F (Michail Yakushin) [obsolete]
- Updated keys:
    1C2A3F08 (Sergey V Turchin)
    6BE5C0AB (Anton Farygin)
    B60FC299 (Alexander Bokovoy)
    E3069EBD (Alex V. Myltsev)
- Removed all non-ALT uids, no need to duplicate pgp network.

* Tue Feb 21 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.9-alt3
- Added keys:
    FCE000BA (Oleg Parashchenko)
    E3AB63F3 (Serge Polkovnikov)

* Wed Feb 01 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3.9-alt2
- Added keys:
    D779C9B8 (Dmitriy Khanzhin)
    B7AF5448 (Sergey Godunov)

* Tue Jan 24 2006 Dmitry V. Levin <ldv@altlinux.org> 0.3.9-alt1
- Added keys:
    80EF7625 (ALT Security Team)
- Removed keys:
    9058FE5B (Igor Homyakov) [expired: 2006-01-01]

* Mon Dec 19 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.8-alt1
- Added keys:
    A891000F (Andrey Orlov)
    F7DDBB3A (Dmitry V. Levin)
- Removed keys:
    EC6375F8 (Vadim Gorodisky) [expired: 2005-08-11]
    D765EC45 (Yuri N. Sedunov) [expired: 2005-11-01]
    D6D3FCDC (Sergey Degtyaryov) [expired: 2004-12-24]
    AD0D73E5 (leader) [expired: 2005-03-02]
    297CA5DD (Gerasimov S. Dmitry) [expired: 2005-07-05]
    BD9AC682 (Andrey Orlov) [expired: 2005-10-14]

* Thu Dec 15 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt12
- Added keys:
    F770695E (Eugene Prokopiev)
    56C5158F (led)
- Updated keys:
    DFC51816 (Sergey Bolshakov)

* Tue Dec 06 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt11
- Added keys:
    1C215DE0 (Alexander Plikus)

* Thu Nov 03 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt10
- Updated keys:
    F913F30A (Alexey I. Froloff)
- Replaced keys:
    855D19CD with E62B43B4 (Artem K. Jouravsky)

* Tue Sep 27 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt8
- Replaced keys:
    3ADE1756 with 55F938BD (Alexey Lokhin)

* Fri Sep 16 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt7
- Added keys:
    1B6CC304 (Damir Shayhutdinov)
    81790F8A (Eugene V. Upenik)

* Wed Sep 14 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt6
- Added keys:
    8937F34F (Eugene Suchkov)
    64610D3A (Sergei Epiphanov)

* Wed Aug 10 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt5
- Added keys:
    77EEE930 (Semen)
    063B36C8 (Avramenko Andrew)
    419BF2CD (Maxim Bodyansky)

* Thu Jul 21 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt4
- Added keys:
    2617D562 (Boldin Pavel)
    CD7C4DA7 (Tumalevich Konstantin)

* Fri Jul 15 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt3
- Added keys:
    1462F45E (Vladimir V Kamarzin)

* Fri Jul 01 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.7-alt2
- Added keys:
    8E5A40B8 (Taras Ablamsky)
    71F22C05 (Anton Gorlov)

* Thu Jun 16 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.7-alt1
- Relocated keyring from %%_libdir to %%_prefix/lib.

* Thu Jun 09 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.6-alt5
- Added keys:
    667F7B2C (Eugene Ostapets)
    DA567B89 (Andrey Fomichev)
    9FDBEDFF (Erokhin Vitaliy)
    B83C1BBD (xstranger)
- Replaced keys:
    7027AD89 with AC93C324 (Igor Zubkov)

* Fri May 20 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.6-alt4
- Added keys:
    5D11AE85 (Grigory Fateyev)
    7027AD89 (Igor Zubkov)
    8F022DAA (Vladimir Petuhov)

* Fri May 06 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.6-alt3
- Added keys:
    6B858CF7 (Markelov Alexander)
    2CD6636F (Dmitry Marochko)
    B87D28B7 (Serge Ryabchun)
- Replaced keys:
    D3D94C61 with 9B8C3E56 (Dmitri Kuzishchin)
    47E8B80A with BCA066BF (Vitaliy Smirnov)

* Fri Apr 29 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.6-alt2
- Added keys:
    47E8B80A (Vitaliy Smirnov)
    8FA5956C (php-coder)
    85505A9E (Peter Volkov)
- Replaced keys:
    78D4A8A6 with 050FD52C (Peter V. Saveliev)

* Mon Apr 04 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.6-alt1
- Options: renamed to gpg.conf, added "quiet".
- Replaced keys:
    565F3312 with E618D733 (Eugene V. Horohorin).

* Tue Mar 15 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.5-alt6
- Added keys:
    E3069EBD (Alex V. Myltsev)
    884158D4 (Konstantin N. Bezruchenko)
- Updated keys:
    C18ED673 (Konstantin A. Lepikhov (LAKostis))
    7DE22DB1 (Sergey N. Yatskevich)

* Fri Feb 25 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.5-alt5
- Added keys:
    074CAE35 (Slava Dubrovskiy)
    9686CB9E (Mike Matveev)
- Replaced keys:
    690C9AA8 with 8770BF09 (Alexey Rusakov)

* Mon Jan 31 2005 Stanislav Ievlev <inger@altlinux.ru> 0.3.5-alt4
- Added keys:
    690C9AA8 (Alexey Rusakov)
    4C8055EB (Nikolay A. Fetisov)
- Replaced keys:
    9BE2F1F8 with 855D19CD (Artem K. Jouravsky)

* Thu Dec 23 2004 Stanislav Ievlev <inger@altlinux.ru> 0.3.5-alt3
- Added keys:
    ED1B7E12 (Yarik)
    E26C6950 (Serge Pavlovsky)
    CF22BF31 (Mikhael Korneev)
- Replaced keys:
    398074EE with C668B665 (Andy Gorev)
    E0B93E34 with 2460FA4E (Vitaly A. Ostanin)
- Removed keys:
    CFB74837 (Andrey Orlov) [expired  2004-11-10]

* Mon Nov 29 2004 Stanislav Ievlev <inger@altlinux.ru> 0.3.5-alt2
- Added keys:
    05171A88 (Ruslan Popov)
    3E1D08A9 (Sergey Lebedev)
    EF2A6826 (Stanislav Ievlev)
    07CE0B64 (Sasha Martsinuk)
    0F71D515 (Valery Pipin)

* Mon Oct 18 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3.5-alt1
- Added keys:
    BD9AC682 (Andrey Orlov)

* Tue Oct 12 2004 Stanislav Ievlev <inger@altlinux.ru> 0.3.4-alt2
- Added keys:
    845A2763 (Igor Vlasenko)
- Replaced keys:
    8799AAFE with 4B3567CE (Denis Klykvin)

* Wed Sep 22 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3.4-alt1
- Added keys:
    AE4AE412 (R. E. Gnimocni <incominger@altlinux.org>)

* Tue Sep 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt1
- Added keys:
    3E11BB57 (Leonid Shalupov)
- Replaced keys:
    7FB42AE0 with C56C8F21 (Albert R. Valiev)

* Mon Aug 30 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3.2-alt1
- Updated keys:
    C6C9CD8E (Anatoly Yakushin)

* Thu Aug 12 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- Removed keys:
    A4A75910 (Sergey Bolshakov)

* Wed Aug 11 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3.0-alt1
- Updated keys:
    EAC91CA0 (ALT Security Team)
    C1E23429 (Dmitry V. Levin)
    826EFA39 (Alexey Voinov)
    1C2A3F08 (Sergey V Turchin)
    B60FC299 (Alexander Bokovoy)
    D3C994B8 (Mikhail Zabaluev)
    9C0CCD48 (Aleksandr Blokhin)
- Replaced keys:
    C8941ACC with 9469A7A7 (Peter Novodvorsky)
- Removed keys:
    AB32681A (Sergey Pinaev)
    AA8D27DA (Victor V Ismakaev) [expires: 2004-05-30]

* Fri Jul 23 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.6-alt5
- Replaced keys:
    B7FB4E53 with E4A4648A (Mike A. Plugnikov)
    4251EB46 with 3F6E400C (Alexander Borovsky)
- Added keys:
    81153278 (Volkov Mike)
    FAAB9084 (Pavlov Konstantin)

* Thu Jul 08 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.6-alt4
- Replaced keys:
    548AAAF4 with 297CA5DD (Gerasimov S. Dmitry)
- Added keys:
    0A210834 (Serge A. Volkov)
    4251EB46 (Alexander Borovsky)
    048EF2B2 (Eugene Vlasov)

* Thu Jun 24 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.6-alt3
- Replaced keys:
    424A8E80 with 1E82EC87 (Alex Gorbachenko)
    7508B90A with A02ACF73 (Constantin Mikhaylenko)
- Added keys:
    E45731F1 (Ilya Evseev)
    4274EBA0 (Stanislav Yadykin)

* Mon May 24 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.6-alt2
- Replaced keys:
    95F00AA3 with 9BC907B4 (Kirill Maslinsky)
- Added keys:
    BE63B4B7 (Andrey Rogovsky)
    60B1A651 (Sergey A. Telitsyn)
    2F8D995B (Ivan Fedorov)
    B316FB51 (Alexey Vakhov)

* Fri May 21 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.6-alt1
- Added keys:
    FD39D372 (Alexey Morozov)
- Removed keys:
    0A210834 (Serge A. Volkov) [expires: 2003-03-07]
    52A9D67A (Peter V. Saveliev) [expires: 2004-01-25]
    548AAAF4 (Gerasimov Dmitry) [expires: 2004-05-05]

* Thu Apr 29 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.5-alt1
- Added keys:
    E93E890D (Alexey Tourbin)

* Thu Apr 29 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt9
- Replaced keys:
    2C482235 with FDF0ECB8 (Yury Konovalov)
- Added keys:
    424A8E80 (Alex Gorbachenko)
    7508B90A (Constantin Mikhaylenko)
    77E800F5 (Dmitry Porollo)
    C9DB6FF2 (Tkachenko Maxim)

* Tue Apr 13 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt8
- Added keys:
    8B1AE734 (Alexander Kotelnikov)

* Mon Apr 05 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.4-alt7
- Replaced keys:
    01D6FB51 with D24EBCA4 (Dmitry Lebkov)

* Fri Mar 26 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt6
- Added keys:
    C770E431 (Anton Korbin)
    11F19995 (Vladimir Lettiev)
    565F3312 (Eugene V. Horohorin)
    E40EE89B (Andrew Kornilov)
    AD0D73E5 (Valery Grazhdankin)
    6822A15B (Pavel Vainerman)
    9B808E2F (Sergey Ivanov)

* Thu Feb 05 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt5
- Replaced keys:
    F30AEFA4 with CBEF2737 (Igor Muratov)
    8EB2C7BA with 84147704 (Aleksey Avdeev)
    C72DAB66 with 9058FE5B (Igor Homyakov)
- Added keys:
    2E60DC67 (Nick S. Grechukh)

* Tue Feb 03 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt4
- Replaced keys:
    BA5CC9B7 with E504A88E, FEBC4AB1 (Yury Shramko)
- Added keys:
    D06F61FB (Sergey Y. Afonin)
    AB32681A, 785C5D0C (Sergey Pinaev)
    D3D94C61 (Dmitri Kuzishchin)
    82A040A8 (Dimitry V. Ketov)
    6704D662 (Sergey P. Kondratyev)

* Wed Jan 14 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt3
- Added keys:
    78D4A8A6 (Peter V. Saveliev)

* Tue Jan 06 2004 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt2
- Added keys:
    3BEFE928: (Gleb Stiblo)
    7FEF434E: (Andrei Bulava)
    0B8DB3D5: (Gennady Kovalev)
    21F067FA: (Konstantin Klimchev)
    D6D3FCDC: (Sergey Degtyaryov)
    8EB2C7BA: (Aleksey Avdeev)
- Updated keys:
    B60C9B72 (Michael Shigorin) - 5 new user IDs, 5 new signatures

* Fri Dec 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt1
- Added keys:
    61E38C74: (Ilya Kuznecov)
    66AD8D7E: (Alexey Borovskoy)
    A921DACA: (Evgeny Sinelnikov)
    BA5CC9B7: (Yury Shramko)

* Mon Nov 24 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt1
- Really complete the change mentioned in previous release.

* Wed Nov 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt1
- Added keys:
    CFB74837 (Andrey Orlov)
- Removed expired keys:
    F0F5CE65 (Andrey Orlov)

* Mon Nov 03 2003 Stanislav Ievlev <inger@altlinux.ru> 0.2.1-alt1
- Changed keys:
    9CD59F7C (Yuri N. Sedunov)
    A4C683B3 (Denis Klykvin)
- Added keys:
    5E47BC8A (Valery Inozemtsev)
    64BB2D9F (Michail Yakushin)
    E1D27426 (Denis Smirnov)

* Tue Oct 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Added keys:
    02DADC87 (Alex Yustasov)
    7C10D900 (Fr. Br. George)
- Removed unused keys:
    0C01FDB2 (Alexandr Bulankin)
    11924CB4 (Dimitry Saveliev)
    427929A0 (Nazar Yurpeak)
    5DA9A035 (Dmitry Smirnov)
    68B983AB (Yehuda Ben-Yosef)
    694058DF (Sergie Pugachev)
    7446DBF3 (Lenya L. Khachaturov)
    8E7A9657 (Alexey I. Froloff)
    90D17723 (Anton Kachalov)
    93527316 (Nazar Yurpeak)
    971A8D74 (Oleg Filippov)
    AD9D7336 (Stanislav Makarchuk)
    F6FEA0B3 (Nikita Gergel)
    FAC35F8C (Grigory Milev)
    FED140D7 (Nikita Gergel)

* Tue Oct 07 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt20
- Added keys:
    B7FB4E53: (Plugnikov A. Mike)
    A6E82964: (Michael Pozhidaev)
    F60AB998: (Dmitry Sinyavin)
    B7DBFAED: (Vasya Borisov)
    1166B795: (Andrey Rahmatullin)
- Removed keys:
    E31A2A27: (Maxim Dzumanenko)

* Fri Sep 26 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt19
- Added keys:
    3ADE1756 (Alexey Lokhin)
    B6B30094 (Yury Aliaev)
    5A3D03BA (Alexey Shabalin)
    F9A5DD55 (Vital Khilko)
    0A210834 (Serge A. Volkov)

* Thu Sep 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt18
- Added keys:
    CF39B9D3 (canis@altlinux.ru)
    457D9E8E (Ilya Mashkin)
    FB2AFE30 (Pavel Mironchik)

* Tue Aug 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt17
- Added keys:
    ECC29296 (Alexei Takaseev)
    6D1844F2 (Denis Ovsienko)
    CD94DF33 (Alexandre Prokoudine)

* Tue Jul 29 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt16
- Added keys:
    30B9BFAA (Kirill A. Shutemov)
    19C87447 (Marat Khairullin)
- Updated keys:
    F913F30A (Alexey I. Froloff)

* Fri Jun 27 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt15
- Added keys:
    0C01FDB2 (Alexandr Bulankin)
    FA2527F1 (Pavel S. Khmelinsky)
    A4C683B3 (Denis Klykvin)
    C98CF3D2 (Egor S. Orlov)
    A3F088F5 (Alexander V. Denisov)
    069F0CD9 (Zhenja Kaluta)
    19C87447 (Marat Khairullin)
- Removed keys (unused)
    E6CA9105 (Dmitry Chernyakov)

* Thu May 22 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt14
- Removed keys (replace):
    702A2E56,06C49742 (Grigory Batalov)
- Removed keys (unused):
    5DABB324 (Alex Zhukov)
- Added keys:
    B948AB6E (Grigory Batalov)
    548AAAF4 (Gerasimov Dmitry)
    450C39A7 (Ed V. Bartosh)
    52A9D67A (Peter V. Saveliev)
    0EB72CE8 (Ilya Krawez)

* Fri Apr 11 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt13
- Update keys:
    C1E23429 (Dmitry V. Levin)
    C8941ACC (Peter Novodvorsky)
- Added keys:
    637B61FD (Eugeny Korekin)
    4458F01F (Alexander Belov)
    59ADF9BD (Ivan Evtuhovich)
    1D6DC85D (Dmitry Vukolov)
    E906C708 (Serhii Hlodin)

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt12
- Removed keys:
    C8941ACC (Peter Novodvorsky)
    7BF73937 (Alexey Gladkov)
- Added new/again:
    C6C9CD8E (Anatoly Yakushin)
    68E31E54 (Alexey Gladkov)
    B0EFCC66 (Andrey Semenov)
    1B898CCD (Alex Murygin)
    C8941ACC (Peter Novodvorsky)
    ED6CE75C (Sergei Dolmatov)

* Wed Dec 18 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt11
- Added keys:
    7E70F2A3 (Nikita Gergel)
    23C409AB (Alexander V. Nikolaev)
    881ED0FA (Valentina Vaneeva)
- Updated keys:
    F913F30A (Alexey I. Froloff)

* Sun Dec 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt10
- Added keys:
    56D99BDE (Pavel Morozov)
    398074EE (Andy Gorev)
    FEA58EA9 (Michael Bykov)
    FA4D2E9B (Oleg Prokopyev)
    2C482235 (Yury Konovalov)
    38E7BB46 (Alexey Tourbin)

* Wed Nov 13 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt9
- Added keys:
    26D958FA (Andrey V Khavryuchenko)
    7BF73937 (Alexey Gladkov)
    DD89E169 (Artem Pastukhov)
    1DB4F366 (Alexey V.Lubimov)
    C18ED673 (Konstantin A Lepikhov)
    605AF46D (Naumen: Vladimir Pastukhov)

* Sat Oct 19 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt8
- Added keys:
    F0F5CE65 (Andrey Orlov)
- Removed keys:
    C00F064B (Andrey Orlov)

* Tue Sep 24 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt7
- Added keys:
    9C0CCD48 (Aleksandr Blokhin)
- Updated keys:
    9A490530 (Alexey Tourbin)

* Thu Sep 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt6
- Added keys:
    C72DAB66 (Igor Homyakov)

* Tue Sep 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt5
- Packager tag set to ALT Security Team.
- Removed keys:
    7B995D72 (Dmitry Lebkov)
    C32DEF05 (Alex Ott)
    DD575901 (Alex Ott)
- Added keys:
    01D6FB51 (Dmitry Lebkov)
    26A9E254 (Alex Ott)
    DDA2F63B (Mikhail Yakshin)
    65E7F7F2 (meaty aka Andrey Zakirov)

* Mon Aug 19 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt4
- Added keys:
    885B6677 (Andrey Brindeew)
    A00B441F (Alexey Dyachenko)

* Mon Aug 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt3
- Added keys:
    A090B5C8 (Aleksey Smirnov)
- Removed keys:
    83A5C7A8 (Aleksey Smirnov)
- Updated keys (added uids):
    EAC91CA0 (ALT Security Team)
    C1E23429 (Dmitry V. Levin)

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt2
- Updated keys.

* Mon Jul 22 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
