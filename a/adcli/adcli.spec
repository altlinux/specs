
Name: adcli
Version: 0.8.1

Release: alt1
Summary: Active Directory enrollment
License: LGPLv2+
Group: Networking/Other

Url: http://cgit.freedesktop.org/realmd/adcli
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: intltool
BuildRequires: /usr/bin/krb5-config
BuildRequires: libldap-devel libsasl2-devel
BuildRequires: libxslt
BuildRequires: xmlto

%description
adcli is a library and tool for joining an Active Directory domain using
standard LDAP and Kerberos calls.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static --disable-silent-rules
%make_build


%install
%makeinstall_std

%check
%make_build check

%files
%_sbindir/adcli
%doc AUTHORS COPYING ChangeLog NEWS README
%_mandir/*/*

%changelog
* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Nov 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.6-alt1
- 0.7.6 (ALT #31470)

* Wed Apr 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.7.5-alt1
- Initial build package
