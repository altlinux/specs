%define _libexecdir %_prefix/libexec
%define oldname mate-file-manager-share
%define oldname caja-share
Name:				mate-file-manager-share
Version:			0.7.3
Release:			alt1_2
Summary:			Easy sharing folder via Samba (CIFS protocol)
Group:				File tools
License:			GPLv2+
URL:				https://github.com/mate-desktop/mate-file-manager-share
Source0:			%{name}-%{version}.tar.gz
Source1:			caja-share-setup-instructions
Source2:			caja-share-smb.conf.example

BuildRequires:		libdaemon-devel
BuildRequires:		mate-file-manager-devel
BuildRequires:		gettext
BuildRequires:		perl(XML/Parser.pm)
BuildRequires:		gtk+-devel
BuildRequires:		libglade2-devel
BuildRequires: 	    mate-common
BuildRequires:		intltool
Requires:			samba >= 3.6.1
Source44: import.info

%description
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} SETUP
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/lib%{oldname}.la
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/samba/
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/samba/
%find_lang %{oldname}


%files -f %{oldname}.lang
%doc AUTHORS COPYING README TODO SETUP
%{_libdir}/caja/extensions-2.0/*
%{_datadir}/caja-share/
%{_sysconfdir}/samba/%{oldname}-smb.conf.example


%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1_2
- initial release

