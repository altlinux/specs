Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-alternatives
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global vimdatadir %{_datadir}/vim/vimfiles

Name:           environment-modules
Version:        5.3.1
Release:        alt1_2
Summary:        Provides dynamic modification of a user's environment

License:        GPL-2.0-or-later
URL:            http://modules.sourceforge.net/
Source0:        http://downloads.sourceforge.net/modules/modules-%{version}.tar.bz2

BuildRequires:  libtcl tcl
BuildRequires:  dejagnu
BuildRequires:  sed
BuildRequires:  less
BuildRequires:  coreutils
BuildRequires:  libprocps procps
# specific requirements to build extension library
BuildRequires:  gcc
BuildRequires:  tcl-devel
Requires:       libtcl tcl
Requires:       sed
Requires:       less
Requires:       libprocps procps
Requires:       man-db
Requires(post): coreutils
Provides:       environment(modules)
Obsoletes:      environment-modules-compat <= 4.8.99

# Tcl linter is useful for module lint command
#Recommends:     nagelfar
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



%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name modules
Group: Development/Other
BuildArch: noarch

%description -n rpm-macros-%name
Set of RPM macros for packaging %name modules.
Install this package if you want to create RPM packages that use GNAT.

%prep
%setup -q -n modules-%{version}


%build
%configure --prefix=%{_datadir}/Modules \
	--with-tcl-inc=/usr/include \
           --libdir=%{_libdir}/%{name} \
           --etcdir=%{_sysconfdir}/%{name} \
           --bindir=%{_datadir}/Modules/bin \
           --libexecdir=%{_libdir}/Modules/libexec \
           --mandir=%{_mandir} \
           --vimdatadir=%{vimdatadir} \
           --nagelfardatadir=%{_datadir}/Modules/nagelfar \
           --with-bashcompletiondir=%{_datadir}/bash-completion/completions \
           --with-fishcompletiondir=%{_datadir}/fish/vendor_completions.d \
           --with-zshcompletiondir=%{_datadir}/zsh/site-functions \
           --enable-multilib-support \
           --disable-doc-install \
           --enable-modulespath \
           --with-python=/usr/bin/python3 \
           --with-modulepath=%{_datadir}/Modules/modulefiles:%{_sysconfdir}/modulefiles:%{_datadir}/modulefiles \
           --with-quarantine-vars='LD_LIBRARY_PATH LD_PRELOAD'

%make_build


%install
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_datadir}/fish/vendor_conf.d
mkdir -p %{buildroot}%{_bindir}

# setup for alternatives
touch %{buildroot}%{_sysconfdir}/profile.d/modules.{csh,sh}
touch %{buildroot}%{_datadir}/fish/vendor_conf.d/modules.fish
touch %{buildroot}%{_bindir}/modulecmd
# remove modulecmd wrapper as it will be handled by alternatives
rm -f %{buildroot}%{_datadir}/Modules/bin/modulecmd

# major utilities go to regular bin dir
mv %{buildroot}%{_datadir}/Modules/bin/envml %{buildroot}%{_bindir}/

mv {doc/build/,}NEWS.txt
mv {doc/build/,}MIGRATING.txt
mv {doc/build/,}CONTRIBUTING.txt
mv {doc/build/,}INSTALL.txt
mv {doc/build/,}changes.txt

# install the rpm config file
install -Dpm 644 contrib/rpm/macros.%{name} %{buildroot}/%{_rpmmacrosdir}/%{name}
for rpm404_ghost in %{_sysconfdir}/profile.d/modules.csh %{_sysconfdir}/profile.d/modules.sh %{_datadir}/fish/vendor_conf.d/modules.fish %{_bindir}/modulecmd
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/modules.sh_environment-modules<<EOF
%{_sysconfdir}/profile.d/modules.sh	%{_datadir}/Modules/init/profile.sh	40
%{_sysconfdir}/profile.d/modules.csh	%{_datadir}/Modules/init/profile.csh	%{_datadir}/Modules/init/profile.sh
%{_datadir}/fish/vendor_conf.d/modules.fish	%{_datadir}/Modules/init/fish	%{_datadir}/Modules/init/profile.sh
%{_bindir}/modulecmd	%{_libdir}/Modules/libexec/modulecmd.tcl	%{_datadir}/Modules/init/profile.sh
EOF



%post
[ ! -L %{_sysconfdir}/profile.d/modules.sh ] &&  rm -f %{_sysconfdir}/profile.d/modules.sh
[ ! -L %{_sysconfdir}/profile.d/modules.csh ] &&  rm -f %{_sysconfdir}/profile.d/modules.csh
[ ! -L %{_datadir}/fish/vendor_conf.d/modules.fish ] &&  rm -f %{_datadir}/fish/vendor_conf.d/modules.fish
[ ! -L %{_bindir}/modulecmd ] &&  rm -f %{_bindir}/modulecmd

# Migration from version 3.x to 4
if [ "$(readlink /etc/alternatives/modules.sh)" = '%{_datadir}/Modules/init/modules.sh' ]; then
  :
fi

:

%files
%_altdir/modules.sh_environment-modules
%doc --no-dereference COPYING.GPLv2
%doc ChangeLog.gz README NEWS.txt MIGRATING.txt INSTALL.txt CONTRIBUTING.txt changes.txt
%{_sysconfdir}/modulefiles
%dir %{_datadir}/fish/vendor_conf.d
%{_bindir}/envml
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libtclenvmodules.so
%dir %{_datadir}/Modules
%{_datadir}/Modules/bin
%dir %{_libdir}/Modules/libexec
%{_libdir}/Modules/libexec/modulecmd.tcl
%dir %{_datadir}/Modules/init
%{_datadir}/Modules/init/*
# do not need to require shell package as we "own" completion dir
%{_datadir}/bash-completion/completions/module
%{_datadir}/bash-completion/completions/ml
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_module
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/module.fish
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/initrc
%config(noreplace) %{_sysconfdir}/%{name}/modulespath
%config(noreplace) %{_sysconfdir}/%{name}/siteconfig.tcl
%{_datadir}/Modules/modulefiles
%{_datadir}/modulefiles
%{_mandir}/man1/ml.1*
%{_mandir}/man1/module.1*
%{_mandir}/man4/modulefile.4*
%{vimdatadir}/ftdetect/modulefile.vim
%{vimdatadir}/ftplugin/modulefile.vim
%{vimdatadir}/syntax/modulefile.vim
%dir %{_datadir}/Modules/nagelfar
%{_datadir}/Modules/nagelfar/*

%files -n rpm-macros-%name
%_rpmmacrosdir/*



%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 5.3.1-alt1_2
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Mon Oct 25 2021 Igor Vlasenko <viy@altlinux.org> 5.0.1-alt1_1
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 5.0.0-alt1_1
- update to new release by fcimport

* Tue May 18 2021 Igor Vlasenko <viy@altlinux.org> 4.7.1-alt1_1
- new version

* Tue Jan 26 2021 Igor Vlasenko <viy@altlinux.ru> 4.6.1-alt1_1
- update to new release by fcimport

* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 4.5.3-alt1_1
- new version

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 4.4.1-alt1_2
- new version

* Sun Jul 21 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt3_23
- fixed build

* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt2_23
- fixed build

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_23.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-rpm-macros-packaging for environment-modules

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_23
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_21
- update to new release by fcimport

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.2.10-alt1_20.qa1
- NMU: rebuilt against Tcl/Tk 8.6

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.10-alt1_20
- update to new release by fcimport

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

