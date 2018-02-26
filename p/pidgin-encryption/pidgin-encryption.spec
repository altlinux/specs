%def_disable static
%define pidgin_ver 2.0.0

Summary:    Encription Plugin for Gaim
Name:       pidgin-encryption
Version:    3.1
Release:    alt2

License:    GPL
Group:      Networking/Instant messaging
Url:        http://gaim-encryption.sourceforge.net/
Source:     %name-%version.tar.gz

Requires:	pidgin => %pidgin_ver
Requires:	libnspr libnss

#BuildRequires: pidgin-devel => %pidgin_ver
BuildRequires: pidgin-devel
BuildRequires: gcc-c++ libgtk+2-devel
BuildRequires: libnspr-devel libnss-devel

Obsoletes: gaim-encryption
Provides: gaim-encryption = %version

%description
Pidgin-Encryption uses NSS to provide transparent RSA encryption as a Pidgin plugin.

%prep
%setup -q -n %name-%version

%build
%configure %{subst_enable static} \
        --with-nss-includes=%_includedir/nss \
	--with-nspr-includes=%_includedir/nspr \
	--with-nspr-libs=%_libdir \
	--with-nss-libs=%_libdir

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc COPYING README
%_libdir/pidgin/*.so
%exclude %_libdir/pidgin/*.la 
%dir %_datadir/pixmaps/pidgin-encryption
%_datadir/pixmaps/pidgin-encryption/*

%changelog
* Thu Aug 12 2010 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt2
- update buildreq

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt1
- 3.1 release

* Mon May 07 2007 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt3
- 3.0 release
- rename gaim-encryption -> pidgin-encryption

* Mon Feb 26 2007 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt2beta8
- 3.0beta8 for gaim-2.0.0beta6

* Thu Nov 30 2006 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt1beta7
- version 3.0 for gaim-2.0.0
- fixed BuildRequires
- %%set_verify_elf_method relaxed

* Fri Jun 23 2006 Andrei Bulava <abulava@altlinux.ru> 2.38-alt2
- snapped up from orphaned
- fixed BuildRequires
- added Requires: libnspr libnss to depend on these correct packages
- minor fixes regarding %%build, %%install and %%files sections

* Thu Dec 08 2005 Vital Khilko <vk@altlinux.ru> 2.38-alt1
- gaim 1.5.0
- 2.38

* Mon May 16 2005 Vital Khilko <vk@altlinux.ru> 2.37-alt1
- gaim 1.3.0
- 2.37

* Mon Apr 04 2005 Vital Khilko <vk@altlinux.ru> 2.36-alt2
- gaim 1.2.1

* Fri Apr 01 2005 Vital Khilko <vk@altlinux.ru> 2.36-alt1
- new version

* Fri Mar 11 2005 Vital Khilko <vk@altlinux.ru> 2.35-alt1
- first release
