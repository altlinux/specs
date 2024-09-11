%define _libexecdir %_prefix/libexec

Name: platon
Version: 20240822
Release: alt1

Summary: PLATON is a versatile SHELX compatible multipurpose crystallographic tool
License: ALT-Proprietary-PLATON
Group: Sciences/Chemistry

Url: http://www.platonsoft.nl/platon/
Source: http://www.platonsoft.nl/spek/xraysoft/unix/%name.tar.gz
Source1: %name.sh
Source2: http://www.platonsoft.nl/spek/xraysoft/update_history_platon.html
Source3: http://www.platonsoft.nl/spek/xraysoft/old_update_history_platon.html
Source4: PERMISSION.txt

# Automatically added by buildreq on Fri Nov 28 2008
BuildRequires: gcc-fortran libX11-devel

Requires: %name-doc = %version-%release

%description
PLATON is a versatile SHELX compatible multipurpose
crystallographic tool.

Most PLATON features complement those available in the excellent
and widely distributed SHELX package for crystal structure
determination and refinement.

Historically (1980) PLATON started out as a program for the
automated calculation of derived geometrical data (i.e. bond
distances, bond angles and torsion angles, including su's
(esd's)) for structures refined with SHELX76.  Since then,
that basic function evolved into an automatic function to
calculate everything of possible interest (both intra- and
intermolecular)for a given structural parameter set
(Instruction: CALC).

Over time, various other tools were introduced (Molecular
Graphics i.e. PLUTON & ORTEP, Absorption correction, Data
Validation etc.), some of which requiring a reflection datafile
as well.

Several functions in PLATON (e.g. SPGR and EXOR) are there to
implement calculations needed for datareduction, structure
determination and refinement with a program system called
'SYSTEM-S'.

------------------------------------------------------------
PLATON is free of charge for Academics.

Please note that commecrial users should apply for a license:
http://www.cryst.chem.uu.nl/platon/pl030000.html

See also %_defaultdocdir/%name-common-%version/PERMISSION.txt

%package common
Summary: Common package for %name
Group: Sciences/Chemistry
BuildArch: noarch

%description common
PLATON is a versatile SHELX97 compatible multipurpose
crystallographic tool. This is common package for PLATON.


%package doc
Summary: English manual for PLATON
Group: Sciences/Chemistry
BuildArch: noarch
Requires: %name-bin = %version-%release

%description doc
PLATON is a versatile SHELX97 compatible multipurpose
crystallographic tool. This package contains the English
version of the PLATON user's manual.

%package bin
Summary: PLATON is a versatile SHELX97 compatible multipurpose crystallographic tool
Group: Sciences/Chemistry
Requires: %name-common = %version-%release

%description bin
PLATON is a versatile SHELX97 compatible multipurpose
crystallographic tool. This package contains the
executable binary file.

%prep
%setup -n %name
gunzip platon.f.gz
gunzip xdrvr.c.gz
tar -vvxf platon_html.tar.gz
mv platon doc
rm -f doc/index.html
chmod -c -Rf u+rwX,go-w doc
mv TEST test
cp -a %SOURCE1 .
cp -a %SOURCE2 .
cp -a %SOURCE3 .
cp -a %SOURCE4 .

%build
g77 %optflags -o platon platon.f xdrvr.c -lX11

%install
install -d %buildroot%_bindir
install -pm755 %name.sh %buildroot%_bindir/%name

# add pseudonyms
ln -s %name %buildroot%_bindir/pluton
ln -s %name %buildroot%_bindir/s
ln -s %name %buildroot%_bindir/cifchk
ln -s %name %buildroot%_bindir/helena
ln -s %name %buildroot%_bindir/stidy

install -d %buildroot%_libexecdir/%name
install -pm755 %name %buildroot%_libexecdir/%name

install -d %buildroot%_datadir/%name
install -pm644 check.def %buildroot%_datadir/%name

install -d %buildroot%_datadir/%name/{ABSORB_EXAMPLE,ABSTOMPA_EXAMPLE,ABSTOMPA_TEST,ADDSYM_EXAMPLE,ASYM_EXAMPLE,MULABS_EXAMPLE,PSICOR_EXAMPLE,SQUEEZE_EXAMPLE}
install -pm644 test/ABSORB_EXAMPLE/* %buildroot%_datadir/%name/ABSORB_EXAMPLE/
install -pm644 test/ABSTOMPA_EXAMPLE/* %buildroot%_datadir/%name/ABSTOMPA_EXAMPLE/
install -pm644 test/ABSTOMPA_TEST/* %buildroot%_datadir/%name/ABSTOMPA_TEST/
install -pm644 test/ADDSYM_EXAMPLE/* %buildroot%_datadir/%name/ADDSYM_EXAMPLE/
install -pm644 test/ASYM_EXAMPLE/* %buildroot%_datadir/%name/ASYM_EXAMPLE/
install -pm644 test/MULABS_EXAMPLE/* %buildroot%_datadir/%name/MULABS_EXAMPLE/
install -pm644 test/PSICOR_EXAMPLE/* %buildroot%_datadir/%name/PSICOR_EXAMPLE/
install -pm644 test/SQUEEZE_EXAMPLE/* %buildroot%_datadir/%name/SQUEEZE_EXAMPLE/

install -d %buildroot%_defaultdocdir/%name/{images,PLATON-MANUAL.data,pl000314_files}
#install -pm644 doc/{*.html,*.pdf,*.lis,*.spf,*.ps,*.res,*.mis,*.hkl,*.ins,*.dat,*.Z,*.fcf,*.acc,*.sup,*.lps,*.pdb,*.eps,*.jnl,*.cif} \
#        %buildroot%_defaultdocdir/%name
install -pm644 doc/{*.html,*.pdf,*.lis,*.spf,*.ps,*.res,*.mis,*.hkl,*.ins,*.Z,*.fcf,*.acc,*.sup,*.lps,*.pdb,*.eps,*.jnl,*.cif} \
        %buildroot%_defaultdocdir/%name
ln -s pl000000.html %buildroot%_defaultdocdir/%name/index.html
install -pm644 doc/images/* %buildroot%_defaultdocdir/%name/images
install -pm644 doc/PLATON-MANUAL.data/* %buildroot%_defaultdocdir/%name/PLATON-MANUAL.data
install -pm644 doc/pl000314_files/* %buildroot%_defaultdocdir/%name/pl000314_files

%files
# nothing to pack

%files common
%doc README README.ADDSYM README.LEPAGE update_history_platon.html old_update_history_platon.html PERMISSION.txt
%_bindir/*
%_datadir/%name

%files bin
%_libexecdir/%name

%files doc
%_defaultdocdir/%name

%changelog
* Wed Sep 11 2024 Denis G. Samsonenko <ogion@altlinux.org> 20240822-alt1
- new version

* Mon Aug 19 2024 Denis G. Samsonenko <ogion@altlinux.org> 20240807-alt1
- new version

* Tue May 21 2024 Denis G. Samsonenko <ogion@altlinux.org> 20240513-alt1
- new version

* Mon May 06 2024 Denis G. Samsonenko <ogion@altlinux.org> 20240505-alt1
- new version

* Fri Feb 02 2024 Denis G. Samsonenko <ogion@altlinux.org> 20240106-alt1
- new version

* Wed Nov 15 2023 Denis G. Samsonenko <ogion@altlinux.org> 20231114-alt1
- new version

* Tue Oct 10 2023 Denis G. Samsonenko <ogion@altlinux.org> 20230927-alt1
- new version

* Mon Sep 25 2023 Denis G. Samsonenko <ogion@altlinux.org> 20230917-alt1
- new version

* Thu Jul 27 2023 Denis G. Samsonenko <ogion@altlinux.org> 20230721-alt1
- new version

* Wed Apr 12 2023 Denis G. Samsonenko <ogion@altlinux.org> 20230411-alt1
- new version

* Wed Dec 28 2022 Denis G. Samsonenko <ogion@altlinux.org> 20221205-alt1
- new version

* Sat Sep 03 2022 Denis G. Samsonenko <ogion@altlinux.org> 20220902-alt1
- new version

* Tue Aug 09 2022 Denis G. Samsonenko <ogion@altlinux.org> 20220807-alt1
- new version

* Fri Mar 11 2022 Denis G. Samsonenko <ogion@altlinux.org> 20220308-alt1
- new version

* Wed Jul 14 2021 Denis G. Samsonenko <ogion@altlinux.org> 20210713-alt1
- new version

* Fri Apr 30 2021 Denis G. Samsonenko <ogion@altlinux.org> 20210427-alt1
- new version

* Sun Jul 12 2020 Denis G. Samsonenko <ogion@altlinux.org> 20200708-alt1
- new version

* Mon Jun 22 2020 Denis G. Samsonenko <ogion@altlinux.org> 20200618-alt1
- new version

* Thu Feb 20 2020 Denis G. Samsonenko <ogion@altlinux.org> 20200213-alt1
- new version

* Mon Dec 16 2019 Denis G. Samsonenko <ogion@altlinux.org> 20191212-alt1
- new version

* Fri Oct 25 2019 Denis G. Samsonenko <ogion@altlinux.org> 20191021-alt1
- new version

* Fri Apr 12 2019 Denis G. Samsonenko <ogion@altlinux.org> 20190410-alt1
- new version

* Sun Jan 20 2019 Denis G. Samsonenko <ogion@altlinux.org> 20190115-alt1
- new version

* Sun Nov 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 20181101-alt1
- nuw version

* Sat Sep 15 2018 Denis G. Samsonenko <ogion@altlinux.org> 20180911-alt1
- new version

* Thu Aug 16 2018 Denis G. Samsonenko <ogion@altlinux.org> 20180808-alt1
- new version

* Sun Feb 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 20180130-alt1
- new version

* Thu Jan 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 20180103-alt1
- new version

* Sat Aug 26 2017 Denis G. Samsonenko <ogion@altlinux.org> 20170813-alt1
- new version

* Sat Jul 08 2017 Denis G. Samsonenko <ogion@altlinux.org> 20170629-alt1
- new version

* Sun May 07 2017 Denis G. Samsonenko <ogion@altlinux.org> 20170428-alt1
- new version

* Sat Jan 28 2017 Denis G. Samsonenko <ogion@altlinux.org> 20170122-alt1
- new version

* Sat Jul 02 2016 Denis G. Samsonenko <ogion@altlinux.org> 20160615-alt1
- new version

* Thu Apr 28 2016 Denis G. Samsonenko <ogion@altlinux.org> 20160427-alt1
- new version

* Fri Apr 08 2016 Denis G. Samsonenko <ogion@altlinux.org> 20160403-alt1
- new version

* Sun Oct 25 2015 Denis G. Samsonenko <ogion@altlinux.org> 20151001-alt1
- new version

* Sun Jun 28 2015 Denis G. Samsonenko <ogion@altlinux.org> 20150626-alt1
- new version

* Thu Feb 12 2015 Denis G. Samsonenko <ogion@altlinux.org> 20150210-alt1
- new version

* Mon Nov 03 2014 Denis G. Samsonenko <ogion@altlinux.org> 20141103-alt1
- new version

* Tue Jul 22 2014 Denis G. Samsonenko <ogion@altlinux.org> 20140722-alt1
- new version

* Thu Nov 21 2013 Denis G. Samsonenko <ogion@altlinux.org> 20131025-alt1
- new version

* Wed Jul 17 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130713-alt1
- new version

* Sat Jun 01 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130528-alt1
- new version

* Sat Apr 13 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130410-alt1
- new version

* Tue Feb 19 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130219-alt1
- new version

* Mon Feb 04 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130201-alt1
- new version

* Sun Jan 13 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130102-alt1
- new version

* Thu Nov 29 2012 Denis G. Samsonenko <ogion@altlinux.org> 20121129-alt1
- new version

* Tue Oct 16 2012 Denis G. Samsonenko <ogion@altlinux.org> 20121015-alt1
- new version

* Fri Oct 12 2012 Denis G. Samsonenko <ogion@altlinux.org> 20121012-alt1
- new version

* Thu Aug 23 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120822-alt1
- new version

* Thu Aug 09 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120809-alt1
- new version

* Mon Jul 30 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120727-alt1
- new version

* Thu Jul 19 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120718-alt1
- new version
- fixed zdate function in xdrvr.c leading to buffer overflow (see #21582)
- come back to compilation of platon.f and xdrvr.c together with optimizations

* Sun Jul 15 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120713-alt1
- new version
- separated compilation of platon.f (with optimizations) and xdrvr.c (without optimizations)

* Mon Jul 09 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120704-alt1
- new version
- optimization flags added

* Sat May 26 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120523-alt0.M60P.1
- build for M60P

* Sat May 26 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120523-alt1
- new version
- changelog fixed

* Fri May 25 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120521-alt1
- new version

* Wed May 16 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120515-alt1
- new version

* Tue Apr 10 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120405-alt1
- new version
- changelog fixed

* Tue Apr 03 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120329-alt1
- new version

* Wed Mar 21 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120316-alt1
- new version

* Wed Feb 08 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120203-alt1
- new version

* Sat Dec 24 2011 Denis G. Samsonenko <ogion@altlinux.org> 20111221-alt0.M60T.1
- Backport to M60T

* Sat Dec 24 2011 Denis G. Samsonenko <ogion@altlinux.org> 20111221-alt1
- new version

* Sat Oct 22 2011 Denis G. Samsonenko <ogion@altlinux.org> 20111019-alt0.M60T.1
- Backport to M60T

* Sat Oct 22 2011 Denis G. Samsonenko <ogion@altlinux.org> 20111019-alt1
- new version
- URLs changed
- _libexecdir changed to %_prefix/libexec
- path to user's manual changed
- spec cleanup

* Thu Oct 20 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110915-alt1.M60T.1
- Backport to M60T

* Thu Oct 20 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110915-alt2
- platon divided into platon-bin and platon-common
- platon is now empty package

* Fri Sep 16 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110915-alt0.M60T.1
- Backport to M60T

* Fri Sep 16 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110915-alt1
- new version
- subpackage for PLATON html manual

* Mon Sep 12 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110901-alt1.M60T.1
- Backport to M60T

* Mon Sep 12 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110901-alt2
- start script fixed to remove checkbashisms warning

* Sat Sep 10 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110901-alt0.M60T.1
- Backport to M60T

* Thu Sep 08 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110901-alt1
- new version
- start script rewritten
- symlinks added
- spec cleanup

* Wed Aug 31 2011 Michael Shigorin <mike@altlinux.org> 20110814-alt1
- rebuilt for Sisyphus; Denis, you're welcome! :) (closes: #26171)

* Sat Aug 27 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110814-alt0.sdg1
- new version

* Sun Jul 10 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110706-alt0.sdg1
- new version
- change sources location

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 20101011-alt2
- really merged Denis' spec, shame on me (closes: #23830)

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 20101011-alt1
- 20101011 (thanks Denis G. Samsonenko)

* Sun Aug 01 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20101011-alt0.sdg1
- New version

* Sun Aug 01 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100716-alt0.sdg2
- optflags added

* Wed Jul 28 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100716-alt0.sdg1
- New version

* Sat Feb 20 2010 Michael Shigorin <mike@altlinux.org> 20100121-alt2
- clarified License:
- added PERMISSION.txt to package documentation

* Sat Feb 20 2010 Michael Shigorin <mike@altlinux.org> 20100121-alt1
- accepted changes by Denis (closes: #21582)
- spec cleanup

* Fri Jan 22 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100121-alt0.sdg1
- New version

* Sun Jan 03 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20091218-alt0.sdg1
- New version.
- Minor changes in spec file.
- Biult with -O0 because of crashes (#21582).

* Wed Jun 03 2009 Pavel V. Solntsev <p_solntsev at altlinux.org> 20090603-alt1
- New version. Platon can be started by script pltn.

* Fri May 15 2009 Pavel V. Solntsev <p_solntsev at altlinux.org> 20090513-alt1.M41
- Backport to M41

* Fri May 15 2009 Pavel V. Solntsev <p_solntsev at altlinux.org> 20090513-alt1
- New version
- platon can be run by pltn command

* Thu Mar 12 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 20090310-alt1
- New version.
- Start script has been updated.

* Fri Feb 27 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 20090227-alt1
- New version

* Wed Feb 04 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 20090204-alt1
- New version

* Fri Jan 09 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 20090107-alt1.M41.1
- Backport M41.

* Fri Jan 09 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 20090107-alt1
- New version.

* Mon Dec 29 2008 Pavel V. Solntsev <p_solntsev@altlinux.org> 20081215-alt1
- New version. Source code and check.def file are updated.
- Desktop and icon file have been removed.

* Thu Nov 27 2008 Pavel V. Solntsev <p_solntsev at altlinux.org> 20081127-alt1
- First build package for ALTLinux Team
- Package based on the Pascal's Fedora package <pascal22p at parois dot net>.

