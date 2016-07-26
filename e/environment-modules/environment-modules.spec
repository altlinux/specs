# BEGIN SourceDeps(oneline):
BuildRequires: imake libXt-devel xorg-cf-files
# END SourceDeps(oneline)
%define fedora 24

Name:           environment-modules
Version:        3.2.10
Release:        alt1_17
Summary:        Provides dynamic modification of a user's environment

Group:          System/Base
License:        GPLv2+
URL:            http://modules.sourceforge.net/
Source0:        http://downloads.sourceforge.net/modules/modules-%{version}.tar.bz2
Source1:        modules.sh
Source2:        createmodule.sh
Source3:        createmodule.py
Source4:        macros.%{name}
Patch0:         environment-modules-3.2.7-bindir.patch
# Comment out stray module use in modules file when not using versioning
# https://bugzilla.redhat.com/show_bug.cgi?id=895555
Patch1:         environment-modules-versioning.patch
# Fix module clear command
# https://bugzilla.redhat.com/show_bug.cgi?id=895551
Patch2:         environment-modules-clear.patch
# Patch from modules list to add completion to avail command
Patch3:         environment-modules-avail.patch
# Fix -Werror=format-security
# https://bugzilla.redhat.com/show_bug.cgi?id=1037053
# https://sourceforge.net/p/modules/patches/13/
Patch4:         environment-modules-format.patch
# Support Tcl 8.6
# https://sourceforge.net/p/modules/feature-requests/14/
Patch5:         environment-modules-tcl86.patch
# python 3 support
# https://sourceforge.net/p/modules/patches/15/
# https://bugzilla.redhat.com/show_bug.cgi?id=1184979
Patch6:         environment-modules-py3-and-doc-fix.patch
# Fix unload from loaded modulefile
# https://bugzilla.redhat.com/show_bug.cgi?id=1117334
Patch7:         environment-modules-3.2.10-unload-from-module.patch

BuildRequires:  tcl-devel, tclx, libX11-devel
BuildRequires:  dejagnu
BuildRequires: man man-whatis
#For ps in startup script
Requires: procps sysvinit-utils
Provides:	environment(modules)
Source44: import.info

%description
The Environment Modules package provides for the dynamic modification of
a user's environment via modulefiles.

Each modulefile contains the information needed to configure the shell
for an application. Once the Modules package is initialized, the
environment can be modified on a per-module basis using the module
command which interprets modulefiles. Typically modulefiles instruct
the module command to alter or set shell environment variables such as
PATH, MANPATH, etc. modulefiles may be shared by many users on a system
and users may have their own collection to supplement or replace the
shared modulefiles.

Modules can be loaded and unloaded dynamically and atomically, in an
clean fashion. All popular shells are supported, including bash, ksh,
zsh, sh, csh, tcsh, as well as some scripting languages such as perl.

Modules are useful in managing different versions of applications.
Modules can also be bundled into metamodules that will load an entire
suite of different applications.

NOTE: You will need to get a new shell after installing this package to
have access to the module alias.


%prep
%setup -q -n modules-%{version}
%patch0 -p1 -b .bindir
%patch1 -p1 -b .versioning
%patch2 -p1 -b .clear
%patch3 -p1 -b .avail
%patch4 -p1 -b .format
%patch5 -p1 -b .tcl86
%patch6 -p1 -b .py3
%patch7 -p1 -b .unload-from-module


%build
%configure --disable-versioning \
	--with-tcl-inc=/usr/include \
           --prefix=%{_datadir} \
           --exec-prefix=%{_datadir}/Modules \
           --with-man-path=$(manpath) \
           --with-module-path=%{_sysconfdir}/modulefiles:%{_datadir}/modulefiles
#           --with-debug=42 --with-log-facility-debug=stderr
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
touch %{buildroot}%{_sysconfdir}/profile.d/modules.{csh,sh}
cp -p %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/Modules/init/modules.sh
cp -p %SOURCE2 %SOURCE3 $RPM_BUILD_ROOT%{_datadir}/Modules/bin
%if 0%{?fedora} >= 22
sed -i -e 1s,/usr/bin/python,/usr/bin/python3, \
    $RPM_BUILD_ROOT%{_datadir}/Modules/bin/createmodule.py
%endif
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modulefiles \
         $RPM_BUILD_ROOT%{_datadir}/modulefiles
# Install the rpm config file
install -Dpm 644 %{SOURCE4} %{buildroot}/%{_rpmmacrosdir}/%{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/modules.sh_environment-modules<<EOF
%{_sysconfdir}/profile.d/modules.sh	%{_datadir}/Modules/init/modules.sh	40
%{_sysconfdir}/profile.d/modules.csh	%{_datadir}/Modules/init/csh	%{_datadir}/Modules/init/modules.sh
EOF


%post
[ ! -L %{_bindir}/modules.sh ] && rm -f %{_sysconfdir}/profile.d/modules.sh
:

%files
%_altdir/modules.sh_environment-modules
%doc LICENSE.GPL README TODO
%{_sysconfdir}/modulefiles
%{_bindir}/modulecmd
%dir %{_datadir}/Modules
%{_datadir}/Modules/bin/
%dir %{_datadir}/Modules/init
%config(noreplace) %{_datadir}/Modules/init/*
%config(noreplace) %{_datadir}/Modules/init/.modulespath
%{_datadir}/Modules/modulefiles
%{_datadir}/modulefiles
%{_mandir}/man1/module.1*
%{_mandir}/man4/modulefile.4*
%{_rpmmacrosdir}/%{name}


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_16
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_11
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_10
- converted for ALT Linux by srpmconvert tools

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_8
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_6
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_5
- update to new release by fcimport

* Fri Apr 19 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_4
- update to new release by fcimport

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_3
- fc update

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_2
- fc update

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_1
- update to new release by fcimport

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.9c-alt1_5
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.9c-alt1_4
- update to new release by fcimport

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.9c-alt1_3
- new release

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.9c-alt1_2
- update to new release by fcimport

* Thu Dec 15 2011 Igor Vlasenko <viy@altlinux.ru> 3.2.9c-alt1_1
- update to new release by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.8a-alt1_3.1
- Rebuild with Python-2.7

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 3.2.8a-alt1_3
- update to new release by fcimport

* Sat Jun 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.2.8a-alt1_2
- initial release by fcimport

