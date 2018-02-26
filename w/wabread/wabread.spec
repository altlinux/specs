%define oname libwab
Name: wabread
Version: 060901
Release: alt0.1

Summary: Read binary .wab files produced by the Windows Address Book

Group: System/Libraries
License: LGPL
Url: http://lilith.tec-man.com/libwab/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://lilith.tec-man.com/libwab/files/%oname-%version.tar.bz2

%description
libwab is a tool that can read binary .wab files produced by the Windows
Address Book application and output the data in ldif format. It can also
read broken files and recover deleted addresses.

%prep
%setup -q -n %oname-%version

%build
%configure
%make_build

%install
%makeinstall

%files
%doc README ChangeLog
%_bindir/%name

%changelog
* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 060901-alt0.1
- new version (060901)

* Wed Feb 15 2006 Vitaly Lipatov <lav@altlinux.ru> 060214-alt0.1
- initial build for ALT Linux Sisyphus
