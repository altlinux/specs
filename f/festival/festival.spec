%define fst_version 2.0.95
%define est_version 2.0.95
%define est_soversion 2.0.95
%define estsuffix 2.0
%define festival_user _festival
%define festival_group audio
%define festival_home '/'
%def_disable static
%def_with festival_dynamic_build
%def_with est_dynamic_build
# rms voice is missing yet
%def_disable festival_test
%def_without legacy_server_scripts
%define festival_libexec_dir /usr/lib/festival

Summary:	general multi-lingual speech synthesis system
Name:		festival
Version:	%{fst_version}
Release:	alt1
Group:		Sound
Packager:	Igor Vlasenko <viy@altlinux.ru>
# the emacs file is GPL+, there is one TCL licensed source file
License:	MIT and GPL+ and TCL

URL:		http://www.cstr.ed.ac.uk/projects/festival.html
%define srcURL0  http://www.cstr.ed.ac.uk/downloads/festival/1.95
%define srcURL1  http://festvox.org/packed/festival/%{fst_version}
%define srcURL2  http://www.speech.cs.cmu.edu/awb/fftest

Source0:	%srcURL1/festival-%{fst_version}-beta.tar
Source1:	%srcURL1/speech_tools-%{est_version}-beta.tar
Source2:	README.ALTLinux
Source3:	festival.init
Source4:	server.scm
Source5:	festival-1.96-0.7-alt-siteinit.scm
Source6:	festival-1.96-0.7-alt-sitevars.scm

# for make test; TODO: # rms voice is missing yet
BuildRequires: festvox_kallpc16k festvox_don festvox_rablpc16k
### TODO:
#README.alt
#french lang?
#xml dir apply
###

# adds /usr/lib/festival to PATH inside festival. 
# It makes /usr/lib/festival useful place for external progs like mbrola.
Patch0:		festival-2.0.95-alt-fix-path-audsp.patch
# is not too nesessary if alt-fix-path-audsp.patch is applied
Patch1:		festival-1.4.1-audsp.patch
Patch2:		festival-1.96-alt-russian-voice_msu_ru_nsh_cg.patch
Patch3:		festival-1.4.3-alt-info-header.patch
Patch4:		festival-2.0.95-alt-shared-lib-support-in-install.patch
Patch5:		festival-1.96-alt-unsafe-tmp-usage.patch

# misc alt patches 
# use /etc/festival/*.scm
# base required by sysconfdir.diff; is contained in datadir.diff
Patch140: festival-1.96-alt-sysconfdir-base.diff
Patch141: festival-1.96-alt-sysconfdir.diff

################################################
# festival_1.4.3 debian patches
# from festival_1.4.3-17.1.diff.gz
################################################
# support for possibility of xml data movement
#Patch9: festival_1.4.3-xml-base.diff // partially applied.
# report to upstream an inconsistency with lib/singing-mode.scm
Patch9: festival-2.0.95-alt-sable-xml-base.patch

Patch10: festival_1.4.3-debian-dir.diff
Patch11: festival_1.4.3-alaw.diff
Patch12: festival_1.96-scm.diff
Patch13: festival-1.96-deb-1.4.3-examples-in-docdir-festival.diff
Patch14: festival-1.96-deb-1.4.3-languages-it-fi.diff

# TODO: outdated
# not applied; used if we move dtds; requires xml-base.diff
Patch15: festival_1.4.3-xmldir.diff

# not applied; we directly echo variables in config;
# the piece of fixed libestools location is not needed too
# because we do not split festival and speech_tools
Patch16: festival_1.4.3-config.diff
# not applied; we do not apply --datadir for estools too
# replaces sysconfdir-base
Patch17: festival_1.4.3-datadir.diff
# not applied; kept for consistency only. require --datadir
# removed SuSE festival-1.95-examples.patch
Patch18: festival_1.4.3-makefile.diff
# Not used; It is for consistency only; we use SuSE manpage
Patch19: festival_1.4.3-text2wave-manpage.diff
# not applied; kept for reference; breaks alt-fix-path-audsp.patch
# removes append ftlibdir/etc/$(OSTYPE):ftlibdir/etc to PATH
Patch20: festival_1.4.3-no-lib-etc.diff

################################################
# festival fedora patches
################################################
# fedora patches against festival-1.96-11

# Set defaults to American English instead of British English - the OALD
# dictionary (free for non-commercial use only) is needed for BE support
# Additionally, prefer the smaller (and I think nicer sounding) nitech hts
# voices.
# TODO:
Patch201: festival-1.96-nitech-american.patch

# Whack some buildroot references
#Patch202: festival-buildroot.patch
# note: it is a piece of patch. 
# I moved libestools part and removed SuSE examples.patch
Patch202: festival-1.95-buildroot-fedora.patch

# Look for siteinit and sitevars in /etc/festival
# not applied: fully contained in alt-siteinit* patches
Patch208: festival-1.96-etcsiteinit.patch

# Alias old cmu names to new nitech ones
Patch209: festival-1.96-alias_cmu_to_nitech.patch

# Look for speech tools in subdir. we use ../ as default
#Patch210: festival-1.96-findspeechtools.patch

# Build main library as shared, not just speech-tools
#Patch211: festival-1.96-main-shared-build.patch
# revert back for 2.1 festival if version will be 2.1
Patch211: festival-2.0.95-main-shared-build.patch


# This makes festival use /usr/lib[arch]/festival/etc for its
# arch-specific "etc-path", rather than /usr/share/festival/etc/system_type.
# Then I use sed to replace the token with actual arch-specific libdir.
# A better way would be to actually make this a flexible makefile parameter,
# but that's something to take up with upstream.
# TODO:
Patch231: festival-1.96-kludge-etcpath-into-libarch.patch

# contained in Suse patch
#Patch293: festival-1.96-fefora-gcc43.patch

#TODO: (can't use pulceaudio by default now)
# Work with pulseaudio (bug 467531)
Patch294: festival-1.96-fedora-11-use-pacat.patch
#------------------------------------------------------


# SuSE patches
# was: festival-1.96-suse.patch rediffed as 
Patch100: festival-2.0.95-suse-alt-refiffed.patch
Patch99: festival-2.0.95-alt-volatile.patch

# includes Patch23 fedora gcc;
Patch101:         festival-1.95-gcc4.patch
Patch102:         festival-1.95-examples.patch
Patch103:         festival-text2wave-manpage.patch
# it is safe to remove, as we set FTLIBDIR manually
Patch104:         festival-1.95-libdir.patch
# the same as  festival-1.4.1-audsp.patch
# Patch107:         festival-1.95-audsp.patch

# TODO: apply changes to init script too
Patch108:         festival-1.96-chroot.patch


# identical to fedora festival-1.95-fix-localhost-connections.patch
#Patch106:         festival-1.95-allow-localhost.patch
# identical to festival-1.4.1-audsp.patch
#Patch107:         festival-1.95-audsp.patch
# end festival SuSE patches

# Gentoo patches
Patch120:         festival-2.0.95-asterisk.patch


# ark patches from 2.0.95-1ark
# TODO: whether worth applying (includes not applied festival-1.95-fsstnd-fedora.patch)
# Fix up various locations to be more FSSTND compliant
# Patch600: festival-1.95-fsstnd.patch

# TODO:
# Set defaults to American English instead of British English - the OALD
# dictionary (free for non-commercial use only) is needed for BE support
#Patch601: festival-american.patch

# TODO:
# Whack some buildroot references
#Patch602: festival-buildroot.patch

# TODO:
# Use shared libraries
#Patch603: festival-1.95-shared-build.patch

# TODO:
# Use konqueror, not Netscape dirt
#Patch604: festival-1.95-konqueror.patch

# TODO:
# Patches from OGI, based on OGIfestpatch-1.4.1.2.tar.gz
# from http://cslu.cse.ogi.edu/tts/download/index.html#plugin
#Patch605: festival-1.95-OGIfixes.patch

# TODO:
# Patches from IMS, based on festival-1.4.1-fixes.tgz
# from http://www.ims.uni-stuttgart.de/phonetik/synthesis/festival/
#Patch606: festival-1.95-imsfixes.patch

# Don't crash when compiled with a decent compiler
# Patch608: festival-1.96-gcc4-crashfixes.patch contains in speech_tools-1.2.96-gcc41.patch


# -------- speech_tools patches --------------------------
# speech-tools_1.2.95-0.4-*.diff are pieces of
# heavily edited debian's speech-tools_1.2.3-9.3.diff.gz

# a way to build shared libraries
# not applied in favor of Patch62: festival-1.96-bettersonamehack.patch
Patch40: speech-tools-2.0.95-0.4-config-library.diff
Patch41: speech-tools_1.2.95-0.4-debian-dir.diff
# TODO: 
#  * cleanup using festival-1.96-bettersonamehack.patch
#  * do not patch obscure configs, just ignore them;
#  * instead gcc295 use gcc_default
#  * merge Patch53: festival-1.96-speechtools-shared-build.patch
Patch42: speech-tools-2.0.95-0.4-config.diff
# Do we need it? try without! and rediff to fix fuzz
Patch43: speech-tools_1.2.95-0.4-remnants.diff
# mix c/c++ with sstream; 
Patch45: speech-tools_1.2.96-0.4-esd-block-interrupts.diff
# not applied; should be improved in /doc
Patch46: speech-tools_1.2.95-0.4-datadir.diff
# TODO: do we need it in 2.0.95 ? it has alsa
Patch49: speech-tools_1.2.96-0.4-sunaudio-default.diff

# not applied; TODO:
# 1.96 has simpler verison of this patch with conflict in EST_wave_utils.cc
# proper way is undo 1.96 changes and apply orig 1.95 patch
Patch50: speech-tools_1.2.96-0.4-alaw.diff

# fedora patches against festival-1.96-5
# Use shared libraries
# Patch703: festival-1.96-speechtools-shared-build.patch
# contained in Patch42: speech-tools_1.2.96-0.4-config.diff

# Build (but don't enable by default) the ESD module
# TODO: split and apply properly
Patch704: festival-1.96-speechtools-buildesdmodule.patch

# already in suse speech_tools-1.2.96-gcc41.patch
# Fix a coding error (see bug #162137). Need to upstream.
# Patch705: festival-1.96-speechtools-rateconvtrivialbug.patch

# Link libs with libm, libtermcap, and libesd (see bug #198190).
# Need to upstream this.
Patch706: festival-1.96-speechtools-linklibswithotherlibs.patch

# Done other way
# For some reason, CXX is set to gcc on everything but Mac OS Darwin,
# where it's set to g++. Yeah, well. We need it to be right too.
# Patch707: festival-1.96-speechtools-ohjeezcxxisnotgcc.patch

# a speech_tools piece of fedora buildroot.patch
Patch702: speech_tools-1.2.95-buildroot-fedora.patch

# speechtools part of fedora festival-1.96-main-shared-build.patch
Patch711: festival-1.96-speechtools-main-shared-build.patch

# This is a hack to make the shared libraries build with actual
# sonames. Should pretty much do the right thing, although note
# of course that the sonames aren't official upstream.
Patch712: festival-1.96-bettersonamehack.patch

# is contained in suse Patch115
#Patch793: speech_tools-1.2.96-fefora-gcc43.patch

# is contained in 2.0.95 upstream
#Patch795: speech_tools-1.2.96-fedora-11-gcc44.patch


# SuSE patches (as of festival-1.96-101); note that 2.0.95 ones are manually rediffed.
Patch111:        speech_tools-1.2.96-gcc4.patch
#Origname112:        speech_tools-1.2.95-config.patch
Patch112:        speech_tools-1.2.95-config-warn-on-suse.patch
Patch113:        speech_tools-1.2.96-gcc41.patch
Patch114:        speech_tools-2.0.95-returnvalue.patch
# removed tail for previous speech_tools build
Patch115:	 speech_tools-1.2.96-beta-suse.patch

# misc alt patches 
Patch138: speech_tools-1.2.95-alt-hts_support-fest1.96.patch
# set up shared lib version
Patch139: speech_tools-2.0.95-alt-config-project.patch


Requires:	festvox

# --displayname
Requires:	service => 0.5.9-alt1

# Automatically added by buildreq on Mon Sep 25 2006
BuildRequires: esound-devel gcc-c++ libaudiofile-devel libncurses-devel libstdc++-devel libtinfo-devel

# upgrade to 2.0.95
Conflicts: festvox_cmu_us_awb_arctic_hts < 2.0
Conflicts: festvox_cmu_us_bdl_arctic_hts < 2.0
Conflicts: festvox_cmu_us_jmk_arctic_hts < 2.0
Conflicts: festvox_cmu_us_slt_arctic_hts < 2.0
Conflicts: festvox_nitech_us_awb_arctic_hts < 0.20070000
Conflicts: festvox_nitech_us_bdl_arctic_hts < 0.20070000
Conflicts: festvox_nitech_us_clb_arctic_hts < 0.20070000
Conflicts: festvox_nitech_us_jmk_arctic_hts < 0.20070000
Conflicts: festvox_nitech_us_rms_arctic_hts < 0.20070000
Conflicts: festvox_nitech_us_slt_arctic_hts < 0.20070000


%description
Festival is a general purpose text-to-speech system.  As well as
simply rendering text as speech it can be used in an interactive
command mode for testing and developing various aspects of speech
synthesis technology.

Festival offers a full text to speech system with various APIs, as 
 well an environment for development and research of speech synthesis
 techniques. It includes a Scheme-based command interpreter.

 Besides research into speech synthesis, festival is useful as a
 stand-alone speech synthesis program. It is capable of producing
 clearly understandable speech from text.

%package -n libfestival-devel
Summary: development kit for the Festival speech synthesis system
Group: Development/C
Requires: %name = %fst_version-%release
Provides: festival-devel = %fst_version-%release
Obsoletes: festival-devel < 1.96-alt3
#Requires: libestools1.2-devel (>= 1:1.2.3-9)

%description -n libfestival-devel
This package contains the library and headers that can be used to
 develop programs that use Festival.  Documentation is now contained in the
 separate festival-doc package

%if_enabled static
%package -n libfestival-devel-static
Summary: development kit for the Festival speech synthesis system
Group: Development/C
Requires: libfestival-devel = %fst_version-%release

%description -n libfestival-devel-static
This package contains the static library that can be used to
 develop programs that use Festival.
%endif

%package -n speech_tools
Summary: Edinburgh Speech Tools - user binaries
Group:          Development/Other
Version: %est_version
Requires: libestools%estsuffix  = %est_version-%release
Provides: speech_tools-clients
Obsoletes: speech_tools-clients < 1.2.2-ipl3mdk

%description -n speech_tools
This package contains the various highly useful (to speech scientists, at
 least) utility programs that use and accompany the Edinburgh Speech Tools
 Library.

%package -n libestools%estsuffix
Summary: Edinburgh Speech Tools Library
Version: %est_version
License: X11-style
Group: Sound
URL: http://www.cstr.ed.ac.uk/projects/festival.html
Obsoletes: speech_tools < 1.2.2-ipl3mdk

%description -n libestools%estsuffix
A library for use in speech software, such as the festival speech synthesis
 system.

%package -n libestools-devel
Summary: Edinburgh Speech Tools Library - developer's libraries and docs
# emacs syntax color cheat '
Version: %est_version
Group:          Development/C
Requires: libestools%estsuffix  = %est_version-%release
Obsoletes: speech_tools-devel < 1.2.2-ipl3mdk

%description -n libestools-devel
This package contains the header files, static libraries, and documentation
 that developers using the Edinburgh Speech Tools Library will need.

%if_enabled static
%package -n libestools-devel-static
Summary: Edinburgh Speech Tools Library - static libraries
Group:          Development/C
Version: %est_version
Requires: libestools-devel  = %est_version-%release

%description -n libestools-devel-static
This package contains the static libraries
 that developers using the Edinburgh Speech Tools Library may need.
%endif

%prep
%setup -q -n festival
%setup -q -T -b 1 -n speech_tools

cd $RPM_BUILD_DIR/festival
%patch0 -p2
%patch1 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p2

# /etc/festival dir
%patch140 -p1
%patch141 -p1

%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%patch14 -p1
# need not to depend on Patch14 (merge?)
%patch2 -p1

#patch201 -p1 -b .nitech
%patch202 -p1 -b .buildrootrefs
%patch209 -p1 -b .cmu2nitech
# patch209 creates a new file; patch helpfully makes a "backup" of the
# non-existent "original", which then has bad permissions. zap.
rm -f lib/alias_cmu_to_nitech.scm.cmu2nitech
%patch211 -p1 -b .shared

#patch231 -p1 -b .libarch
## finish the kludge for arch-specific "etc" (misc. binaries)
#for f in speech_tools/main/siod_main.cc src/arch/festival/festival.cc; do
#  sed -i -e 's,{{HORRIBLELIBARCHKLUDGE}},"%{_libdir}",' $f
#done

%patch99 -p0
%patch100 -p0
%patch101 -p0
%patch102 -p1
%patch103 -p1
%patch104 -p0
%patch108 -p0

%patch120 -p2


cd $RPM_BUILD_DIR/speech_tools
%patch41 -p1
%patch42 -p2
%patch43 -p1
%patch45 -p1
# # --libdir is used in build process :(
# #%patch46 -p1
%patch49 -p1
# 1.96 has simpler verison of this patch with conflict in EST_wave_utils.cc
# proper way is undo 1.96 changes and apply orig 1.95 patch
# ###>>>%patch50 -p1
%patch702 -p1
#patch704 -p2 -b .esd
%patch706 -p2 -b .liblinking
%patch711 -p2
%patch712 -p2 -b .soname


%patch111 -p1
%patch112 -p0
%patch113 -p1
%patch114 -p2
%patch115 -p0

%patch138 -p1
%patch139 -p2




# prep Edinburgh Speech Tools
%__subst s/'# INCLUDE_MODULES += ESD_AUDIO'/'INCLUDE_MODULES += ESD_AUDIO'/ \
       config/config.in
%__subst -p 's,/usr/local\>,/usr,g' config/systems/default.mak
%if_with est_dynamic_build
%__subst s/'#SHARED='/'SHARED='/ config/config.in
%endif

# linking against libraries to avoid unresolved symbols
echo "PROJECT_LIBRARY_NEEDS_SYSLIBS_estbase = 1" >> config/project.mak
echo "PROJECT_LIBRARY_NEEDS_SYSLIBS_esttools = 1" >> config/project.mak
#echo "PROJECT_LIBRARY_USES_estools = estbase" >> config/project.mak
# is tinfo altlinux specific?
echo "PROJECT_LIBRARY_USES_estools = estbase tinfo" >> config/project.mak

%build
# Build Edinburgh Speech Tools
cd $RPM_BUILD_DIR/speech_tools
%add_optflags -Wno-non-template-friend

# parallel build fails :( so not %make
#-------------
# new g++ 4.3 have no -fno-shared-data option
#make MAKE_SHARED_LIB="g++ -shared -fno-shared-data -o XXX -Wl,--as-needed -Wl,-soname -Wl,YYY"
## TODO! as a patch...
%__subst s,-fno-shared-data,,g config/compilers/gcc_defaults.mak
./configure
make MAKE_SHARED_LIB="g++ -shared -o XXX -Wl,--as-needed -Wl,-soname -Wl,YYY"

%if_enabled festival_test
make test
%endif

# Build Festival
cd $RPM_BUILD_DIR/festival
%configure
cat <<EOF >>config/config
# FESTIVAL_HOME := %_prefix
# INCLUDE_TCL=1
FTLIBDIR := %_datadir/festival
# indicates that speech_tools are built shared
# SHARED = 1
# GCC_MAKE_SHARED_LIB = gcc -shared -o XXX
EOF

# hack...
echo "PROJECT_LIBRARY_NEEDS_SYSLIBS_Festival = 1" >> config/project.mak
echo "PROJECT_LIBRARY_USES_Festival = estbase eststring" >> config/project.mak

#make_build 
# gcc4
#FTLIBDIR=%{_datadir}/festival make  CXXFLAGS="-ffriend-injection -fpermissive -Wno-deprecated -Wno-non-template-friend -fPIC" CFLAGS="-ffriend-injection -fpermissive -Wno-deprecated -Wno-non-template-friend -O0 -fPIC"
# gcc3
make  CXXFLAGS="-fpermissive -Wno-non-template-friend -fPIC" CFLAGS="-fpermissive -Wno-non-template-friend -O0 -fPIC"

export LD_LIBRARY_PATH=`pwd`/../speech_tools/lib
pushd doc && %make_build festival.info && popd
# TODO:
#make test

%install

# Install Edinburgh Speech Tools
cd $RPM_BUILD_DIR/speech_tools

S_PROGRAMS="bcat ch_lab ch_track ch_utt ch_wave dp na_play na_record ngram_build \
	ngram_test ols ols_test	pda pitchmark scfg_make scfg_parse scfg_test \
	scfg_train sig2fv sigfilter spectgen tilt_analysis tilt_synthesis \
	viterbi wagon wagon_test wfst_build wfst_run"
S_UNDOC="bcat dp ngram_build \
	ngram_test ols ols_test	pda pitchmark scfg_make scfg_parse scfg_test \
	scfg_train sig2fv sigfilter spectgen tilt_analysis tilt_synthesis \
	viterbi wagon wagon_test wfst_build wfst_run pm make_wagon_desc \
	raw_to_xgraph resynth"
S_SCRIPTS="pm.prl raw_to_xgraph.prl make_wagon_desc.sh resynth.sh"
export S_PROGRAMS S_UNDOC S_SCRIPTS

install -d $RPM_BUILD_ROOT{%_libdir,%_bindir,%_datadir,%_includedir}

%if_with est_dynamic_build
# -- Installing package libestools1.2 --
cp lib/*.so.%{est_soversion} $RPM_BUILD_ROOT%_libdir/
ln -sf libestbase.so.%{est_soversion} $RPM_BUILD_ROOT%_libdir/libestbase.so.%estsuffix
ln -sf libestools.so.%{est_soversion} $RPM_BUILD_ROOT%_libdir/libestools.so.%estsuffix
ln -sf libeststring.so.%{est_soversion} $RPM_BUILD_ROOT%_libdir/libeststring.so.%estsuffix
%endif

# -- Installing package speech_tools --
pushd main 
cp $S_PROGRAMS $RPM_BUILD_ROOT%_bindir/
popd
pushd scripts
	for i in $S_SCRIPTS; do \
		dest=`echo $i | sed -e 's/\.\(prl\|sh\)$//'`; \
		sed -e 's,__PERL__,/usr/bin/perl,g' \
			<$i >$RPM_BUILD_ROOT%_bindir/$dest; \
		chmod +x $RPM_BUILD_ROOT%_bindir/$dest; \
	done
popd

# -- Installing package libestools1.2-dev --
install -d $RPM_BUILD_ROOT%_libdir/speech_tools/lib/siod \
	$RPM_BUILD_ROOT%_includedir/speech_tools/{unix,instantiate,sigpr,rxp,ling_class}
cp lib/*.a $RPM_BUILD_ROOT%_libdir/
%if_with est_dynamic_build
ln -sf libestbase.so.%estsuffix   $RPM_BUILD_ROOT%_libdir/libestbase.so
ln -sf libestools.so.%estsuffix   $RPM_BUILD_ROOT%_libdir/libestools.so
ln -sf libeststring.so.%estsuffix $RPM_BUILD_ROOT%_libdir/libeststring.so
%endif

cp include/*.h $RPM_BUILD_ROOT%_includedir/speech_tools/
cp include/unix/*.h $RPM_BUILD_ROOT%_includedir/speech_tools/unix/
# Note: these are possibly internal headers (C++ lossage)
cp include/instantiate/*.h $RPM_BUILD_ROOT%_includedir/speech_tools/instantiate/

cp include/sigpr/*.h $RPM_BUILD_ROOT%_includedir/speech_tools/sigpr/
cp include/ling_class/*.h $RPM_BUILD_ROOT%_includedir/speech_tools/ling_class/
cp include/rxp/*.h $RPM_BUILD_ROOT%_includedir/speech_tools/rxp/
cp base_class/*.h $RPM_BUILD_ROOT%_includedir/speech_tools/

# Needed to compile things against speech_tools
cp -R config $RPM_BUILD_ROOT%_libdir/speech_tools/config
find $RPM_BUILD_ROOT%_libdir/speech_tools/config/ \
	\( -name SCCS -o -name CVS -o -name RCS \) -print0 | \
	xargs -0r rm -rf
cp make.include $RPM_BUILD_ROOT%_libdir/speech_tools/
cp lib/siod/*.scm $RPM_BUILD_ROOT%_libdir/speech_tools/lib/siod/

chmod +x $RPM_BUILD_ROOT%_libdir/speech_tools/config/rules/modules.sh
chmod +x $RPM_BUILD_ROOT%_libdir/speech_tools/config/system.sh

# we already instantiated templates in libsetools.
# it prevents festival from trying to instantiate it from speech_tools source
%__subst 's/^TEMPLATE_SPECIFIC = -DINSTANTIATE_TEMPLATES/TEMPLATE_SPECIFIC =/' \
$RPM_BUILD_ROOT%_libdir/speech_tools/config/compilers/gcc_defaults.mak

# Compatibility with past packages
ln -sf speech_tools $RPM_BUILD_ROOT%_includedir/estools
ln -sf speech_tools $RPM_BUILD_ROOT%_includedir/est

SBTM=$RPM_BUILD_ROOT%_man1dir
mkdir -p $SBTM
install -m644 debian/manpage.1 $SBTM/speech-tools.1
gzip -9 $SBTM/speech-tools.1
for f in $S_UNDOC ; do ln -sf speech-tools.1.gz $SBTM/$f.1.gz ; done

# installing debian man pages
install -d $RPM_BUILD_ROOT%_man1dir/

install -m644 debian/ch_track.1 $RPM_BUILD_ROOT%_man1dir/ch_track.1
install -m644 debian/na_play.1 $RPM_BUILD_ROOT%_man1dir/na_play.1
install -m644 debian/na_record.1 $RPM_BUILD_ROOT%_man1dir/na_record.1
install -m644 debian/ch_lab.1 $RPM_BUILD_ROOT%_man1dir/ch_lab.1
install -m644 debian/ch_utt.1 $RPM_BUILD_ROOT%_man1dir/ch_utt.1
install -m644 debian/ch_wave.1 $RPM_BUILD_ROOT%_man1dir/ch_wave.1

# Install Festival

cd $RPM_BUILD_DIR/festival
install -d $RPM_BUILD_ROOT%_bindir

# install binarys
install -D bin/text2wave $RPM_BUILD_ROOT%_bindir/text2wave
install -m 755 bin/festival_server* $RPM_BUILD_ROOT%_bindir/
install -m 755 src/main/festival $RPM_BUILD_ROOT%_bindir
install -m 755 src/main/festival_client $RPM_BUILD_ROOT%_bindir
install -m 755 examples/saytime $RPM_BUILD_ROOT%_bindir/
# install configs
#install -D lib/festival.scm $RPM_BUILD_ROOT%_sysconfdir/festival.scm
install -m644 -D %{SOURCE5} $RPM_BUILD_ROOT%_sysconfdir/festival/siteinit.scm
install -m644 -D %{SOURCE6} $RPM_BUILD_ROOT%_sysconfdir/festival/sitevars.scm
# server config; loaded directly in init script
install -m644 -D %{SOURCE4} $RPM_BUILD_ROOT%_sysconfdir/festival/server.scm

install -m755 -D %{SOURCE3} $RPM_BUILD_ROOT%_initdir/festival

set `find ./lib/etc -name audsp`
install -D $1 $RPM_BUILD_ROOT%festival_libexec_dir/audsp

install -d $RPM_BUILD_ROOT%_datadir/emacs/site-lisp
install -m 644 lib/festival.el $RPM_BUILD_ROOT%_datadir/emacs/site-lisp

install -d $RPM_BUILD_ROOT%_datadir/festival/multisyn
install -m 644 lib/*.scm $RPM_BUILD_ROOT%_datadir/festival/
install -m 644 lib/multisyn/*.scm $RPM_BUILD_ROOT%_datadir/festival/multisyn/
#install -m 644 lib/sable-latin.ent $RPM_BUILD_ROOT%_datadir/festival
#install -m 644 lib/Sable.v0_2.dtd $RPM_BUILD_ROOT%_datadir/festival
#install -m 644 lib/scfg_wsj_wp20.gram $RPM_BUILD_ROOT%_datadir/festival
#install -m 644 lib/sec.B.hept.ngrambin $RPM_BUILD_ROOT%_datadir/festival
#install -m 644 lib/sec.ts20.quad.ngrambin $RPM_BUILD_ROOT%_datadir/festival
install -m 644 lib/*.ent $RPM_BUILD_ROOT%_datadir/festival
install -m 644 lib/*.dtd $RPM_BUILD_ROOT%_datadir/festival
install -m 644 lib/*.gram $RPM_BUILD_ROOT%_datadir/festival
install -m 644 lib/*.ngrambin $RPM_BUILD_ROOT%_datadir/festival
install -m 644 lib/*.ngrambin $RPM_BUILD_ROOT%_datadir/festival

# install manpages
install -d $RPM_BUILD_ROOT%_man1dir
install -m 644 doc/*.1 $RPM_BUILD_ROOT%_man1dir
# TODO:
#install -D -m 644 doc/festival.1 $RPM_BUILD_ROOT%_man1dir/festival.1
#install -m 644 doc/festival_client.1 $RPM_BUILD_ROOT%_man1dir/
#install -m 644 doc/text2wave.1 $RPM_BUILD_ROOT%_man1dir/

mkdir $RPM_BUILD_ROOT%{_infodir}
cp -p doc/info/* $RPM_BUILD_ROOT%{_infodir}/

# ALTLinux README
cp %{SOURCE2} .

# Install libfestival-devel
install -d $RPM_BUILD_ROOT%_includedir/festival
install -m 644 src/include/*.h $RPM_BUILD_ROOT%_includedir/festival/

%if_enabled static
# Install libfestival-devel-static
install -m 644 src/lib/libFestival.a $RPM_BUILD_ROOT%_libdir/
%endif

%if_with festival_dynamic_build
install -m 644 src/lib/libFestival.so* $RPM_BUILD_ROOT%_libdir/
%endif

# install examples 
# preparing hardcoded path to examples (/usr/share/doc/festival/examples)
mkdir -p $RPM_BUILD_ROOT%_datadir/doc
# cleaning examples dir
ln -s %{name}-%{fst_version} $RPM_BUILD_ROOT%_datadir/doc/%{name}
rm -f examples/Makefile examples/songs/Makefile examples/*.sh


# RedHat Fedora festival-1.95 based
#######################################################################
# Fix up the headers to look for other includes where we want them, not
# where they're supposed to be in the source tree
# There is probably a better way to do this, I'm not (yet) a sed expert.
# What this does is, basically, replacing "EST_*.h" with <speech_tools/EST_*.h>.
for i in `find $RPM_BUILD_ROOT%{_includedir}/speech_tools/ -type f \( -name '*.h' -or -name '*.cc' \)` `find $RPM_BUILD_ROOT%{_includedir}/festival/ -type f \( -name '*.h' -or -name '*.cc' \)`; do
  sed \
	-e 's,"\(EST.*\.h\)",\<speech_tools/\1\>,g' \
	-e 's,"\(siod.*\.h\)",\<speech_tools/\1\>,g' \
	-e 's,"\(instantiate/.*\.h\)",\<speech_tools/\1\>,g' \
	-e 's,"\(ling_class/.*\.h\)",\<speech_tools/\1\>,g' \
	-e 's,"rxp\.h",\<speech_tools/rxp/rxp\.h\>,g' \
	-e 's,"\(rxp/.*\.h\)",\<speech_tools/\1\>,g' \
  	-e 's,"\(sigpr/.*\.h\)",\<speech_tools/\1\>,g' \
	-e 's,"\(unix/.*\.h\)",\<speech_tools/\1\>,g' \
	-e 's,"festival\.h",\<festival/festival.h\>,g' \
  	-e 's,"ModuleDescription\.h",\<festival/ModuleDescription.h\>,g' \
  	-e 's,"Phone\.h",\<festival/Phone.h\>,g' \
      $i >$i-alt
  mv -f $i-alt $i
done

%pre
/usr/sbin/groupadd -r -f %festival_group ||:
grep '^%festival_user:' /etc/passwd >/dev/null || \
/usr/sbin/useradd -g %festival_group -c 'The Festival Speech Synthesizer' \
        -d %festival_home -s /dev/null -r %festival_user ||:

%files
%doc ../festival/{README,ACKNOWLEDGMENTS,COPYING,NEWS}
%doc ../festival/debian/README.Debian
%doc ../festival/README.ALTLinux
%_initdir/festival
%config(noreplace) %_sysconfdir/festival/server.scm
%dir %_sysconfdir/festival
%config(noreplace) %_sysconfdir/festival/siteinit.scm
%config(noreplace) %_sysconfdir/festival/sitevars.scm
# examples
%doc %_datadir/doc/%{name}
%doc ../festival/examples
# end examples
#%_bindir/festival*
%_bindir/festival
%_bindir/festival_client
%if_with legacy_server_scripts
%_bindir/festival_server
%_bindir/festival_server_control
%else
%exclude %_bindir/festival_server
%exclude %_bindir/festival_server_control
%endif
%_bindir/text2wave
%_bindir/saytime
%dir %_datadir/festival/
%dir %festival_libexec_dir
%festival_libexec_dir/audsp
%_datadir/festival/*
%{_infodir}/festival*
%_man1dir/festival*
%_man1dir/text2wave*
%_datadir/emacs/site-lisp/festival.el
%if_with festival_dynamic_build
%_libdir/libFestival.so.*
%endif

%if_with est_dynamic_build
%files -n libestools%estsuffix
%_libdir/libest*.so.*
%endif

%files -n libfestival-devel
%dir %{_includedir}/festival
%{_includedir}/festival/*
%if_with festival_dynamic_build
%_libdir/libFestival.so
%endif

%if_enabled static
%files -n libfestival-devel-static
%_libdir/libFestival.a
%endif

%files -n libestools-devel
%doc ../speech_tools/README
%_includedir/estools
%_includedir/est
%dir %{_includedir}/speech_tools
%{_includedir}/speech_tools/*
%_libdir/speech_tools/*
%if_with est_dynamic_build
%_libdir/libest*.so
%endif
%if_enabled static
%files -n libestools-devel-static
%_libdir/libest*.a
%else
%exclude %_libdir/libest*.a
%endif

%files -n speech_tools
%doc ../speech_tools/README
%_bindir/[^f]*
%_man1dir/[^f]*.1*
%exclude %_bindir/festival*
%exclude %_bindir/text2wave
%exclude %_bindir/saytime
%exclude %_man1dir/text2wave*


%changelog
* Sat Jul 31 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.95-alt1
- new version (beta)

* Fri Jun 05 2009 Igor Vlasenko <viy@altlinux.ru> 1.96-alt7
- spec cleanup
- gcc44 support

* Thu Nov 27 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt6
- fixed bug in init script

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt5.1
- removed deprecated calls to ldconfig

* Wed Oct 22 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt5
- added festival-1.96-alt-unsafe-tmp-usage.patch (repocop@)
- fixed build with g++ 4.3

* Thu Aug 28 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt4
- fixed bug with x86_64

* Sun Aug 03 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt3.1
- updated patch2 to support voice_msu_ru_nsh_clunits

* Wed Jul 30 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt3
 - updated speech_tools from awb
 - synced patches with fedora and suse (still some TODO)
 - libFestival built as shared library (#12569)

* Fri Dec 29 2006 Igor Vlasenko <viy@altlinux.ru> 1.96-alt2.6
 - updated 2006.12.26 from awb to unofficial 1.96

* Mon Dec 18 2006 Igor Vlasenko <viy@altlinux.ru> 1.96-alt2.5
- russian diphone patch is no more needed -- removed
- added patch for --language russian option
  (picks up festvox_msu_ru_nsh_cg)

* Sun Nov 12 2006 Igor Vlasenko <viy@altlinux.ru> 1.96-alt2.4
- speech_tools are updated to unofficial 1.96
- added workaround for festival1.96 and buggy scms in multisyn voices
- patches are adapted to 1.96

* Fri Nov 03 2006 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
- festival is updated to unofficial 1.96
- updated russian patch (russian is still disabled by default)
- speech_tools SuSE patches are synced with SuSE festival-1.96-11
- init script is polished (thanks to all ALT friends)

* Wed Nov 01 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.8.5
- fixed multisyn installation
- disabled russian voice patch to enable multisyn voices.
- TODO: build something like festival-russian?
- added init script
- now festival creates pseudo user _festival : audio

* Sat Oct 28 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.7.9
- added README.ALTLinux
- preparations for server mode festival
- configs moved to /etc/festival/

* Fri Oct 20 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.7.5
- added alt-fix-path-audsp.patch 
  (setup path for right location of /usr/lib/festival/audsp)
- added asterisk patch

* Wed Oct 18 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.7.3
- separated language.diff from scm.diff;
- remade sysconf.diff;
- enabled Requires:	festvox again;
- applied sysconf.diff patch; now configs are searched in /etc

* Wed Oct 18 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.7.0
- added support for Russian voice
- fixed broken symlink doc/festival

* Sun Oct 15 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.6.5
- added post, postun ldconfig;
- added info (and fixed info dir entry: festival-1.4.3-alt-info-header.patch)
- added examples;
- disabled for a while Requires:	festvox;
  (until festvox_CMU will pass incoming)

* Wed Oct 11 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.6.1
- rest of festival debian patches are added to srpm;
  applied:
   * alaw support
   * debian dir
   * misc scm fixes

* Fri Sep 29 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt0.5.9
- new version;
- picked up from orphaned;
- merged Debian, SuSE, Fedora patches;
- built with gcc41, as-needed, strict verify-elf

* Thu Mar 29 2001 Lev Levitin <lev@mccme.ru>
  [festival-1.4.1-ipl3mdk]
- audsp moved to /usr/lib/festival as an internal use binary
  to correspond FHS.

* Mon Feb 5 2001 Lev Levitin <lev@mccme.ru>
  [festival-1.4.1-ipl2mdk]
- Edinburgh Speech Tools building included into this spec
  file because their source is needed to compile Festival

* Sat Feb 3 2001 Lev Levitin <lev@mccme.ru>
  [festival-1.4.1-ipl1mdk]
- Initial Mandrake RE release
