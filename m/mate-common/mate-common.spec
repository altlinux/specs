Group: Development/Tools
%define _libexecdir %_prefix/libexec
Name:	mate-common
Summary:	mate common build files
Version:	1.5.0
Release:	alt1_1

License:	GPLv3+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/mate-common-%{version}.tar.xz

BuildArch: noarch

BuildRequires:	automake autoconf
Requires: automake autoconf gettext intltool libtool gtk-doc
Source44: import.info
Patch33: mate-common-1.3.0-alt-fix-libtool-not-found.patch

%description
binaries for building all MATE desktop sub components

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build
%configure
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/mate-*
%{_datadir}/aclocal/mate-*.m4
%{_datadir}/mate-common/
%{_mandir}/man1/mate-*

%changelog
* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

