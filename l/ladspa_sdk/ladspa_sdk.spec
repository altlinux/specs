Name: ladspa_sdk
Version: 1.13
Release: alt1

Summary: The Linux Audio Developer's Simple Plugin API (LADSPA)
License: LGPL
Group: Sound
Url: http://www.ladspa.org

Source: http://www.ladspa.org/download/%name.tgz
Patch0: %name-1.11-alt-makefile.patch
Patch1: %name-1.11-alt-silent.build.patch
Patch2: %name-1.11-alt-notmp_makefile.patch
Patch3: %name-1.12-alt-libs.patch
Patch4: %name-1.12-alt-gcc4.1.patch

Requires: common-licenses

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ time

%description
The Linux Audio Developer's Simple Plugin API (LADSPA) attempts
to give programmers the ability to write simple `plugin' audio
processors in C/C++ and link them dynamically against a range of
host applications.

%define _ladspa_path %_libdir/ladspa
%define _ladspa_datadir %_datadir/ladspa

%prep
%setup -q -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%__subst 's,mkdirhier,mkdir -p,' src/makefile

%build
%define _optlevel 3
pushd src
%make_build CFLAGS="\$(INCLUDES) -Werror -fPIC $RPM_OPT_FLAGS"
popd

%install
%__mkdir_p %buildroot%_datadir/ladspa/rdf
pushd src
%make_install PREFIX=%prefix DESTDIR=%buildroot \
	INSTALL_PLUGINS_DIR=%_ladspa_path \
	install
popd

# install docs and license
%__rm -f doc/COPYING
%__ln_s -f %_licensedir/LGPL-2 COPYING
%__ln_s -f %_includedir/ladspa.h doc/ladspa.h.txt
%__ln_s -f doc/index.html index.html

# Applications using LADSPA-plugins needs environment variable LADSPA_PATH.
%__cat << __SH__ >ladspa.sh
# where LADSPA plugins installed
LADSPA_PATH="%_ladspa_path"
export LADSPA_PATH
__SH__

%__cat << __CSH__ >ladspa.csh
# where LADSPA plugins installed
setenv LADSPA_PATH "%_ladspa_path"
__CSH__

%__install -d %buildroot%_sysconfdir/profile.d
%__install -m755 ladspa.{sh,csh} %buildroot%_sysconfdir/profile.d

# Creating ladspa_sdk buildreq filter
%__cat <<__BUILDREQS__ > %name.buildreq
# ladspa buildreq filter.
^%_ladspa_path
__BUILDREQS__

%__install -pD -m644 %name.buildreq %buildroot%_sysconfdir/buildreqs/files/ignore.d/ladspa

# rpm macros for ladspa related software
%__cat <<__RPM_MACROS__ >ladspa.rpm_macros
%%_ladspa_path %%_libdir/ladspa
%%_ladspa_datadir %%_datadir/ladspa
__RPM_MACROS__

%__install -pD -m644 ladspa.rpm_macros %buildroot%_rpmlibdir/macros.d/%name

%files
%_bindir/*
%_includedir/ladspa.h
%_ladspa_path
%dir %_ladspa_datadir
%dir %_ladspa_datadir/rdf
%_sysconfdir/profile.d/*
%_rpmlibdir/macros.d/*
%config %_sysconfdir/buildreqs/files/ignore.d/*
%doc --no-dereference index.html doc README COPYING

%changelog
* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 1.13-alt1
- new version
- moved rpm macros to %%_rpmlibdir from /etc

* Mon May 29 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.12-alt4
- x86_64 fix from Damir Shayhutdinov (bug 8541)
- Patch3: link order fix
- Patch4: gcc 4.1 fixes
- Added the bundled plugins to the filelist

* Thu Sep 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.12-alt3
- make buildable.

* Tue Dec 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.12-alt2
- %_ladspa_datadir{,/rdf} owned by ladspa_sdk
- Added rpmmacros %_ladspa_path, %_ladspa_datadir
- removed deps on csh by fixing headers of /etc/profile.d files

* Wed Nov 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.12-alt1
- 1.12
- fixed ladspa.csh (close #1532)

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.11-alt5
- rebuild with gcc-3.2

* Mon Jan 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.11-alt4
- cleanups

* Fri Dec 14 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.11-alt3
- example plugins removed from sdk, its present in CMT package.
- initscripts added.

* Mon Nov 12 2001 Stanislav Ievlev <inger@altlinux.ru> 1.11-alt2
- fix build process

* Sat Nov 10 2001 Yuri N. Sedunov <aris@altlinux.ru>
- first build for Sisyphus
