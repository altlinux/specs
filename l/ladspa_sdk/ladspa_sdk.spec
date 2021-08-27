Name: ladspa_sdk
Version: 1.15
Release: alt1

Summary: The Linux Audio Developer's Simple Plugin API (LADSPA)
License: LGPL
Group: Sound

Url: http://www.ladspa.org
Source: http://www.ladspa.org/download/%{name}_%version.tgz
Patch0: %name-1.15-alt-Makefile.patch
Patch1: %name-1.15-alt-libs.patch

Requires: common-licenses

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ time
Requires: rpm-macros-%name = %version-%release

%description
The Linux Audio Developer's Simple Plugin API (LADSPA) attempts
to give programmers the ability to write simple `plugin' audio
processors in C/C++ and link them dynamically against a range of
host applications.

%define _ladspa_path %_libdir/ladspa
%define _ladspa_datadir %_datadir/ladspa

%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
# uncomment if macros are platform-neutral
#BuildArch: noarch
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: ladspa_sdk <= 1.13-alt1

%description -n rpm-macros-%name
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%setup -n %{name}_%version
%patch0 -p1
%patch1 -p1

%build
%define _optlevel 3
%ifarch %e2k
# Some plugins use C++ and need lcxa. It can't be loaded
# dynamically, so all binaries should be linked with it.
cc --version | grep -q '^lcc:1.21' && export LIBS+=" -lcxa"
# lcc: "analyseplugin.c", line 353: error: nonstandard first parameter
#   "const int" of "main", expected "int" [-Werror=main]
%else
%add_optflags -Werror
%endif
pushd src
%make_build CFLAGS="\$(INCLUDES) -fPIC %optflags $LIBS"
popd

%install
mkdir -p %buildroot%_datadir/ladspa/rdf
pushd src
%makeinstall_std PREFIX=%prefix INSTALL_PLUGINS_DIR=%_ladspa_path
popd

# install docs and license
rm -f doc/COPYING
ln -sf %_licensedir/LGPL-2 COPYING
ln -sf %_includedir/ladspa.h doc/ladspa.h.txt
ln -sf doc/index.html index.html

# Applications using LADSPA-plugins needs environment variable LADSPA_PATH.
cat << __SH__ >ladspa.sh
# where LADSPA plugins installed
LADSPA_PATH="%_ladspa_path"
export LADSPA_PATH
__SH__

cat << __CSH__ >ladspa.csh
# where LADSPA plugins installed
setenv LADSPA_PATH "%_ladspa_path"
__CSH__

install -d %buildroot%_sysconfdir/profile.d
install -pm755 ladspa.{sh,csh} %buildroot%_sysconfdir/profile.d

# Creating ladspa_sdk buildreq filter
cat <<__BUILDREQS__ > %name.buildreq
# ladspa buildreq filter.
^%_ladspa_path
__BUILDREQS__

install -pDm644 %name.buildreq %buildroot%_sysconfdir/buildreqs/files/ignore.d/ladspa

# rpm macros for ladspa related software
cat <<__RPM_MACROS__ >ladspa.rpm_macros
%%_ladspa_path %%_libdir/ladspa
%%_ladspa_datadir %%_datadir/ladspa
__RPM_MACROS__

install -pDm644 ladspa.rpm_macros %buildroot%_rpmlibdir/macros.d/%name

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
%exclude %_rpmmacrosdir/*

%files -n rpm-macros-%name
%_rpmmacrosdir/*

%changelog
* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 1.15-alt1
- updated to 1.15

* Fri Dec 28 2018 Michael Shigorin <mike@altlinux.org> 1.13-alt1.qa3
- support e2kv4, lcc-1.23

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.13-alt1.qa2
- E2K: avoid -Werror with implicit -Wmain
- minor spec cleanup

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1.13-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-rpm-macros-packaging for ladspa_sdk
  * postclean-03-private-rpm-macros for the spec file

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
