# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)
BuildRequires: gcc-c++
%global nbmversion 1.7
%global geditver 0.4

Name: beesu
Version: 2.7
# Don't ever decrease this version (unless all beesu, nbm, and gbp update) or the subpackages will go backwards.
# It is easier to do this than to track a separate release field.
Release: alt2_7
Summary: Graphical wrapper for su
URL: http://www.honeybeenet.altervista.org
Group: System/Base
License: GPLv2+
Source0: http://honeybeenet.altervista.org/beesu/files/beesu-sources/%{name}-%{version}.tar.bz2
Source1: http://honeybeenet.altervista.org/beesu/files/beesu-manager/nautilus-beesu-manager-%{nbmversion}.tar.bz2
Source2: http://honeybeenet.altervista.org/beesu/files/beesu-gedit/gedit-beesu-plugin-%{geditver}.tar.bz2
Patch0:  beesu-gedit-plugin-fix.patch
Patch1:  beesu-nautilus-no-browser.patch
BuildRequires: desktop-file-utils
Requires: pam consolehelper
Source44: import.info

%description
Beesu is a wrapper around su and works with consolehelper under
Fedora to let you have a graphic interface like gksu.

%package -n nautilus-beesu-manager
Version:	%{nbmversion}
BuildArch:	noarch
Requires:	beesu zenity nautilus
Group:		System/Base
Summary:	Utility to add beesu scripts to nautilus

%description -n nautilus-beesu-manager
nautilus-beesu-manager is a little utility to add some useful scripts
to the Nautilus file browser; nautilus-beesu-manager can add scripts
to Nautilus using beesu to elevate the user's privileges to root.

%package -n gedit-beesu-plugin
Version:	%{geditver}
Requires:	gedit beesu pygtk2
Group:		System/Base
Summary:	Allows normal users to open files in gedit as root

%description -n gedit-beesu-plugin
This package contains a plugin for gedit which allows normal users to open 
files as root (via beesu). After installation, to activate the plugin in
gedit, go to Edit -> Preferences -> Plugins and check the box next to
Open as root.

%prep
%setup -q -a1 -a2
%patch0 -p1 -b .fix
%patch1 -p1
chmod -x nautilus-beesu-manager-%{nbmversion}/COPYING nautilus-beesu-manager-%{nbmversion}/README

%build
make CFLAGS="%{optflags} -fno-delete-null-pointer-checks"

pushd gedit-beesu-plugin-%{geditver}
./configure --frontend beesu --buildroot %{buildroot} --libexecdir %{_libexecdir} --libdir %{_libdir}
make CFLAGS="%{optflags}"
popd

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
make DESTDIR=%{buildroot} install

#nbm
pushd nautilus-beesu-manager-%{nbmversion}
mkdir -v -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
mkdir -v -p %{buildroot}%{_datadir}/applications/
install -p -m 755 nautilus-beesu-manager %{buildroot}%{_bindir}
install -p -m 644 nautilus-beesu-manager.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
desktop-file-install --dir %{buildroot}%{_datadir}/applications --mode 0644 nautilus-beesu-manager.desktop
mkdir -v -p %{buildroot}%{_libexecdir}/nautilus-beesu-manager/
install -p -m 755 libexec/api %{buildroot}%{_libexecdir}/nautilus-beesu-manager/
cp -a libexec/scripts %{buildroot}%{_libexecdir}/nautilus-beesu-manager/
install -p -m 644 libexec/local-launcher %{buildroot}%{_libexecdir}/nautilus-beesu-manager/ 
popd

#gbp
pushd gedit-beesu-plugin-%{geditver}
make install
popd
mkdir -p %buildroot/etc/pam.d
cat > %buildroot/etc/pam.d/config-util <<'EOF'
#%%PAM-1.0
auth		sufficient	pam_rootok.so
auth		sufficient	pam_timestamp.so
auth		include		system-auth
account		required	pam_permit.so
session		required	pam_permit.so
session		optional	pam_xauth.so
session		optional	pam_timestamp.so
EOF

%files
%doc COPYING README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%{_sysconfdir}/profile.d/%{name}-bash-completion.sh
%{_sbindir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
/etc/pam.d/config-util

%files -n nautilus-beesu-manager
%doc nautilus-beesu-manager-%{nbmversion}/COPYING nautilus-beesu-manager-%{nbmversion}/README
%{_bindir}/nautilus-beesu-manager
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/32x32/apps/nautilus-beesu-manager.png 
%{_libexecdir}/nautilus-beesu-manager/

%files -n gedit-beesu-plugin
%{_libdir}/gedit/plugins/beesu.plugin
%{_libdir}/gedit/plugins/beesu/__init__.py*
%{_libdir}/gedit/plugins/beesu/beesu.py*
%{_libexecdir}/gedit-beesu-plugin

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_6
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_6
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_5
- update to new release by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7-alt1_4.1
- Rebuild with Python-2.7

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_4
- initial release by fcimport

