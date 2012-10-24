%define _libexecdir %_prefix/libexec
%define oldname caja-sound-converter
Name:           mate-file-manager-sound-converter
Version:        3.0.2
Release:        alt2_3.1
Summary:        Caja extension to convert audio files

Group:          Graphical desktop/Other
License:        GPLv2+
URL:            https://github.com/benpicco/caja-sound-converter
Source0:        %{oldname}-%{version}.tar.gz

Patch0:			caja-sound-converter_media-profiles.patch

BuildRequires:  mate-file-manager-devel >= 1.1.0
BuildRequires:  glib2-devel >= 2.16.0
BuildRequires:  gstreamer-devel >= 0.10.19
BuildRequires:  mate-media-devel
BuildRequires:	intltool
BuildRequires:  perl(XML/Parser.pm)
BuildRequires:	mate-conf
BuildRequires: 	mate-common

ExcludeArch:    s390 s390x

Requires(pre): mate-conf
Requires(post): mate-conf
Requires(preun): mate-conf
# The bare minimum plugins needed.
Requires:       gst-plugins-good
Requires:       gst-plugins-base
Source44: import.info


%description
Adds a "Convert Sound File..." menu item to the context menu
of audio files. This opens a dialog where you can decide what audio
format you wish to convert the selected files to.


%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1 -b .caja-sound-converter_media-profiles
NOCONFIGURE=1 ./autogen.sh


%build

%configure \
	--disable-static

make %{?_smp_mflags}


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{oldname}
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;


%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/caja-sound-converter.schemas \
	> /dev/null || :
fi


%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/caja-sound-converter.schemas \
	> /dev/null || :


%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/caja-sound-converter.schemas \
	> /dev/null || :
fi


%files -f %{oldname}.lang
%doc COPYING README NEWS
%{_datadir}/%{oldname}/
%{_libdir}/caja/extensions-2.0/*.so
%{_sysconfdir}/mateconf/schemas/%{oldname}.schemas


%changelog
* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.0.2-alt2_3.1
- Build for Sisyphus

* Sun Oct 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_3
- restored i586 build

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_3
- new release

