%define _libexecdir %_prefix/libexec
Name:           mate-common
Version:        1.4.0
Release:        alt1_1.1
Summary:        mate-common contains useful things common to building mate packages

Group:          Development/Tools
BuildArch:      noarch
License:        GPL
URL: 			http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

# This will pull in the latest version; if your package requires something older,
# well, BuildRequire it in that spec.  At least until such time as we have a
# build system that is intelligent enough to inspect your source code
# and auto-inject those requirements.

BuildRequires: automake
BuildRequires: autoconf

Requires: automake
Requires: autoconf
Requires: libtool
Requires: gettext
Patch33: mate-common-1.3.0-alt-fix-libtool-not-found.patch

%description
Contains files required to bootstrap various Mate modules when building
from CVS.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build
%configure

make %{?_smp_mflags}
cp doc-build/README doc-README
# No sense making a doc subdir in the rpm pkg for one file.
cp doc/usage.txt usage.txt

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc doc-README README COPYING usage.txt ChangeLog
%{_bindir}/*
%{_datadir}/aclocal/*
%{_datadir}/%{name}
%{_mandir}/*/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

