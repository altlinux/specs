# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mateconftool-2 /usr/bin/pkg-config pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-open-terminal
Name:           mate-file-manager-open-terminal
Version:        1.4.0
Release:        alt1_1.1
Summary:        Caja extension for an open terminal shortcut

Group:          Graphical desktop/Other
License:        GPLv2+
URL:            http://pub.mate-desktop.org
Source0:		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	intltool
# need extensions
BuildRequires:	mate-file-manager-devel
BuildRequires:  autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mate-conf-devel
BuildRequires: 	mate-common
BuildRequires: 	mate-desktop-devel
Requires(pre): 	mate-conf
Requires(post): mate-conf
Requires(preun): mate-conf

%description
The caja-open-terminal extension provides a right-click "Open
Terminal" option for caja users who prefer that option.

%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/caja/extensions-2.0/*.{l,}a

%find_lang %{oldname}


%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
              %{_sysconfdir}/mateconf/schemas/%{oldname}.schemas > /dev/null || :
fi

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 \
	    --makefile-install-rule \
	    %{_sysconfdir}/mateconf/schemas/%{oldname}.schemas >/dev/null || :

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
              %{_sysconfdir}/mateconf/schemas/%{oldname}.schemas > /dev/null || :
fi


%files -f %{oldname}.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%config(noreplace) %{_sysconfdir}/mateconf/schemas/*
%{_libdir}/caja/extensions-2.0/*.so*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- 20120622 mate snapshot

