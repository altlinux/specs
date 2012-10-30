%define _libexecdir %_prefix/libexec
%define oldname ffmpegthumbnailer-caja
Name:           mate-file-manager-ffmpegthumbnailer
Version:        1.4.0
Release:        alt1_1.1
Summary:        ffmpegthumbnailer-caja make thumbnails of video files in caja file manager

Group:          Development/Tools
BuildArch:      noarch
License:        GPL
URL: 			http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{oldname}-%{version}.tar.xz

#change /usr/share/mateconf to /etc/mateconf
Patch1:			ffmpegthumbnailer-caja_mateconf.patch

Requires: 		mate-conf >= 1.1.0-1
Requires:		mate-file-manager >= 1.1.0-1
Requires:		ffmpegthumbnailer

%description
This package install a MateConf schemas to use ffmpegthumbnailer to
make thumbnails of video files in caja file manager.

%prep
%setup -q -n %{oldname}-%{version}
%patch1 -p1 -b .ffmpegthumbnailer-caja_mateconf

%build
#no configure needed

make %{?_smp_mflags}

cp AUTHORS README

%install
make install DESTDIR=$RPM_BUILD_ROOT

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/ffmpegthumbnailer-caja.schemas \
	> /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/ffmpegthumbnailer-caja.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/ffmpegthumbnailer-caja.schemas \
	> /dev/null || :
fi

%files
%doc AUTHORS README
%{_sysconfdir}/mateconf/schemas/ffmpegthumbnailer-caja.schemas

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

