# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:				mate-file-manager-share
Version:			1.6.0
Release:			alt1_3
Summary:			Easy sharing folder via Samba (CIFS protocol)
Group:				File tools
License:			GPLv2+
URL:				http://pub.mate-desktop.org
Source0:			http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
Source1:			caja-share-setup-instructions
Source2:			caja-share-smb.conf.example

BuildRequires:		mate-file-manager-devel
BuildRequires:		mate-common

Requires:			samba
Source44: import.info

%description
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%prep
%setup -q
cp %{SOURCE1} SETUP
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/samba/
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/samba/

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/caja/extensions-2.0/*
%{_datadir}/mate-file-manager-share/
%config(noreplace) %{_sysconfdir}/samba/caja-share-smb.conf.example


%changelog
* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1_2
- initial release

