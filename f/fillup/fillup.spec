Name: fillup
Version: 1.42
Release: alt6

Summary: Tool for merging config files
License: GPL
Group: System/Base

Source0: fillup-%version.tar.bz2
Source1: fillup.macros
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Sep 24 2008
BuildRequires: OpenSP sgml-tools
Requires: rpm-macros-%{name} = %{version}-%{release}

%description
fillup merges files that hold variables.  A variable is defined by an
entity composed of a preceding comment, a variable name, an assignment
delimiter, and a related variable value.  A variable is determined by
its variable name.

Authors:
--------
    Joerg Dippel <jd/suse.de>


%package -n rpm-macros-%{name}
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: fillup <= 1.42-alt5

%description -n rpm-macros-%{name}
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%setup -q

%build
%make clean
%make compile
%make test
pushd SGML
%make fillup.txt
popd

%install
mkdir -p %buildroot/%_datadir/fillup-templates
install -pDm755 TEST/fillup %buildroot/bin/%name
install -pDm644 %SOURCE1 %buildroot%_rpmmacrosdir/%name
install -pDm644 SGML/fillup.8.gz %buildroot%_man8dir/%name.8.gz

%files
%doc SGML/fillup.txt
/bin/%name
%_man8dir/fillup*
#%_rpmmacrosdir/%name
%dir %_datadir/fillup-templates
%exclude %_rpmmacrosdir/*

%files -n rpm-macros-%{name}
%_rpmmacrosdir/*


%changelog
* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.42-alt6
- applied repocop patch

* Wed Sep 24 2008 Michael Shigorin <mike@altlinux.org> 1.42-alt5
- build fix
- spec cleanup

* Wed Mar 22 2006 Anton Farygin <rider@altlinux.ru> 1.42-alt4
- added fillup_config macros for %_sysconfdir/<package>/ configs

* Tue Jul 05 2005 Anton Farygin <rider@altlinux.ru> 1.42-alt3
- fillup directory changed to %_datadir/fillup-templates

* Fri Jul 01 2005 Anton Farygin <rider@altlinux.ru> 1.42-alt2
- added fillup_sysconfig rpm macros

* Thu Jun 30 2005 Anton Farygin <rider@altlinux.ru> 1.42-alt1
- first build for Sisyphus
