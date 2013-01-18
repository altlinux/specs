%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%def_enable pam
%def_enable consolekit
%def_enable grub2

Name: entrance
Version: 0.0.4
Release: alt0.1
Serial: 1

Summary: The Enlightenment Display Manager
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://enlightenment.org
# VCS: git://git.enlightenment.fr/vcs/svn/PROTO/entrance.git

Source: %name-%version.tar
Source1: entrance.wms-method
# enable LFS support
Patch: %name-0.0.4-alt-build.patch
# replace hardcoded sessions desktop dir
Patch1: %name-0.0.4-alt-sessions_dir.patch
Patch2: %name-0.0.4-alt-entrance.conf.patch
# especially for prefdm.service
Patch3: %name-0.0.4-alt-bad_options.patch

%{?_enable_consolekit:Requires: ConsoleKit-x11}

# from configure.ac
BuildRequires: libeet-devel libecore-devel libevas-devel
BuildRequires: libefreet-devel libxcb-devel libedje-devel libelementary-devel
BuildRequires: edje embryo_cc
%{?_enable_pam:BuildRequires: libpam-devel}
%{?_enable_consolekit:BuildRequires: libdbus-devel libConsoleKit-devel}

%description
Entrance is a login/display manager for Enlightenment desktop.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure \
	%{subst_enable pam} \
	%{subst_enable consolekit} \
	%{subst_enable grub2}

%make_build

%install
%makeinstall_std
# install external hook for update_wms
mkdir -p %buildroot%_sysconfdir/X11/wms-methods.d
install -m755 %SOURCE1 %buildroot%_sysconfdir/X11/wms-methods.d/%name

# dirs under /var
mkdir -p %buildroot%_localstatedir/lib/%name
mkdir -p %buildroot%_localstatedir/cache/%name/users

# PAM-config
cat > %buildroot%_sysconfdir/pam.d/%name <<_PAM_
#%PAM-1.0
auth	required	pam_shells.so
auth	required	pam_succeed_if.so quiet uid ne 0
auth	sufficient	pam_succeed_if.so user ingroup nopasswdlogin
auth	substack	common-login
auth	optional	pam_gnome_keyring.so
account	include		common-login
password	include		common-login
session		substack	common-login
session		optional	pam_console.so
session		required	pam_namespace.so
session		optional	pam_gnome_keyring.so auto_start
_PAM_

%find_lang %name

%pre
%_sbindir/groupadd -r -f %name >/dev/null 2>&1 || :
%_sbindir/useradd -M -r -d %_localstatedir/lib/%name -s /bin/false -c "Entrance daemon" -g %name %name >/dev/null 2>&1 || :

%files -f %name.lang
%_sbindir/%name
%config %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/X11/wms-methods.d/%name
%dir %_libdir/%name
%{?_enable_consolekit:%_libdir/%name/entrance_ck_launch}
%_libdir/%name/entrance_client
%_libdir/%name/entrance_wait
%_datadir/%name/
%attr(1770,%name,%name) %dir %_localstatedir/lib/%name
%attr(775,%name,%name) %dir %_localstatedir/cache/%name
%attr(775,%name,%name) %dir %_localstatedir/cache/%name/users
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Fri Jan 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.4-alt0.1
- first preview for Sisyphus (c0b37925acf)

