%add_findprov_lib_path %_libdir/pidgin
%set_verify_elf_method relaxed
%define pidgin_ver 2.0.0

Summary:    Guifications Plugin for Pidgin
Name:       pidgin-guifications
Version:    2.16
Release:    alt1

License:    GPL
Group:      Networking/Instant messaging
Url:        http://plugins.guifications.org
Source:     http://downloads.guifications.org/pidgins/Guifications2/%name-%version.tar.bz2

Requires:  pidgin >= %pidgin_ver

BuildRequires: libgtk+2-devel perl-XML-Parser
BuildRequires: pidgin-devel >= %pidgin_ver

Obsoletes: gaim-guifications 
Provides: gaim-guifications = %version

%description
Guifications is a graphical notification plugin for the open source instant messaging client Pidgin

%prep
%setup -q -n %name-%version

%build
%configure --disable-deprecated 
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang guifications

%files -f guifications.lang
%doc AUTHORS ChangeLog COPYING README doc/flow.png doc/flow.dia doc/QUOTES
%_libdir/pidgin/*.so
%exclude %_libdir/pidgin/*.la
%dir %_datadir/pixmaps/pidgin/guifications
%_datadir/pixmaps/pidgin/guifications/*

%changelog
* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.16-alt1
- 2.16
- update source url

* Tue May 08 2007 Alexey Shabalin <shaba@altlinux.ru> 2.14-alt1
- 2.14 relase
- rename gaim-guifications -> pidgin-guifications

* Mon Feb 26 2007 Alexey Shabalin <shaba@altlinux.ru> 2.13-alt1beta6
- 2.13beta6 for gaim-2.0.0beta6
- cleanup spec

* Thu Dec 08 2005 Vital Khilko <vk@altlinux.ru> 2.12-alt1
- 2.12
- removed translated package description

* Thu Aug 04 2005 Vital Khilko <vk@altlinux.ru> 2.11-alt1
- 2.11

* Mon May 16 2005 Vital Khilko <vk@altlinux.ru> 2.9-alt2
- fixed dependencies

* Thu Feb 24 2005 Vital Khilko <vk@altlinux.ru> 2.9-alt1
- 2.9

* Thu Jan 20 2005 Vital Khilko <vk@altlinux.ru> 2.8-alt1
- 2.8
