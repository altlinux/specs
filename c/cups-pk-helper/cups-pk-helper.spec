Name: cups-pk-helper
Version: 0.2.7
Release: alt0.1.ge8f9df2
Summary: A helper that makes system-config-printer use PolicyKit
Group: System/Libraries

License: GPLv2+
Url: http://www.freedesktop.org/wiki/Software/cups-pk-helper/
Source0: http://www.freedesktop.org/software/cups-pk-helper/releases/cups-pk-helper-%version.tar

Patch0: polkit_result.patch

BuildRequires: libcups-devel >= 1.2
BuildRequires: glib2-devel >= 2.29.8
BuildRequires: libgtk+2-devel >= 2.12.0
BuildRequires: libdbus-glib-devel >= 0.74
BuildRequires: libpolkit-devel >= 0.97
BuildRequires: intltool >= 0.40.6
BuildRequires: gettext-devel >= 0.17
BuildRequires: gnome-common

%description
cups-pk-helper is an application which makes cups configuration
interfaces available under control of PolicyKit.

%prep
%setup
%patch0 -p1 -b .polkit-result

%build
%autoreconf
%configure --libexecdir=%_prefix/libexec
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %name

%files -f %name.lang
%_prefix/libexec/cups-pk-helper-mechanism
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
%_datadir/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
%_datadir/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy
%doc AUTHORS COPYING NEWS

%changelog
* Sun May 26 2019 L.A. Kostis <lakostis@altlinux.ru> 0.2.7-alt0.1.ge8f9df2
- Initial build for ALTLinux.


