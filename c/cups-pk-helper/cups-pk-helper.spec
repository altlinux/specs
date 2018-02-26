Name: cups-pk-helper
Version: 0.0.4
Release: alt1
Summary: A helper that makes system-config-printer use PolicyKit

Group: System/Configuration/Printing
License: GPLv2+
Url: http://www.vuntz.net/download/cups-pk-helper/
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

Source: http://www.vuntz.net/download/cups-pk-helper/cups-pk-helper-%version.tar.bz2

Patch: polkit-1.patch
Patch1: get_devices.patch
Patch2: polkit_result.patch
Patch3: edit_job.patch

BuildRequires: libtool >= 1.4.3
BuildRequires: libcups-devel >= 1.2
BuildRequires: python-devel >= 2.4
BuildRequires: glib2-devel >= 2.14.0
BuildRequires: gtk2-devel >= 2.12.0
BuildRequires: libdbus-glib-devel >= 0.74
BuildRequires: libpolkit1-devel >= 0.92
BuildRequires: libpolkit-gnome-devel >= 0.92
BuildRequires: intltool >= 0.40.0
BuildRequires: gettext-devel >= 0.17
BuildRequires: gnome-common >= 2.26

%description
cups-pk-helper is an application which makes cups configuration
interfaces available under control of PolicyKit.

%prep
%setup -q

%patch0 -p1 -b .polkit-1
%patch1 -p1 -b .get-devices
%patch2 -p1 -b .polkit-result
%patch3 -p1 -b .edit-job

%build
autoreconf -fisv

%configure
%make_build

%install
%makeinstall_std

%files
%_libexecdir/cups-pk-helper-mechanism
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
%_datadir/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
%_datadir/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy
%doc AUTHORS COPYING NEWS

%changelog
* Wed Jan 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.0.4-alt1
-  build for Sisyphus

* Tue Aug 18 2009 Marek Kasik <mkasik@redhat.com> - 0.0.4-7
- Fix policies to check when editing a job.

* Tue Aug 18 2009 Marek Kasik <mkasik@redhat.com> - 0.0.4-6
- Check result of polkit_authority_check_authorization_sync() for NULL.

* Thu Aug 13 2009 Marek Kasik <mkasik@redhat.com> - 0.0.4-5
- Add parameters to DevicesGet method.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Marek Kasik <mkasik@redhat.com> - 0.0.4-3
- Add devices_get() function.

* Thu Jun 18 2009 Marek Kasik <mkasik@redhat.com> - 0.0.4-2
- Update to polkit-1

* Tue Mar 31 2009 Marek Kasik <mkasik@redhat.com> - 0.0.4-1
- Update to 0.0.4

* Fri Feb 27 2009 Marek Kasik <mkasik@redhat.com> - 0.0.3-6
- Replace job-cancel, job-restart and job-set-hold-until with job-edit
- Replace job-cancel-another-owner, job-restart-another-owner
  and job-set-hold-until-another-owner with job-not-owned-edit
- Add cph_cups_job_get_status() function + some minor changes

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Marek Kasik <mkasik@redhat.com> 0.0.3-4
- Add ability to reconnect to CUPS server after its reload
  (caused by cupsAdminSetServerSettings() or cupsPutFile())

* Tue Jan 28 2009 Marek Kasik <mkasik@redhat.com> 0.0.3-3
- Add functions for handling jobs (JobRestart, JobCancel, JobSetHoldUntil)

* Tue Jan 26 2009 Marek Kasik <mkasik@redhat.com> 0.0.3-2
- Add handling of file:/ protocol
- Change order of checked policies so the PolicyKit asks only for
  "printer-enable" policy when enabling/disabling a printer
- Change order of checked policies so the PolicyKit asks only for
  "printer-set-default" policy when setting default printer

* Tue Jan 13 2009 Marek Kasik <mkasik@redhat.com> 0.0.3-1
- Initial spec file.
